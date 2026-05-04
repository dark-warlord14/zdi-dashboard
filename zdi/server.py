"""Local static dashboard server."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from zdi.config import DIST_DIR, ROOT_DIR


def serve(port: int = 8080, directory: Path | None = None) -> None:
    directory = directory or (DIST_DIR if DIST_DIR.exists() else ROOT_DIR / "ui")
    handler = partial(SimpleHTTPRequestHandler, directory=str(directory))
    httpd = ThreadingHTTPServer(("127.0.0.1", port), handler)
    print(f"Serving {directory} at http://127.0.0.1:{port}")
    httpd.serve_forever()
