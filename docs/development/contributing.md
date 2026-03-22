# Contributing

## Development Setup

```bash
git clone https://github.com/BlockScience/assurances-audits-accountability
cd assurances-audits-accountability
uv sync
```

## Running Tests

```bash
make test          # Run full test suite
pytest tests/ -v   # Or directly with pytest
```

## Code Quality

```bash
make lint          # Check linting and formatting
make format        # Auto-fix formatting
```

We use [ruff](https://docs.astral.sh/ruff/) for linting and formatting. Configuration is in `pyproject.toml`.

## Project Structure

```
src/aaa/
├── cli.py           # Main CLI entry point (Click)
├── schema.py        # RDF/OWL schema definition
├── codecs/          # Document type parsers (Pydantic models)
├── commands/        # CLI subcommands (verify, build, audit, check, init)
├── foundation/      # Foundation layer documents (packaged as data)
└── templates/       # Document templates (packaged as data)
```

## Pull Request Workflow

1. Create a feature branch from `main`
2. Make your changes
3. Run `make all` (lint + test)
4. Open a PR against `main`

## Adding a New Document Type

1. Create a Pydantic model in `src/aaa/codecs/`
2. Register it in `src/aaa/codecs/__init__.py`
3. Add the type to the schema in `src/aaa/schema.py`
4. Create a template in `src/aaa/templates/`
5. Write tests in `tests/`
