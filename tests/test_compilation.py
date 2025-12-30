#!/usr/bin/env python3
"""
Tests for compile_document.py

Tests document compilation with Obsidian embed expansion:
- Extract content without frontmatter
- Resolve embed paths
- Expand simple embeds
- Expand nested embeds
- Handle missing embeds gracefully
"""

import sys
from pathlib import Path
import tempfile

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from compile_document import (
    extract_content_without_frontmatter,
    resolve_embed_path,
    compile_document
)


class TestExtractContentWithoutFrontmatter:
    """Test frontmatter extraction."""

    def test_file_with_frontmatter(self, tmp_path):
        """Test extracting content from file with frontmatter."""
        test_file = tmp_path / "test.md"
        test_file.write_text("""---
type: vertex/persona
id: v:persona:test
---

# Test Persona

This is the content.
""")

        content = extract_content_without_frontmatter(test_file)
        assert content.startswith("# Test Persona")
        assert "type: vertex/persona" not in content
        assert "---" not in content

    def test_file_without_frontmatter(self, tmp_path):
        """Test extracting content from file without frontmatter."""
        test_file = tmp_path / "test.md"
        test_file.write_text("""# Test Document

This is the content.
""")

        content = extract_content_without_frontmatter(test_file)
        assert content.startswith("# Test Document")

    def test_file_not_found(self, tmp_path):
        """Test that FileNotFoundError is raised for missing files."""
        test_file = tmp_path / "does-not-exist.md"

        try:
            extract_content_without_frontmatter(test_file)
            assert False, "Should have raised FileNotFoundError"
        except FileNotFoundError as e:
            assert "does-not-exist.md" in str(e)


class TestResolveEmbedPath:
    """Test embed path resolution."""

    def test_resolve_with_md_extension(self, tmp_path):
        """Test resolving embed with .md extension."""
        base_dir = tmp_path / "00_vertices"
        base_dir.mkdir(exist_ok=True)

        test_file = base_dir / "persona-claude.md"
        test_file.write_text("# Persona")

        resolved = resolve_embed_path("persona-claude.md", base_dir)
        assert resolved == test_file

    def test_resolve_without_md_extension(self, tmp_path):
        """Test resolving embed without .md extension (auto-appends)."""
        base_dir = tmp_path / "00_vertices"
        base_dir.mkdir(exist_ok=True)

        test_file = base_dir / "persona-claude.md"
        test_file.write_text("# Persona")

        resolved = resolve_embed_path("persona-claude", base_dir)
        assert resolved == test_file

    def test_resolve_from_parent_directory(self, tmp_path):
        """Test resolving embed from parent directory."""
        vertices_dir = tmp_path / "00_vertices"
        vertices_dir.mkdir(exist_ok=True)

        test_file = vertices_dir / "persona-claude.md"
        test_file.write_text("# Persona")

        # Resolve from a different subdirectory
        other_dir = tmp_path / "other"
        other_dir.mkdir()

        resolved = resolve_embed_path("persona-claude.md", other_dir)
        assert resolved == test_file

    def test_resolve_not_found(self, tmp_path):
        """Test that FileNotFoundError is raised when embed can't be resolved."""
        base_dir = tmp_path / "00_vertices"
        base_dir.mkdir(exist_ok=True)

        try:
            resolve_embed_path("does-not-exist.md", base_dir)
            assert False, "Should have raised FileNotFoundError"
        except FileNotFoundError as e:
            assert "does-not-exist" in str(e)


class TestCompileDocument:
    """Test document compilation."""

    def test_compile_simple_embed(self, tmp_path):
        """Test compiling document with simple embed."""
        base_dir = tmp_path / "00_vertices"
        base_dir.mkdir(exist_ok=True)

        # Create embedded file
        persona_file = base_dir / "persona-claude.md"
        persona_file.write_text("""---
type: vertex/persona
---

# Persona - Claude

I am an AI assistant.
""")

        # Create source file with embed
        source_file = base_dir / "system_prompt-claude.md"
        source_file.write_text("""---
type: vertex/system_prompt
---

# System Prompt

![[persona-claude]]

That's my persona.
""")

        # Compile
        output_file = tmp_path / "compiled.md"
        compile_document(source_file, output_file, base_dir)

        # Check output
        compiled = output_file.read_text()
        assert "# Persona - Claude" in compiled
        assert "I am an AI assistant." in compiled
        assert "That's my persona." in compiled
        # Frontmatter should NOT be in the embedded content
        assert compiled.count("type: vertex/persona") == 0
        # Original frontmatter should still be there
        assert "type: vertex/system_prompt" in compiled

    def test_compile_multiple_embeds(self, tmp_path):
        """Test compiling document with multiple embeds."""
        base_dir = tmp_path / "00_vertices"
        base_dir.mkdir(exist_ok=True)

        # Create embedded files
        persona_file = base_dir / "persona.md"
        persona_file.write_text("""---
type: vertex/persona
---

# Persona

Persona content.
""")

        purpose_file = base_dir / "purpose.md"
        purpose_file.write_text("""---
type: vertex/purpose
---

# Purpose

Purpose content.
""")

        # Create source with multiple embeds
        source_file = base_dir / "system_prompt.md"
        source_file.write_text("""---
type: vertex/system_prompt
---

# System Prompt

![[persona]]

![[purpose]]

Combined prompt.
""")

        # Compile
        output_file = tmp_path / "compiled.md"
        compile_document(source_file, output_file, base_dir)

        # Check both embeds expanded
        compiled = output_file.read_text()
        assert "Persona content." in compiled
        assert "Purpose content." in compiled
        assert "Combined prompt." in compiled

    def test_compile_nested_embeds(self, tmp_path):
        """Test compiling with nested embeds (embed within embed)."""
        base_dir = tmp_path / "00_vertices"
        base_dir.mkdir(exist_ok=True)

        # Create innermost file
        inner_file = base_dir / "inner.md"
        inner_file.write_text("""---
type: vertex/doc
---

Inner content.
""")

        # Create middle file that embeds inner
        middle_file = base_dir / "middle.md"
        middle_file.write_text("""---
type: vertex/doc
---

Middle start.

![[inner]]

Middle end.
""")

        # Create outer file that embeds middle
        outer_file = base_dir / "outer.md"
        outer_file.write_text("""---
type: vertex/doc
---

Outer start.

![[middle]]

Outer end.
""")

        # Compile outer (recursive expansion - should expand ALL levels)
        output_file = tmp_path / "compiled.md"
        compile_document(outer_file, output_file, base_dir)

        # Check ALL levels expanded (full recursive expansion)
        compiled = output_file.read_text()
        assert "Outer start." in compiled
        assert "Middle start." in compiled
        assert "Inner content." in compiled  # Should be expanded!
        assert "Middle end." in compiled
        assert "Outer end." in compiled
        # Fully compiled means NO embed syntax should remain
        assert "![[" not in compiled

    def test_compile_missing_embed_warning(self, tmp_path):
        """Test that missing embeds generate warning but don't fail."""
        base_dir = tmp_path / "00_vertices"
        base_dir.mkdir(exist_ok=True)

        # Create source with missing embed
        source_file = base_dir / "test.md"
        source_file.write_text("""---
type: vertex/doc
---

# Test

![[does-not-exist]]

Rest of content.
""")

        # Compile (should not raise error)
        output_file = tmp_path / "compiled.md"
        compile_document(source_file, output_file, base_dir)

        # Check that embed syntax is preserved (not expanded)
        compiled = output_file.read_text()
        assert "![[does-not-exist]]" in compiled
        assert "Rest of content." in compiled

    def test_compile_no_embeds(self, tmp_path):
        """Test compiling document with no embeds."""
        base_dir = tmp_path / "00_vertices"
        base_dir.mkdir(exist_ok=True)

        # Create source without embeds
        source_file = base_dir / "test.md"
        source_file.write_text("""---
type: vertex/doc
---

# Test

Just normal content.
""")

        # Compile
        output_file = tmp_path / "compiled.md"
        compile_document(source_file, output_file, base_dir)

        # Check content is unchanged
        compiled = output_file.read_text()
        assert compiled == source_file.read_text()


class TestWithRealDocuments:
    """Test with actual repository documents."""

    def test_compile_actual_system_prompt(self):
        """Test compiling an actual system prompt from repository."""
        repo_root = Path(__file__).parent.parent
        vertices_dir = repo_root / "00_vertices"

        # Find a system_prompt file
        system_prompts = list(vertices_dir.glob("system_prompt-*.md"))
        if not system_prompts:
            print("⚠ Skipping: No system_prompt files found")
            return

        # Try to compile the first one
        source_file = system_prompts[0]
        if "-compiled" in source_file.name:
            print("⚠ Skipping: File is already compiled")
            return

        # Read to check if it has embeds
        content = source_file.read_text()
        if "![[" not in content:
            print(f"⚠ Skipping: {source_file.name} has no embeds")
            return

        # Compile to temp file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as tmp:
            output_file = Path(tmp.name)

        try:
            compile_document(source_file, output_file, vertices_dir)

            # Check that output exists and has content
            compiled = output_file.read_text()
            assert len(compiled) > len(content)  # Should be larger (embeds expanded)
            assert "![[" not in compiled or compiled.count("![[") < content.count("![[")  # Fewer embeds

            print(f"✓ Compiled {source_file.name} ({len(content)} → {len(compiled)} bytes)")
        finally:
            # Cleanup
            if output_file.exists():
                output_file.unlink()


def run_tests():
    """Run all compilation tests."""
    import tempfile

    print("=" * 70)
    print("Document Compilation Tests")
    print("=" * 70)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        # TestExtractContentWithoutFrontmatter
        print("\n--- Extract Content Tests ---")
        extract_tests = TestExtractContentWithoutFrontmatter()

        try:
            extract_tests.test_file_with_frontmatter(tmp_path)
            print("✓ test_file_with_frontmatter")
        except AssertionError as e:
            print(f"✗ test_file_with_frontmatter: {e}")
            return False

        try:
            extract_tests.test_file_without_frontmatter(tmp_path)
            print("✓ test_file_without_frontmatter")
        except AssertionError as e:
            print(f"✗ test_file_without_frontmatter: {e}")
            return False

        try:
            extract_tests.test_file_not_found(tmp_path)
            print("✓ test_file_not_found")
        except AssertionError as e:
            print(f"✗ test_file_not_found: {e}")
            return False

        # TestResolveEmbedPath
        print("\n--- Resolve Embed Path Tests ---")
        resolve_tests = TestResolveEmbedPath()

        try:
            resolve_tests.test_resolve_with_md_extension(tmp_path)
            print("✓ test_resolve_with_md_extension")
        except AssertionError as e:
            print(f"✗ test_resolve_with_md_extension: {e}")
            return False

        try:
            resolve_tests.test_resolve_without_md_extension(tmp_path)
            print("✓ test_resolve_without_md_extension")
        except AssertionError as e:
            print(f"✗ test_resolve_without_md_extension: {e}")
            return False

        try:
            resolve_tests.test_resolve_from_parent_directory(tmp_path)
            print("✓ test_resolve_from_parent_directory")
        except AssertionError as e:
            print(f"✗ test_resolve_from_parent_directory: {e}")
            return False

        try:
            resolve_tests.test_resolve_not_found(tmp_path)
            print("✓ test_resolve_not_found")
        except AssertionError as e:
            print(f"✗ test_resolve_not_found: {e}")
            return False

        # TestCompileDocument
        print("\n--- Compile Document Tests ---")
        compile_tests = TestCompileDocument()

        try:
            compile_tests.test_compile_simple_embed(tmp_path)
            print("✓ test_compile_simple_embed")
        except AssertionError as e:
            print(f"✗ test_compile_simple_embed: {e}")
            return False

        try:
            compile_tests.test_compile_multiple_embeds(tmp_path)
            print("✓ test_compile_multiple_embeds")
        except AssertionError as e:
            print(f"✗ test_compile_multiple_embeds: {e}")
            return False

        try:
            compile_tests.test_compile_nested_embeds(tmp_path)
            print("✓ test_compile_nested_embeds")
        except AssertionError as e:
            print(f"✗ test_compile_nested_embeds: {e}")
            return False

        try:
            compile_tests.test_compile_missing_embed_warning(tmp_path)
            print("✓ test_compile_missing_embed_warning")
        except AssertionError as e:
            print(f"✗ test_compile_missing_embed_warning: {e}")
            return False

        try:
            compile_tests.test_compile_no_embeds(tmp_path)
            print("✓ test_compile_no_embeds")
        except AssertionError as e:
            print(f"✗ test_compile_no_embeds: {e}")
            return False

        # TestWithRealDocuments
        print("\n--- Real Document Tests ---")
        real_tests = TestWithRealDocuments()

        try:
            real_tests.test_compile_actual_system_prompt()
            print("✓ test_compile_actual_system_prompt")
        except AssertionError as e:
            print(f"✗ test_compile_actual_system_prompt: {e}")
            return False

    print("\n" + "=" * 70)
    print("All compilation tests passed!")
    print("=" * 70)
    return True


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
