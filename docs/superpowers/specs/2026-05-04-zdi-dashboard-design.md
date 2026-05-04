# ZDI Dashboard Design

Date: 2026-05-04

## Goal

Build a standalone static dashboard for Zero Day Initiative advisories. The site indexes both published and upcoming advisories, refreshes daily through GitHub Actions, deploys through Cloudflare Pages GitHub integration, and exposes clean data files plus `skill.md` so AI agents can consume the archive directly.

The UI should follow the visual system from `/Users/shantanughumade/workspace/AI-Fuzzing/VRP-REPORTS`: compact, dark/light capable, monochrome-first, table-focused, and optimized for security research workflows.

## Scope

The MVP will include:

- Full historical published advisory indexing.
- Current upcoming advisory indexing.
- Published advisory detail-page scraping.
- Stored public JSON and Markdown data for UI and agent consumers.
- Static dashboard UI with separate Published and Upcoming tabs.
- Search, multi-filtering, sorting, pagination, stats, and detail views.
- Daily GitHub Actions refresh that stores data in the repository.
- Cloudflare Pages deploy support.
- Agent-facing `skill.md`, `schema.json`, and `llms.txt`.

The MVP will not include:

- A server-side search API.
- A database.
- User accounts or saved searches.
- Change-history UI for end users.

## Recommended Approach

Use a static-first Python scraper plus static single-page app.

This keeps the system simple, cheap, portable, and easy for agents to consume. ZDI advisory volume is small enough for browser-side search and filtering, while stored JSON/Markdown records provide a stable API-like surface without needing a backend.

## Data Pipeline

The scraper will collect published advisory list pages from:

- `https://www.zerodayinitiative.com/advisories/published/`

For each published row, it will capture fields available in the list, including:

- ZDI ID
- ZDI-CAN ID
- Vendor
- CVE
- CVSS
- Published date
- Updated date
- Title
- Advisory URL

For each published advisory detail page, it will extract structured fields when present:

- Advisory date
- Affected products
- Vulnerability details
- Additional details
- Disclosure timeline
- Credit or discoverer
- CVSS vector
- Source and reference links
- Clean full-text body for search

The scraper will collect upcoming advisories from:

- `https://www.zerodayinitiative.com/advisories/upcoming/`

Upcoming records will include:

- ZDI-CAN ID
- Vendor
- CVSS
- Reported date
- Deadline
- Discoverer
- Vendor and CVSS links where present
- Status `upcoming`

## Public Data Files

The generated public data contract will be:

- `data/index.json`: unified lightweight index for UI and agents.
- `data/published.json`: list records for the Published tab.
- `data/upcoming.json`: list records for the Upcoming tab.
- `data/stats.json`: aggregate counters and chart data.
- `data/advisories/<zdi_id>/advisory.json`: full structured published advisory.
- `data/advisories/<zdi_id>/advisory.md`: generated Markdown advisory.
- `schema.json`: JSON Schema for advisory records.
- `skill.md`: agent usage guide.
- `llms.txt`: LLM discoverability manifest.

The UI and agents should only depend on these clean public files. Any scrape state, raw HTML cache, or update bookkeeping remains internal.

## UI Design

The UI will be adapted from the VRP-REPORTS dashboard structure:

- Sticky masthead with brand, tabs, stats link, agent link, and theme toggle.
- Dark and light themes using the same restrained visual language.
- KPI strip at the top of list views.
- Dense filter toolbar with search and multi-filter controls.
- Sortable, paginated tables.
- Compact badges for CVSS, CVE presence, and advisory state.
- Detail pages with structured metadata and rendered Markdown.

Main views:

- Published tab: ZDI ID, vendor, CVE, CVSS, published date, updated date, title, and detail/source actions.
- Upcoming tab: ZDI-CAN, vendor, CVSS, reported date, deadline, discoverer, and deadline state.
- Advisory detail route: generated Markdown, metadata, source links, CVE/NVD links, CVSS vector, affected products, timeline, and JSON/Markdown URLs.
- Stats view: published totals, upcoming totals, high-CVSS counts, top vendors, yearly trends, CVE coverage, and deadline aging.

Filters:

- Free-text search across IDs, title, vendor, CVE, affected products, and detail body text.
- Vendor.
- CVSS range or severity band.
- Year or date range.
- CVE present or missing for Published.
- Deadline state for Upcoming.

Filter, sort, tab, and page state will be encoded in the URL hash so views can be shared.

## Architecture

Repository structure:

```text
zdi-dashboard/
├── .github/workflows/update-data.yml
├── data/
├── docs/superpowers/specs/
├── tests/
├── ui/
│   ├── index.html
│   ├── css/app.css
│   ├── js/app.js
│   ├── js/components.js
│   ├── skill.md
│   ├── schema.json
│   └── llms.txt
├── zdi/
│   ├── cli.py
│   ├── config.py
│   ├── markdown_gen.py
│   ├── models.py
│   ├── parser.py
│   ├── scraper.py
│   ├── server.py
│   └── stats.py
├── build.sh
├── pyproject.toml
└── README.md
```

The Python package responsibilities:

- `models.py`: typed advisory/list/upcoming/stat models.
- `scraper.py`: HTTP fetch and pagination orchestration.
- `parser.py`: structured extraction from ZDI list and detail HTML.
- `markdown_gen.py`: generated advisory Markdown.
- `stats.py`: aggregate data generation.
- `cli.py`: commands for `run`, `scrape`, `index`, `serve`, and `status`.
- `server.py`: local static server for development.

## GitHub Actions And Deployment

The daily workflow will:

1. Install Python dependencies.
2. Run the scraper and rebuild data.
3. Run tests or at least schema/build validation.
4. Commit refreshed `data/` files when there are changes.
5. Build `dist/` for Cloudflare Pages.

Cloudflare Pages will deploy through GitHub integration from the generated static output. The build script will copy UI assets, public data, `_headers`, `skill.md`, `schema.json`, and `llms.txt` into `dist/`.

## Reliability

The scraper must be idempotent and safe to rerun.

Existing advisory detail records may be reused when the list metadata has not changed. When an advisory has a newer updated date, the detail record should be refreshed.

Network or parse failures should fail the CI run rather than silently publishing incomplete new data. Optional missing fields should become `null` or empty arrays, not malformed records.

Every advisory record must preserve its canonical ZDI source URL.

## Testing

Test coverage will focus on behavior with offline fixtures:

- Published list parser fixture.
- Upcoming list parser fixture.
- Published detail parser fixture.
- Index and stats generation.
- Markdown generation.
- Schema validity for generated records.
- Build output validation.
- UI smoke tests for data loading, tab switching, search, filters, sorting, pagination, and detail routes.

## Open Decisions

No open decisions remain for the MVP. The selected MVP is a static-first dashboard with full published history, upcoming advisories, detail-page scraping, stored JSON/Markdown data, separate UI tabs, daily GitHub Actions refresh, and Cloudflare Pages deployment.
