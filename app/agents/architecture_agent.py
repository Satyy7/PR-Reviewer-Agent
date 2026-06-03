from app.services.gemini_service import GeminiService

from app.prompts.architecture_prompt import (
    ARCHITECTURE_PROMPT
)
from app.core.logger import logger
logger.info(
    "Architecture agent started"
)

def architecture_agent(state):

    diff = state["diff"]

    prompt = ARCHITECTURE_PROMPT.replace(
        "__DIFF_PLACEHOLDER__",
        diff
    )

    findings = (
    GeminiService()
    .generate_findings(prompt)
)
    logger.info(
    "Architecture agent completed"
)
    return {
        "architecture_review": findings
    }