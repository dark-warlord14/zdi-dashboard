import json

import pytest

from zdi.models import AdvisoryDetail, PublishedAdvisory, UpcomingAdvisory
from zdi.scraper import guard_against_empty_scrape, write_public_data
from zdi.stats import build_stats


def sample_published() -> PublishedAdvisory:
    return PublishedAdvisory(
        zdi_id="ZDI-26-040",
        zdi_can="ZDI-CAN-27057",
        vendor="Discord",
        cve="CVE-2026-0776",
        cvss=7.3,
        published_date="2026-01-09",
        updated_date="2026-01-09",
        title="Discord Client Privilege Escalation",
        url="https://www.zerodayinitiative.com/advisories/ZDI-26-040/",
        detail_path="advisories/ZDI-26-040",
    )


def sample_upcoming() -> UpcomingAdvisory:
    return UpcomingAdvisory(
        zdi_can="ZDI-CAN-30796",
        vendor="Docker",
        cvss=6.5,
        reported_date="2026-04-30",
        deadline="2026-08-28",
        discoverer="Nitesh Surana",
    )


def sample_detail() -> AdvisoryDetail:
    return AdvisoryDetail(
        zdi_id="ZDI-26-040",
        zdi_can="ZDI-CAN-27057",
        title="Discord Client Privilege Escalation",
        advisory_date="2026-01-09",
        cve="CVE-2026-0776",
        cvss=7.3,
        cvss_vector="AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H",
        affected_vendors=["Discord"],
        affected_products=["Client"],
        vulnerability_details="Local attackers can escalate privileges.",
        source_url="https://www.zerodayinitiative.com/advisories/ZDI-26-040/",
    )


def test_build_stats_counts_core_dimensions():
    stats = build_stats([sample_published()], [sample_upcoming()])

    assert stats.total_published == 1
    assert stats.total_upcoming == 1
    assert stats.high_cvss == 1
    assert stats.cve_coverage == 1
    assert stats.by_year == {"2026": 1}
    assert stats.by_vendor["Discord"] == 1
    assert stats.by_vendor["Docker"] == 1
    assert stats.by_cvss_band["high"] == 1


def test_write_public_data_creates_index_and_detail_files(tmp_path):
    write_public_data(tmp_path, [sample_published()], [sample_upcoming()], {"ZDI-26-040": sample_detail()})

    index = json.loads((tmp_path / "index.json").read_text(encoding="utf-8"))
    published = json.loads((tmp_path / "published.json").read_text(encoding="utf-8"))
    upcoming = json.loads((tmp_path / "upcoming.json").read_text(encoding="utf-8"))
    detail_json = tmp_path / "advisories" / "ZDI-26-040" / "advisory.json"

    assert index[0]["id"] == "ZDI-26-040"
    assert index[0]["description_snippet"] == "Local attackers can escalate privileges."
    assert "detail_markdown" not in index[0]
    assert index[1]["id"] == "ZDI-CAN-30796"
    assert published[0]["zdi_id"] == "ZDI-26-040"
    assert published[0]["description_snippet"] == "Local attackers can escalate privileges."
    assert upcoming[0]["zdi_can"] == "ZDI-CAN-30796"
    assert detail_json.exists()


def test_guard_against_empty_scrape_raises_when_published_collapses(tmp_path):
    (tmp_path / "published.json").write_text(json.dumps([{"id": i} for i in range(20)]), encoding="utf-8")

    with pytest.raises(RuntimeError):
        guard_against_empty_scrape(tmp_path, [], [sample_upcoming()])


def test_guard_against_empty_scrape_allows_normal_fluctuation(tmp_path):
    (tmp_path / "published.json").write_text(json.dumps([{"id": i} for i in range(20)]), encoding="utf-8")

    guard_against_empty_scrape(tmp_path, [sample_published() for _ in range(18)], [sample_upcoming()])


def test_guard_against_empty_scrape_ignores_missing_existing_file(tmp_path):
    guard_against_empty_scrape(tmp_path, [], [])
