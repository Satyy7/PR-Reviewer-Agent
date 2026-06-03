from fastapi import APIRouter, Request

from app.services.github_service import GitHubService

router = APIRouter()


@router.post("/github")
async def github_webhook(request: Request):

    payload = await request.json()

    event_type = request.headers.get("X-GitHub-Event")

    if event_type == "pull_request":

        pr_info = GitHubService.extract_pr_info(payload)

        print("=" * 80)
        print(pr_info)
        print("=" * 80)

    return {"message": "received"}
