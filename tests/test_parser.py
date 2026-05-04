from pathlib import Path

from zdi.parser import parse_advisory_detail, parse_published, parse_upcoming, parse_years


FIXTURES = Path(__file__).parent / "fixtures"


def read_fixture(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


def test_parse_years_from_published_page():
    assert parse_years(read_fixture("published.html")) == [2026, 2025]


def test_parse_published_row():
    records = parse_published(read_fixture("published.html"))

    assert len(records) == 1
    record = records[0]
    assert record.zdi_id == "ZDI-26-040"
    assert record.zdi_can == "ZDI-CAN-27057"
    assert record.vendor == "Discord"
    assert record.cve == "CVE-2026-0776"
    assert record.cvss == 7.3
    assert record.published_date == "2026-01-09"
    assert record.updated_date == "2026-01-09"
    assert record.url == "https://www.zerodayinitiative.com/advisories/ZDI-26-040/"
    assert "Discord Client" in record.title


def test_parse_upcoming_row():
    records = parse_upcoming(read_fixture("upcoming.html"))

    assert len(records) == 1
    record = records[0]
    assert record.zdi_can == "ZDI-CAN-30796"
    assert record.vendor == "Docker"
    assert record.vendor_url == "https://www.docker.com/"
    assert record.cvss == 6.5
    assert record.cvss_vector == "AV:L/AC:L/PR:L/UI:N/S:C/C:N/I:N/A:H"
    assert record.reported_date == "2026-04-30"
    assert record.deadline == "2026-08-28"
    assert record.discoverer == "Nitesh Surana (niteshsurana.com) of TrendAI Research"


def test_parse_detail_page():
    detail = parse_advisory_detail(
        read_fixture("detail.html"),
        source_url="https://www.zerodayinitiative.com/advisories/ZDI-26-040/",
    )

    assert detail.zdi_id == "ZDI-26-040"
    assert detail.zdi_can == "ZDI-CAN-27057"
    assert detail.title.startswith("(0Day) Discord Client")
    assert detail.advisory_date == "2026-01-09"
    assert detail.cve == "CVE-2026-0776"
    assert detail.cvss == 7.3
    assert detail.cvss_vector == "AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H"
    assert detail.affected_vendors == ["Discord"]
    assert detail.affected_products == ["Client"]
    assert "local attackers" in detail.vulnerability_details
    assert "submitted the report" in detail.additional_details
    assert detail.disclosure_timeline[0] == "2025-07-08 - Vulnerability reported to vendor"
    assert detail.credit == "T. Doga Gelisli"
    assert detail.source_url == "https://www.zerodayinitiative.com/advisories/ZDI-26-040/"
