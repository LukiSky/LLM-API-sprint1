from fastapi import APIRouter

from story_api.schemas.abstract import AbstractGenerateRequest, AbstractItem, AbstractOnlyItem
from story_api.services.abstract_service import AbstractService


router = APIRouter(prefix="/abstract", tags=["abstract"])
abstract_service = AbstractService()


@router.post("/generate", response_model=list[AbstractItem])
def generate_abstract(payload: AbstractGenerateRequest) -> list[AbstractItem]:
    """
    Generate story abstracts from a theme or "why?" question.

    Returns a list of abstract outputs. Use count to request multiple.
    Set include_story_prompt=true to include story_prompt in each item.
    Set include_story_prompt=false to return abstract-only items.
    """
    return abstract_service.generate_abstract(payload)
