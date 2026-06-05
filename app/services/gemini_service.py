import json

from google import genai

from groq import Groq

from app.core.config import settings

from app.prompts.review_prompt import (
    REVIEW_PROMPT
)

from app.schemas.review_schema import (
    ReviewResponse
)


class GeminiService:

    def __init__(self):

        self.gemini_client = (
            genai.Client(
                api_key=settings.gemini_api_key
            )
        )

        self.groq_client = (
            Groq(
                api_key=settings.groq_api_key
            )
        )

    def _clean_response(
        self,
        text: str
    ) -> str:

        return (
            text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

    def _generate_with_gemini(
        self,
        prompt: str
    ) -> str:

        response = (
            self.gemini_client
            .models
            .generate_content(
                model=settings.gemini_model,
                contents=prompt
            )
        )

        return self._clean_response(
            response.text
        )

    def _generate_with_groq(
        self,
        prompt: str
    ) -> str:

        response = (
            self.groq_client
            .chat
            .completions
            .create(
                model=settings.groq_model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0
            )
        )

        return self._clean_response(
            response
            .choices[0]
            .message
            .content
        )

    def _generate(
        self,
        prompt: str
    ) -> str:

        try:

            print(
                "Using Gemini..."
            )

            return (
                self._generate_with_gemini(
                    prompt
                )
            )

        except Exception as gemini_error:

            print(
                f"Gemini failed: "
                f"{gemini_error}"
            )

            print(
                "Falling back to Groq..."
            )

            try:

                return (
                    self._generate_with_groq(
                        prompt
                    )
                )

            except Exception as groq_error:

                print(
                    f"Groq failed: "
                    f"{groq_error}"
                )

                return "[]"
    # --------------------------------------------------
    # Single Agent
    # --------------------------------------------------

    def generate_json_review(
        self,
        prompt: str
    ) -> dict:

        cleaned_text = (
            self._generate(
                prompt
            )
        )

        review_json = json.loads(
            cleaned_text
        )

        validated_review = (
            ReviewResponse
            .model_validate(
                review_json
            )
        )

        return (
            validated_review
            .model_dump()
        )

    # --------------------------------------------------
    # Multi Agent
    # --------------------------------------------------

    def generate_findings(
        self,
        prompt: str,
        agent_name: str = "unknown"
    ) -> list:

        cleaned_text = (
            self._generate(
                prompt
            )
        )

        try:

            findings = json.loads(
                cleaned_text
            )

        except Exception:

            return []

        if not isinstance(
            findings,
            list
        ):
            raise ValueError(
                "Expected JSON array "
                "from agent"
            )

        return findings

    # --------------------------------------------------
    # Backward Compatibility
    # --------------------------------------------------

    def review_diff(
        self,
        diff_content: str
    ) -> dict:

        prompt = (
            REVIEW_PROMPT.replace(
                "__DIFF_PLACEHOLDER__",
                diff_content
            )
        )

        return (
            self.generate_json_review(
                prompt
            )
        )