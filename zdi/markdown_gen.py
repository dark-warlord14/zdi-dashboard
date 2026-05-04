"""Generate Markdown records for published advisories."""

from zdi.models import AdvisoryDetail


def section(title: str, body: str | None) -> str:
    if not body:
        return ""
    return f"\n## {title}\n\n{body}\n"


def render_advisory_markdown(detail: AdvisoryDetail) -> str:
    lines = [
        f"# {detail.zdi_id}: {detail.title}",
        "",
        "## Metadata",
        "",
        f"- **ZDI ID:** {detail.zdi_id}",
        f"- **ZDI-CAN:** {detail.zdi_can or 'N/A'}",
        f"- **Date:** {detail.advisory_date or 'N/A'}",
        f"- **CVE:** {detail.cve or 'N/A'}",
        f"- **CVSS:** {detail.cvss if detail.cvss is not None else 'N/A'}",
        f"- **CVSS Vector:** {detail.cvss_vector or 'N/A'}",
        f"- **Affected Vendors:** {', '.join(detail.affected_vendors) or 'N/A'}",
        f"- **Affected Products:** {', '.join(detail.affected_products) or 'N/A'}",
        f"- **Credit:** {detail.credit or 'N/A'}",
        f"- **Source:** {detail.source_url}",
    ]
    markdown = "\n".join(lines)
    markdown += section("Vulnerability Details", detail.vulnerability_details)
    markdown += section("Additional Details", detail.additional_details)
    if detail.disclosure_timeline:
        markdown += "\n## Disclosure Timeline\n\n"
        markdown += "\n".join(f"- {item}" for item in detail.disclosure_timeline)
        markdown += "\n"
    return markdown.rstrip() + "\n"
