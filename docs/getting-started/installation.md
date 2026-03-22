# Installation

## As a Package

Install `aaa-docware` to use the framework in your own projects:

```bash
pip install aaa-docware
```

Or with [uv](https://github.com/astral-sh/uv):

```bash
uv add aaa-docware
```

### Requirements

- Python 3.12+

## For Development

Clone and set up the development environment:

```bash
git clone https://github.com/BlockScience/assurances-audits-accountability
cd assurances-audits-accountability
uv sync

# Run tests
make test

# Lint
make lint
```

### Development Dependencies

Install with dev extras:

```bash
pip install -e ".[dev]"
```

This includes:

- `pytest` — test framework
- `ruff` — linting and formatting
