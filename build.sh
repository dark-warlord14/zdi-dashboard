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

mkdir -p "${DIST}/data"
cp "${DATA}/index.json" "${DIST}/data/"
cp "${DATA}/published.json" "${DIST}/data/"
cp "${DATA}/upcoming.json" "${DIST}/data/"
cp "${DATA}/stats.json" "${DIST}/data/"

if [ -d "${DATA}/advisories" ]; then
    mkdir -p "${DIST}/data/advisories"
    cp -R "${DATA}/advisories/." "${DIST}/data/advisories/"
fi

COUNT=$(find "${DIST}/data/advisories" -name advisory.json 2>/dev/null | wc -l | tr -d ' ')
SIZE=$(du -sh "${DIST}" | cut -f1)
echo "Done: ${DIST}/ is ${SIZE}, ${COUNT} advisories deployed."
