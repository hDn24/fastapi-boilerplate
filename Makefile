# Local development
.PHONY: api db backend lint
api:
	poetry run python app/init_data.py
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

db:
	docker compose up -d --build --force-recreate db
	poetry run python app/init_data.py

backend:
	docker compose up -d --build --force-recreate backend
	docker compose logs -f backend

local:
	docker compose up

lint:
	poetry run black --check app
	poetry run ruff check app --fix
	poetry run mypy app
