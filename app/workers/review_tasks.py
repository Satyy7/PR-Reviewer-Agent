from app.workers.celery_app import (
    celery_app
)

from app.services.pr_review_service import (
    PRReviewService
)

from requests.exceptions import ConnectionError, Timeout

@celery_app.task(
    bind=True,
    autoretry_for=(
        ConnectionError,
        Timeout,
    ),
    retry_backoff=True,
    max_retries=3
)

def review_pr_task(
    self,
    payload: dict
):

    PRReviewService.review_pull_request(
        payload
    )