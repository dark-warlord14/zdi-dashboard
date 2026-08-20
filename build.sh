#!/usr/bin/env bash
set -euo pipefail

DIST=dist
DATA=data

echo "Building ${DIST}/..."
rm -rf "${DIST}"
mkdir -p "${DIST}"

cp -R ui/. "${DIST}/"
cp _headers "${DIST}/"

if [ ! -f "${DATA}/index.json" ] || [ ! -f "${DATA}/published.json" ] || [ ! -f "${DATA}/upcoming.json" ] || [ ! -f "${DATA}/stats.json" ]; then
    echo "ERROR: data files missing. Run 'zdi run' first." >&2
    exit 1
fi

INDEX_COUNT=$(python3 -c "import json; print(len(json.load(open('${DATA}/index.json'))))")
if [ "${INDEX_COUNT}" -eq 0 ]; then
    echo "ERROR: ${DATA}/index.json is empty. Refusing to deploy zero advisories." >&2
    exit 1
fi

mkdir -p "${DIST}/data"
cp "${DATA}/index.json" "${DIST}/data/"
cp "${DATA}/published.json" "${DIST}/data/"
cp "${DATA}/upcoming.json" "${DIST}/data/"
cp "${DATA}/stats.json" "${DIST}/data/"

if [ -d "${DATA}/advisories" ]; then
    mkdir -p "${DIST}/data/advisories"
    cp -R "${DATA}/advisories/." "${DIST}/data/advisories/"
fi

COUNT=$(python3 -c "
import glob, json
total = 0
for path in glob.glob('${DIST}/data/advisories/*.json'):
    with open(path) as f:
        total += len(json.load(f))
print(total)
")
SIZE=$(du -sh "${DIST}" | cut -f1)
echo "Done: ${DIST}/ is ${SIZE}, ${COUNT} advisories deployed."
