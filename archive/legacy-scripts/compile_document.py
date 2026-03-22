#!/usr/bin/env python3
"""
Compile Obsidian documents by expanding embeds deterministically.

This script reads a markdown document containing Obsidian embed syntax (![[filename]])
and expands all embeds inline by reading the referenced files and inserting their
content (excluding frontmatter). The result is a standalone markdown file suitable
for deployment or assurance verification.

Usage:
    python scripts/compile_document.py <source.md> <output.md> [--base-dir <dir>]

Example:
    python scripts/compile_document.py \\
        00_vertices/system_prompt-claude-assistant.md \\
        00_vertices/system_prompt-claude-assistant-compiled.md
"""

import re
import sys
from pathlib import Path
from typing import Tuple, Optional


def extract_content_without_frontmatter(file_path: Path) -> str:
    """
    Read a markdown file and return content without YAML frontmatter.

    Args:
        file_path: Path to markdown file

    Returns:
        File content with frontmatter removed

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Embedded file not found: {file_path}")

    content = file_path.read_text(encoding='utf-8')

    # Check if file starts with frontmatter (---)
    if content.startswith('---\n'):
        # Find the closing --- of frontmatter
        parts = content.split('---\n', 2)
        if len(parts) >= 3:
            # parts[0] is empty, parts[1] is frontmatter, parts[2] is content
            return parts[2].lstrip('\n')

    # No frontmatter found, return full content
    return content


def resolve_embed_path(embed_ref: str, base_dir: Path) -> Path:
    """
    Resolve an Obsidian embed reference to a file path.

    Args:
        embed_ref: The reference string from ![[reference]]
        base_dir: Base directory to search from (usually 00_vertices)

    Returns:
        Resolved path to the embedded file

    Raises:
        FileNotFoundError: If referenced file can't be found
    """
    # Try with .md extension if not present
    if not embed_ref.endswith('.md'):
        embed_ref = f"{embed_ref}.md"

    # Try relative to base_dir
    candidate = base_dir / embed_ref
    if candidate.exists():
        return candidate

    # Try in parent directory (for 00_vertices/file.md referencing other files in 00_vertices)
    parent_candidate = base_dir.parent / "00_vertices" / embed_ref
    if parent_candidate.exists():
        return parent_candidate

    raise FileNotFoundError(f"Cannot resolve embed reference: {embed_ref}")


def compile_document(source_path: Path, output_path: Path, base_dir: Optional[Path] = None) -> None:
    """
    Compile a document by expanding all Obsidian embeds.

    Args:
        source_path: Path to source document with embeds
        output_path: Path to write compiled output
        base_dir: Base directory for resolving embeds (defaults to source_path parent)
    """
    if base_dir is None:
        base_dir = source_path.parent

    # Read source document
    if not source_path.exists():
        raise FileNotFoundError(f"Source document not found: {source_path}")

    source_content = source_path.read_text(encoding='utf-8')

    # Pattern to match Obsidian embeds: ![[reference]]
    embed_pattern = re.compile(r'!\[\[([^\]]+)\]\]')

    def expand_embed(match: re.Match) -> str:
        """Replace embed with actual content."""
        embed_ref = match.group(1)
        try:
            embed_path = resolve_embed_path(embed_ref, base_dir)
            embedded_content = extract_content_without_frontmatter(embed_path)
            return embedded_content.rstrip('\n')  # Remove trailing newlines
        except FileNotFoundError as e:
            # If embed can't be resolved, leave it as-is and warn
            print(f"WARNING: {e}", file=sys.stderr)
            return match.group(0)  # Return original embed syntax

    # Expand all embeds recursively (keep expanding until no embeds remain)
    compiled_content = source_content
    max_iterations = 100  # Prevent infinite loops
    iteration = 0

    while embed_pattern.search(compiled_content) and iteration < max_iterations:
        compiled_content = embed_pattern.sub(expand_embed, compiled_content)
        iteration += 1

    if iteration >= max_iterations:
        print(f"WARNING: Reached maximum iterations ({max_iterations}), possible circular embeds", file=sys.stderr)

    # Write compiled output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(compiled_content, encoding='utf-8')

    print(f"✓ Compiled: {source_path} → {output_path} ({iteration} passes)")


def main():
    """Main entry point."""
    if len(sys.argv) < 3:
        print("Usage: python scripts/compile_document.py <source.md> <output.md> [--base-dir <dir>]")
        print()
        print("Example:")
        print("  python scripts/compile_document.py \\")
        print("      00_vertices/system_prompt-claude-assistant.md \\")
        print("      00_vertices/system_prompt-claude-assistant-compiled.md")
        sys.exit(1)

    source_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    base_dir = None
    if len(sys.argv) >= 5 and sys.argv[3] == '--base-dir':
        base_dir = Path(sys.argv[4])

    try:
        compile_document(source_path, output_path, base_dir)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
