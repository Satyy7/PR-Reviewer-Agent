from google import genai

from app.core.config import settings


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

    def review_diff(
        self,
        diff_content: str
    ) -> str:

        prompt = f"""
You are an expert software engineer.

Review the following Git diff.

Identify:
- Bugs
- Security Issues
- Performance Problems
- Code Quality Issues

Provide actionable feedback.

Diff:

{diff_content}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text