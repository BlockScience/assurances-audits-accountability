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
    # First: look for templates relative to this file's location
    # This works for editable installs, development, and standard pip installs
    package_root = Path(__file__).parent.parent
    templates_path = package_root / 'templates'
    if templates_path.exists():
        return templates_path

    # Try importlib.resources approach for installed packages
    # This handles cases where resources are in zip files or other non-filesystem locations
    try:
        templates_ref = files('aaa').joinpath('templates')
        # For traversable resources, try to get the actual path
        if hasattr(templates_ref, '_path'):
            # This is a Path-like object from importlib.resources
            path = Path(templates_ref._path)
            if path.exists():
                return path
        # Try as_file as a fallback (creates temp copy if needed)
        with as_file(templates_ref) as temp_path:
            if temp_path.exists():
                # Return the path - caller must use it within context
                return Path(temp_path)
    except (TypeError, FileNotFoundError, AttributeError):
        pass

    raise FileNotFoundError(
        "Templates directory not found. If you installed the package, "
        "you may need to reinstall. For development, ensure the templates/ "
        "directory exists at the repository root."
    )


def get_bundled_foundation_path() -> Path:
    """
    Return path to bundled foundation documents (e.g., ontology-base.md).

    Returns the path to foundation documents bundled with the package.
    For development (editable install), this returns the source foundation directory.
    For installed packages, this returns the installed foundation location.

    Returns:
        Path to foundation directory

    Raises:
        FileNotFoundError: If foundation directory cannot be found
    """
    # First: look for foundation relative to this file's location
    # This works for editable installs, development, and standard pip installs
    package_root = Path(__file__).parent.parent
    foundation_path = package_root / 'foundation'
    if foundation_path.exists():
        return foundation_path

    # Try importlib.resources approach for installed packages
    try:
        foundation_ref = files('aaa').joinpath('foundation')
        if hasattr(foundation_ref, '_path'):
            path = Path(foundation_ref._path)
            if path.exists():
                return path
        with as_file(foundation_ref) as temp_path:
            if temp_path.exists():
                return Path(temp_path)
    except (TypeError, FileNotFoundError, AttributeError):
        pass

    raise FileNotFoundError(
        "Foundation directory not found. If you installed the package, "
        "you may need to reinstall. For development, ensure the design/ "
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
