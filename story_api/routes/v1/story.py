from fastapi import APIRouter

from schemas.story import (
    StoryGenerateWithQualityRequest,
    StoryGenerateWithQualityResponse,
    StoryQualityCheckRequest,
    StoryQualityCheckResponse,
    StoryRequest,
    StoryResponse,
)
from services.story_service import StoryService


router = APIRouter(prefix="/stories", tags=["stories"])
story_service = StoryService()


@router.post("/generate", response_model=StoryResponse)
def generate_story(payload: StoryRequest) -> StoryResponse:
    return story_service.generate_story(payload)


@router.post("/quality-check", response_model=StoryQualityCheckResponse)
def quality_check_story(payload: StoryQualityCheckRequest) -> StoryQualityCheckResponse:
    return story_service.quality_check_story(payload)


@router.post("/generate-with-quality-gate", response_model=StoryGenerateWithQualityResponse)
def generate_story_with_quality_gate(
    payload: StoryGenerateWithQualityRequest,
) -> StoryGenerateWithQualityResponse:
    return story_service.generate_story_with_quality_gate(payload)
