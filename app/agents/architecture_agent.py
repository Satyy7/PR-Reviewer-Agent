from app.services.gemini_service import GeminiService

from app.prompts.architecture_prompt import (
    ARCHITECTURE_PROMPT
)


def architecture_agent(state):

    diff = state["diff"]

    prompt = ARCHITECTURE_PROMPT.replace(
        "__DIFF_PLACEHOLDER__",
        diff
    )

    review = (
        GeminiService()
        .generate_json_review(prompt)
    )

    return {
        "architecture_review": review
    }