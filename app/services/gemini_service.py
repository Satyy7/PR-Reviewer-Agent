import json

from google import genai

from app.core.config import settings
from app.schemas.review_schema import ReviewResponse


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

    def generate_json_review(
        self,
        prompt: str
    ) -> dict:

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