"""
Tests for verify_structure.py
"""

import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from verify_structure import verify_directory, verify_all


def test_verify_empty_directory(tmp_path):
    """Test verifying an empty directory."""
    errors = verify_directory(tmp_path, 'vertex')
    assert len(errors) == 0


def test_verify_nonexistent_directory(tmp_path):
    """Test verifying a nonexistent directory."""
    nonexistent = tmp_path / "nonexistent"
    errors = verify_directory(nonexistent, 'vertex')
    assert len(errors) == 0  # Not an error - may be legitimately missing


def test_verify_valid_vertices(tmp_path):
    """Test verifying valid vertex files."""
    vertices_dir = tmp_path / "00_vertices"
    vertices_dir.mkdir()

    (vertices_dir / "test1.md").write_text("""---
type: vertex/vertex
extends: null
id: v:test1
name: Test 1
tags:
  - vertex
version: 1.0.0
---
""")

    (vertices_dir / "test2.md").write_text("""---
type: vertex/vertex
extends: null
id: v:test2
name: Test 2
tags:
  - vertex
version: 1.0.0
---
""")

    errors = verify_directory(vertices_dir, 'vertex')
    assert len(errors) == 0
