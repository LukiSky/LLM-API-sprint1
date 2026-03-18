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

- `GET /health`
- `POST /generate-story`

Example request:

```json
{
  "prompt": "Write a funny educational story for kids about a lunar eclipse.",
  "temperature": 0.7,
  "max_tokens": 1400
}
```

Example curl:

```powershell
curl -X POST "http://127.0.0.1:8000/generate-story" `
  -H "Content-Type: application/json" `
  -d "{\"prompt\":\"Write a 5-minute children's story about a lunar eclipse, plain text only.\"}"
```

Interactive docs:

- http://127.0.0.1:8000/docs
