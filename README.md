# Dota Insight

Pet project: Dota stats / insights (FastAPI + Postgres + позже frontend).

## Quick start

Репо уже содержит `backend/`, `frontend/`, `docs/`, `docker-compose.yml`. После clone остаётся окружение и запуск:

```bash
git clone <repo-url> dota-insight
cd dota-insight

cp backend/.env.example backend/.env

docker compose up -d

cd backend
uv sync
uv run uvicorn app.main:app --reload
```

Проверка: http://127.0.0.1:8000/health

## Нужно на машине

- [uv](https://docs.astral.sh/uv/)
- Docker (Postgres)

`uv sync` и `uvicorn` — из папки `backend/` (там `pyproject.toml` и код API).
