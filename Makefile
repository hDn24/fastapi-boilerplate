.PHONY: app
app:
	docker compose up -d --build --force-recreate app
	docker compose logs -f app