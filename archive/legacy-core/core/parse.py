"""
Parse markdown files with YAML frontmatter into structured element data.

This module provides core parsing functionality for knowledge complex elements
(vertices, edges, faces, charts).
"""

import yaml
import re
from pathlib import Path
from typing import Dict, Any, Optional, List


class ParseError(Exception):
    """Raised when parsing fails."""
    pass


def extract_frontmatter(content: str) -> tuple[Optional[Dict[str, Any]], str]:
    """
    Extract YAML frontmatter and body from markdown content.

    Args:
        content: Raw markdown file content

    Returns:
        Tuple of (frontmatter_dict, body_content)
        frontmatter_dict is None if no frontmatter found

    Raises:
        ParseError: If frontmatter is malformed
    """
    # Match YAML frontmatter: --- at start, content, --- end
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)

    if not match:
        return None, content

    frontmatter_str, body = match.groups()

    try:
        frontmatter = yaml.safe_load(frontmatter_str)
        return frontmatter, body.strip()
    except yaml.YAMLError as e:
        raise ParseError(f"Invalid YAML frontmatter: {e}")


def parse_element(file_path: Path) -> Dict[str, Any]:
    """
    Parse a single element file (vertex, edge, face, or chart).

    Args:
        file_path: Path to markdown file

    Returns:
        Dictionary containing:
            - file: Relative path from repo root
            - All frontmatter fields
            - body: Markdown body content

    Raises:
        ParseError: If file cannot be parsed or is missing required fields
    """
    if not file_path.exists():
        raise ParseError(f"File not found: {file_path}")

    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        raise ParseError(f"Cannot read file {file_path}: {e}")

    frontmatter, body = extract_frontmatter(content)

    if frontmatter is None:
        raise ParseError(f"No YAML frontmatter found in {file_path}")

    # Validate required fields
    required_fields = ['type', 'id', 'name', 'tags', 'version']
    missing = [f for f in required_fields if f not in frontmatter]
    if missing:
        raise ParseError(f"Missing required fields in {file_path}: {missing}")

    # Build element dictionary
    element = {
        'file': str(file_path),
        **frontmatter,
        'body': body
    }

    return element


def parse_vertex(file_path: Path) -> Dict[str, Any]:
    """Parse a vertex file with vertex-specific validation."""
    element = parse_element(file_path)

    if not element['type'].startswith('vertex/'):
        raise ParseError(f"Expected vertex type, got {element['type']}")

    # Vertices must have 'vertex' tag
    if 'vertex' not in element['tags']:
        raise ParseError(f"Vertex {element['id']} missing 'vertex' tag")

    return element


def parse_edge(file_path: Path) -> Dict[str, Any]:
    """Parse an edge file with edge-specific validation."""
    element = parse_element(file_path)

    if not element['type'].startswith('edge/'):
        raise ParseError(f"Expected edge type, got {element['type']}")

    # Edges must have required structural fields
    required = ['source', 'target', 'source_type', 'target_type', 'orientation']
    missing = [f for f in required if f not in element]
    if missing:
        raise ParseError(f"Edge {element['id']} missing fields: {missing}")

    # Edges must have 'edge' tag
    if 'edge' not in element['tags']:
        raise ParseError(f"Edge {element['id']} missing 'edge' tag")

    # Validate orientation
    if element['orientation'] not in ['directed', 'undirected']:
        raise ParseError(f"Edge {element['id']} has invalid orientation: {element['orientation']}")

    return element


def parse_face(file_path: Path) -> Dict[str, Any]:
    """Parse a face file with face-specific validation."""
    element = parse_element(file_path)

    if not element['type'].startswith('face/'):
        raise ParseError(f"Expected face type, got {element['type']}")

    # Faces must have required structural fields
    required = ['vertices', 'edges', 'orientation']
    missing = [f for f in required if f not in element]
    if missing:
        raise ParseError(f"Face {element['id']} missing fields: {missing}")

    # Faces must have 'face' tag
    if 'face' not in element['tags']:
        raise ParseError(f"Face {element['id']} missing 'face' tag")

    # Validate structure
    if not isinstance(element['vertices'], list) or len(element['vertices']) != 3:
        raise ParseError(f"Face {element['id']} must have exactly 3 vertices")

    if not isinstance(element['edges'], list) or len(element['edges']) != 3:
        raise ParseError(f"Face {element['id']} must have exactly 3 edges")

    # Validate orientation
    if element['orientation'] not in ['oriented', 'unoriented']:
        raise ParseError(f"Face {element['id']} has invalid orientation: {element['orientation']}")

    return element


def parse_chart(file_path: Path) -> Dict[str, Any]:
    """Parse a chart file with chart-specific validation."""
    element = parse_element(file_path)

    if not element['type'].startswith('chart/'):
        raise ParseError(f"Expected chart type, got {element['type']}")

    # Charts must have 'chart' tag
    if 'chart' not in element['tags']:
        raise ParseError(f"Chart {element['id']} missing 'chart' tag")

    # Charts must have elements section
    if 'elements' not in element:
        raise ParseError(f"Chart {element['id']} missing 'elements' section")

    elements = element['elements']
    required = ['vertices', 'edges', 'faces']
    missing = [f for f in required if f not in elements]
    if missing:
        raise ParseError(f"Chart {element['id']} elements missing: {missing}")

    # Validate all are lists
    for key in required:
        if not isinstance(elements[key], list):
            raise ParseError(f"Chart {element['id']} elements.{key} must be a list")

    return element


def parse_directory(directory: Path, element_type: str) -> List[Dict[str, Any]]:
    """
    Parse all markdown files in a directory.

    Args:
        directory: Path to directory containing element files
        element_type: One of 'vertex', 'edge', 'face', 'chart'

    Returns:
        List of parsed element dictionaries

    Raises:
        ParseError: If any file fails to parse
    """
    parsers = {
        'vertex': parse_vertex,
        'edge': parse_edge,
        'face': parse_face,
        'chart': parse_chart,
    }

    if element_type not in parsers:
        raise ValueError(f"Unknown element type: {element_type}")

    parser = parsers[element_type]
    elements = []

    if not directory.exists():
        return elements  # Empty list if directory doesn't exist

    # For charts, search recursively in subdirectories
    # For other types, only search direct children
    if element_type == 'chart':
        md_files = sorted(directory.glob('**/*.md'))
    else:
        md_files = sorted(directory.glob('*.md'))

    # Common non-element files to skip silently
    SKIP_FILES = {'README.md', 'TEACHING-GUIDE.md', 'CHANGELOG.md', 'LICENSE.md'}

    parse_errors = []
    for md_file in md_files:
        # Silently skip known non-element files
        if md_file.name in SKIP_FILES:
            continue

        try:
            element = parser(md_file)
            elements.append(element)
        except ParseError as e:
            # Skip files without frontmatter or that don't match expected structure
            # Track errors for debugging (excluding known skip files)
            parse_errors.append((md_file, str(e)))
            continue

    # If we have parse errors for unexpected files, print them as warnings
    if parse_errors:
        import sys
        print(f"Warning: {len(parse_errors)} files skipped in {directory}:", file=sys.stderr)
        for file_path, error in parse_errors[:5]:  # Show first 5 errors
            print(f"  {file_path.name}: {error}", file=sys.stderr)
        if len(parse_errors) > 5:
            print(f"  ... and {len(parse_errors) - 5} more", file=sys.stderr)

    return elements
