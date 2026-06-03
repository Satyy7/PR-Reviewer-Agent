from app.services.gemini_service import GeminiService

from app.prompts.performance_prompt import (
    PERFORMANCE_PROMPT
)


def performance_agent(state):

    diff = state["diff"]

    prompt = PERFORMANCE_PROMPT.replace(
        "__DIFF_PLACEHOLDER__",
        diff
    )

    findings = (
    GeminiService()
    .generate_findings(prompt)
)

    return {
        "performance_review": findings
    }