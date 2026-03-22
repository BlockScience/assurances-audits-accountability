.PHONY: install test lint format docs docs-build clean build publish all

install:
	pip install -e ".[dev]"

test:
	pytest tests/ -v

lint:
	ruff check src/ tests/
	ruff format --check src/ tests/

format:
	ruff format src/ tests/
	ruff check --fix src/ tests/

docs:
	mkdocs serve

docs-build:
	mkdocs build

clean:
	rm -rf dist/ build/ *.egg-info/ site/ complex.json graph.ttl graph.jsonld
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

build:
	hatch build

publish:
	hatch publish

all: lint test
