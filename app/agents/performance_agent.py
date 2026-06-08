from app.services.gemini_service import GeminiService

from app.prompts.performance_prompt import (
    PERFORMANCE_PROMPT
)
from app.core.logger import logger

def performance_agent(state):

    logger.info(
    "Performance agent started"
)


    diff = state["diff"]

    prompt = PERFORMANCE_PROMPT.replace(
        "__DIFF_PLACEHOLDER__",
        diff
    )

    findings = (
    GeminiService()
    .generate_findings(prompt,agent_name="performance")
)

    logger.info(
    "Performance agent completed"
)
    return {
        "performance_review": findings
    }