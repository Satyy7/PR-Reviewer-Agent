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

    findings = (
    GeminiService()
    .generate_findings(prompt)
)

    return {
        "quality_review": findings
    }