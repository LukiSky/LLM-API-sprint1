# Story Generation FastAPI

FastAPI service for story generation using:

- Provider route: Hugging Face Router
- LLM model: MiniMaxAI/MiniMax-M2.5:novita

## 1) Setup

From this folder:

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Set your token (choose one):

- Copy `.env.example` to `.env` and set `HF_TOKEN`
- Or set `HF_TOKEN` in your environment

## 2) Run API

```powershell
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 3) Endpoints

- `GET /api/v1/health`
- `POST /api/v1/abstract/generate` — Generate a story abstract from a theme or "why?" question
- `POST /api/v1/story/generate` — Generate a full story from an abstract
- `POST /api/v1/story/quality-check`
- `POST /api/v1/story/generate-with-quality-gate`

### Generate Abstract (from theme / "why?")

Returns a list of `{abstract, story_prompt}`. Set `count` to generate multiple.

Response example:
```json
[
  { "abstract": "...", "story_prompt": "..." },
  { "abstract": "...", "story_prompt": "..." }
]
```

Request:
```json
{
  "theme": "Why does the moon change shape?",
  "temperature": 0.85,
  "max_tokens": 600,
  "count": 1
}
```

### Generate Story (from abstract)

Example request (use `abstract` and `story_prompt` from an item in the abstract list):

```json
{
  "abstract": "A lunar eclipse happens when Earth moves between the Sun and Moon...",
  "education_topic": "Lunar eclipse",
  "story_prompt": "Turn this abstract into a funny and easy-to-understand 5-minute story for children age 8-12. Include clear explanations and playful reactions.",
  "temperature": 0.7,
  "max_tokens": 1400
}
```

Example curl (two-step: abstract first, then story using abstract + story_prompt):

```powershell
curl -X POST "http://127.0.0.1:8000/api/v1/abstract/generate" `
  -H "Content-Type: application/json" `
  -d "{\"theme\":\"Why does the moon change shape?\"}"

curl -X POST "http://127.0.0.1:8000/api/v1/story/generate" `
  -H "Content-Type: application/json" `
  -d "{\"abstract\":\"...\",\"education_topic\":\"Lunar eclipse\",\"story_prompt\":\"...\"}"
```

Interactive docs:

- http://127.0.0.1:8000/docs
