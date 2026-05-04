"""Typed records for ZDI advisory data."""

from pydantic import BaseModel, Field


class PublishedAdvisory(BaseModel):
    kind: str = "published"
    zdi_id: str
    zdi_can: str | None = None
    vendor: str | None = None
    vendor_url: str | None = None
    cve: str | None = None
    cvss: float | None = None
    cvss_vector: str | None = None
    published_date: str | None = None
    updated_date: str | None = None
    title: str
    url: str
    detail_path: str | None = None


class UpcomingAdvisory(BaseModel):
    kind: str = "upcoming"
    zdi_can: str
    vendor: str | None = None
    vendor_url: str | None = None
    cvss: float | None = None
    cvss_vector: str | None = None
    reported_date: str | None = None
    deadline: str | None = None
    discoverer: str | None = None
    status: str = "upcoming"


class AdvisoryDetail(BaseModel):
    kind: str = "published"
    zdi_id: str
    zdi_can: str | None = None
    title: str
    advisory_date: str | None = None
    updated_date: str | None = None
    cve: str | None = None
    cve_url: str | None = None
    cvss: float | None = None
    cvss_vector: str | None = None
    affected_vendors: list[str] = Field(default_factory=list)
    affected_products: list[str] = Field(default_factory=list)
    vulnerability_details: str | None = None
    additional_details: str | None = None
    disclosure_timeline: list[str] = Field(default_factory=list)
    credit: str | None = None
    source_url: str
    search_text: str = ""


class Stats(BaseModel):
    total_published: int = 0
    total_upcoming: int = 0
    high_cvss: int = 0
    cve_coverage: int = 0
    by_year: dict[str, int] = Field(default_factory=dict)
    by_vendor: dict[str, int] = Field(default_factory=dict)
    by_cvss_band: dict[str, int] = Field(default_factory=dict)
    upcoming_deadline_state: dict[str, int] = Field(default_factory=dict)
