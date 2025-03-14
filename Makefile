# Local development
.PHONY: lint
lint:
	poetry run black --check app
	poetry run ruff check app --fix
	poetry run mypy app

.PHONY: app
api:
	poetry run python app/init_data.py
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

db:
	mkdir -p data
	docker compose up --build --force-recreate db
	poetry run python app/tests/integration/create_dummy_db.py

ddb:
	mkdir -p data
	docker compose up -d --build --force-recreate db
	poetry run python app/tests/integration/create_dummy_db.py

rmdb:
	docker stop fastapi-boilerplate-db
	docker rm fastapi-boilerplate-db

be:
	docker compose up --build --force-recreate backend
	docker compose logs -f backend

dbe:
	docker compose up -d --build --force-recreate backend

rmbe:
	docker stop fastapi-boilerplate-backend
	docker rm fastapi-boilerplate-backend

local:
	docker compose -f docker-compose.yml build

up-local:
	docker compose -f docker-compose.yml up

local-force:
	docker compose -f docker-compose.yml build --no-cache
