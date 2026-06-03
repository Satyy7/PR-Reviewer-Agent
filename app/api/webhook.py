from fastapi import APIRouter
from fastapi import Request
import asyncio

from app.core.logger import logger

from app.services.pr_review_service import (
    PRReviewService
)

from app.utils.security import (
    verify_github_signature
)

router = APIRouter()


async def run_review(
    payload: dict
):

    try:

        logger.info(
            "Starting AI review..."
        )

        PRReviewService.review_pull_request(
            payload
        )

        logger.info(
            "Review completed."
        )

    except Exception as e:

        logger.exception(
            f"Review failed: {str(e)}"
        )


@router.post("/github")
async def github_webhook(
    request: Request
):

    body = await request.body()

    signature = request.headers.get(
        "X-Hub-Signature-256"
    )

    if not verify_github_signature(
        body,
        signature
    ):

        logger.warning(
            "Invalid GitHub signature"
        )

        return {
            "message": "invalid signature"
        }

    payload = await request.json()

    event_type = request.headers.get(
        "X-GitHub-Event"
    )

    if event_type != "pull_request":

        return {
            "message": "ignored"
        }

    action = payload.get(
        "action"
    )

    if payload["pull_request"]["draft"]:

        logger.info(
            "Draft PR ignored"
        )

        return {
            "message": "draft pr ignored"
        }

    if action in [
        "opened",
        "synchronize"
    ]:

        asyncio.create_task(
            run_review(payload)
        )

    return {
        "message": "accepted"
    }