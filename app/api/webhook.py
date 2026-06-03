# from fastapi import APIRouter

# from app.services.github_service import GitHubService

# router = APIRouter()


# @router.post("/github")
# async def github_webhook(payload: dict):

#     pr_info = GitHubService.extract_pr_info(payload)

#     print(pr_info)

#     return {
#         "message": "received",
#         "data": pr_info
#     }

from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/github")
async def github_webhook(request: Request):

    payload = await request.json()

    event_type = request.headers.get("X-GitHub-Event")

    print("=" * 100)
    print("EVENT:", event_type)
    print("PAYLOAD KEYS:", payload.keys())
    print("=" * 100)

    return {"message": "received"}