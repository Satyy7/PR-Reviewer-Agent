from fastapi import FastAPI

from app.api.webhook import router as webhook_router
from app.api.health import router as health_router
from app.api.github_test import router as github_test_router




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


@app.get("/")
async def root():
    return {
        "status": "running"
    }