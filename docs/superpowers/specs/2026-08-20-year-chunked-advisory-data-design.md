# Year-Chunked Advisory Data Storage Redesign

Date: 2026-08-20

## Problem

`data/advisories/<zdi_id>/advisory.json` stores one file per published advisory. As of 2026-08-20 that's 16,992 files, growing by roughly 1,500-2,000/year. This causes three concrete problems, not a style preference:

1. **Cloudflare Pages file ceiling.** The Free plan caps deployments at 20,000 files; paid plans report the same cap unless an undocumented env var is set correctly. At current growth this project hits that wall in 12-18 months and the site stops deploying entirely.
2. **Unbounded git bloat.** Every full re-scrape (e.g. after a parser fix) touches thousands of files in one commit, and git retains every historical version of every one of those files forever.
3. **Wasted re-fetching.** `load_existing_detail()` only reuses a cached record when `record.updated_date` is truthy and matches. 67% of published advisories (11,408/16,992) have no `updated_date`, so those records are re-fetched over the network and re-written on every single `zdi run`, whether or not anything changed. This is the direct cause of the previous incident's data corruption spreading further than it needed to, and it hammers ZDI's server for no reason.

## Goals

- Cap the number of advisory-detail files at roughly one per calendar year, permanently solving the Cloudflare file-count ceiling.
- Shrink routine daily commits back down to touching a handful of files, not thousands.
- Stop re-fetching/re-parsing advisories whose content can't have changed.
- Preserve the existing agent/LLM contract as closely as possible (`llms.txt`, `skill.md`, `schema.json` describe a stable way to fetch one advisory's full detail).
- No server-side compute. Cloudflare Pages stays a pure static deploy — this was an explicit constraint from the user after comparing against a Workers/KV/D1 approach.

## Non-goals

- Not solving this via Cloudflare KV/D1/Workers. Considered and rejected in favor of staying static-only.
- Not changing `index.json`, `published.json`, `upcoming.json`, or `stats.json` — these are already single consolidated files and work fine as-is.
- Not rewriting existing git history. The old per-file blobs stay in history; we only stop adding new ones.
- Not guaranteeing old deep links (`/data/advisories/<zdi_id>/advisory.json`) keep working. The site had zero real traffic during the outage; breaking these is an acceptable one-time cost. (A `_redirects`-based compatibility shim is possible but out of scope for this pass.)

## Architecture

Replace the per-advisory file tree with one JSON object per year:

```text
data/advisories/2005.json
data/advisories/2006.json
...
data/advisories/2026.json
data/advisories/unknown.json   # fallback bucket, see Edge Cases
```

Each file is an object keyed by ZDI ID, not an array, so lookup by ID is O(1) instead of a linear scan:

```json
{
  "ZDI-26-001": { "...full AdvisoryDetail fields as today...": "..." },
  "ZDI-26-002": { "...": "..." }
}
```

The year for a record comes from `PublishedAdvisory.published_date[:4]` — the same field `zdi/stats.py` already uses for `by_year`. This is the single source of truth for chunk assignment; do not derive it from parsing the ZDI ID string or from `AdvisoryDetail.advisory_date`.

## Data Flow Changes

**`zdi/scraper.py`:**

- `write_public_data()` groups `details` by year (via the matching `PublishedAdvisory.published_date` from the `published` list, joined by `zdi_id`) and writes one `data/advisories/<year>.json` per year present in the current run's full dataset. Every run regenerates each year's file completely from the in-memory dataset — the same "full rewrite" model `index.json`/`published.json` already use today. No incremental patching, no merge logic.
- `load_existing_detail()` / the caching path changes from "does `data/advisories/<id>/advisory.json` exist" to "does an entry for this ID exist in the already-loaded `data/advisories/<year>.json`". **Performance requirement:** load each existing year-chunk file into memory once at the start of a run (a `dict[str, dict[str, AdvisoryDetail]]` keyed by year), not once per record — with ~17,000 records this must not turn into 17,000 individual file reads of a multi-MB file.
- `guard_against_empty_scrape()` runs one additional check before any year-chunk file is overwritten: read the existing `data/advisories/<year>.json` (if present), and if it has N ≥ 10 keys while the newly-built chunk for that same year has fewer than N/2 keys, raise `RuntimeError` and write nothing for that run. Same failure mode this guard already protects against (a broken parser silently producing near-empty output), applied per year file instead of only to the top-level published/upcoming counts.

**Edge cases:**

- A record with a missing/empty `published_date` (none exist in current data, but don't assume that holds forever) goes into `data/advisories/unknown.json` instead of crashing or silently dropping the record.
- A year that goes from having entries to zero entries (shouldn't happen, but: ZDI has never un-published an advisory) is treated as the empty-scrape guard failing, not as "delete the file."

**`ui/js/app.js`:**

- The detail view currently does `fetch(`/data/advisories/${id}/advisory.json`)`. It already has the record's `published_date` from the list view that navigated to it. Change to: derive year from `published_date`, `fetch(`/data/advisories/${year}.json`)`, read `data[id]` from the result. Same number of HTTP requests as today.
- The "JSON" raw-view link in the detail view updates to point at the year-chunk file (with the understanding that it now shows the whole year, not just one record — acceptable, matches the new contract).

**Docs (`ui/llms.txt`, `ui/skill.md`):**

- Update the documented advisory-detail endpoint from `/data/advisories/<zdi_id>/advisory.json` to `/data/advisories/<year>.json`, and describe the lookup as "fetch the record's `published_date` from `/data/index.json` first, then fetch that year's file and look up by ZDI ID."
- `schema.json` is unaffected — it describes one advisory record's shape, which is unchanged; only the file it lives in changes.

**`build.sh`:**

- Replace the `find dist/data/advisories -name advisory.json | wc -l` advisory count with counting keys across `dist/data/advisories/*.json`.
- Keep (and extend) the existing zero-length guard: fail if any expected year file is missing or if the total key count across all year files is zero.

## Migration Plan

The existing per-ID files on disk already hold correct, freshly-scraped data (from the parser-fix PR). The migration must reshuffle that data into year buckets **without touching the network** — re-fetching 16,992 pages from ZDI just to change file layout would be the exact waste this redesign exists to eliminate. Ordering matters here to avoid a chicken-and-egg problem between "code that reads the old format" and "code that reads the new format":

1. Write a small one-off migration script (not part of the permanent `zdi` CLI — e.g. `scripts/migrate_advisories_to_year_chunks.py`, deleted after use) that:
   - Globs `data/advisories/*/advisory.json` (the current, pre-change layout) and loads every record.
   - Joins each record against `data/published.json` by `zdi_id` to get its `published_date` (falls back to the record's own `advisory_date` if a published-list match isn't found; falls back to `unknown` if neither is present).
   - Writes `data/advisories/<year>.json` (object keyed by ZDI ID) for every year bucket.
   - Prints a summary: total records read, total records written, any records that fell into `unknown`.
2. Run it locally. Verify the printed total written matches `data/published.json`'s record count exactly (16,992) — no data loss, nothing silently dropped.
3. Only now apply the code changes described above (`write_public_data`, `load_existing_detail`, `rebuild_index`'s glob, `build.sh`, `app.js`, docs) so they read/write the new chunked format going forward.
4. Run `zdi index` (rebuilds from what's already on disk, no network) to confirm the updated code produces byte-identical output to the migration script's output — this is the check that the "permanent" code path agrees with the one-off migration.
5. `git rm -r data/advisories/ZDI-*` to remove the old per-ID tree (old blobs remain in git history; only new commits stop referencing them as tracked files). Delete the one-off migration script.
6. Commit the new `data/advisories/<year>.json` files.

Only after all of this is validated locally should a real `zdi run` be executed, to confirm the *ongoing* (network-fetching) path also behaves correctly — at that point the vast majority of records should hit cache (found in their year's chunk file) and only genuinely new/changed advisories should trigger a network fetch. A near-100% cache-miss result at this stage would indicate the cache-lookup code is wrong, not a reason to proceed.

This all happens on `redesign/year-chunked-advisory-data`, not `main`. Nothing here touches production until the PR is reviewed and merged, same process as the parser-fix PR.

## Testing Strategy

Comprehensive coverage, matching what broke last time (a parser rewrite that touched real data with no test catching the label-leak bug until manual spot-checking found it):

- **Unit — chunking logic:** records group into the correct year file; a record with no matching year bucket falls into `unknown.json`; regenerating is idempotent (same input twice produces byte-identical output); an existing chunk file with cached entries is correctly reused instead of triggering a re-fetch.
- **Unit — guard rail:** per-year collapse (e.g. 2024's chunk drops from 1748 to 50 keys) raises, same shape as the existing `guard_against_empty_scrape` tests.
- **Unit — build.sh:** update `test_build.py` to seed year-chunked fixture data and assert `build.sh` produces the new layout and still rejects empty data.
- **Unit — frontend:** update/extend `test_ui_search.py`-style source assertions to confirm `app.js` no longer references the old per-ID URL pattern and does reference the year-chunk fetch + lookup.
- **Integration — migration:** given a directory of legacy per-ID files, the one-time migration produces year-chunk files containing every record with no loss, verified by comparing the full set of ZDI IDs before and after.
- **End-to-end local validation (required before opening the PR, not optional):**
  1. Run the full test suite.
  2. Run `zdi run` against the live site and confirm published/upcoming counts match current production (16,992 / 696).
  3. Run `build.sh` and confirm it passes its own validation.
  4. Serve `dist/` locally and, in a real browser, confirm: the list view loads and paginates, clicking into an advisory renders its full detail (fetched from the new year-chunk endpoint), and the raw JSON link resolves.
  5. Directly `curl` a couple of `/data/advisories/<year>.json` URLs from the served `dist/` and confirm the expected records are present by ID.

## Rollback Plan

If something is wrong post-merge: revert the PR. `main` still has full git history of the old per-file tree, so reverting restores the exact previous state (Cloudflare redeploys from the reverted commit). No data is destroyed by this migration since nothing is deleted from git history, only from the working tree going forward.

## Open Risks

- Old bookmarked/indexed per-advisory URLs (search engines, LLM crawlers that read `llms.txt` before this change) will 404 after merge. Accepted per Non-goals; can be revisited later with a `_redirects` compatibility layer if it turns out to matter.
- Year-chunk files for very active years (~2,000 records, full `AdvisoryDetail` payloads) are estimated at a few MB uncompressed; Cloudflare serves static assets with automatic compression, so this is not expected to be a real problem, but should be spot-checked during local validation (step 5 above already covers this).
