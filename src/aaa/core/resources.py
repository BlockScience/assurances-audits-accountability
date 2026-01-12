"""
Resource utilities for AAA package.

Provides functions to locate bundled templates and other package resources.
"""

from pathlib import Path
from importlib.resources import files, as_file
from typing import Optional


def get_bundled_templates_path() -> Path:
    """
    Return path to bundled templates.

    Returns the path to templates bundled with the package. For development
    (editable install), this returns the source templates directory.
    For installed packages, this returns the installed templates location.

    Returns:
        Path to templates directory

    Raises:
        FileNotFoundError: If templates directory cannot be found
    """
    # Try importlib.resources approach for installed packages
    try:
        templates_ref = files('aaa').joinpath('templates')
        # Check if this path exists
        with as_file(templates_ref) as templates_path:
            if templates_path.exists():
                return templates_path
    except (TypeError, FileNotFoundError):
        pass

    # Fallback: look for templates relative to this file's location
    # This works for editable installs and development
    package_root = Path(__file__).parent.parent
    templates_path = package_root / 'templates'
    if templates_path.exists():
        return templates_path

    # Another fallback: look in repo root (for development without install)
    repo_root = package_root.parent.parent
    templates_path = repo_root / 'templates'
    if templates_path.exists():
        return templates_path

    raise FileNotFoundError(
        "Templates directory not found. If you installed the package, "
        "you may need to reinstall. For development, ensure the templates/ "
        "directory exists at the repository root."
    )


def get_templates_path(custom_path: Optional[Path] = None) -> Path:
    """
    Get templates path, preferring custom path if provided.

    Args:
        custom_path: Optional custom path to templates directory

    Returns:
        Path to templates directory (custom if provided, bundled otherwise)

    Raises:
        FileNotFoundError: If templates cannot be found
    """
    if custom_path is not None:
        custom_path = Path(custom_path)
        if not custom_path.exists():
            raise FileNotFoundError(f"Custom templates path not found: {custom_path}")
        return custom_path

    return get_bundled_templates_path()
