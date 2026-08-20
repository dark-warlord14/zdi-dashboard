from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_ui_assets_and_agent_files_exist():
    required = [
        ROOT / "ui" / "index.html",
        ROOT / "ui" / "css" / "app.css",
        ROOT / "ui" / "js" / "app.js",
        ROOT / "ui" / "js" / "components.js",
        ROOT / "ui" / "js" / "vendor" / "chart.umd.min.js",
        ROOT / "ui" / "js" / "vendor" / "markdown-it.min.js",
        ROOT / "ui" / "skill.md",
        ROOT / "ui" / "schema.json",
        ROOT / "ui" / "llms.txt",
    ]

    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    assert missing == []


def test_index_exposes_published_upcoming_and_agents():
    html = (ROOT / "ui" / "index.html").read_text(encoding="utf-8")

    assert "ZDI Advisories" in html
    assert 'data-nav="published"' in html
    assert 'data-nav="upcoming"' in html
    assert "/skill.md" in html
    assert "js/app.js" in html


def test_llms_txt_and_skill_md_document_year_chunked_advisories():
    llms = (ROOT / "ui" / "llms.txt").read_text(encoding="utf-8")
    skill = (ROOT / "ui" / "skill.md").read_text(encoding="utf-8")

    assert "/data/advisories/<zdi_id>/advisory.json" not in llms
    assert "/data/advisories/<year>.json" in llms
    assert "/data/advisories/<zdi_id>/advisory.json" not in skill
    assert "/data/advisories/<year>.json" in skill
