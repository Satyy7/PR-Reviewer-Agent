from typing import List

from pydantic import BaseModel


class Finding(BaseModel):
    severity: str
    category: str
    title: str
    description: str
    recommendation: str


class Summary(BaseModel):
    total_findings: int
    overall_severity: str


class ReviewResponse(BaseModel):
    summary: Summary
    findings: List[Finding]