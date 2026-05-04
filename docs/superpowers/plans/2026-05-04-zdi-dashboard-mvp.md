# ZDI Dashboard MVP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a static Zero Day Initiative advisory dashboard with daily data refresh, searchable UI, and agent-readable JSON/Markdown outputs.

**Architecture:** A Python package fetches ZDI HTML, parses published/upcoming/detail records, generates public JSON/Markdown/stats, and assembles a static UI. The browser app loads static data files and performs tabbed search, filtering, sorting, pagination, detail rendering, and stats locally.

**Tech Stack:** Python 3.10+, `requests`, `beautifulsoup4`, `pydantic`, `click`, `pytest`, vanilla HTML/CSS/JS, vendored Chart.js and markdown-it, GitHub Actions, Cloudflare Pages.

---

### Task 1: Project Skeleton And Fixtures

**Files:**
- Create: `zdi-dashboard/pyproject.toml`
- Create: `zdi-dashboard/README.md`
- Create: `zdi-dashboard/zdi/__init__.py`
- Create: `zdi-dashboard/zdi/config.py`
- Create: `zdi-dashboard/tests/fixtures/*.html`
- Create: `zdi-dashboard/tests/test_parser.py`

- [ ] Create package metadata with runtime and dev dependencies.
- [ ] Add a README with local setup, `zdi run`, `zdi serve`, and Cloudflare Pages notes.
- [ ] Save representative published, upcoming, and detail HTML fixtures based on the observed ZDI table structures.
- [ ] Write parser tests first for one published row, one upcoming row, available years, and one detail page.
- [ ] Run `python -m pytest tests/test_parser.py -v` and confirm tests fail because parser code does not exist.

### Task 2: Models And Parser

**Files:**
- Create: `zdi-dashboard/zdi/models.py`
- Create: `zdi-dashboard/zdi/parser.py`
- Modify: `zdi-dashboard/tests/test_parser.py`

- [ ] Define `PublishedAdvisory`, `UpcomingAdvisory`, and `AdvisoryDetail` Pydantic models.
- [ ] Implement HTML parsing with BeautifulSoup, normalizing whitespace, dates, CVSS floats, absolute URLs, and empty table cells.
- [ ] Parse detail table fields by row label: CVE ID, CVSS SCORE, AFFECTED VENDORS, AFFECTED PRODUCTS, VULNERABILITY DETAILS, ADDITIONAL DETAILS, DISCLOSURE TIMELINE, CREDIT.
- [ ] Run `python -m pytest tests/test_parser.py -v` and confirm parser tests pass.

### Task 3: Scraper, Markdown, Stats, And Data Generation

**Files:**
- Create: `zdi-dashboard/zdi/scraper.py`
- Create: `zdi-dashboard/zdi/markdown_gen.py`
- Create: `zdi-dashboard/zdi/stats.py`
- Create: `zdi-dashboard/zdi/cli.py`
- Create: `zdi-dashboard/tests/test_pipeline.py`
- Create: `zdi-dashboard/tests/test_markdown_gen.py`

- [ ] Write tests for Markdown generation, stats aggregation, and public data shape.
- [ ] Implement HTTP fetching with retries and a clear user agent.
- [ ] Discover published years from the current published page and fetch `?year=<year>` style URLs when supported, falling back to the current page shape if needed.
- [ ] Fetch detail pages for published advisories and reuse existing detail JSON when the list `updated_date` has not changed.
- [ ] Generate `data/published.json`, `data/upcoming.json`, `data/index.json`, `data/stats.json`, and per-advisory `advisory.json`/`advisory.md`.
- [ ] Add CLI commands: `zdi run`, `zdi scrape`, `zdi index`, `zdi serve`, `zdi status`.
- [ ] Run `python -m pytest tests/test_pipeline.py tests/test_markdown_gen.py -v` and confirm they pass.

### Task 4: Static UI And Agent Files

**Files:**
- Create: `zdi-dashboard/ui/index.html`
- Create: `zdi-dashboard/ui/css/app.css`
- Create: `zdi-dashboard/ui/js/app.js`
- Create: `zdi-dashboard/ui/js/components.js`
- Copy: `zdi-dashboard/ui/js/vendor/chart.umd.min.js`
- Copy: `zdi-dashboard/ui/js/vendor/markdown-it.min.js`
- Create: `zdi-dashboard/ui/skill.md`
- Create: `zdi-dashboard/ui/schema.json`
- Create: `zdi-dashboard/ui/llms.txt`
- Create: `zdi-dashboard/tests/test_ui_assets.py`

- [ ] Port the VRP-REPORTS visual system, changing branding and fields for ZDI.
- [ ] Implement separate Published and Upcoming tabs with shared search/filter/sort/pagination behavior.
- [ ] Implement advisory detail route backed by `advisory.md` and `advisory.json`.
- [ ] Implement Stats view using precomputed `stats.json`.
- [ ] Add agent files that document the public data contract.
- [ ] Run `python -m pytest tests/test_ui_assets.py -v` and confirm required assets/endpoints exist.

### Task 5: Build, CI, And Verification

**Files:**
- Create: `zdi-dashboard/build.sh`
- Create: `zdi-dashboard/_headers`
- Create: `zdi-dashboard/.github/workflows/update-data.yml`
- Create: `zdi-dashboard/tests/test_build.py`

- [ ] Write a build test that verifies `dist/index.html`, `dist/data/index.json`, `dist/skill.md`, `dist/schema.json`, and `dist/llms.txt`.
- [ ] Implement `build.sh` to copy UI, public data, `_headers`, and agent files into `dist/`.
- [ ] Implement the daily/manual GitHub Actions workflow to install dependencies, run tests, run `zdi run`, commit data changes, and leave Cloudflare Pages to deploy via GitHub integration.
- [ ] Run the full test suite with `python -m pytest -v`.
- [ ] Run `./build.sh` and verify `dist/` is complete.
- [ ] Start `zdi serve` and check the local dashboard URL.

## Self-Review

- Spec coverage: the plan covers the static scraper, full history, upcoming advisories, detail scraping, JSON/Markdown outputs, UI tabs, search/filter/sort, stats, `skill.md`, GitHub Actions, and Cloudflare Pages build output.
- Placeholder scan: no `TBD`, `TODO`, or unspecified implementation slots remain.
- Type consistency: model names and data file names match the approved design spec.
