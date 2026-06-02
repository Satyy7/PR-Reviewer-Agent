from fastapi import FastAPI

from app.api.webhook import router as webhook_router
from app.api.health import router as health_router

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


@app.get("/")
async def root():
    return {
        "status": "running"
    }