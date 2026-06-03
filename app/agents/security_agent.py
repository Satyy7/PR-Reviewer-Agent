from app.services.gemini_service import GeminiService

from app.prompts.security_prompt import (
    SECURITY_PROMPT
)


def security_agent(state):

    diff = state["diff"]

    prompt = SECURITY_PROMPT.replace(
        "__DIFF_PLACEHOLDER__",
        diff
    )

    review = (
        GeminiService()
        .generate_json_review(prompt)
    )

    return {
        "security_review": review
    }