from typing import TypedDict


class ReviewState(TypedDict):

    diff: str

    security_review: str

    performance_review: str

    quality_review: str

    architecture_review: str

    final_review: dict