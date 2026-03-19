from typing import Optional

from fastapi import HTTPException
from openai import OpenAI

from core.config import DEFAULT_MODEL, HF_ROUTER_BASE_URL, read_hf_token
from schemas.story import StoryRequest, StoryResponse


class StoryService:
    def __init__(self) -> None:
        self.client: Optional[OpenAI] = None

    def _get_client(self) -> OpenAI:
        if self.client is not None:
            return self.client

        hf_token = read_hf_token()
        if not hf_token:
            raise HTTPException(
                status_code=500,
                detail="Hugging Face token not found. Set HF_TOKEN (or HugginFaceToken) in environment or .env.",
            )

        self.client = OpenAI(
            base_url=HF_ROUTER_BASE_URL,
            api_key=hf_token,
        )
        return self.client

    def generate_story(self, payload: StoryRequest) -> StoryResponse:
        plain_text_guardrail = (
            "\n\nOUTPUT FORMAT REQUIREMENTS (STRICT):\n"
            "- Return plain text only.\n"
            "- Do not return HTML, XML, or tags.\n"
            "- Do not return Markdown, code fences, or backticks.\n"
            "- Return only final story text.\n"
        )

        generation_prompt = (
            "You are a professional children's storyteller.\n\n"
            "Write a fun and educational story in plain text.\n"
            f"Education topic: {payload.education_topic}\n\n"
            "Abstract source material:\n"
            f"{payload.abstract}\n\n"
            "Instructions for using the abstract:\n"
            f"{payload.abstract_prompt}\n"
        )

        try:
            completion = self._get_client().chat.completions.create(
                model=DEFAULT_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": generation_prompt + plain_text_guardrail,
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
