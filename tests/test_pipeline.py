import json

import pytest

from zdi.models import AdvisoryDetail, PublishedAdvisory, UpcomingAdvisory
from zdi.scraper import (
    advisory_year,
    group_details_by_year,
    guard_against_empty_scrape,
    guard_against_year_chunk_collapse,
    load_advisory_chunks,
    write_advisory_chunks,
    write_public_data,
)
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
    year_chunk = json.loads((tmp_path / "advisories" / "2026.json").read_text(encoding="utf-8"))

    assert index[0]["id"] == "ZDI-26-040"
    assert index[0]["description_snippet"] == "Local attackers can escalate privileges."
    assert "detail_markdown" not in index[0]
    assert index[1]["id"] == "ZDI-CAN-30796"
    assert published[0]["zdi_id"] == "ZDI-26-040"
    assert published[0]["description_snippet"] == "Local attackers can escalate privileges."
    assert upcoming[0]["zdi_can"] == "ZDI-CAN-30796"
    assert year_chunk["ZDI-26-040"]["title"] == "Discord Client Privilege Escalation"


def test_guard_against_empty_scrape_raises_when_published_collapses(tmp_path):
    (tmp_path / "published.json").write_text(json.dumps([{"id": i} for i in range(20)]), encoding="utf-8")

    with pytest.raises(RuntimeError):
        guard_against_empty_scrape(tmp_path, [], [sample_upcoming()])


def test_guard_against_empty_scrape_allows_normal_fluctuation(tmp_path):
    (tmp_path / "published.json").write_text(json.dumps([{"id": i} for i in range(20)]), encoding="utf-8")

    guard_against_empty_scrape(tmp_path, [sample_published() for _ in range(18)], [sample_upcoming()])


def test_guard_against_empty_scrape_ignores_missing_existing_file(tmp_path):
    guard_against_empty_scrape(tmp_path, [], [])


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
