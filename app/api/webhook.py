from fastapi import APIRouter, Request

from app.services.github_service import GitHubService

router = APIRouter()


@router.post("/github")
async def github_webhook(request: Request):

    payload = await request.json()

    event_type = request.headers.get("X-GitHub-Event")

    if event_type == "pull_request":

        pr_info = GitHubService.extract_pr_info(payload)

        pr_details = GitHubService.get_pr_details(
            owner=pr_info["owner"],
            repo=pr_info["repo_name"],
            pr_number=pr_info["pr_number"]
        )

        print("=" * 80)
        print("DIFF URL:", pr_details["diff_url"])
        print("=" * 80)

    return {"message": "received"}
