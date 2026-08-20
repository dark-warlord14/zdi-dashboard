# Deployment

This project is intended for Cloudflare Pages Git integration.

Live site: https://zdi-dashboard.pages.dev/

## GitHub

The repository is private. The production branch is `main`.

Daily data refresh is handled by `.github/workflows/update-data.yml`:

1. Install Python dependencies.
2. Run tests.
3. Run `zdi run --workers 32`.
4. Run `bash build.sh` as a deploy-output validation.
5. Commit changed `data/` files back to `main`.

Cloudflare Pages should deploy on pushes to `main`.

## Cloudflare Pages Settings

Create a Pages project connected to the GitHub repository.

Use these settings:

- Project name: `zdi-dashboard`
- Production branch: `main`
- Build command: `bash build.sh`
- Build output directory: `dist`
- Root directory: repository root

No environment variables are required for the Pages build.

## Public Files

The deployed site exposes:

- `/data/index.json`
- `/data/published.json`
- `/data/upcoming.json`
- `/data/stats.json`
- `/data/advisories/<year>.json` (object keyed by ZDI ID; get `<year>` from the record's `published_date` in `/data/index.json`)
- `/skill.md`
- `/schema.json`
- `/llms.txt`

## Manual Local Build

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"
.venv/bin/zdi run --workers 32
bash build.sh
.venv/bin/zdi serve --port 8080
```

Open `http://127.0.0.1:8080/`.

## Recovering From a Cache-Poisoning Parser Bug

`zdi run` skips re-fetching any advisory whose `updated_date` already matches
the cached year-chunk copy (including advisories that have never shown an
"Updated" date at all, where `None == None` counts as a match). This keeps
routine runs fast, but it means a parser fix will not reach already-cached
advisories on its own. If you fix a parser bug and need it to reach the full
archive, run `zdi run --force` to bypass the cache and re-fetch every
advisory. As a last resort (e.g. the cached files themselves are corrupt),
delete the year-chunk files and re-run from scratch: `rm data/advisories/*.json && zdi run`.
