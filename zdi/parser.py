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
    query = parse_qs(urlparse(url).query)
    vector = query.get("vector", [None])[0]
    return vector or None


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
    for option in soup.select("#select-year option"):
        value = clean_text(option.get("value") or option.get_text())
        if value.isdigit():
            years.append(int(value))
    return years


def parse_published(html: str) -> list[PublishedAdvisory]:
    soup = BeautifulSoup(html, "html.parser")
    records: list[PublishedAdvisory] = []
    for row in soup.select("tr#publishedAdvisories"):
        cells = row.find_all("td")
        if len(cells) < 8:
            continue
        title_link = cells[7].find("a")
        url = urljoin(BASE_URL, title_link.get("href", "")) if title_link else ""
        vendor_link = cells[2].find("a")
        records.append(
            PublishedAdvisory(
                zdi_id=clean_text(cells[0].get_text()),
                zdi_can=empty_to_none(cells[1].get_text()),
                vendor=empty_to_none(cells[2].get_text()),
                vendor_url=urljoin(BASE_URL, vendor_link["href"]) if vendor_link and vendor_link.get("href") else None,
                cve=empty_to_none(cells[3].get_text()),
                cvss=parse_float(cells[4].get_text()),
                published_date=empty_to_none(cells[5].get_text()),
                updated_date=empty_to_none(cells[6].get_text()),
                title=clean_text(title_link.get_text() if title_link else cells[7].get_text()),
                url=url,
                detail_path=f"advisories/{clean_text(cells[0].get_text())}",
            )
        )
    return records


def parse_upcoming(html: str) -> list[UpcomingAdvisory]:
    soup = BeautifulSoup(html, "html.parser")
    records: list[UpcomingAdvisory] = []
    for row in soup.select("tr#upcomingAdvisories"):
        cells = row.find_all("td")
        if len(cells) < 6:
            continue
        vendor_link = cells[1].find("a")
        cvss_link = cells[2].find("a")
        reported = clean_text(cells[3].contents[0] if cells[3].contents else cells[3].get_text())
        discoverer = clean_text(cells[5].get_text()).removeprefix("Discovered by:").strip()
        records.append(
            UpcomingAdvisory(
                zdi_can=clean_text(cells[0].get_text()),
                vendor=empty_to_none(cells[1].get_text()),
                vendor_url=vendor_link.get("href") if vendor_link and vendor_link.get("href") else None,
                cvss=parse_float(cells[2].get_text()),
                cvss_vector=extract_vector(cvss_link.get("href") if cvss_link else None),
                reported_date=empty_to_none(reported),
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


def parse_advisory_detail(html: str, source_url: str) -> AdvisoryDetail:
    soup = BeautifulSoup(html, "html.parser")
    content = soup.select_one(".advisories-details") or soup
    title = clean_text(content.find("h2").get_text() if content.find("h2") else "")
    id_text = content.find("h3").get_text(" ") if content.find("h3") else ""
    ids = re.findall(r"ZDI-\d{2,5}-\d{3,5}|ZDI-CAN-\d{3,6}", id_text)
    zdi_id = next((i for i in ids if i.startswith("ZDI-") and not i.startswith("ZDI-CAN-")), "")
    zdi_can = next((i for i in ids if i.startswith("ZDI-CAN-")), None)
    fields: dict[str, object] = {}

    for row in content.select("table tr"):
        cells = row.find_all("td")
        if len(cells) < 2:
            continue
        label = clean_text(cells[0].get_text()).upper()
        value = cells[1]
        fields[label] = value

    cve_node = fields.get("CVE ID")
    cvss_node = fields.get("CVSS SCORE")
    cve_link = cve_node.find("a") if cve_node else None
    cvss_link = cvss_node.find("a") if cvss_node else None
    timeline_node = fields.get("DISCLOSURE TIMELINE")
    timeline = [clean_text(li.get_text()) for li in timeline_node.find_all("li")] if timeline_node else []

    detail = AdvisoryDetail(
        zdi_id=zdi_id,
        zdi_can=zdi_can,
        title=title,
        advisory_date=parse_display_date(content.find("data").get_text() if content.find("data") else None),
        cve=html_to_text(cve_node),
        cve_url=cve_link.get("href") if cve_link and cve_link.get("href") else None,
        cvss=parse_float(html_to_text(cvss_node)),
        cvss_vector=extract_vector(cvss_link.get("href") if cvss_link else None),
        affected_vendors=link_texts(fields.get("AFFECTED VENDORS")),
        affected_products=link_texts(fields.get("AFFECTED PRODUCTS")),
        vulnerability_details=html_to_text(fields.get("VULNERABILITY DETAILS")),
        additional_details=html_to_text(fields.get("ADDITIONAL DETAILS")),
        disclosure_timeline=timeline,
        credit=html_to_text(fields.get("CREDIT")),
        source_url=source_url,
    )
    detail.search_text = clean_text(" ".join(str(v) for v in detail.model_dump().values() if v))
    return detail
