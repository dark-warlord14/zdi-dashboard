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
