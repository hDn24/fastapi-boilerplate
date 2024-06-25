# Local development
.PHONY: data app lint
db:
	docker compose up -d --build --force-recreate db

app:
	docker compose up -d --build --force-recreate app
	docker compose logs -f app

lint:
	poetry run python -m ruff check
