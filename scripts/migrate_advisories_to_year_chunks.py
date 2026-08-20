#!/usr/bin/env python3
"""One-time migration: consolidate data/advisories/<id>/advisory.json files
into data/advisories/<year>.json. Run once locally, no network calls.
Delete this script (and tests/test_migration_script.py) once the migration
has been verified and committed.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def migrate(data_dir: Path) -> dict:
    published = json.loads((data_dir / "published.json").read_text(encoding="utf-8"))
    published_lookup = {record["zdi_id"]: record.get("published_date") for record in published}

    grouped: dict[str, dict[str, dict]] = {}
    read_count = 0
    unknown_count = 0
    for path in sorted((data_dir / "advisories").glob("*/advisory.json")):
        detail = json.loads(path.read_text(encoding="utf-8"))
        zdi_id = detail["zdi_id"]
        read_count += 1
        candidate = published_lookup.get(zdi_id) or detail.get("advisory_date") or ""
        year = candidate[:4] if candidate[:4].isdigit() else "unknown"
        if year == "unknown":
            unknown_count += 1
        grouped.setdefault(year, {})[zdi_id] = detail

    written_count = 0
    for year, details_by_id in grouped.items():
        out_path = data_dir / "advisories" / f"{year}.json"
        out_path.write_text(
            json.dumps(details_by_id, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        written_count += len(details_by_id)

    return {
        "read_count": read_count,
        "written_count": written_count,
        "year_count": len(grouped),
        "unknown_count": unknown_count,
    }


def main() -> None:
    summary = migrate(ROOT / "data")
    print(
        f"Read {summary['read_count']} advisory files, wrote {summary['written_count']} "
        f"records across {summary['year_count']} year files, "
        f"{summary['unknown_count']} fell into 'unknown'."
    )


if __name__ == "__main__":
    main()
