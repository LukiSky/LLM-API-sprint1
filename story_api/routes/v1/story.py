from fastapi import APIRouter

from story_api.schemas.story import (
    StoryGenerateWithQualityRequest,
    StoryGenerateWithQualityResponse,
    StoryQualityCheckRequest,
    StoryQualityCheckResponse,
    StoryRequest,
    StoryResponse,
)
from story_api.services.story_service import StoryService


router = APIRouter(prefix="/story", tags=["story"])
story_service = StoryService()


@router.post("/generate", response_model=StoryResponse)
def generate_story(payload: StoryRequest) -> StoryResponse:
    """
    Generate a full story from an abstract.

    Use the abstract from POST /abstract/generate, or provide your own.
    Requires education_topic and story_prompt to guide the transformation. Use story_prompt from POST /abstract/generate.
    """
    return story_service.generate_story(payload)


@router.post("/quality-check", response_model=StoryQualityCheckResponse)
def quality_check_story(payload: StoryQualityCheckRequest) -> StoryQualityCheckResponse:
    return story_service.quality_check_story(payload)


@router.post("/generate-with-quality-gate", response_model=StoryGenerateWithQualityResponse)
def generate_story_with_quality_gate(
    payload: StoryGenerateWithQualityRequest,
) -> StoryGenerateWithQualityResponse:
    return story_service.generate_story_with_quality_gate(payload)
