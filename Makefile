# Local development
.PHONY: app lint
app:
	docker compose up -d --build --force-recreate app
	docker compose logs -f app

lint:
	poetry run python -m ruff check
