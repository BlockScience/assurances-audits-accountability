"""
tests/test_init.py

Tests for `aaa init` project scaffolding.
"""

from click.testing import CliRunner

from aaa.commands.init import init


def test_init_creates_directory_structure(tmp_path):
    runner = CliRunner()
    project = tmp_path / "my-project"
    result = runner.invoke(init, [str(project), "--no-git"])
    assert result.exit_code == 0
    assert project.exists()
    assert (project / "00_vertices").is_dir()
    assert (project / "01_edges").is_dir()
    assert (project / "02_faces").is_dir()
    assert (project / "charts").is_dir()


def test_init_copies_foundation_files(tmp_path):
    runner = CliRunner()
    project = tmp_path / "test-project"
    result = runner.invoke(init, [str(project), "--no-git"])
    assert result.exit_code == 0

    # Foundation should include spec-for-spec in 00_vertices
    foundation_vertices = list((project / "00_vertices").glob("*.md"))
    assert len(foundation_vertices) > 0

    # Foundation should include edges
    foundation_edges = list((project / "01_edges").glob("*.md"))
    assert len(foundation_edges) > 0

    # Foundation should include faces
    foundation_faces = list((project / "02_faces").glob("*.md"))
    assert len(foundation_faces) > 0


def test_init_creates_gitignore(tmp_path):
    runner = CliRunner()
    project = tmp_path / "gi-project"
    result = runner.invoke(init, [str(project), "--no-git"])
    assert result.exit_code == 0
    gitignore = project / ".gitignore"
    assert gitignore.exists()
    content = gitignore.read_text()
    assert "complex.json" in content
    assert "graph.ttl" in content


def test_init_creates_readme(tmp_path):
    runner = CliRunner()
    project = tmp_path / "readme-project"
    result = runner.invoke(init, [str(project), "--no-git"])
    assert result.exit_code == 0
    readme = project / "README.md"
    assert readme.exists()
    assert "readme-project" in readme.read_text()


def test_init_fails_if_target_exists(tmp_path):
    runner = CliRunner()
    project = tmp_path / "exists-project"
    project.mkdir()
    result = runner.invoke(init, [str(project)])
    assert result.exit_code != 0
    assert "already exists" in result.output or "already exists" in (result.stderr or "")


def test_init_no_git_skips_git(tmp_path):
    runner = CliRunner()
    project = tmp_path / "no-git-project"
    result = runner.invoke(init, [str(project), "--no-git"])
    assert result.exit_code == 0
    assert not (project / ".git").exists()
