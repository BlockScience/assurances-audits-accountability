"""
Verify structural correctness of element files.

Checks that all markdown files have valid YAML frontmatter and required fields.
"""

import argparse
from pathlib import Path
from typing import List

from parse_chart import parse_directory, ParseError


def verify_directory(directory: Path, element_type: str) -> List[str]:
    """
    Verify all files in a directory.

    Args:
        directory: Path to directory
        element_type: Type of elements expected ('vertex', 'edge', 'face', 'chart')

    Returns:
        List of error messages (empty if no errors)
    """
    errors = []

    if not directory.exists():
        # Not an error - directory may be legitimately empty for some repos
        return errors

    if not directory.is_dir():
        errors.append(f"{directory} is not a directory")
        return errors

    try:
        elements = parse_directory(directory, element_type)
        print(f"✓ {directory}: {len(elements)} {element_type}(s) verified")
    except ParseError as e:
        errors.append(f"{directory}: {e}")

    return errors


def verify_all(root_path: Path) -> List[str]:
    """
    Verify all element directories in a repository.

    Args:
        root_path: Root directory containing element directories

    Returns:
        List of all error messages (empty if no errors)
    """
    all_errors = []

    # Verify each directory
    directories = [
        (root_path / '00_vertices', 'vertex'),
        (root_path / '01_edges', 'edge'),
        (root_path / '02_faces', 'face'),
        (root_path / 'charts', 'chart'),
    ]

    for directory, element_type in directories:
        errors = verify_directory(directory, element_type)
        all_errors.extend(errors)

    return all_errors


def main():
    """Command-line interface for verify_structure."""
    parser = argparse.ArgumentParser(
        description='Verify structural correctness of element files'
    )
    parser.add_argument(
        'path',
        type=Path,
        nargs='?',
        default=Path.cwd(),
        help='Directory or file to verify (default: current directory)'
    )
    parser.add_argument(
        '--type',
        choices=['vertex', 'edge', 'face', 'chart'],
        help='Element type (required if path is a directory of elements)'
    )

    args = parser.parse_args()

    path = args.path

    if path.is_file():
        # Single file verification
        # Infer type from path
        if '/00_vertices/' in str(path) or path.parent.name == '00_vertices':
            element_type = 'vertex'
        elif '/01_edges/' in str(path) or path.parent.name == '01_edges':
            element_type = 'edge'
        elif '/02_faces/' in str(path) or path.parent.name == '02_faces':
            element_type = 'face'
        elif '/charts/' in str(path) or path.parent.name == 'charts':
            element_type = 'chart'
        elif args.type:
            element_type = args.type
        else:
            print("Error: Cannot infer element type. Use --type to specify.")
            return 1

        try:
            from parse_chart import parse_vertex, parse_edge, parse_face, parse_chart
            parsers = {
                'vertex': parse_vertex,
                'edge': parse_edge,
                'face': parse_face,
                'chart': parse_chart,
            }
            parsers[element_type](path)
            print(f"✓ {path}: Valid {element_type}")
            return 0
        except ParseError as e:
            print(f"✗ {path}: {e}")
            return 1

    elif path.is_dir():
        # Directory verification
        if args.type:
            # Single directory with known type
            errors = verify_directory(path, args.type)
        else:
            # Root directory - verify all subdirectories
            errors = verify_all(path)

        if errors:
            print(f"\n✗ Verification failed with {len(errors)} error(s):")
            for error in errors:
                print(f"  {error}")
            return 1
        else:
            print("\n✓ All verifications passed!")
            return 0

    else:
        print(f"Error: {path} does not exist")
        return 1


if __name__ == '__main__':
    exit(main())
