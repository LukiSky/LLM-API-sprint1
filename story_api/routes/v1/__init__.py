from fastapi import APIRouter

from routes.v1.abstract import router as abstract_router
from routes.v1.health import router as health_router
from routes.v1.story import router as story_router


api_v1_router = APIRouter(prefix="/v1")
api_v1_router.include_router(health_router)
api_v1_router.include_router(abstract_router)
api_v1_router.include_router(story_router)
