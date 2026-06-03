import json

from google import genai

from app.core.config import settings
from app.prompts.review_prompt import REVIEW_PROMPT
from app.schemas.review_schema import ReviewResponse


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

    def review_diff(
        self,
        diff_content: str
    ) -> dict:

        prompt = REVIEW_PROMPT.format(
            diff=diff_content
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        cleaned_text = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        review_json = json.loads(
            cleaned_text
        )

        validated_review = (
            ReviewResponse.model_validate(
                review_json
            )
        )

        return validated_review.model_dump()