from prometheus_client import (
    Counter,
    Histogram
)

PR_REVIEWS_TOTAL = Counter(
    "pr_reviews_total",
    "Total PR reviews processed"
)

PR_REVIEW_FAILURES_TOTAL = Counter(
    "pr_review_failures_total",
    "Total PR review failures"
)

LLM_REQUESTS_TOTAL = Counter(
    "llm_requests_total",
    "Total LLM requests",
    ["provider"]
)

LLM_FAILURES_TOTAL = Counter(
    "llm_failures_total",
    "Total LLM failures",
    ["provider"]
)

REVIEW_DURATION_SECONDS = Histogram(
    "review_duration_seconds",
    "PR review duration"
)