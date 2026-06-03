from app.services.gemini_service import GeminiService

from app.prompts.quality_prompt import (
    QUALITY_PROMPT
)
from app.core.logger import logger
logger.info(
    "Quality agent started"
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
    logger.info(
    "Quality agent completed"
)
    return {
        "quality_review": findings
    }