"""Project paths and ZDI source URLs."""

from pathlib import Path

BASE_URL = "https://www.zerodayinitiative.com"
PUBLISHED_URL = f"{BASE_URL}/advisories/published/"
UPCOMING_URL = f"{BASE_URL}/advisories/upcoming/"

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
ADVISORIES_DIR = DATA_DIR / "advisories"
UI_DIR = ROOT_DIR / "ui"
DIST_DIR = ROOT_DIR / "dist"

PUBLISHED_FILE = DATA_DIR / "published.json"
UPCOMING_FILE = DATA_DIR / "upcoming.json"
INDEX_FILE = DATA_DIR / "index.json"
STATS_FILE = DATA_DIR / "stats.json"
