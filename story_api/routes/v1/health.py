from fastapi import APIRouter

from story_api.core.config import DEFAULT_MODEL


router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict:
    return {"status": "ok", "model": DEFAULT_MODEL}
