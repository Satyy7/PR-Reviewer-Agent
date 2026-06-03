from app.services.gemini_service import GeminiService

from app.prompts.quality_prompt import (
    QUALITY_PROMPT
)


def quality_agent(state):

    diff = state["diff"]

    prompt = QUALITY_PROMPT.replace(
        "__DIFF_PLACEHOLDER__",
        diff
    )

    review = (
        GeminiService()
        .generate_json_review(prompt)
    )

    return {
        "quality_review": review
    }