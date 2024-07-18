# Local development
.PHONY: api db app lint
api:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

db:
	docker compose up -d --build --force-recreate db
	poetry run python app/init_data.py

app:
	docker compose up -d --build --force-recreate app
	docker compose logs -f app

build:
	docker compose up -d

lint:
	poetry run black --check app
	poetry run ruff check app --fix
	poetry run mypy app