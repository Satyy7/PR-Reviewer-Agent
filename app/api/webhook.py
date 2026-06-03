from fastapi import APIRouter, Request

from app.services.github_service import GitHubService

router = APIRouter()


@router.post("/github")
async def github_webhook(request: Request):

    payload = await request.json()

    event_type = request.headers.get("X-GitHub-Event")

    print("=" * 80)
    print(f"EVENT TYPE: {event_type}")
    print("=" * 80)

    if event_type == "pull_request":

        pr_info = GitHubService.extract_pr_info(payload)

        print("PR INFO")
        print(pr_info)

        pr_details = GitHubService.get_pr_details(
            owner=pr_info["owner"],
            repo=pr_info["repo_name"],
            pr_number=pr_info["pr_number"]
        )
        diff_content = GitHubService.get_pr_diff(
            pr_details["diff_url"]
        )

        print("=" * 80)
        print("DIFF CONTENT")
        print("=" * 80)

        print(diff_content[:3000])

        print("\nPR DETAILS")
        print(f"Title      : {pr_details['title']}")
        print(f"State      : {pr_details['state']}")
        print(f"Author     : {pr_details['user']['login']}")
        print(f"Diff URL   : {pr_details['diff_url']}")
        print(f"Patch URL  : {pr_details['patch_url']}")

    return {
        "message": "received"
    }