# Year-Chunked Advisory Data Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace `data/advisories/<zdi_id>/advisory.json` (17,000+ individual files, growing ~1,500-2,000/year) with `data/advisories/<year>.json` (one JSON object per calendar year, keyed by ZDI ID), to stay under Cloudflare Pages' file-count ceiling and stop needlessly re-fetching the 67% of advisories that have no `updated_date`.

**Architecture:** Advisory details are grouped by the year in `PublishedAdvisory.published_date` (falling back to `AdvisoryDetail.advisory_date`, then an `unknown` bucket) and written as one JSON object per year instead of one file per record. The scraper's cache-lookup path loads all existing year-chunk files into memory once per run instead of doing a file-existence check per record. The public URL contract for agents changes from "fetch one advisory by ID" to "fetch the record's year from the index, then fetch that year's chunk and look up by ID" — the same two-request shape as today.

**Tech Stack:** Python 3.12, pytest, click, pydantic, BeautifulSoup (existing stack — no new dependencies). Vanilla JS frontend (no build step).

## Global Constraints

- Spec: `docs/superpowers/specs/2026-08-20-year-chunked-advisory-data-design.md` — read it before starting if anything here is ambiguous.
- Work happens on branch `redesign/year-chunked-advisory-data` (already created off `main`). Never commit to `main` directly.
- No server-side compute (no Cloudflare Workers/KV/D1). Cloudflare Pages stays a pure static deploy.
- Year is always derived from `published_date[:4]` first; only fall back to `AdvisoryDetail.advisory_date[:4]`, then the literal string `"unknown"`. Never parse the year out of the ZDI ID string.
- `index.json`, `published.json`, `upcoming.json`, `stats.json` are unaffected by this change — do not modify their schema or generation logic.
- `schema.json` (the per-advisory JSON Schema) is unaffected — only which file a record lives in changes, not its shape.
- Every new function needs a test. Every existing test that touches changed behavior must be updated, not deleted, unless the spec explicitly says the behavior it tested no longer applies.
- Run `/tmp/zdi-venv/bin/python -m pytest -v` (or your own venv with `pip install -e ".[dev]"`) after every task — all tests must pass before moving to the next task.

---

## Milestone 1: Core chunking primitives in `zdi/scraper.py`

### Task 1: `advisory_year()` and `group_details_by_year()`

**Files:**
- Modify: `zdi/scraper.py` (add functions near the top, after the existing helper functions like `description_snippet`)
- Test: `tests/test_pipeline.py`

**Interfaces:**
- Produces: `advisory_year(zdi_id: str, published_lookup: dict[str, str], detail: AdvisoryDetail | None = None) -> str`
- Produces: `group_details_by_year(details: dict[str, AdvisoryDetail], published: list[PublishedAdvisory]) -> dict[str, dict[str, AdvisoryDetail]]`

- [ ] **Step 1: Write the failing tests**

Add to `tests/test_pipeline.py` (add `advisory_year, group_details_by_year` to the existing `from zdi.scraper import ...` line):

```python
def test_advisory_year_uses_published_date_first():
    lookup = {"ZDI-26-001": "2026-03-01"}
    assert advisory_year("ZDI-26-001", lookup) == "2026"


def test_advisory_year_falls_back_to_detail_advisory_date():
    detail = AdvisoryDetail(
        zdi_id="ZDI-10-001", title="Old", source_url="https://x", advisory_date="2010-05-01"
    )
    assert advisory_year("ZDI-10-001", {}, detail) == "2010"


def test_advisory_year_falls_back_to_unknown_when_no_date_available():
    assert advisory_year("ZDI-00-000", {}) == "unknown"


def test_group_details_by_year_buckets_by_published_date():
    published = [
        sample_published(),
        PublishedAdvisory(
            zdi_id="ZDI-10-001", title="Old", url="https://x", published_date="2010-05-01"
        ),
    ]
    details = {
        "ZDI-26-040": sample_detail(),
        "ZDI-10-001": AdvisoryDetail(zdi_id="ZDI-10-001", title="Old", source_url="https://x"),
    }

    grouped = group_details_by_year(details, published)

    assert set(grouped["2026"]) == {"ZDI-26-040"}
    assert set(grouped["2010"]) == {"ZDI-10-001"}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_pipeline.py -v -k "advisory_year or group_details_by_year"`
Expected: FAIL with `ImportError: cannot import name 'advisory_year'`

- [ ] **Step 3: Implement**

Add to `zdi/scraper.py`:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_pipeline.py -v -k "advisory_year or group_details_by_year"`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add zdi/scraper.py tests/test_pipeline.py
git commit -m "feat: add advisory_year and group_details_by_year helpers"
```

---

### Task 2: `load_advisory_chunks()` and `write_advisory_chunks()`

**Files:**
- Modify: `zdi/scraper.py`
- Test: `tests/test_pipeline.py`

**Interfaces:**
- Consumes: nothing new from Task 1 (independent I/O helpers)
- Produces: `load_advisory_chunks(data_dir: Path) -> dict[str, dict[str, AdvisoryDetail]]`
- Produces: `write_advisory_chunks(data_dir: Path, grouped: dict[str, dict[str, AdvisoryDetail]]) -> None`

- [ ] **Step 1: Write the failing tests**

Add to `tests/test_pipeline.py` (add `load_advisory_chunks, write_advisory_chunks` to the import line):

```python
def test_write_and_load_advisory_chunks_round_trip(tmp_path):
    grouped = {"2026": {"ZDI-26-040": sample_detail()}}

    write_advisory_chunks(tmp_path, grouped)
    loaded = load_advisory_chunks(tmp_path)

    assert set(loaded) == {"2026"}
    assert loaded["2026"]["ZDI-26-040"].title == sample_detail().title


def test_load_advisory_chunks_returns_empty_dict_when_dir_missing(tmp_path):
    assert load_advisory_chunks(tmp_path) == {}


def test_load_advisory_chunks_skips_unreadable_files(tmp_path):
    advisories_dir = tmp_path / "advisories"
    advisories_dir.mkdir()
    (advisories_dir / "2026.json").write_text("not valid json", encoding="utf-8")

    assert load_advisory_chunks(tmp_path) == {}


def test_load_advisory_chunks_skips_schema_invalid_file_but_keeps_valid_ones(tmp_path):
    write_advisory_chunks(tmp_path, {"2025": {"ZDI-25-001": sample_detail()}})
    advisories_dir = tmp_path / "advisories"
    (advisories_dir / "2026.json").write_text(
        json.dumps({"ZDI-26-999": {"not_a_real_field": "boom"}}), encoding="utf-8"
    )

    loaded = load_advisory_chunks(tmp_path)

    assert set(loaded) == {"2025"}
    assert loaded["2025"]["ZDI-25-001"].title == sample_detail().title
```

This uses `json` (already imported at the top of `tests/test_pipeline.py`). The schema-invalid record (missing `AdvisoryDetail`'s required `title` and `source_url` fields) must raise `pydantic.ValidationError` inside `AdvisoryDetail.model_validate(...)` — the fix in Step 3 below must catch that alongside `json.JSONDecodeError`/`OSError`, or this test fails with an unhandled `ValidationError` instead of skipping the bad file.

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_pipeline.py -v -k "advisory_chunks"`
Expected: FAIL with `ImportError: cannot import name 'load_advisory_chunks'`

- [ ] **Step 3: Implement**

Add to `zdi/scraper.py`:

Add `from pydantic import ValidationError` to the top of `zdi/scraper.py`'s import block.

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_pipeline.py -v -k "advisory_chunks"`
Expected: 3 passed

- [ ] **Step 5: Commit**

```bash
git add zdi/scraper.py tests/test_pipeline.py
git commit -m "feat: add load_advisory_chunks and write_advisory_chunks"
```

---

### Task 3: `guard_against_year_chunk_collapse()`

**Files:**
- Modify: `zdi/scraper.py`
- Test: `tests/test_pipeline.py`

**Interfaces:**
- Consumes: nothing new (reads year-chunk files directly by path, same pattern as existing `guard_against_empty_scrape`)
- Produces: `guard_against_year_chunk_collapse(data_dir: Path, grouped: dict[str, dict[str, AdvisoryDetail]]) -> None`, raises `RuntimeError` on collapse

- [ ] **Step 1: Write the failing tests**

Add to `tests/test_pipeline.py` (add `guard_against_year_chunk_collapse` to the import line):

```python
def test_guard_against_year_chunk_collapse_raises_on_drop(tmp_path):
    write_advisory_chunks(tmp_path, {"2026": {f"ZDI-26-{i:03d}": sample_detail() for i in range(20)}})

    with pytest.raises(RuntimeError):
        guard_against_year_chunk_collapse(tmp_path, {"2026": {"ZDI-26-001": sample_detail()}})


def test_guard_against_year_chunk_collapse_allows_growth(tmp_path):
    write_advisory_chunks(tmp_path, {"2026": {f"ZDI-26-{i:03d}": sample_detail() for i in range(20)}})

    guard_against_year_chunk_collapse(
        tmp_path, {"2026": {f"ZDI-26-{i:03d}": sample_detail() for i in range(25)}}
    )


def test_guard_against_year_chunk_collapse_ignores_new_year(tmp_path):
    guard_against_year_chunk_collapse(tmp_path, {"2026": {"ZDI-26-001": sample_detail()}})
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_pipeline.py -v -k "year_chunk_collapse"`
Expected: FAIL with `ImportError: cannot import name 'guard_against_year_chunk_collapse'`

- [ ] **Step 3: Implement**

Add to `zdi/scraper.py`:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_pipeline.py -v -k "year_chunk_collapse"`
Expected: 3 passed

- [ ] **Step 5: Commit**

```bash
git add zdi/scraper.py tests/test_pipeline.py
git commit -m "feat: add guard_against_year_chunk_collapse"
```

---

## Milestone 2: Wire chunking into the read/write pipeline

### Task 4: Update `write_public_data()` to write year-chunked files

**Files:**
- Modify: `zdi/scraper.py:151-166` (the `write_public_data` function and the old per-ID loop it contains)
- Modify: `tests/test_pipeline.py:65-78` (existing test, update its assertions)

**Interfaces:**
- Consumes: `group_details_by_year`, `guard_against_year_chunk_collapse`, `write_advisory_chunks` from Tasks 1-3
- Produces: `write_public_data(...)` keeps its existing signature; callers in `zdi/cli.py` and `zdi/scraper.py::run()` need no changes for this task

- [ ] **Step 1: Update the existing test first**

Replace `test_write_public_data_creates_index_and_detail_files` in `tests/test_pipeline.py` with:

```python
def test_write_public_data_creates_index_and_detail_files(tmp_path):
    write_public_data(tmp_path, [sample_published()], [sample_upcoming()], {"ZDI-26-040": sample_detail()})

    index = json.loads((tmp_path / "index.json").read_text(encoding="utf-8"))
    published = json.loads((tmp_path / "published.json").read_text(encoding="utf-8"))
    upcoming = json.loads((tmp_path / "upcoming.json").read_text(encoding="utf-8"))
    year_chunk = json.loads((tmp_path / "advisories" / "2026.json").read_text(encoding="utf-8"))

    assert index[0]["id"] == "ZDI-26-040"
    assert index[0]["description_snippet"] == "Local attackers can escalate privileges."
    assert "detail_markdown" not in index[0]
    assert index[1]["id"] == "ZDI-CAN-30796"
    assert published[0]["zdi_id"] == "ZDI-26-040"
    assert published[0]["description_snippet"] == "Local attackers can escalate privileges."
    assert upcoming[0]["zdi_can"] == "ZDI-CAN-30796"
    assert year_chunk["ZDI-26-040"]["title"] == "Discord Client Privilege Escalation"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_pipeline.py::test_write_public_data_creates_index_and_detail_files -v`
Expected: FAIL — `FileNotFoundError` for `advisories/2026.json` (old code still writes `advisories/ZDI-26-040/advisory.json`)

- [ ] **Step 3: Implement**

In `zdi/scraper.py`, replace the body of `write_public_data`:

```python
def write_public_data(
    data_dir: Path,
    published: list[PublishedAdvisory],
    upcoming: list[UpcomingAdvisory],
    details: dict[str, AdvisoryDetail],
) -> None:
    data_dir.mkdir(parents=True, exist_ok=True)
    dump_json(data_dir / "published.json", published_entries(published, details))
    dump_json(data_dir / "upcoming.json", [record.model_dump() for record in upcoming])
    dump_json(data_dir / "index.json", index_entries(published, upcoming, details))
    dump_json(data_dir / "stats.json", build_stats(published, upcoming).model_dump())
    grouped = group_details_by_year(details, published)
    guard_against_year_chunk_collapse(data_dir, grouped)
    write_advisory_chunks(data_dir, grouped)
```

This removes the old trailing loop:

```python
    for zdi_id, detail in details.items():
        target = data_dir / "advisories" / zdi_id
        target.mkdir(parents=True, exist_ok=True)
        dump_json(target / "advisory.json", detail.model_dump())
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_pipeline.py -v`
Expected: all tests in the file pass

- [ ] **Step 5: Commit**

```bash
git add zdi/scraper.py tests/test_pipeline.py
git commit -m "feat: write_public_data writes year-chunked advisory files"
```

---

### Task 5: Update the caching path — `load_existing_detail`, `fetch_detail`, `scrape_details`

**Files:**
- Modify: `zdi/scraper.py:68-109` (all three functions)
- Test: `tests/test_pipeline.py`

**Interfaces:**
- Consumes: `load_advisory_chunks`, `advisory_year` from Tasks 1-2
- Produces: `load_existing_detail(chunks: dict[str, dict[str, AdvisoryDetail]], published_lookup: dict[str, str], record: PublishedAdvisory) -> AdvisoryDetail | None` (signature changes — no test or caller outside this file references the old signature, confirmed by repo-wide grep before writing this plan)
- Produces: `fetch_detail(record: PublishedAdvisory, chunks: dict[str, dict[str, AdvisoryDetail]], published_lookup: dict[str, str], fetch=fetch_html) -> AdvisoryDetail`
- `scrape_details(...)` keeps its existing public signature

- [ ] **Step 1: Write the failing test**

Add to `tests/test_pipeline.py` (add `load_existing_detail` to the import line):

```python
def test_load_existing_detail_reuses_cache_when_updated_date_matches():
    cached = sample_detail()
    cached.updated_date = "2026-01-09"
    chunks = {"2026": {"ZDI-26-040": cached}}
    record = sample_published()
    record.updated_date = "2026-01-09"

    result = load_existing_detail(chunks, {"ZDI-26-040": "2026-01-09"}, record)

    assert result is cached


def test_load_existing_detail_misses_cache_when_updated_date_differs():
    cached = sample_detail()
    cached.updated_date = "2026-01-01"
    chunks = {"2026": {"ZDI-26-040": cached}}
    record = sample_published()
    record.updated_date = "2026-01-09"

    result = load_existing_detail(chunks, {"ZDI-26-040": "2026-01-09"}, record)

    assert result is None


def test_load_existing_detail_reuses_cache_when_updated_date_is_null_on_both_sides():
    cached = sample_detail()
    cached.updated_date = None
    chunks = {"2026": {"ZDI-26-040": cached}}
    record = sample_published()
    record.updated_date = None

    result = load_existing_detail(chunks, {"ZDI-26-040": "2026-01-09"}, record)

    assert result is cached


def test_load_existing_detail_misses_cache_when_only_new_updated_date_is_present():
    cached = sample_detail()
    cached.updated_date = None
    chunks = {"2026": {"ZDI-26-040": cached}}
    record = sample_published()
    record.updated_date = "2026-01-09"

    result = load_existing_detail(chunks, {"ZDI-26-040": "2026-01-09"}, record)

    assert result is None
```

An advisory that ZDI has never shown an "Updated" date for (67% of the real archive, verified: 11,408/16,992 published advisories) has `updated_date: null` on both the cached copy and every future scrape of the same list page. Requiring `record.updated_date` to be truthy before trusting the cache means these records NEVER hit cache — they're re-fetched over the network on every single run, forever. This was measured directly: a real `zdi run --workers 32` took 14 minutes with a 32.9% cache-hit rate, when it should complete in well under a minute. Treating `None == None` as a match (i.e. "this advisory has never been revised, on either side") fixes this while still correctly detecting the transition from never-updated to updated (a record whose `updated_date` newly becomes truthy no longer equals the cached `None` and correctly misses cache, as covered by the second test above).

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_pipeline.py -v -k "load_existing_detail"`
Expected: FAIL — `TypeError: load_existing_detail() missing 1 required positional argument` (old signature is `(data_dir, record)`)

- [ ] **Step 3: Implement**

In `zdi/scraper.py`, replace `load_existing_detail`, `fetch_detail`, and the body of `scrape_details`:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/ -v`
Expected: all tests pass (this is the point in the plan where a full-suite run first exercises every changed function together)

- [ ] **Step 5: Commit**

```bash
git add zdi/scraper.py tests/test_pipeline.py
git commit -m "feat: cache lookups read from preloaded year-chunk files"
```

---

### Task 6: Update `zdi/cli.py` `rebuild_index` to read year-chunk files

**Files:**
- Modify: `zdi/cli.py:37-56`
- Test: `tests/test_cli.py` (new file)

**Interfaces:**
- Consumes: `load_advisory_chunks` from Task 2

- [ ] **Step 1: Write the failing test**

Create `tests/test_cli.py`:

```python
import json
from pathlib import Path

from click.testing import CliRunner

from zdi.cli import cli
from zdi.models import AdvisoryDetail, PublishedAdvisory
from zdi.scraper import write_public_data


def test_rebuild_index_cli_reads_year_chunk_files(tmp_path):
    data_dir = tmp_path / "data"
    published = [
        PublishedAdvisory(
            zdi_id="ZDI-26-040",
            title="Discord Client Privilege Escalation",
            url="https://www.zerodayinitiative.com/advisories/ZDI-26-040/",
            published_date="2026-01-09",
        )
    ]
    details = {
        "ZDI-26-040": AdvisoryDetail(
            zdi_id="ZDI-26-040",
            title="Discord Client Privilege Escalation",
            source_url="https://www.zerodayinitiative.com/advisories/ZDI-26-040/",
            vulnerability_details="Local attackers can escalate privileges.",
        )
    }
    write_public_data(data_dir, published, [], details)

    runner = CliRunner()
    result = runner.invoke(cli, ["index", "--data-dir", str(data_dir)])

    assert result.exit_code == 0
    assert "Rebuilt index for 1 published and 0 upcoming advisories" in result.output
    index = json.loads((data_dir / "index.json").read_text(encoding="utf-8"))
    assert index[0]["description_snippet"] == "Local attackers can escalate privileges."
```

The final assertion is the one that actually exercises the code change: `write_public_data` (already updated in Task 4) writes `data/advisories/2026.json`, and `rebuild_index` must read that file to find `vulnerability_details` and recompute the snippet. Against the current (pre-fix) `rebuild_index`, which globs the old `*/advisory.json` layout, this glob matches nothing, `details` ends up empty, and the snippet is lost.

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_cli.py -v`
Expected: FAIL — `AssertionError` on the `description_snippet` check (it comes back `None` because the old glob finds nothing in the new year-chunked layout)

- [ ] **Step 3: Implement**

In `zdi/cli.py`, update the import line:

```python
from zdi.scraper import load_advisory_chunks, run as run_pipeline, scrape_published, scrape_upcoming, write_public_data
```

Replace the body of `rebuild_index`'s detail-loading loop:

```python
    details: dict[str, AdvisoryDetail] = {}
    for year_details in load_advisory_chunks(data_dir).values():
        details.update(year_details)
```

(This replaces the old `for path in (data_dir / "advisories").glob("*/advisory.json"): ...` loop.)

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_cli.py -v`
Expected: PASS

- [ ] **Step 5: Run the full suite and commit**

```bash
pytest tests/ -v
git add zdi/cli.py tests/test_cli.py
git commit -m "feat: zdi index reads advisory details from year-chunk files"
```

---

## Milestone 3: Downstream consumers — build, frontend, docs

### Task 7: Update `build.sh` and `tests/test_build.py` for the new layout

**Files:**
- Modify: `build.sh`
- Modify: `tests/test_build.py`

**Interfaces:**
- No new functions; this is a shell script + fixture path change

- [ ] **Step 1: Update the test first**

In `tests/test_build.py`, in the `required` list inside `test_build_script_creates_cloudflare_dist`, replace:

```python
            project / "dist" / "data" / "advisories" / "ZDI-26-040" / "advisory.json",
```

with:

```python
            project / "dist" / "data" / "advisories" / "2026.json",
```

Remove the now-meaningless trailing line (the directory it checks can no longer exist under the new layout):

```python
        assert not (project / "dist" / "data" / "advisories" / "ZDI-26-040" / "advisory.md").exists()
```

- [ ] **Step 2: Run test to verify it passes**

Run: `pytest tests/test_build.py -v`
Expected: PASS already — Task 4 already made `write_public_data` produce `data/advisories/2026.json`, so this fixture-path update has nothing left to fix on the Python side. This step exists to lock in the new expected layout as a regression test, not to catch a bug in this task. The real remaining gap is `build.sh`'s advisory-count line, which has no pytest coverage at all (it's a shell one-liner) — that's Step 3.

- [ ] **Step 3: Update `build.sh`'s advisory count**

Replace this line in `build.sh`:

```bash
COUNT=$(find "${DIST}/data/advisories" -name advisory.json 2>/dev/null | wc -l | tr -d ' ')
```

with:

```bash
COUNT=$(python3 -c "
import glob, json
total = 0
for path in glob.glob('${DIST}/data/advisories/*.json'):
    with open(path) as f:
        total += len(json.load(f))
print(total)
")
```

- [ ] **Step 4: Manually verify `build.sh` runs cleanly against the real repo**

Run: `bash build.sh` (from the repo root)
Expected: the script succeeds and prints a `Done: ...` line. At this point in the plan, the real `data/advisories/` on disk still has the OLD per-ID layout (migration is Milestone 4, not yet done), so the new `glob.glob('.../advisories/*.json')` pattern matches nothing yet and `COUNT` will print `0`. That is expected here, not a bug — it becomes the real count once Task 11 migrates the data. Do not "fix" this by touching the migration order; the spec's sequencing (code first, migrate from local data second, per the corrected Migration Plan) is intentional.

- [ ] **Step 5: Commit**

```bash
git add build.sh tests/test_build.py
git commit -m "feat: build.sh counts advisories across year-chunk files"
```

---

### Task 8: Update `ui/js/app.js` detail view to fetch year-chunk files

**Files:**
- Modify: `ui/js/app.js:242-266` (the `showDetail` method)
- Test: `tests/test_ui_detail.py` (new file)

**Interfaces:**
- Consumes: `this.index` (already populated by `loadData()` before any route runs — confirmed by reading `init()`), specifically each record's `published_date` field

- [ ] **Step 1: Write the failing test**

Create `tests/test_ui_detail.py`:

```python
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_show_detail_fetches_year_chunk_instead_of_per_id_file():
    app_js = (ROOT / "ui" / "js" / "app.js").read_text(encoding="utf-8")

    assert "/data/advisories/${id}/advisory.json" not in app_js
    assert "/data/advisories/${year}.json" in app_js
    assert "published_date.slice(0, 4)" in app_js
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_ui_detail.py -v`
Expected: FAIL — `app.js` still contains the old `/data/advisories/${id}/advisory.json` pattern

- [ ] **Step 3: Implement**

In `ui/js/app.js`, replace the `showDetail` method body:

```javascript
    async showDetail(id) {
        const app = document.getElementById('app');
        app.innerHTML = '<p class="loading-initial">Loading advisory...</p>';
        const notFound = () => { app.innerHTML = '<div class="panel">Advisory detail not found.</div>'; };

        const indexRecord = (this.index || []).find(r => r.id === id);
        const year = indexRecord && indexRecord.published_date ? indexRecord.published_date.slice(0, 4) : null;
        if (!year) return notFound();

        const chunkRes = await fetch(`/data/advisories/${year}.json`);
        if (!chunkRes.ok) return notFound();

        const chunk = await chunkRes.json();
        const detail = chunk[id];
        if (!detail) return notFound();

        const markdown = this.detailMarkdown(detail);
        app.innerHTML = `
            <div class="detail-layout">
                <article class="panel markdown">${this.md.render(markdown)}</article>
                <aside class="panel meta-list">
                    ${this.meta('ZDI ID', detail.zdi_id)}
                    ${this.meta('ZDI-CAN', detail.zdi_can)}
                    ${this.meta('CVE', detail.cve)}
                    ${this.meta('CVSS', detail.cvss)}
                    ${this.meta('Vendor', (detail.affected_vendors || []).join(', '))}
                    <a class="outline" href="${detail.source_url}" target="_blank" rel="noopener">Source</a>
                    <a class="outline" href="/data/advisories/${year}.json">JSON</a>
                </aside>
            </div>
        `;
    },
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_ui_detail.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add ui/js/app.js tests/test_ui_detail.py
git commit -m "feat: detail view fetches year-chunk advisory files"
```

---

### Task 9: Update `ui/llms.txt` and `ui/skill.md`

**Files:**
- Modify: `ui/llms.txt`
- Modify: `ui/skill.md`
- Test: `tests/test_ui_assets.py`

**Interfaces:**
- None (documentation only)

- [ ] **Step 1: Write the failing test**

Add to `tests/test_ui_assets.py`:

```python
def test_llms_txt_and_skill_md_document_year_chunked_advisories():
    llms = (ROOT / "ui" / "llms.txt").read_text(encoding="utf-8")
    skill = (ROOT / "ui" / "skill.md").read_text(encoding="utf-8")

    assert "/data/advisories/<zdi_id>/advisory.json" not in llms
    assert "/data/advisories/<year>.json" in llms
    assert "/data/advisories/<zdi_id>/advisory.json" not in skill
    assert "/data/advisories/<year>.json" in skill
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_ui_assets.py -v`
Expected: FAIL — both docs still reference the old per-ID path

- [ ] **Step 3: Implement**

In `ui/llms.txt`, replace the last line:

```text
- Advisory detail: /data/advisories/<zdi_id>/advisory.json
```

with:

```text
- Advisory detail: /data/advisories/<year>.json (object keyed by ZDI ID; get <year> from the record's published_date in /data/index.json)
```

In `ui/skill.md`, replace this table row:

```markdown
| `/data/advisories/<zdi_id>/advisory.json` | Full structured published advisory. |
```

with:

```markdown
| `/data/advisories/<year>.json` | Full structured advisory details for that year, keyed by ZDI ID. |
```

And replace the `## Usage` section:

```markdown
## Usage

Fetch `/data/index.json` once per session and filter client-side. For full context on a published advisory, fetch its `advisory.json` using the ZDI ID.

Upcoming advisories use ZDI-CAN IDs and do not have detail pages until public disclosure.
```

with:

```markdown
## Usage

Fetch `/data/index.json` once per session and filter client-side. Each record includes `published_date`. For full detail on a published advisory, take the year from its `published_date` (first 4 characters), fetch `/data/advisories/<year>.json`, and look up the record by ZDI ID.

Upcoming advisories use ZDI-CAN IDs and do not have detail pages until public disclosure.
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_ui_assets.py -v`
Expected: PASS

- [ ] **Step 5: Run the full suite and commit**

```bash
pytest tests/ -v
git add ui/llms.txt ui/skill.md tests/test_ui_assets.py
git commit -m "docs: document year-chunked advisory endpoint for agents"
```

---

## Milestone 4: One-time data migration

### Task 10: Write and test the migration script

**Files:**
- Create: `scripts/migrate_advisories_to_year_chunks.py` (temporary — deleted in Task 12)
- Test: `tests/test_migration_script.py` (temporary — deleted in Task 12)

**Interfaces:**
- Produces: `migrate(data_dir: Path) -> dict` returning `{"read_count": int, "written_count": int, "year_count": int, "unknown_count": int}`

- [ ] **Step 1: Write the failing tests**

Create `tests/test_migration_script.py`:

```python
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from migrate_advisories_to_year_chunks import migrate  # noqa: E402


def test_migrate_groups_by_published_date_year(tmp_path):
    (tmp_path / "published.json").write_text(
        json.dumps([
            {"zdi_id": "ZDI-26-001", "published_date": "2026-01-01"},
            {"zdi_id": "ZDI-25-999", "published_date": "2025-12-31"},
        ]),
        encoding="utf-8",
    )
    for zdi_id in ("ZDI-26-001", "ZDI-25-999"):
        advisory_dir = tmp_path / "advisories" / zdi_id
        advisory_dir.mkdir(parents=True)
        (advisory_dir / "advisory.json").write_text(
            json.dumps({"zdi_id": zdi_id, "title": f"Title for {zdi_id}"}), encoding="utf-8"
        )

    summary = migrate(tmp_path)

    assert summary == {"read_count": 2, "written_count": 2, "year_count": 2, "unknown_count": 0}
    year_2026 = json.loads((tmp_path / "advisories" / "2026.json").read_text(encoding="utf-8"))
    year_2025 = json.loads((tmp_path / "advisories" / "2025.json").read_text(encoding="utf-8"))
    assert year_2026["ZDI-26-001"]["title"] == "Title for ZDI-26-001"
    assert year_2025["ZDI-25-999"]["title"] == "Title for ZDI-25-999"


def test_migrate_falls_back_to_advisory_date_then_unknown(tmp_path):
    (tmp_path / "published.json").write_text(json.dumps([]), encoding="utf-8")
    old_dir = tmp_path / "advisories" / "ZDI-10-001"
    old_dir.mkdir(parents=True)
    (old_dir / "advisory.json").write_text(
        json.dumps({"zdi_id": "ZDI-10-001", "title": "Old one", "advisory_date": "2010-05-01"}),
        encoding="utf-8",
    )
    orphan_dir = tmp_path / "advisories" / "ZDI-00-000"
    orphan_dir.mkdir(parents=True)
    (orphan_dir / "advisory.json").write_text(
        json.dumps({"zdi_id": "ZDI-00-000", "title": "No dates anywhere"}), encoding="utf-8"
    )

    summary = migrate(tmp_path)

    assert summary == {"read_count": 2, "written_count": 2, "year_count": 2, "unknown_count": 1}
    year_2010 = json.loads((tmp_path / "advisories" / "2010.json").read_text(encoding="utf-8"))
    unknown = json.loads((tmp_path / "advisories" / "unknown.json").read_text(encoding="utf-8"))
    assert year_2010["ZDI-10-001"]["title"] == "Old one"
    assert unknown["ZDI-00-000"]["title"] == "No dates anywhere"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_migration_script.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'migrate_advisories_to_year_chunks'`

- [ ] **Step 3: Implement**

Create `scripts/migrate_advisories_to_year_chunks.py`:

```python
#!/usr/bin/env python3
"""One-time migration: consolidate data/advisories/<id>/advisory.json files
into data/advisories/<year>.json. Run once locally, no network calls.
Delete this script (and tests/test_migration_script.py) once the migration
has been verified and committed.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def migrate(data_dir: Path) -> dict:
    published = json.loads((data_dir / "published.json").read_text(encoding="utf-8"))
    published_lookup = {record["zdi_id"]: record.get("published_date") for record in published}

    grouped: dict[str, dict[str, dict]] = {}
    read_count = 0
    unknown_count = 0
    for path in sorted((data_dir / "advisories").glob("*/advisory.json")):
        detail = json.loads(path.read_text(encoding="utf-8"))
        zdi_id = detail["zdi_id"]
        read_count += 1
        candidate = published_lookup.get(zdi_id) or detail.get("advisory_date") or ""
        year = candidate[:4] if candidate[:4].isdigit() else "unknown"
        if year == "unknown":
            unknown_count += 1
        grouped.setdefault(year, {})[zdi_id] = detail

    written_count = 0
    for year, details_by_id in grouped.items():
        out_path = data_dir / "advisories" / f"{year}.json"
        out_path.write_text(
            json.dumps(details_by_id, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        written_count += len(details_by_id)

    return {
        "read_count": read_count,
        "written_count": written_count,
        "year_count": len(grouped),
        "unknown_count": unknown_count,
    }


def main() -> None:
    summary = migrate(ROOT / "data")
    print(
        f"Read {summary['read_count']} advisory files, wrote {summary['written_count']} "
        f"records across {summary['year_count']} year files, "
        f"{summary['unknown_count']} fell into 'unknown'."
    )


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_migration_script.py -v`
Expected: 2 passed

- [ ] **Step 5: Commit**

```bash
git add scripts/migrate_advisories_to_year_chunks.py tests/test_migration_script.py
git commit -m "feat: add one-time advisory-to-year-chunk migration script"
```

---

### Task 11: Run the migration against real data and verify no data loss

**Files:** none modified by code — this task operates on `data/`

This task has no new tests (the migration logic is already tested in Task 10); it's a verified execution runbook.

- [ ] **Step 1: Record the pre-migration baseline**

```bash
python3 -c "import json; print(len(json.load(open('data/published.json'))))"
find data/advisories -name advisory.json | wc -l
```
Expected: both print `16992` (or whatever the current real count is — record the actual number and use it in the next check, don't assume it's still exactly 16992)

- [ ] **Step 2: Run the migration**

```bash
python3 scripts/migrate_advisories_to_year_chunks.py
```
Expected output: `Read 16992 advisory files, wrote 16992 records across N year files, 0 fell into 'unknown'.` — the read/written counts must match the Step 1 baseline exactly, and `unknown_count` must be `0` for current real data (every real advisory has a `published_date`).

- [ ] **Step 3: Verify total record count across year-chunk files matches**

```bash
python3 -c "
import glob, json
total = 0
for path in glob.glob('data/advisories/*.json'):
    total += len(json.load(open(path)))
print(total)
"
```
Expected: matches the Step 1 baseline count exactly

- [ ] **Step 4: Verify `zdi index` (the now-updated CLI, from Task 6) agrees with the migration script's output**

```bash
python3 -m zdi.cli index
```
Expected: `Rebuilt index for <N> published and <M> upcoming advisories` where N matches the baseline. This confirms the "permanent" code path (`load_advisory_chunks` + `write_public_data`, both already updated in Tasks 2 and 4) reads what the migration script wrote and reproduces it correctly — if this step fails or changes counts, stop and debug before proceeding; do not delete the old per-ID tree yet.

- [ ] **Step 5: Remove the old per-ID tree and the temporary migration tooling**

```bash
git rm -r data/advisories/ZDI-*
git rm scripts/migrate_advisories_to_year_chunks.py
git rm tests/test_migration_script.py
```

- [ ] **Step 6: Run the full test suite**

```bash
pytest tests/ -v
```
Expected: all tests pass (the migration script's own tests are gone since the script is gone — this is expected, not a regression, since Task 10 already proved the logic correct and Step 4 above re-verified it against real data through the permanent code path)

- [ ] **Step 7: Commit**

```bash
git add data/advisories/
git commit -m "chore: migrate advisory data to year-chunked files"
```

---

## Milestone 5: Full local validation before opening a PR

### Task 12: End-to-end validation

**Files:** none modified — this is a verification pass, matching the spec's "End-to-end local validation (required before opening the PR, not optional)" section

- [ ] **Step 1: Run the full test suite one more time**

```bash
pytest tests/ -v
```
Expected: all tests pass

- [ ] **Step 2: Run a real `zdi run` and confirm the ongoing caching path works**

```bash
python3 -m zdi.cli run --workers 32
```
Expected: published/upcoming counts match current production (confirm against the Milestone 4 baseline — should be very close, possibly a handful more if ZDI published new advisories since). Watch the console output: this run should complete much faster than the original full re-scrape, since almost every record should now hit cache via the year-chunk files instead of re-fetching over the network. If it looks like every record is being re-fetched (no speedup at all vs. a cold run), stop — that indicates the cache-lookup wiring from Task 5 is broken, not something to paper over.

- [ ] **Step 3: Run `build.sh` and confirm it passes**

```bash
bash build.sh
```
Expected: succeeds, `COUNT` in the final "Done:" line is now a real non-zero number of advisories (not the `0` seen in Task 7 Step 4, since the data is migrated now)

- [ ] **Step 4: Serve `dist/` locally and validate in a real browser**

```bash
cd dist && python3 -m http.server 8099
```

In a separate step (using the Playwright MCP tools, same approach as the earlier parser-fix validation in this project):
- Navigate to `http://127.0.0.1:8099/`
- Confirm the list view loads and shows a non-zero "Showing X of N records" count
- Click into any advisory row
- Confirm the detail view renders (title, metadata, vulnerability details) — this is the real proof that `app.js`'s new year-chunk fetch (Task 8) works against real data, not just the source-string test
- Confirm the "JSON" link on the detail page resolves to a working `/data/advisories/<year>.json` URL

- [ ] **Step 5: Spot-check a few year-chunk files directly**

```bash
curl -s http://127.0.0.1:8099/data/advisories/2026.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d), list(d)[:3])"
curl -s http://127.0.0.1:8099/data/advisories/2010.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d), list(d)[:3])"
```
Expected: both return real record counts and ZDI IDs, not empty objects

- [ ] **Step 6: Stop the local server**

```bash
pkill -f "http.server 8099"
```

- [ ] **Step 7: Push the branch (do not open a PR without explicit go-ahead — this branch has already been created per user instruction; opening the PR is a separate, explicit step to confirm with the user first, same as the parser-fix PR)**

```bash
git push -u origin redesign/year-chunked-advisory-data
```

---

## Self-Review Notes

- **Spec coverage:** Architecture (Task 1-4), caching performance requirement (Task 5, explicit in-memory preload), guard rail (Task 3), frontend contract (Task 8), docs (Task 9), migration ordering to avoid a needless re-scrape (Tasks 10-11, matches the corrected spec sequencing), end-to-end local validation (Task 12), branch discipline (Global Constraints + Task 12 Step 7). The `_redirects` compatibility shim was explicitly out of scope in the spec's Non-goals — no task implements it, correctly.
- **Type consistency check:** `advisory_year(zdi_id, published_lookup, detail=None)` signature is identical everywhere it's called (Tasks 1, 5). `load_advisory_chunks(data_dir) -> dict[str, dict[str, AdvisoryDetail]]` return shape is consumed identically in Tasks 5 and 6. `write_public_data`'s public signature never changes, so `zdi/cli.py`'s `run` and `scrape` commands need no changes at all — confirmed by the earlier repo-wide grep, no task touches them.
- **No placeholders:** every step above shows complete, real code — no "add error handling here" or "similar to Task N" shortcuts.
