from fastapi import APIRouter

from app.services.github_service import GitHubService

router = APIRouter()


@router.post("/github")
async def github_webhook(payload: dict):

    pr_info = GitHubService.extract_pr_info(payload)

    print(pr_info)

    return {
        "message": "received",
        "data": pr_info
    }