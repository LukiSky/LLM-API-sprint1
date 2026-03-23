from pydantic import BaseModel, Field


class AbstractGenerateRequest(BaseModel):
    """
    Request model for generating a detailed, educational, story-based abstract
    built around a central "why?" question or learning theme.

    The generated abstract is designed to teach school-level concepts through
    storytelling. Instead of presenting information as plain facts, the system
    creates a narrative where characters explore a question, encounter situations,
    and gradually discover the explanation.

    For example, for the theme "Why does the moon change shape?",
    the story might follow a curious student observing the night sky,
    asking questions, and learning about moon phases through guided discovery.

    The goal is to combine:
    - Clear educational explanations (accurate and age-appropriate)
    - Engaging storytelling (characters, setting, and events)
    - Curiosity-driven learning (focused on a "why?" question)
    """

    theme: str = Field(
        ...,
        min_length=5,
        description=(
            "A central 'why?' question or educational topic, typically from school subjects "
            "like science, nature, or everyday phenomena. Examples include: "
            "'Why does the moon change shape?', 'How do plants grow?', "
            "'Why do we have seasons?'. "
            "This theme will be transformed into a story-like abstract that teaches "
            "the concept through characters and gradual explanation."
        ),
    )

    temperature: float = Field(
        0.85,
        ge=0.0,
        le=1.5,
        description=(
            "Controls how creative the generated story is. "
            "Higher values (0.9–1.2) make the story more imaginative and varied, "
            "while lower values (0.6–0.8) make it more structured and predictable. "
            "A range of 0.7–0.9 is recommended for a balance between creativity and clarity."
        ),
    )

    max_tokens: int = Field(
        600,
        ge=100,
        le=1500,
        description=(
            "Defines the maximum length of the generated abstract. "
            "Higher values allow for more detailed storytelling, including character development "
            "and deeper explanations of the concept. Lower values produce shorter, more concise stories. "
            "A range of 400–800 is recommended for balanced educational storytelling."
        ),
    )

    count: int = Field(
        1,
        ge=1,
        le=5,
        description="Number of abstracts to generate. Each will have a unique abstract and story_prompt.",
    )


class AbstractItem(BaseModel):
    """A single abstract with its story prompt."""

    abstract: str
    story_prompt: str


class AbstractOnlyItem(BaseModel):
    """A single abstract without story prompt."""

    abstract: list[str]
