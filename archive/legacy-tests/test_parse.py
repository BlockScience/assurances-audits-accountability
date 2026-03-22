#!/usr/bin/env python3
"""
Tests for parse_chart.py
"""

from pathlib import Path
import sys
import tempfile

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from parse_chart import (
    extract_frontmatter,
    parse_element,
    parse_vertex,
    parse_edge,
    parse_face,
    parse_chart,
    ParseError
)


class TestExtractFrontmatter:
    """Test frontmatter extraction."""

    def test_extract_frontmatter_valid(self):
        """Test extracting valid YAML frontmatter."""
        content = """---
type: vertex/vertex
id: v:test
---
Body content here
"""
        frontmatter, body = extract_frontmatter(content)
        assert frontmatter is not None
        assert frontmatter['type'] == 'vertex/vertex'
        assert frontmatter['id'] == 'v:test'
        assert body == 'Body content here'

    def test_extract_frontmatter_missing(self):
        """Test content without frontmatter."""
        content = "Just plain markdown"
        frontmatter, body = extract_frontmatter(content)
        assert frontmatter is None
        assert body == content

    def test_extract_frontmatter_invalid_yaml(self):
        """Test malformed YAML raises ParseError."""
        content = """---
type: vertex
  invalid: yaml: structure
---
Body
"""
        try:
            extract_frontmatter(content)
            assert False, "Should have raised ParseError"
        except ParseError as e:
            assert "Invalid YAML frontmatter" in str(e)


class TestParsing:
    """Test parsing different element types."""

    def test_parse_vertex(self, tmp_path):
        """Test parsing a valid vertex file."""
        vertex_file = tmp_path / "test-vertex.md"
        vertex_file.write_text("""---
type: vertex/vertex
extends: null
id: v:test:alpha
name: Test Vertex
tags:
  - vertex
version: 1.0.0
---
Test content
""")

        vertex = parse_vertex(vertex_file)
        assert vertex['id'] == 'v:test:alpha'
        assert vertex['type'] == 'vertex/vertex'
        assert 'vertex' in vertex['tags']
        assert vertex['body'] == 'Test content'

    def test_parse_edge(self, tmp_path):
        """Test parsing a valid edge file."""
        edge_file = tmp_path / "test-edge.md"
        edge_file.write_text("""---
type: edge/edge
extends: null
id: e:test:a:b
name: Test Edge
source: v:test:a
target: v:test:b
source_type: vertex/vertex
target_type: vertex/vertex
orientation: undirected
tags:
  - edge
version: 1.0.0
---
Edge content
""")

        edge = parse_edge(edge_file)
        assert edge['id'] == 'e:test:a:b'
        assert edge['source'] == 'v:test:a'
        assert edge['target'] == 'v:test:b'
        assert edge['orientation'] == 'undirected'

    def test_parse_face(self, tmp_path):
        """Test parsing a valid face file."""
        face_file = tmp_path / "test-face.md"
        face_file.write_text("""---
type: face/face
extends: null
id: f:test:a:b:c
name: Test Face
vertices:
  - v:test:a
  - v:test:b
  - v:test:c
edges:
  - e:test:a:b
  - e:test:b:c
  - e:test:a:c
orientation: unoriented
tags:
  - face
version: 1.0.0
---
Face content
""")

        face = parse_face(face_file)
        assert face['id'] == 'f:test:a:b:c'
        assert len(face['vertices']) == 3
        assert len(face['edges']) == 3

    def test_parse_face_invalid_vertex_count(self, tmp_path):
        """Test that faces must have exactly 3 vertices."""
        face_file = tmp_path / "test-face.md"
        face_file.write_text("""---
type: face/face
extends: null
id: f:test
name: Test
vertices:
  - v:test:a
  - v:test:b
edges:
  - e:test:a:b
orientation: unoriented
tags:
  - face
version: 1.0.0
---
""")

        try:
            parse_face(face_file)
            assert False, "Should have raised ParseError"
        except ParseError as e:
            assert "exactly 3 vertices" in str(e)

    def test_parse_chart(self, tmp_path):
        """Test parsing a valid chart file."""
        chart_file = tmp_path / "test-chart.md"
        chart_file.write_text("""---
type: chart/chart
extends: null
id: c:test
name: Test Chart
elements:
  vertices:
    - v:test:a
  edges:
    - e:test:a:b
  faces: []
allowed_types:
  vertices: null
  edges: null
  faces: null
constraints: []
tags:
  - chart
version: 1.0.0
---
Chart content
""")

        chart = parse_chart(chart_file)
        assert chart['id'] == 'c:test'
        assert 'elements' in chart
        assert isinstance(chart['elements']['vertices'], list)


def run_tests():
    """Run all parse tests."""
    print("=" * 70)
    print("Element Parsing Tests")
    print("=" * 70)

    # TestExtractFrontmatter
    print("\n--- Frontmatter Extraction Tests ---")
    frontmatter_tests = TestExtractFrontmatter()

    try:
        frontmatter_tests.test_extract_frontmatter_valid()
        print("✓ test_extract_frontmatter_valid")
    except AssertionError as e:
        print(f"✗ test_extract_frontmatter_valid: {e}")
        return False

    try:
        frontmatter_tests.test_extract_frontmatter_missing()
        print("✓ test_extract_frontmatter_missing")
    except AssertionError as e:
        print(f"✗ test_extract_frontmatter_missing: {e}")
        return False

    try:
        frontmatter_tests.test_extract_frontmatter_invalid_yaml()
        print("✓ test_extract_frontmatter_invalid_yaml")
    except AssertionError as e:
        print(f"✗ test_extract_frontmatter_invalid_yaml: {e}")
        return False

    # TestParsing
    print("\n--- Element Parsing Tests ---")
    parsing_tests = TestParsing()

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        try:
            parsing_tests.test_parse_vertex(tmp_path)
            print("✓ test_parse_vertex")
        except AssertionError as e:
            print(f"✗ test_parse_vertex: {e}")
            return False

        try:
            parsing_tests.test_parse_edge(tmp_path)
            print("✓ test_parse_edge")
        except AssertionError as e:
            print(f"✗ test_parse_edge: {e}")
            return False

        try:
            parsing_tests.test_parse_face(tmp_path)
            print("✓ test_parse_face")
        except AssertionError as e:
            print(f"✗ test_parse_face: {e}")
            return False

        try:
            parsing_tests.test_parse_face_invalid_vertex_count(tmp_path)
            print("✓ test_parse_face_invalid_vertex_count")
        except AssertionError as e:
            print(f"✗ test_parse_face_invalid_vertex_count: {e}")
            return False

        try:
            parsing_tests.test_parse_chart(tmp_path)
            print("✓ test_parse_chart")
        except AssertionError as e:
            print(f"✗ test_parse_chart: {e}")
            return False

    print("\n" + "=" * 70)
    print("All element parsing tests passed!")
    print("=" * 70)
    return True


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
