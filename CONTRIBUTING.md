# Contributing to AAA Docware

## Development Setup

```bash
git clone https://github.com/BlockScience/assurances-audits-accountability
cd assurances-audits-accountability
uv sync
```

Or with pip:

```bash
pip install -e ".[dev]"
```

## Running Tests

```bash
make test          # Full test suite
pytest tests/ -v   # Direct pytest invocation
```

## Code Quality

We use [ruff](https://docs.astral.sh/ruff/) for linting and formatting:

```bash
make lint          # Check linting and formatting
make format        # Auto-fix formatting
```

## Project Structure

```
src/aaa/
├── cli.py           # Main CLI entry point (Click)
├── schema.py        # RDF/OWL schema definition
├── codecs/          # Document type parsers (Pydantic models)
├── commands/        # CLI subcommands (verify, build, audit, check, init)
├── foundation/      # Foundation layer documents (packaged as data)
└── templates/       # Document templates (packaged as data)

tests/
├── test_*.py        # Test modules
└── fixtures/        # Test fixtures
```

## Pull Request Workflow

1. Create a feature branch from `main`
2. Make your changes
3. Run `make all` (lint + test)
4. Open a PR against `main`

CI will run tests, linting, document verification, and assurance audits on your PR.

## Adding a New Document Type

1. Create a Pydantic model in `src/aaa/codecs/`
2. Register it in `src/aaa/codecs/__init__.py`
3. Add the type to the schema in `src/aaa/schema.py`
4. Create a template in `src/aaa/templates/`
5. Write tests in `tests/`

## Building Documentation

```bash
make docs          # Serve docs locally at http://localhost:8000
make docs-build    # Build static site to site/
```

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.
