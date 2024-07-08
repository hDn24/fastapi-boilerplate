# Local development
.PHONY: api db app lint
api:
	poetry run python app/init_data.py
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

db:
	docker compose up -d --build --force-recreate db

app:
	docker compose up -d --build --force-recreate app
	docker compose logs -f app

build:
	docker compose up -d

lint:
	poetry run python -m ruff format app
