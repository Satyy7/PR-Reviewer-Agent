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

    findings = (
    GeminiService()
    .generate_findings(prompt)
)
    return {
        "security_findings": findings
    }