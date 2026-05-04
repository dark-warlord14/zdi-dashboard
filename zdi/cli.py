"""Command-line interface for the ZDI dashboard."""

from pathlib import Path

import click

from zdi.config import DATA_DIR
from zdi.models import AdvisoryDetail, PublishedAdvisory, UpcomingAdvisory
from zdi.scraper import run as run_pipeline, scrape_published, scrape_upcoming, write_public_data
from zdi.server import serve as serve_dashboard


@click.group()
def cli() -> None:
    """Zero Day Initiative advisory dashboard tools."""


@cli.command()
@click.option("--data-dir", type=click.Path(path_type=Path), default=DATA_DIR)
@click.option("--workers", default=12, show_default=True, help="Concurrent detail fetch workers.")
def run(data_dir: Path, workers: int) -> None:
    """Fetch advisories and rebuild public data files."""
    published, upcoming = run_pipeline(data_dir=data_dir, max_workers=workers, verbose=True)
    click.echo(f"Wrote {len(published)} published and {len(upcoming)} upcoming advisories to {data_dir}")


@cli.command()
@click.option("--data-dir", type=click.Path(path_type=Path), default=DATA_DIR)
def scrape(data_dir: Path) -> None:
    """Fetch list pages only and write list data without details."""
    published = scrape_published()
    upcoming = scrape_upcoming()
    write_public_data(data_dir, published, upcoming, {})
    click.echo(f"Wrote list data for {len(published)} published and {len(upcoming)} upcoming advisories")


@cli.command("index")
@click.option("--data-dir", type=click.Path(path_type=Path), default=DATA_DIR)
def rebuild_index(data_dir: Path) -> None:
    """Rebuild index and stats from existing public data files."""
    import json

    published = [
        PublishedAdvisory.model_validate(item)
        for item in json.loads((data_dir / "published.json").read_text(encoding="utf-8"))
    ]
    upcoming = [
        UpcomingAdvisory.model_validate(item)
        for item in json.loads((data_dir / "upcoming.json").read_text(encoding="utf-8"))
    ]
    details: dict[str, AdvisoryDetail] = {}
    for path in (data_dir / "advisories").glob("*/advisory.json"):
        detail = AdvisoryDetail.model_validate_json(path.read_text(encoding="utf-8"))
        details[detail.zdi_id] = detail
    write_public_data(data_dir, published, upcoming, details)
    click.echo(f"Rebuilt index for {len(published)} published and {len(upcoming)} upcoming advisories")


@cli.command()
@click.option("--port", default=8080, show_default=True)
def serve(port: int) -> None:
    """Serve the dashboard locally."""
    serve_dashboard(port=port)


@cli.command()
@click.option("--data-dir", type=click.Path(path_type=Path), default=DATA_DIR)
def status(data_dir: Path) -> None:
    """Print local data counts."""
    import json

    published_file = data_dir / "published.json"
    upcoming_file = data_dir / "upcoming.json"
    published = json.loads(published_file.read_text(encoding="utf-8")) if published_file.exists() else []
    upcoming = json.loads(upcoming_file.read_text(encoding="utf-8")) if upcoming_file.exists() else []
    click.echo(f"Published: {len(published)}")
    click.echo(f"Upcoming: {len(upcoming)}")


if __name__ == "__main__":
    cli()
