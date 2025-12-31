#!/usr/bin/env python3
"""
Verify dependency hierarchy correctness.

Ensures that:
- Specs only depend on other specs
- Guidances only depend on other guidances
- Concrete documents only depend on other concrete documents (not specs/guidances)
- No circular dependencies

This enforces proper separation between type/template level and instance level.
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple


def load_cache(cache_path: Path) -> Dict:
    """Load the complex.json cache."""
    if not cache_path.exists():
        raise FileNotFoundError(f"Cache not found: {cache_path}")

    with open(cache_path, 'r') as f:
        return json.load(f)


def get_vertex_type(vertex_id: str, cache: Dict) -> str:
    """
    Determine the category of a vertex.

    Returns: 'spec', 'guidance', 'doc', or 'other'
    """
    vertices = cache['elements']['vertices']

    if vertex_id not in vertices:
        return 'unknown'

    vertex = vertices[vertex_id]
    vertex_type = vertex.get('type', '')

    if vertex_type.startswith('vertex/spec'):
        return 'spec'
    elif vertex_type.startswith('vertex/guidance'):
        return 'guidance'
    elif vertex_type in ['vertex/b0', 'vertex/test', 'vertex/signer']:
        return 'other'  # Boundary vertices, test vertices, and signers are special
    elif vertex_type.startswith('vertex/'):
        # All other typed vertices (persona, purpose, protocol, system_prompt, etc.)
        # are concrete documents
        return 'doc'
    else:
        return 'other'


def verify_dependency_hierarchy(cache: Dict) -> List[str]:
    """
    Verify that dependency hierarchies are correct.

    Rules:
    - Specs can only depend on specs
    - Guidances can only depend on guidances
    - Docs can only depend on docs (not specs or guidances)
    - 'other' types (b0, test) have no restrictions

    Returns:
        List of error messages (empty if valid)
    """
    errors = []
    vertices = cache['elements']['vertices']

    for vertex_id, vertex in vertices.items():
        dependencies = vertex.get('dependencies', [])

        # Skip if no dependencies
        if not dependencies:
            continue

        vertex_category = get_vertex_type(vertex_id, cache)

        # Skip 'other' category vertices (no restrictions)
        if vertex_category == 'other':
            continue

        # Check each dependency
        for dep_id in dependencies:
            dep_category = get_vertex_type(dep_id, cache)

            # Unknown dependencies are errors
            if dep_category == 'unknown':
                errors.append(
                    f"ERROR: {vertex_id} ({vertex_category}) depends on unknown vertex: {dep_id}"
                )
                continue

            # Skip if dependency is 'other' (allowed for all)
            if dep_category == 'other':
                continue

            # Enforce same-category rule
            if vertex_category != dep_category:
                errors.append(
                    f"ERROR: {vertex_id} ({vertex_category}) cannot depend on "
                    f"{dep_id} ({dep_category}) - must depend on same category"
                )

    return errors


def detect_circular_dependencies(cache: Dict) -> List[str]:
    """
    Detect circular dependencies using DFS.

    Returns:
        List of error messages describing cycles (empty if no cycles)
    """
    errors = []
    vertices = cache['elements']['vertices']

    # Build adjacency list
    graph = {vid: vertex.get('dependencies', []) for vid, vertex in vertices.items()}

    # Track visited nodes and current path
    visited = set()
    rec_stack = set()

    def has_cycle(node: str, path: List[str]) -> bool:
        """DFS to detect cycles."""
        visited.add(node)
        rec_stack.add(node)
        path.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if has_cycle(neighbor, path):
                    return True
            elif neighbor in rec_stack:
                # Found a cycle
                cycle_start = path.index(neighbor)
                cycle = path[cycle_start:] + [neighbor]
                errors.append(
                    f"ERROR: Circular dependency detected: {' -> '.join(cycle)}"
                )
                return True

        path.pop()
        rec_stack.remove(node)
        return False

    # Check each unvisited node
    for vertex_id in graph:
        if vertex_id not in visited:
            has_cycle(vertex_id, [])

    return errors


def print_dependency_summary(cache: Dict):
    """Print summary of dependencies by category."""
    vertices = cache['elements']['vertices']

    # Categorize vertices with dependencies
    spec_deps = []
    guidance_deps = []
    doc_deps = []
    other_deps = []

    for vertex_id, vertex in vertices.items():
        dependencies = vertex.get('dependencies', [])
        if not dependencies:
            continue

        category = get_vertex_type(vertex_id, cache)
        dep_info = (vertex_id, dependencies)

        if category == 'spec':
            spec_deps.append(dep_info)
        elif category == 'guidance':
            guidance_deps.append(dep_info)
        elif category == 'doc':
            doc_deps.append(dep_info)
        else:
            other_deps.append(dep_info)

    print("\n=== Dependency Summary ===")
    print(f"\nSpecs with dependencies: {len(spec_deps)}")
    for vid, deps in spec_deps:
        print(f"  {vid} -> {len(deps)} spec(s)")

    print(f"\nGuidances with dependencies: {len(guidance_deps)}")
    for vid, deps in guidance_deps:
        print(f"  {vid} -> {len(deps)} guidance(s)")

    print(f"\nDocs with dependencies: {len(doc_deps)}")
    for vid, deps in doc_deps:
        print(f"  {vid} -> {len(deps)} doc(s)")

    if other_deps:
        print(f"\nOther vertices with dependencies: {len(other_deps)}")
        for vid, deps in other_deps:
            print(f"  {vid} -> {len(deps)} dep(s)")


def main():
    """Main verification routine."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Verify dependency hierarchy correctness'
    )
    parser.add_argument(
        '--cache',
        type=Path,
        default=Path.cwd() / 'complex.json',
        help='Path to complex.json cache file'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print detailed dependency summary'
    )

    args = parser.parse_args()

    # Load cache
    try:
        cache = load_cache(args.cache)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1

    print(f"Verifying dependency hierarchies from: {args.cache}")

    # Check hierarchy rules
    hierarchy_errors = verify_dependency_hierarchy(cache)

    # Check for circular dependencies
    circular_errors = detect_circular_dependencies(cache)

    # Combine all errors
    all_errors = hierarchy_errors + circular_errors

    # Print results
    if all_errors:
        print(f"\n❌ FAILED - {len(all_errors)} error(s) found:\n")
        for error in all_errors:
            print(f"  {error}")

        if args.verbose:
            print_dependency_summary(cache)

        return 1
    else:
        print("\n✅ PASSED - All dependency hierarchies are valid")
        print("  - Specs only depend on specs")
        print("  - Guidances only depend on guidances")
        print("  - Docs only depend on docs")
        print("  - No circular dependencies detected")

        if args.verbose:
            print_dependency_summary(cache)

        return 0


if __name__ == '__main__':
    sys.exit(main())
