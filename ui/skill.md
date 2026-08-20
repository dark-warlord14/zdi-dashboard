---
name: zdi-advisories
description: Query Zero Day Initiative published and upcoming advisories by ZDI ID, ZDI-CAN, CVE, vendor, CVSS, date, deadline, or vulnerability text.
---

# ZDI Advisories

Static JSON archive for Zero Day Initiative advisories.

## Endpoints

| URL | Purpose |
| --- | --- |
| `/data/index.json` | Unified lightweight index for published and upcoming records. |
| `/data/published.json` | Published advisory list records. |
| `/data/upcoming.json` | Upcoming advisory list records. |
| `/data/stats.json` | Precomputed aggregates. |
| `/data/advisories/<year>.json` | Full structured advisory details for that year, keyed by ZDI ID. |
| `/schema.json` | JSON Schema for published advisory detail records. |

## Usage

Fetch `/data/index.json` once per session and filter client-side. Each record includes `published_date`. For full detail on a published advisory, take the year from its `published_date` (first 4 characters), fetch `/data/advisories/<year>.json`, and look up the record by ZDI ID.

Upcoming advisories use ZDI-CAN IDs and do not have detail pages until public disclosure.
