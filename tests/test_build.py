import subprocess
import shutil
from pathlib import Path

from zdi.models import AdvisoryDetail, PublishedAdvisory, UpcomingAdvisory
from zdi.scraper import write_public_data


ROOT = Path(__file__).resolve().parents[1]


def seed_data(data_dir: Path) -> None:
    published = [
        PublishedAdvisory(
            zdi_id="ZDI-26-040",
            zdi_can="ZDI-CAN-27057",
            vendor="Discord",
            cve="CVE-2026-0776",
            cvss=7.3,
            published_date="2026-01-09",
            updated_date="2026-01-09",
            title="Discord Client Privilege Escalation",
            url="https://www.zerodayinitiative.com/advisories/ZDI-26-040/",
        )
    ]
    upcoming = [
        UpcomingAdvisory(
            zdi_can="ZDI-CAN-30796",
            vendor="Docker",
            cvss=6.5,
            reported_date="2026-04-30",
            deadline="2026-08-28",
            discoverer="Nitesh Surana",
        )
    ]
    details = {
        "ZDI-26-040": AdvisoryDetail(
            zdi_id="ZDI-26-040",
            title="Discord Client Privilege Escalation",
            source_url="https://www.zerodayinitiative.com/advisories/ZDI-26-040/",
        )
    }
    write_public_data(data_dir, published, upcoming, details)


def test_build_script_creates_cloudflare_dist():
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        project = Path(tmp) / "project"
        project.mkdir()
        shutil.copytree(ROOT / "ui", project / "ui")
        shutil.copy(ROOT / "_headers", project / "_headers")
        shutil.copy(ROOT / "build.sh", project / "build.sh")
        seed_data(project / "data")

        subprocess.run(["bash", "build.sh"], cwd=project, check=True)

        required = [
            project / "dist" / "index.html",
            project / "dist" / "data" / "index.json",
            project / "dist" / "data" / "advisories" / "2026.json",
            project / "dist" / "skill.md",
            project / "dist" / "schema.json",
            project / "dist" / "llms.txt",
            project / "dist" / "_headers",
        ]
        missing = [str(path.relative_to(project)) for path in required if not path.exists()]
        assert missing == []
