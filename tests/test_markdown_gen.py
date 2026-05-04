from zdi.markdown_gen import render_advisory_markdown
from zdi.models import AdvisoryDetail


def test_render_advisory_markdown_includes_agent_relevant_sections():
    detail = AdvisoryDetail(
        zdi_id="ZDI-26-040",
        zdi_can="ZDI-CAN-27057",
        title="Discord Client Uncontrolled Search Path Element Local Privilege Escalation Vulnerability",
        advisory_date="2026-01-09",
        cve="CVE-2026-0776",
        cvss=7.3,
        cvss_vector="AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H",
        affected_vendors=["Discord"],
        affected_products=["Client"],
        vulnerability_details="Local attackers can escalate privileges.",
        additional_details="ZDI submitted the report to the vendor.",
        disclosure_timeline=["2025-07-08 - Vulnerability reported to vendor"],
        credit="T. Doga Gelisli",
        source_url="https://www.zerodayinitiative.com/advisories/ZDI-26-040/",
    )

    markdown = render_advisory_markdown(detail)

    assert markdown.startswith("# ZDI-26-040")
    assert "## Metadata" in markdown
    assert "- **CVE:** CVE-2026-0776" in markdown
    assert "## Vulnerability Details" in markdown
    assert "Local attackers can escalate privileges." in markdown
    assert "## Disclosure Timeline" in markdown

