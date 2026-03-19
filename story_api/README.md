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
- `POST /api/v1/stories/generate`

Example request:

```json
{
  "abstract": "A lunar eclipse happens when Earth moves between the Sun and Moon, casting Earth's shadow on the Moon. It does not happen every month because the Moon's orbit is tilted.",
  "education_topic": "Lunar eclipse",
  "abstract_prompt": "Turn this abstract into a funny and easy-to-understand 5-minute story for children age 8-12. Include clear explanations and playful reactions.",
  "temperature": 0.7,
  "max_tokens": 1400
}
```

Example curl:

```powershell
curl -X POST "http://127.0.0.1:8000/api/v1/stories/generate" `
  -H "Content-Type: application/json" `
  -d "{\"abstract\":\"A lunar eclipse happens when Earth blocks sunlight from reaching the Moon.\",\"education_topic\":\"Lunar eclipse\",\"abstract_prompt\":\"Write a playful story for kids from this abstract.\"}"
```

Interactive docs:

- http://127.0.0.1:8000/docs
