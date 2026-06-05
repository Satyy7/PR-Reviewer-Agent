from typing import TypedDict


class ReviewState(TypedDict):

    diff: str

    security_review: list

    performance_review: list

    quality_review: list

    architecture_review: list

    final_review: dict