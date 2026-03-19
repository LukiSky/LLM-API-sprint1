from fastapi import APIRouter

from schemas.story import StoryRequest, StoryResponse
from services.story_service import StoryService


router = APIRouter(prefix="/stories", tags=["stories"])
story_service = StoryService()


@router.post("/generate", response_model=StoryResponse)
def generate_story(payload: StoryRequest) -> StoryResponse:
    return story_service.generate_story(payload)
