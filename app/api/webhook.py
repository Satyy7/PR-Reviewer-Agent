from fastapi import APIRouter

router = APIRouter()


@router.post("/github")
async def github_webhook(payload: dict):

    print(payload)

    return {
        "message": "Webhook received"
    }