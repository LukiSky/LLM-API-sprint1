import os
from typing import Optional

from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel, Field


load_dotenv(find_dotenv())

HF_ROUTER_BASE_URL = "https://router.huggingface.co/v1"
DEFAULT_MODEL = "MiniMaxAI/MiniMax-M2.5:novita"


def _read_hf_token() -> Optional[str]:
    token = (
        os.getenv("HF_TOKEN")
        or os.getenv("HugginFaceToken")
        or os.getenv("HuggingFaceToken")
    )
    if not token:
        return None
    return token.strip().strip('"').strip("'")


def _build_client() -> OpenAI:
    hf_token = _read_hf_token()
    if not hf_token:
        raise RuntimeError(
            "Hugging Face token not found. Set HF_TOKEN (or HugginFaceToken) in environment or .env."
        )

    return OpenAI(
        base_url=HF_ROUTER_BASE_URL,
        api_key=hf_token,
    )


client = _build_client()
app = FastAPI(title="Story Generation API", version="1.0.0")


class StoryRequest(BaseModel):
    prompt: str = Field(..., min_length=10, description="Story prompt or instruction")
    temperature: float = Field(0.7, ge=0.0, le=1.5)
    max_tokens: int = Field(1400, ge=200, le=4000)


class StoryResponse(BaseModel):
    model: str
    story: str


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "model": DEFAULT_MODEL}


@app.post("/generate-story", response_model=StoryResponse)
def generate_story(payload: StoryRequest) -> StoryResponse:
    plain_text_guardrail = (
        "\n\nOUTPUT FORMAT REQUIREMENTS (STRICT):\n"
        "- Return plain text only.\n"
        "- Do not return HTML, XML, or tags.\n"
        "- Do not return Markdown, code fences, or backticks.\n"
        "- Return only final story text.\n"
    )

    try:
        completion = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": payload.prompt + plain_text_guardrail,
                }
            ],
            temperature=payload.temperature,
            max_tokens=payload.max_tokens,
            timeout=180,
        )
    except Exception as err:
        raise HTTPException(status_code=502, detail=f"LLM request failed: {err}") from err

    story_text = completion.choices[0].message.content or ""
    if not story_text.strip():
        raise HTTPException(status_code=502, detail="Model returned empty content")

    return StoryResponse(model=DEFAULT_MODEL, story=story_text)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
