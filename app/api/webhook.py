from fastapi import APIRouter
from fastapi import Request

import asyncio

from app.core.logger import logger

from app.services.pr_review_service import (
    PRReviewService
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

    payload = await request.json()

    event_type = (
        request.headers.get(
            "X-GitHub-Event"
        )
    )

    if event_type == "pull_request":

        action = payload.get(
            "action"
        )

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