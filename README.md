# ZDI Dashboard

Static Zero Day Initiative advisory archive with daily data refresh, searchable UI, and agent-readable JSON outputs. Maintained as part of Shantanu Ghumade's professional security tooling network.

Live site: https://zdi-dashboard.pages.dev/

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Commands

```bash
zdi run      # fetch ZDI advisories, generate data files
zdi status   # print local data counts
zdi serve    # serve the dashboard locally at http://localhost:8080
```

## Deployment

`build.sh` assembles `dist/` for Cloudflare Pages. GitHub Actions runs daily and manually to refresh `data/` and commit changed data files. Cloudflare Pages Git integration builds and deploys on pushes to `main`.

See [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md) for the full setup.
