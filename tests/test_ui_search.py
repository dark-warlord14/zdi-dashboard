from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_search_filter_focus_is_restored_after_list_rerender():
    app_js = (ROOT / "ui" / "js" / "app.js").read_text(encoding="utf-8")

    assert 'data-filter="search"' in app_js
    assert "captureFilterFocus()" in app_js
    assert "restoreFilterFocus(focusState)" in app_js
