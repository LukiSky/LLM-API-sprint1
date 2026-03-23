FROM python:3.11-slim

WORKDIR /story_api

COPY requirements.txt /story_api/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /story_api/

# UvicornでFastAPIを起動するコマンド
CMD ["python", "-m", "uvicorn", "story_api.main:app", "--host", "0.0.0.0", "--port", "8090", "--reload"]