# Local development
.PHONY: lint
lint:
	poetry run black --check app
	poetry run ruff check app --fix
	poetry run mypy app

.PHONY: backend
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
	docker compose -f docker-compose.yml build

up-local:
	docker compose -f docker-compose.yml up

local-force:
	docker compose -f docker-compose.yml build --no-cache
