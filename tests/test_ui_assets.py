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
