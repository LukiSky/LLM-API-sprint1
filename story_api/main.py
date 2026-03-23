from fastapi import FastAPI

from story_api.routes.v1 import api_v1_router


app = FastAPI(title="Story Generation API", version="1.0.0")
app.include_router(api_v1_router, prefix="/api")


@app.get("/")
def root() -> dict:
    return {
        "service": "Story Generation API",
        "version": "v1",
        "docs": "/docs",
        "base_path": "/api/v1",
    }

