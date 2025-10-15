
.PHONY: up migrate test fmt seed

up:
	docker compose up --build

migrate:
	cd api && alembic upgrade head

test:
	cd api && pytest -q

fmt:
	cd api && ruff check --fix . && black .
	cd app && eslint . --fix || true

seed:
	python api/scripts/seed.py
