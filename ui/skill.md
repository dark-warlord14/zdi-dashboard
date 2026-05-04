---
name: zdi-advisories
description: Query Zero Day Initiative published and upcoming advisories by ZDI ID, ZDI-CAN, CVE, vendor, CVSS, date, deadline, or vulnerability text.
---

# ZDI Advisories

Static JSON and Markdown archive for Zero Day Initiative advisories.

## Endpoints

| URL | Purpose |
| --- | --- |
| `/data/index.json` | Unified lightweight index for published and upcoming records. |
| `/data/published.json` | Published advisory list records. |
| `/data/upcoming.json` | Upcoming advisory list records. |
| `/data/stats.json` | Precomputed aggregates. |
| `/data/advisories/<zdi_id>/advisory.json` | Full structured published advisory. |
| `/data/advisories/<zdi_id>/advisory.md` | Markdown advisory for LLM context. |
| `/schema.json` | JSON Schema for published advisory detail records. |

## Usage

Fetch `/data/index.json` once per session and filter client-side. For full context on a published advisory, fetch its `advisory.md` or `advisory.json` using the ZDI ID.

Upcoming advisories use ZDI-CAN IDs and do not have detail pages until public disclosure.
