import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from migrate_advisories_to_year_chunks import migrate  # noqa: E402


def test_migrate_groups_by_published_date_year(tmp_path):
    (tmp_path / "published.json").write_text(
        json.dumps([
            {"zdi_id": "ZDI-26-001", "published_date": "2026-01-01"},
            {"zdi_id": "ZDI-25-999", "published_date": "2025-12-31"},
        ]),
        encoding="utf-8",
    )
    for zdi_id in ("ZDI-26-001", "ZDI-25-999"):
        advisory_dir = tmp_path / "advisories" / zdi_id
        advisory_dir.mkdir(parents=True)
        (advisory_dir / "advisory.json").write_text(
            json.dumps({"zdi_id": zdi_id, "title": f"Title for {zdi_id}"}), encoding="utf-8"
        )

    summary = migrate(tmp_path)

    assert summary == {"read_count": 2, "written_count": 2, "year_count": 2, "unknown_count": 0}
    year_2026 = json.loads((tmp_path / "advisories" / "2026.json").read_text(encoding="utf-8"))
    year_2025 = json.loads((tmp_path / "advisories" / "2025.json").read_text(encoding="utf-8"))
    assert year_2026["ZDI-26-001"]["title"] == "Title for ZDI-26-001"
    assert year_2025["ZDI-25-999"]["title"] == "Title for ZDI-25-999"


def test_migrate_falls_back_to_advisory_date_then_unknown(tmp_path):
    (tmp_path / "published.json").write_text(json.dumps([]), encoding="utf-8")
    old_dir = tmp_path / "advisories" / "ZDI-10-001"
    old_dir.mkdir(parents=True)
    (old_dir / "advisory.json").write_text(
        json.dumps({"zdi_id": "ZDI-10-001", "title": "Old one", "advisory_date": "2010-05-01"}),
        encoding="utf-8",
    )
    orphan_dir = tmp_path / "advisories" / "ZDI-00-000"
    orphan_dir.mkdir(parents=True)
    (orphan_dir / "advisory.json").write_text(
        json.dumps({"zdi_id": "ZDI-00-000", "title": "No dates anywhere"}), encoding="utf-8"
    )

    summary = migrate(tmp_path)

    assert summary == {"read_count": 2, "written_count": 2, "year_count": 2, "unknown_count": 1}
    year_2010 = json.loads((tmp_path / "advisories" / "2010.json").read_text(encoding="utf-8"))
    unknown = json.loads((tmp_path / "advisories" / "unknown.json").read_text(encoding="utf-8"))
    assert year_2010["ZDI-10-001"]["title"] == "Old one"
    assert unknown["ZDI-00-000"]["title"] == "No dates anywhere"
