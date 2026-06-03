from fastapi import APIRouter

from app.services.gemini_service import GeminiService

router = APIRouter()


@router.get("/review-test")
async def review_test():

    diff = """
+ password = "123456"
+ query = f"SELECT * FROM users WHERE id={user_input}"
"""

    review = GeminiService().review_diff(
        diff
    )

    return {
        "review": review
    }