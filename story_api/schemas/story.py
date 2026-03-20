from pydantic import BaseModel, Field


class StoryRequest(BaseModel):
    abstract: str = Field(
        ..., min_length=20, description="Short source abstract or summary to base the story on"
    )
    education_topic: str = Field(
        ..., min_length=2, description="Educational topic that must be explained in the story"
    )
    story_prompt: str = Field(
        ..., min_length=10, description="Prompt instruction describing how to transform the abstract into a story"
    )
    temperature: float = Field(0.7, ge=0.0, le=1.5)
    max_tokens: int = Field(1400, ge=200, le=4000)


class StoryResponse(BaseModel):
    story: str


class StoryQualityCheckRequest(BaseModel):
    story: str = Field(..., min_length=100, description="Story text to evaluate")
    story_category: str = Field(
        "Children's educational fiction",
        min_length=2,
        description="Category label used to evaluate tone and educational fit",
    )
    rounds: int = Field(
        2,
        ge=1,
        le=3,
        description="Debate rounds. Round 1 produces independent reviews; later rounds add rebuttals.",
    )
    temperature: float = Field(0.1, ge=0.0, le=1.0)
    max_tokens: int = Field(1200, ge=300, le=4000)


class ModelQualityReview(BaseModel):
    model: str
    round_number: int
    final_score: int | None = None
    summary: str
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    suggested_fix: str | None = None
    raw_response: str


class StoryQualityCheckResponse(BaseModel):
    models: list[str]
    rounds: int
    consensus_model: str
    consensus_score: int | None = None
    consensus_summary: str
    transcript: list[ModelQualityReview]


class StoryGenerateWithQualityRequest(BaseModel):
    abstract: str = Field(
        ..., min_length=20, description="Short source abstract or summary to base the story on"
    )
    education_topic: str = Field(
        ..., min_length=2, description="Educational topic that must be explained in the story"
    )
    story_prompt: str = Field(
        ..., min_length=10, description="Prompt instruction describing how to transform the abstract into a story"
    )

    generation_temperature: float = Field(0.7, ge=0.0, le=1.5)
    generation_max_tokens: int = Field(1400, ge=200, le=4000)

    story_category: str = Field(
        "Children's educational fiction",
        min_length=2,
        description="Category label used to evaluate tone and educational fit",
    )
    rounds: int = Field(
        2,
        ge=1,
        le=3,
        description="Debate rounds. Round 1 produces independent reviews; later rounds add rebuttals.",
    )
    quality_temperature: float = Field(0.1, ge=0.0, le=1.0)
    quality_max_tokens: int = Field(1200, ge=300, le=4000)

    acceptance_score: int = Field(75, ge=0, le=100)
    max_regenerations: int = Field(
        1,
        ge=0,
        le=5,
        description="How many extra generation attempts are allowed if score is below acceptance_score.",
    )


class StoryGenerateWithQualityResponse(BaseModel):
    accepted: bool
    attempts: int
    required_score: int
    final_score: int | None = None
    story_result: StoryResponse
    quality_result: StoryQualityCheckResponse
