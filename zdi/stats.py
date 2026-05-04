"""Build aggregate stats from advisory records."""

from collections import Counter
from datetime import date, datetime

from zdi.models import PublishedAdvisory, Stats, UpcomingAdvisory


def cvss_band(score: float | None) -> str:
    if score is None:
        return "unknown"
    if score >= 9:
        return "critical"
    if score >= 7:
        return "high"
    if score >= 4:
        return "medium"
    return "low"


def deadline_state(deadline: str | None, today: date | None = None) -> str:
    if not deadline:
        return "unknown"
    today = today or date.today()
    try:
        parsed = datetime.strptime(deadline, "%Y-%m-%d").date()
    except ValueError:
        return "unknown"
    if parsed < today:
        return "past_due"
    if (parsed - today).days <= 30:
        return "due_soon"
    return "future"


def build_stats(published: list[PublishedAdvisory], upcoming: list[UpcomingAdvisory]) -> Stats:
    by_year: Counter[str] = Counter()
    by_vendor: Counter[str] = Counter()
    by_cvss: Counter[str] = Counter()
    deadline_counts: Counter[str] = Counter()

    for record in published:
        if record.published_date:
            by_year[record.published_date[:4]] += 1
        if record.vendor:
            by_vendor[record.vendor] += 1
        by_cvss[cvss_band(record.cvss)] += 1

    for record in upcoming:
        if record.vendor:
            by_vendor[record.vendor] += 1
        by_cvss[cvss_band(record.cvss)] += 1
        deadline_counts[deadline_state(record.deadline)] += 1

    return Stats(
        total_published=len(published),
        total_upcoming=len(upcoming),
        high_cvss=sum(1 for r in [*published, *upcoming] if r.cvss is not None and r.cvss >= 7),
        cve_coverage=sum(1 for r in published if r.cve),
        by_year=dict(sorted(by_year.items())),
        by_vendor=dict(by_vendor.most_common(25)),
        by_cvss_band=dict(by_cvss),
        upcoming_deadline_state=dict(deadline_counts),
    )
