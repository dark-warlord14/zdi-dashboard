from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_show_detail_fetches_year_chunk_instead_of_per_id_file():
    app_js = (ROOT / "ui" / "js" / "app.js").read_text(encoding="utf-8")

    assert "/data/advisories/${id}/advisory.json" not in app_js
    assert "/data/advisories/${year}.json" in app_js
    assert "published_date.slice(0, 4)" in app_js
