from fastapi import APIRouter, Request

from app.services.pr_review_service import PRReviewService

router = APIRouter()


@router.post("/github")
async def github_webhook(request: Request):

    payload = await request.json()

    event_type = request.headers.get("X-GitHub-Event")

    if event_type == "pull_request":

        action = payload.get("action")

        if action in ["opened", "synchronize"]:

            result = PRReviewService.review_pull_request(
                payload
            )

            print("=" * 80)
            print("AI REVIEW")
            print("=" * 80)

            print(result["review"])

    return {
        "message": "received"
    }