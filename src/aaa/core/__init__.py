"""
AAA Core Module

This module provides the core functionality for the AAA (Assurances, Audits, Accountability)
framework. It wraps the verification scripts and provides a clean API for use by the CLI
and other tools.

The core module re-exports key classes and functions from the scripts directory,
providing a stable import path for users of the package.
"""

import sys
from pathlib import Path


def _find_repo_root() -> Path:
    """Find the repository root by looking for pyproject.toml or .git."""
    # Start from the package location and work upward
    current = Path(__file__).parent
    for parent in [current] + list(current.parents):
        if (parent / 'pyproject.toml').exists() or (parent / '.git').exists():
            return parent
    # Also try from cwd
    current = Path.cwd()
    for parent in [current] + list(current.parents):
        if (parent / 'pyproject.toml').exists() or (parent / '.git').exists():
            return parent
    return current


# Find repo root and add scripts to path
_repo_root = _find_repo_root()
_scripts_dir = _repo_root / 'scripts'
if _scripts_dir.exists() and str(_scripts_dir) not in sys.path:
    sys.path.insert(0, str(_scripts_dir))

# Re-export key classes and functions
_import_error = None
try:
    from verify_template_based import TemplateBasedVerifier
    from template_parser import TemplateParser, TemplateSpec, TemplateRequirement
    from parse_chart import extract_frontmatter, ParseError
    from build_cache import build_cache, calculate_euler_characteristic
    from audit_assurance_chart import audit_assurance_chart as audit_chart
except ImportError as e:
    # If running outside repo context, these won't be available
    # This allows the package to be imported even when scripts aren't present
    _import_error = e
    TemplateBasedVerifier = None
    TemplateParser = None
    TemplateSpec = None
    TemplateRequirement = None
    extract_frontmatter = None
    ParseError = None
    build_cache = None
    calculate_euler_characteristic = None
    audit_chart = None

__all__ = [
    'TemplateBasedVerifier',
    'TemplateParser',
    'TemplateSpec',
    'TemplateRequirement',
    'extract_frontmatter',
    'ParseError',
    'build_cache',
    'calculate_euler_characteristic',
    'audit_chart',
]
