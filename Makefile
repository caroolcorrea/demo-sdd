.PHONY: run unit integration test-ci coverage lint format install

install:
	poetry install --no-interaction --no-root

run:
	poetry run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

unit:
	poetry run pytest tests/unit -v --timeout=30

integration:
	poetry run pytest tests/integration -v --timeout=60

test-ci:
	poetry run pytest tests/unit tests/integration -v --cov=src --cov-report=xml --cov-report=term-missing -p no:timeout

coverage:
	poetry run pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=80

lint:
	poetry run ruff check src tests
	poetry run ruff format --check src/ tests/

format:
	poetry run ruff format src/ tests/

check: lint unit
