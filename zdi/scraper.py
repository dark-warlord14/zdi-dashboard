"""Fetch ZDI pages and write public dashboard data."""

from __future__ import annotations

import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urljoin

import requests
from pydantic import ValidationError

from zdi.config import BASE_URL, DATA_DIR, PUBLISHED_URL, UPCOMING_URL
from zdi.models import AdvisoryDetail, PublishedAdvisory, UpcomingAdvisory
from zdi.parser import parse_advisory_detail, parse_published, parse_upcoming, parse_years
from zdi.stats import build_stats

HEADERS = {
    "User-Agent": "zdi-dashboard/0.1 (+https://github.com/; security research archive)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def dump_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def fetch_html(url: str, retries: int = 3, delay: float = 1.0) -> str:
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=45)
            response.raise_for_status()
            return response.text
        except requests.RequestException as exc:
            last_error = exc
            if attempt < retries - 1:
                time.sleep(delay * (attempt + 1))
    raise RuntimeError(f"Failed to fetch {url}: {last_error}") from last_error


def published_year_url(year: int) -> str:
    return urljoin(BASE_URL, f"/advisories/published/{year}/")


def scrape_published(fetch=fetch_html, verbose: bool = False) -> list[PublishedAdvisory]:
    first_html = fetch(PUBLISHED_URL)
    years = parse_years(first_html)
    records: list[PublishedAdvisory] = []
    seen: set[str] = set()
    pages = [(None, first_html)] + [(year, None) for year in years if year != (years[0] if years else None)]
    for year, cached_html in pages:
        if verbose:
            print(f"Fetching published list {year or years[0] if years else 'current'}...")
        html = cached_html if cached_html is not None else fetch(published_year_url(year))
        for record in parse_published(html):
            if record.zdi_id not in seen:
                records.append(record)
                seen.add(record.zdi_id)
    return records


def scrape_upcoming(fetch=fetch_html) -> list[UpcomingAdvisory]:
    return parse_upcoming(fetch(UPCOMING_URL))


def load_existing_detail(
    chunks: dict[str, dict[str, AdvisoryDetail]],
    published_lookup: dict[str, str],
    record: PublishedAdvisory,
) -> AdvisoryDetail | None:
    year = advisory_year(record.zdi_id, published_lookup)
    existing = chunks.get(year, {}).get(record.zdi_id)
    if existing and existing.updated_date == record.updated_date:
        return existing
    return None


def fetch_detail(
    record: PublishedAdvisory,
    chunks: dict[str, dict[str, AdvisoryDetail]],
    published_lookup: dict[str, str],
    fetch=fetch_html,
) -> AdvisoryDetail:
    existing = load_existing_detail(chunks, published_lookup, record)
    if existing:
        return existing
    html = fetch(record.url)
    detail = parse_advisory_detail(html, source_url=record.url)
    detail.updated_date = record.updated_date
    return detail


def scrape_details(
    records: list[PublishedAdvisory],
    data_dir: Path = DATA_DIR,
    fetch=fetch_html,
    max_workers: int = 12,
    verbose: bool = False,
) -> dict[str, AdvisoryDetail]:
    chunks = load_advisory_chunks(data_dir)
    published_lookup = {record.zdi_id: record.published_date for record in records if record.published_date}
    details: dict[str, AdvisoryDetail] = {}
    total = len(records)
    completed = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(fetch_detail, record, chunks, published_lookup, fetch): record
            for record in records
        }
        for future in as_completed(futures):
            record = futures[future]
            details[record.zdi_id] = future.result()
            completed += 1
            if verbose and (completed == total or completed % 100 == 0):
                print(f"Fetched details {completed}/{total}")
    return details


def description_snippet(detail: AdvisoryDetail | None, max_length: int = 260) -> str | None:
    if not detail or not detail.vulnerability_details:
        return None
    text = " ".join(detail.vulnerability_details.split())
    if len(text) <= max_length:
        return text
    return text[: max_length - 1].rstrip() + "..."


def advisory_year(zdi_id: str, published_lookup: dict[str, str], detail: AdvisoryDetail | None = None) -> str:
    """Return the 4-digit year bucket for an advisory, or 'unknown' if it can't be determined."""
    published_date = published_lookup.get(zdi_id)
    if published_date and published_date[:4].isdigit():
        return published_date[:4]
    if detail and detail.advisory_date and detail.advisory_date[:4].isdigit():
        return detail.advisory_date[:4]
    return "unknown"


def group_details_by_year(
    details: dict[str, AdvisoryDetail],
    published: list[PublishedAdvisory],
) -> dict[str, dict[str, AdvisoryDetail]]:
    published_lookup = {record.zdi_id: record.published_date for record in published if record.published_date}
    grouped: dict[str, dict[str, AdvisoryDetail]] = {}
    for zdi_id, detail in details.items():
        year = advisory_year(zdi_id, published_lookup, detail)
        grouped.setdefault(year, {})[zdi_id] = detail
    return grouped


def load_advisory_chunks(data_dir: Path) -> dict[str, dict[str, AdvisoryDetail]]:
    """Load every existing data/advisories/<year>.json into memory, once per run."""
    advisories_dir = data_dir / "advisories"
    chunks: dict[str, dict[str, AdvisoryDetail]] = {}
    if not advisories_dir.exists():
        return chunks
    for path in advisories_dir.glob("*.json"):
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
            chunks[path.stem] = {
                zdi_id: AdvisoryDetail.model_validate(payload) for zdi_id, payload in raw.items()
            }
        except (json.JSONDecodeError, OSError, ValidationError):
            continue
    return chunks


def write_advisory_chunks(data_dir: Path, grouped: dict[str, dict[str, AdvisoryDetail]]) -> None:
    advisories_dir = data_dir / "advisories"
    advisories_dir.mkdir(parents=True, exist_ok=True)
    for year, details_by_id in grouped.items():
        payload = {zdi_id: detail.model_dump() for zdi_id, detail in details_by_id.items()}
        dump_json(advisories_dir / f"{year}.json", payload)


def published_entries(published: list[PublishedAdvisory], details: dict[str, AdvisoryDetail]) -> list[dict]:
    entries: list[dict] = []
    for record in published:
        data = record.model_dump()
        data["description_snippet"] = description_snippet(details.get(record.zdi_id))
        entries.append(data)
    return entries


def index_entries(
    published: list[PublishedAdvisory],
    upcoming: list[UpcomingAdvisory],
    details: dict[str, AdvisoryDetail],
) -> list[dict]:
    published_lookup = {record.zdi_id: record.published_date for record in published if record.published_date}
    entries: list[dict] = []
    for record in published:
        data = record.model_dump()
        data["id"] = record.zdi_id
        data["status"] = "published"
        data["description_snippet"] = description_snippet(details.get(record.zdi_id))
        data["detail_json"] = f"/data/advisories/{advisory_year(record.zdi_id, published_lookup)}.json"
        entries.append(data)
    for record in upcoming:
        data = record.model_dump()
        data["id"] = record.zdi_can
        data["status"] = "upcoming"
        entries.append(data)
    return entries


def write_public_data(
    data_dir: Path,
    published: list[PublishedAdvisory],
    upcoming: list[UpcomingAdvisory],
    details: dict[str, AdvisoryDetail],
) -> None:
    data_dir.mkdir(parents=True, exist_ok=True)
    grouped = group_details_by_year(details, published)
    guard_against_year_chunk_collapse(data_dir, grouped)
    dump_json(data_dir / "published.json", published_entries(published, details))
    dump_json(data_dir / "upcoming.json", [record.model_dump() for record in upcoming])
    dump_json(data_dir / "index.json", index_entries(published, upcoming, details))
    dump_json(data_dir / "stats.json", build_stats(published, upcoming).model_dump())
    write_advisory_chunks(data_dir, grouped)


def guard_against_empty_scrape(data_dir: Path, published: list[PublishedAdvisory], upcoming: list[UpcomingAdvisory]) -> None:
    """Refuse to overwrite good data with a near-empty scrape (e.g. site markup changed)."""
    for name, scraped in (("published", published), ("upcoming", upcoming)):
        path = data_dir / f"{name}.json"
        if not path.exists():
            continue
        try:
            existing_count = len(json.loads(path.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError):
            continue
        if existing_count >= 10 and len(scraped) < existing_count * 0.5:
            raise RuntimeError(
                f"Refusing to overwrite {existing_count} {name} advisories with only {len(scraped)} "
                "newly scraped ones. The ZDI site markup likely changed and broke the parser selectors."
            )


def guard_against_year_chunk_collapse(data_dir: Path, grouped: dict[str, dict[str, AdvisoryDetail]]) -> None:
    """Refuse to overwrite a year's advisories with a near-empty result (e.g. a broken parser)."""
    advisories_dir = data_dir / "advisories"
    for year, details_by_id in grouped.items():
        path = advisories_dir / f"{year}.json"
        if not path.exists():
            continue
        try:
            existing_count = len(json.loads(path.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError):
            continue
        if existing_count >= 10 and len(details_by_id) < existing_count * 0.5:
            raise RuntimeError(
                f"Refusing to overwrite {existing_count} advisories in {year}.json with only "
                f"{len(details_by_id)} newly built ones. The parser may be broken."
            )


def run(
    data_dir: Path = DATA_DIR,
    fetch=fetch_html,
    max_workers: int = 12,
    verbose: bool = False,
) -> tuple[list[PublishedAdvisory], list[UpcomingAdvisory]]:
    published = scrape_published(fetch=fetch, verbose=verbose)
    if verbose:
        print(f"Found {len(published)} published advisories")
    upcoming = scrape_upcoming(fetch=fetch)
    if verbose:
        print(f"Found {len(upcoming)} upcoming advisories")
    guard_against_empty_scrape(data_dir, published, upcoming)
    details = scrape_details(published, data_dir=data_dir, fetch=fetch, max_workers=max_workers, verbose=verbose)
    write_public_data(data_dir, published, upcoming, details)
    return published, upcoming
