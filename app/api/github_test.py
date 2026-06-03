from fastapi import APIRouter

from app.services.github_service import GitHubService

router = APIRouter()


@router.get("/me")
async def get_me():

    return GitHubService.get_authenticated_user()