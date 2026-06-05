from app.services.gemini_service import GeminiService

from app.prompts.security_prompt import (
    SECURITY_PROMPT
)
from app.core.logger import logger


def security_agent(state):
    
    logger.info(
    "Security agent started"
)
    
    diff = state["diff"]

    prompt = SECURITY_PROMPT.replace(
        "__DIFF_PLACEHOLDER__",
        diff
    )
    findings = (
    GeminiService()
    .generate_findings(prompt,
        agent_name="security"
    )
)
    logger.info(
    "Security agent completed"
)
    return {
        "security_findings": findings
    }