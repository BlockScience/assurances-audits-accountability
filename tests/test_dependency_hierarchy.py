#!/usr/bin/env python3
"""
Tests for verify_dependency_hierarchy.py

Tests dependency hierarchy enforcement:
- Specs only depend on specs
- Guidances only depend on guidances
- Docs only depend on docs
- No circular dependencies
"""

import sys
from pathlib import Path
import json
import tempfile

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from verify_dependency_hierarchy import (
    get_vertex_type,
    verify_dependency_hierarchy,
    detect_circular_dependencies
)


class TestGetVertexType:
    """Test vertex type categorization."""

    def test_spec_vertex(self):
        """Test that spec vertices are identified as 'spec'."""
        cache = {
            'elements': {
                'vertices': {
                    'v:spec:persona': {'type': 'vertex/spec', 'id': 'v:spec:persona'}
                }
            }
        }
        assert get_vertex_type('v:spec:persona', cache) == 'spec'

    def test_guidance_vertex(self):
        """Test that guidance vertices are identified as 'guidance'."""
        cache = {
            'elements': {
                'vertices': {
                    'v:guidance:persona': {'type': 'vertex/guidance', 'id': 'v:guidance:persona'}
                }
            }
        }
        assert get_vertex_type('v:guidance:persona', cache) == 'guidance'

    def test_doc_vertex(self):
        """Test that doc vertices (persona, purpose, etc.) are identified as 'doc'."""
        cache = {
            'elements': {
                'vertices': {
                    'v:persona:claude': {'type': 'vertex/persona', 'id': 'v:persona:claude'},
                    'v:purpose:assistant': {'type': 'vertex/purpose', 'id': 'v:purpose:assistant'},
                    'v:protocol:workflow': {'type': 'vertex/protocol', 'id': 'v:protocol:workflow'}
                }
            }
        }
        assert get_vertex_type('v:persona:claude', cache) == 'doc'
        assert get_vertex_type('v:purpose:assistant', cache) == 'doc'
        assert get_vertex_type('v:protocol:workflow', cache) == 'doc'

    def test_other_vertex(self):
        """Test that b0 and test vertices are identified as 'other'."""
        cache = {
            'elements': {
                'vertices': {
                    'v:b0': {'type': 'vertex/b0', 'id': 'v:b0'},
                    'v:test': {'type': 'vertex/test', 'id': 'v:test'}
                }
            }
        }
        assert get_vertex_type('v:b0', cache) == 'other'
        assert get_vertex_type('v:test', cache) == 'other'

    def test_unknown_vertex(self):
        """Test that non-existent vertices return 'unknown'."""
        cache = {'elements': {'vertices': {}}}
        assert get_vertex_type('v:does:not:exist', cache) == 'unknown'


class TestVerifyDependencyHierarchy:
    """Test dependency hierarchy validation."""

    def test_specs_depend_on_specs_valid(self):
        """Test that specs can depend on other specs (valid)."""
        cache = {
            'elements': {
                'vertices': {
                    'v:spec:a': {
                        'type': 'vertex/spec',
                        'dependencies': ['v:spec:b']
                    },
                    'v:spec:b': {
                        'type': 'vertex/spec',
                        'dependencies': []
                    }
                }
            }
        }
        errors = verify_dependency_hierarchy(cache)
        assert len(errors) == 0

    def test_guidances_depend_on_guidances_valid(self):
        """Test that guidances can depend on other guidances (valid)."""
        cache = {
            'elements': {
                'vertices': {
                    'v:guidance:a': {
                        'type': 'vertex/guidance',
                        'dependencies': ['v:guidance:b']
                    },
                    'v:guidance:b': {
                        'type': 'vertex/guidance',
                        'dependencies': []
                    }
                }
            }
        }
        errors = verify_dependency_hierarchy(cache)
        assert len(errors) == 0

    def test_docs_depend_on_docs_valid(self):
        """Test that docs can depend on other docs (valid)."""
        cache = {
            'elements': {
                'vertices': {
                    'v:persona:a': {
                        'type': 'vertex/persona',
                        'dependencies': ['v:purpose:b']
                    },
                    'v:purpose:b': {
                        'type': 'vertex/purpose',
                        'dependencies': []
                    }
                }
            }
        }
        errors = verify_dependency_hierarchy(cache)
        assert len(errors) == 0

    def test_spec_depends_on_guidance_invalid(self):
        """Test that spec depending on guidance is invalid."""
        cache = {
            'elements': {
                'vertices': {
                    'v:spec:a': {
                        'type': 'vertex/spec',
                        'dependencies': ['v:guidance:b']
                    },
                    'v:guidance:b': {
                        'type': 'vertex/guidance',
                        'dependencies': []
                    }
                }
            }
        }
        errors = verify_dependency_hierarchy(cache)
        assert len(errors) == 1
        assert 'v:spec:a' in errors[0]
        assert 'v:guidance:b' in errors[0]
        assert 'same category' in errors[0]

    def test_guidance_depends_on_spec_invalid(self):
        """Test that guidance depending on spec is invalid."""
        cache = {
            'elements': {
                'vertices': {
                    'v:guidance:a': {
                        'type': 'vertex/guidance',
                        'dependencies': ['v:spec:b']
                    },
                    'v:spec:b': {
                        'type': 'vertex/spec',
                        'dependencies': []
                    }
                }
            }
        }
        errors = verify_dependency_hierarchy(cache)
        assert len(errors) == 1
        assert 'v:guidance:a' in errors[0]
        assert 'v:spec:b' in errors[0]

    def test_doc_depends_on_spec_invalid(self):
        """Test that doc depending on spec is invalid."""
        cache = {
            'elements': {
                'vertices': {
                    'v:persona:a': {
                        'type': 'vertex/persona',
                        'dependencies': ['v:spec:persona']
                    },
                    'v:spec:persona': {
                        'type': 'vertex/spec',
                        'dependencies': []
                    }
                }
            }
        }
        errors = verify_dependency_hierarchy(cache)
        assert len(errors) == 1
        assert 'v:persona:a' in errors[0]
        assert 'v:spec:persona' in errors[0]

    def test_unknown_dependency_invalid(self):
        """Test that depending on unknown vertex is invalid."""
        cache = {
            'elements': {
                'vertices': {
                    'v:spec:a': {
                        'type': 'vertex/spec',
                        'dependencies': ['v:does:not:exist']
                    }
                }
            }
        }
        errors = verify_dependency_hierarchy(cache)
        assert len(errors) == 1
        assert 'unknown vertex' in errors[0]
        assert 'v:does:not:exist' in errors[0]

    def test_other_type_no_restrictions(self):
        """Test that 'other' type vertices have no dependency restrictions."""
        cache = {
            'elements': {
                'vertices': {
                    'v:b0': {
                        'type': 'vertex/b0',
                        'dependencies': ['v:spec:a', 'v:guidance:b', 'v:persona:c']
                    },
                    'v:spec:a': {'type': 'vertex/spec', 'dependencies': []},
                    'v:guidance:b': {'type': 'vertex/guidance', 'dependencies': []},
                    'v:persona:c': {'type': 'vertex/persona', 'dependencies': []}
                }
            }
        }
        errors = verify_dependency_hierarchy(cache)
        assert len(errors) == 0  # b0 can depend on anything

    def test_multiple_errors(self):
        """Test that multiple errors are detected."""
        cache = {
            'elements': {
                'vertices': {
                    'v:spec:a': {
                        'type': 'vertex/spec',
                        'dependencies': ['v:guidance:b']  # Error 1
                    },
                    'v:guidance:b': {
                        'type': 'vertex/guidance',
                        'dependencies': ['v:spec:c']  # Error 2
                    },
                    'v:spec:c': {'type': 'vertex/spec', 'dependencies': []}
                }
            }
        }
        errors = verify_dependency_hierarchy(cache)
        assert len(errors) == 2


class TestDetectCircularDependencies:
    """Test circular dependency detection."""

    def test_no_circular_dependencies(self):
        """Test that no circular dependencies are detected when none exist."""
        cache = {
            'elements': {
                'vertices': {
                    'v:a': {'dependencies': ['v:b']},
                    'v:b': {'dependencies': ['v:c']},
                    'v:c': {'dependencies': []}
                }
            }
        }
        errors = detect_circular_dependencies(cache)
        assert len(errors) == 0

    def test_simple_circular_dependency(self):
        """Test detection of simple circular dependency (A -> B -> A)."""
        cache = {
            'elements': {
                'vertices': {
                    'v:a': {'dependencies': ['v:b']},
                    'v:b': {'dependencies': ['v:a']}
                }
            }
        }
        errors = detect_circular_dependencies(cache)
        assert len(errors) == 1
        assert 'Circular dependency' in errors[0]
        assert 'v:a' in errors[0] and 'v:b' in errors[0]

    def test_self_circular_dependency(self):
        """Test detection of self-circular dependency (A -> A)."""
        cache = {
            'elements': {
                'vertices': {
                    'v:a': {'dependencies': ['v:a']}
                }
            }
        }
        errors = detect_circular_dependencies(cache)
        assert len(errors) == 1
        assert 'Circular dependency' in errors[0]

    def test_complex_circular_dependency(self):
        """Test detection of complex circular dependency (A -> B -> C -> A)."""
        cache = {
            'elements': {
                'vertices': {
                    'v:a': {'dependencies': ['v:b']},
                    'v:b': {'dependencies': ['v:c']},
                    'v:c': {'dependencies': ['v:a']}
                }
            }
        }
        errors = detect_circular_dependencies(cache)
        assert len(errors) == 1
        assert 'Circular dependency' in errors[0]
        assert 'v:a' in errors[0]
        assert 'v:b' in errors[0]
        assert 'v:c' in errors[0]

    def test_diamond_dependency_no_cycle(self):
        """Test that diamond dependency (A -> B, A -> C, B -> D, C -> D) has no cycle."""
        cache = {
            'elements': {
                'vertices': {
                    'v:a': {'dependencies': ['v:b', 'v:c']},
                    'v:b': {'dependencies': ['v:d']},
                    'v:c': {'dependencies': ['v:d']},
                    'v:d': {'dependencies': []}
                }
            }
        }
        errors = detect_circular_dependencies(cache)
        assert len(errors) == 0  # Diamond is not a cycle


class TestWithRealCache:
    """Test with actual repository cache."""

    def test_with_actual_cache(self):
        """Test dependency hierarchy with actual repository cache."""
        repo_root = Path(__file__).parent.parent
        cache_file = repo_root / "complex.json"

        if not cache_file.exists():
            print(f"⚠ Skipping: {cache_file} not found")
            return

        with open(cache_file, 'r') as f:
            cache = json.load(f)

        # Check hierarchy
        hierarchy_errors = verify_dependency_hierarchy(cache)
        if hierarchy_errors:
            print(f"✗ Hierarchy errors found in actual cache:")
            for error in hierarchy_errors:
                print(f"  {error}")
        else:
            print(f"✓ No hierarchy errors in actual cache")

        assert len(hierarchy_errors) == 0, f"Found hierarchy violations: {hierarchy_errors}"

        # Check circular dependencies
        circular_errors = detect_circular_dependencies(cache)
        if circular_errors:
            print(f"✗ Circular dependencies found in actual cache:")
            for error in circular_errors:
                print(f"  {error}")
        else:
            print(f"✓ No circular dependencies in actual cache")

        assert len(circular_errors) == 0, f"Found circular dependencies: {circular_errors}"


def run_tests():
    """Run all dependency hierarchy tests."""
    print("=" * 70)
    print("Dependency Hierarchy Tests")
    print("=" * 70)

    # TestGetVertexType
    print("\n--- GetVertexType Tests ---")
    type_tests = TestGetVertexType()

    try:
        type_tests.test_spec_vertex()
        print("✓ test_spec_vertex")
    except AssertionError as e:
        print(f"✗ test_spec_vertex: {e}")
        return False

    try:
        type_tests.test_guidance_vertex()
        print("✓ test_guidance_vertex")
    except AssertionError as e:
        print(f"✗ test_guidance_vertex: {e}")
        return False

    try:
        type_tests.test_doc_vertex()
        print("✓ test_doc_vertex")
    except AssertionError as e:
        print(f"✗ test_doc_vertex: {e}")
        return False

    try:
        type_tests.test_other_vertex()
        print("✓ test_other_vertex")
    except AssertionError as e:
        print(f"✗ test_other_vertex: {e}")
        return False

    try:
        type_tests.test_unknown_vertex()
        print("✓ test_unknown_vertex")
    except AssertionError as e:
        print(f"✗ test_unknown_vertex: {e}")
        return False

    # TestVerifyDependencyHierarchy
    print("\n--- Verify Dependency Hierarchy Tests ---")
    hierarchy_tests = TestVerifyDependencyHierarchy()

    hierarchy_test_methods = [
        ('test_specs_depend_on_specs_valid', hierarchy_tests.test_specs_depend_on_specs_valid),
        ('test_guidances_depend_on_guidances_valid', hierarchy_tests.test_guidances_depend_on_guidances_valid),
        ('test_docs_depend_on_docs_valid', hierarchy_tests.test_docs_depend_on_docs_valid),
        ('test_spec_depends_on_guidance_invalid', hierarchy_tests.test_spec_depends_on_guidance_invalid),
        ('test_guidance_depends_on_spec_invalid', hierarchy_tests.test_guidance_depends_on_spec_invalid),
        ('test_doc_depends_on_spec_invalid', hierarchy_tests.test_doc_depends_on_spec_invalid),
        ('test_unknown_dependency_invalid', hierarchy_tests.test_unknown_dependency_invalid),
        ('test_other_type_no_restrictions', hierarchy_tests.test_other_type_no_restrictions),
        ('test_multiple_errors', hierarchy_tests.test_multiple_errors),
    ]

    for name, test_method in hierarchy_test_methods:
        try:
            test_method()
            print(f"✓ {name}")
        except AssertionError as e:
            print(f"✗ {name}: {e}")
            return False

    # TestDetectCircularDependencies
    print("\n--- Detect Circular Dependencies Tests ---")
    circular_tests = TestDetectCircularDependencies()

    circular_test_methods = [
        ('test_no_circular_dependencies', circular_tests.test_no_circular_dependencies),
        ('test_simple_circular_dependency', circular_tests.test_simple_circular_dependency),
        ('test_self_circular_dependency', circular_tests.test_self_circular_dependency),
        ('test_complex_circular_dependency', circular_tests.test_complex_circular_dependency),
        ('test_diamond_dependency_no_cycle', circular_tests.test_diamond_dependency_no_cycle),
    ]

    for name, test_method in circular_test_methods:
        try:
            test_method()
            print(f"✓ {name}")
        except AssertionError as e:
            print(f"✗ {name}: {e}")
            return False

    # TestWithRealCache
    print("\n--- Real Cache Tests ---")
    real_tests = TestWithRealCache()

    try:
        real_tests.test_with_actual_cache()
        print("✓ test_with_actual_cache")
    except AssertionError as e:
        print(f"✗ test_with_actual_cache: {e}")
        return False

    print("\n" + "=" * 70)
    print("All dependency hierarchy tests passed!")
    print("=" * 70)
    return True


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
