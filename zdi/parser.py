"""Parse ZDI advisory HTML pages."""

from __future__ import annotations

import re
from datetime import datetime
from html import unescape
from urllib.parse import parse_qs, urljoin, urlparse

from bs4 import BeautifulSoup

from zdi.config import BASE_URL
from zdi.models import AdvisoryDetail, PublishedAdvisory, UpcomingAdvisory


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    return re.sub(r"\s+", " ", unescape(value).replace("\xa0", " ")).strip()


def empty_to_none(value: str | None) -> str | None:
    cleaned = clean_text(value)
    if not cleaned or cleaned == "&nbsp;":
        return None
    return cleaned


def parse_float(value: str | None) -> float | None:
    if not value:
        return None
    match = re.search(r"\d+(?:\.\d+)?", value)
    return float(match.group(0)) if match else None


def extract_vector(url: str | None) -> str | None:
    if not url:
        return None
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    vector = query.get("vector", [None])[0]
    if vector:
        return vector
    match = re.search(r"CVSS:[\d.]+/(.+)", parsed.fragment)
    return match.group(1) if match else None


def parse_display_date(value: str | None) -> str | None:
    text = clean_text(value)
    if not text:
        return None
    text = re.sub(r"(\d+)(st|nd|rd|th)", r"\1", text)
    for fmt in ("%B %d, %Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(text, fmt).date().isoformat()
        except ValueError:
            continue
    return text


def parse_years(html: str) -> list[int]:
    soup = BeautifulSoup(html, "html.parser")
    years: list[int] = []
    for option in soup.select("#yearSelect option"):
        value = clean_text(option.get("value") or option.get_text())
        if value.isdigit():
            years.append(int(value))
    return years


def parse_published(html: str) -> list[PublishedAdvisory]:
    soup = BeautifulSoup(html, "html.parser")
    records: list[PublishedAdvisory] = []
    for row in soup.select("tr.advisory-row"):
        cells = row.find_all("td")
        if len(cells) < 8:
            continue
        zdi_id = clean_text(cells[0].get_text())
        id_link = cells[0].find("a")
        url = urljoin(BASE_URL, id_link.get("href", "")) if id_link else ""
        vendor_link = cells[2].find("a")
        records.append(
            PublishedAdvisory(
                zdi_id=zdi_id,
                zdi_can=empty_to_none(cells[1].get_text()),
                vendor=empty_to_none(cells[2].get_text()),
                vendor_url=urljoin(BASE_URL, vendor_link["href"]) if vendor_link and vendor_link.get("href") else None,
                cve=empty_to_none(cells[3].get_text()),
                cvss=parse_float(cells[4].get_text()),
                published_date=empty_to_none(cells[5].get_text()),
                updated_date=empty_to_none(cells[6].get_text()),
                title=clean_text(cells[7].get_text()),
                url=url,
            )
        )
    return records


def parse_upcoming(html: str) -> list[UpcomingAdvisory]:
    soup = BeautifulSoup(html, "html.parser")
    records: list[UpcomingAdvisory] = []
    for row in soup.select("tr.advisory-row"):
        cells = row.find_all("td")
        if len(cells) < 6:
            continue
        vendor_link = cells[1].find("a")
        cvss_link = cells[2].find("a")
        discoverer = clean_text(cells[5].get_text()).removeprefix("Discovered by:").strip()
        records.append(
            UpcomingAdvisory(
                zdi_can=clean_text(cells[0].get_text()),
                vendor=empty_to_none(cells[1].get_text()),
                vendor_url=vendor_link.get("href") if vendor_link and vendor_link.get("href") else None,
                cvss=parse_float(cells[2].get_text()),
                cvss_vector=extract_vector(cvss_link.get("href") if cvss_link else None),
                reported_date=empty_to_none(cells[3].get_text()),
                deadline=empty_to_none(cells[4].get_text()),
                discoverer=empty_to_none(discoverer),
            )
        )
    return records


def html_to_text(node) -> str | None:
    if node is None:
        return None
    return empty_to_none(node.get_text(" ", strip=True))


def link_texts(node) -> list[str]:
    values = [clean_text(a.get_text()) for a in node.find_all("a")]
    if values:
        return [v for v in values if v]
    text = html_to_text(node)
    return [text] if text else []


def metadata_value_node(row):
    value = row.select_one(".metadata-value")
    return value if value is not None else row


def sections_by_heading(container) -> dict[str, list]:
    sections: dict[str, list] = {}
    current: str | None = None
    for child in container.find_all(recursive=False):
        name = getattr(child, "name", None)
        if name == "h3":
            current = clean_text(child.get_text()).upper()
            sections[current] = []
            continue
        if name == "ul" and "blog-tags" in (child.get("class") or []):
            break
        if current is not None:
            sections[current].append(child)
    return sections


def section_text(nodes: list) -> str | None:
    texts = [html_to_text(node) for node in nodes if getattr(node, "name", None) == "p"]
    texts = [text for text in texts if text]
    return " ".join(texts) if texts else None


def parse_advisory_detail(html: str, source_url: str) -> AdvisoryDetail:
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article") or soup
    title = clean_text(article.find("h1").get_text() if article.find("h1") else "")

    calendar_icon = article.select_one('i[data-lucide="calendar"]')
    date_span = calendar_icon.find_next_sibling("span") if calendar_icon else None
    advisory_date = parse_display_date(date_span.get_text() if date_span else None)

    metadata: dict[str, object] = {}
    zdi_id = ""
    zdi_can: str | None = None
    metadata_col = article.select_one("#metadata-col")
    if metadata_col:
        rows = metadata_col.select(".metadata-row")
        if rows:
            id_spans = rows[0].select("span.metadata-value")
            zdi_id = clean_text(id_spans[0].get_text()) if id_spans else ""
            zdi_can = empty_to_none(id_spans[1].get_text()) if len(id_spans) > 1 else None
        for row in rows[1:]:
            label_node = row.find("p", class_="metadata-label")
            if label_node:
                metadata[clean_text(label_node.get_text()).upper()] = row

    cve_row = metadata.get("CVE ID")
    cve_link = cve_row.find("a") if cve_row else None
    cvss_row = metadata.get("CVSS SCORE")
    cvss_value_span = cvss_row.select_one("span.metadata-value") if cvss_row else None
    cvss_link = cvss_row.find("a") if cvss_row else None

    content_article = article.select_one(".content-article .prose") or article.select_one(".content-article")
    sections = sections_by_heading(content_article) if content_article else {}
    timeline_list = next((node for node in sections.get("DISCLOSURE TIMELINE", []) if getattr(node, "name", None) == "ul"), None)
    disclosure_timeline = [clean_text(li.get_text()) for li in timeline_list.find_all("li")] if timeline_list else []

    detail = AdvisoryDetail(
        zdi_id=zdi_id,
        zdi_can=zdi_can,
        title=title,
        advisory_date=advisory_date,
        cve=clean_text(cve_link.get_text()) or None if cve_link else None,
        cve_url=cve_link.get("href") if cve_link and cve_link.get("href") else None,
        cvss=parse_float(cvss_value_span.get_text()) if cvss_value_span else None,
        cvss_vector=extract_vector(cvss_link.get("href") if cvss_link else None),
        affected_vendors=link_texts(metadata_value_node(metadata["AFFECTED VENDORS"])) if metadata.get("AFFECTED VENDORS") else [],
        affected_products=link_texts(metadata_value_node(metadata["AFFECTED PRODUCTS"])) if metadata.get("AFFECTED PRODUCTS") else [],
        vulnerability_details=section_text(sections.get("VULNERABILITY DETAILS", [])),
        additional_details=section_text(sections.get("ADDITIONAL DETAILS", [])),
        disclosure_timeline=disclosure_timeline,
        credit=section_text(sections.get("CREDIT", [])),
        source_url=source_url,
    )
    detail.search_text = clean_text(" ".join(str(v) for v in detail.model_dump().values() if v))
    return detail
