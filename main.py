from fastapi import FastAPI

from app.api.webhook import router as webhook_router
from app.api.health import router as health_router
from app.api.github_test import router as github_test_router

from app.api.gemini_test import router as gemini_router
from prometheus_client import (
    generate_latest,
    CONTENT_TYPE_LATEST
)

from fastapi import Response

app = FastAPI(
    title="AI PR Reviewer",
    version="1.0.0"
)

app.include_router(
    webhook_router,
    prefix="/webhook",
    tags=["GitHub Webhooks"]
)

app.include_router(
    health_router,
    prefix="/health",
    tags=["Health"]
)

app.include_router(
    github_test_router,
    prefix="/github",
    tags=["GitHub"]
)

app.include_router(
    gemini_router,
    prefix="/gemini",
    tags=["Gemini"]
)

@app.get("/metrics")
def metrics():

    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )

@app.get("/")
async def root():
    return {
        "status": "running"
    }