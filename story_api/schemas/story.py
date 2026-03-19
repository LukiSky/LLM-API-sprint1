from pydantic import BaseModel, Field


class StoryRequest(BaseModel):
    abstract: str = Field(
        ..., min_length=20, description="Short source abstract or summary to base the story on"
    )
    education_topic: str = Field(
        ..., min_length=2, description="Educational topic that must be explained in the story"
    )
    abstract_prompt: str = Field(
        ..., min_length=10, description="Prompt instruction describing how to transform the abstract into a story"
    )
    temperature: float = Field(0.7, ge=0.0, le=1.5)
    max_tokens: int = Field(1400, ge=200, le=4000)


class StoryResponse(BaseModel):
    model: str
    story: str
