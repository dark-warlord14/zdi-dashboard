from pathlib import Path

from zdi.parser import extract_vector, parse_advisory_detail, parse_published, parse_upcoming, parse_years


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


def test_extract_vector_from_query_param():
    url = "http://nvd.nist.gov/cvss.cfm?calculator&version=3.0&vector=AV:L/AC:L/PR:L/UI:N/S:C/C:N/I:N/A:H"
    assert extract_vector(url) == "AV:L/AC:L/PR:L/UI:N/S:C/C:N/I:N/A:H"


def test_extract_vector_from_url_fragment():
    url = "https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H"
    assert extract_vector(url) == "AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H"


def test_extract_vector_returns_none_when_absent():
    assert extract_vector("https://www.first.org/cvss/calculator/3.0") is None
    assert extract_vector(None) is None


def test_parse_published_skips_rows_with_too_few_cells():
    html = """
    <table><tbody>
      <tr class="advisory-row"><td>ZDI-26-999</td><td>only one cell besides id</td></tr>
    </tbody></table>
    """
    assert parse_published(html) == []


def test_parse_upcoming_skips_rows_with_too_few_cells():
    html = """
    <table><tbody>
      <tr class="advisory-row"><td>ZDI-CAN-1</td><td>vendor</td></tr>
    </tbody></table>
    """
    assert parse_upcoming(html) == []


def test_parse_published_handles_multiple_rows():
    html = """
    <table><tbody>
      <tr class="advisory-row">
        <td><a href="/advisories/ZDI-26-001/">ZDI-26-001</a></td>
        <td>ZDI-CAN-1</td><td>VendorA</td><td>CVE-2026-0001</td><td>5.0</td>
        <td>2026-01-01</td><td>2026-01-01</td><td>Title One</td>
      </tr>
      <tr class="advisory-row">
        <td><a href="/advisories/ZDI-26-002/">ZDI-26-002</a></td>
        <td>ZDI-CAN-2</td><td>VendorB</td><td>CVE-2026-0002</td><td>9.8</td>
        <td>2026-01-02</td><td>2026-01-02</td><td>Title Two</td>
      </tr>
    </tbody></table>
    """
    records = parse_published(html)
    assert [r.zdi_id for r in records] == ["ZDI-26-001", "ZDI-26-002"]
    assert records[1].cvss == 9.8


def test_parse_advisory_detail_affected_vendor_without_link_excludes_label():
    html = """
    <article>
      <h1>Some Title</h1>
      <div id="metadata-col">
        <div class="metadata-row">
          <span class="metadata-value">ZDI-06-001</span>
          <span class="metadata-value">ZDI-CAN-011</span>
        </div>
        <div class="metadata-row">
          <p class="metadata-label">Affected Vendors</p>
          <span class="metadata-value">Clam AntiVirus</span>
        </div>
      </div>
      <div class="content-article"><div class="prose"></div></div>
    </article>
    """
    detail = parse_advisory_detail(html, source_url="https://example.com/advisories/ZDI-06-001/")
    assert detail.affected_vendors == ["Clam AntiVirus"]


def test_parse_advisory_detail_handles_missing_metadata_gracefully():
    html = """
    <article>
      <h1>Some Title</h1>
      <div class="content-article"><div class="prose"></div></div>
    </article>
    """
    detail = parse_advisory_detail(html, source_url="https://example.com/advisories/ZDI-26-999/")
    assert detail.title == "Some Title"
    assert detail.zdi_id == ""
    assert detail.zdi_can is None
    assert detail.cve is None
    assert detail.cvss is None
    assert detail.affected_vendors == []
    assert detail.disclosure_timeline == []
