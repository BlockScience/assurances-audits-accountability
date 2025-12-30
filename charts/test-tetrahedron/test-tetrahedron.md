---
type: chart/chart
extends: doc
id: c:test-tetrahedron
name: Test Tetrahedron Chart
description: Minimal test chart for validating toolchain with deliberate topological hole

# Chart construction metadata
constructed_by: "mzargham"
construction_method: manual
construction_date: 2025-12-27T14:50:00Z

# Chart purpose
purpose: Validate knowledge complex toolchain by providing simple structure with deliberate hole
scope: 4 test vertices forming K4 complete graph, with 3 of 4 possible faces (missing beta-gamma-delta)

# Elements comprising this chart
elements:
  vertices:
    - v:test:alpha
    - v:test:beta
    - v:test:gamma
    - v:test:delta
  edges:
    - e:test:alpha:beta
    - e:test:alpha:gamma
    - e:test:alpha:delta
    - e:test:beta:gamma
    - e:test:beta:delta
    - e:test:gamma:delta
  faces:
    - f:test:alpha:beta:gamma
    - f:test:alpha:beta:delta
    - f:test:alpha:gamma:delta

tags:
  - chart
version: 1.0.0
created: 2025-12-27T14:50:00Z
modified: 2025-12-27T20:00:00Z
---

# Test Tetrahedron Chart

A minimal test chart demonstrating a tetrahedron (4 vertices, 6 edges) with a **deliberate topological hole**.

## Purpose

This chart validates the knowledge complex toolchain by providing:
1. Simple structure for testing parsing and verification
2. Deliberate topological hole for validating hole detection
3. Regression test baseline for all script changes

## Structure

**Vertices (4):**
- [alpha](../00_vertices/test-alpha.md)
- [beta](../00_vertices/test-beta.md)
- [gamma](../00_vertices/test-gamma.md)
- [delta](../00_vertices/test-delta.md)

**Edges (6):** Complete graph K₄ (all pairs connected)
- [alpha-beta](../01_edges/test-alpha-beta.md)
- [alpha-gamma](../01_edges/test-alpha-gamma.md)
- [alpha-delta](../01_edges/test-alpha-delta.md)
- [beta-gamma](../01_edges/test-beta-gamma.md)
- [beta-delta](../01_edges/test-beta-delta.md)
- [gamma-delta](../01_edges/test-gamma-delta.md)

**Faces (3 of 4):** Deliberately incomplete
- [alpha-beta-gamma](../02_faces/test-alpha-beta-gamma.md) ✓
- [alpha-beta-delta](../02_faces/test-alpha-beta-delta.md) ✓
- [alpha-gamma-delta](../02_faces/test-alpha-gamma-delta.md) ✓
- **beta-gamma-delta** ✗ **MISSING** (deliberate topological hole)

## Topological Properties

- **Euler Characteristic:** χ = V - E + F = 4 - 6 + 3 = 1 (correct for surface with one hole)
- **Expected Hole:** The missing face beta-gamma-delta creates a triangular hole
- **Connectivity:** Connected (single component)

## Expected Tool Behavior

| Tool | Expected Result |
|------|-----------------|
| `parse_chart.py` | Successfully parses all elements |
| `build_cache.py` | Generates valid complex.json |
| `verify_structure.py` | All elements have valid frontmatter |
| `verify_chart.py` | Valid simplicial complex (edges have vertex boundaries) |
| `topology.py` | **Detects 1 hole** (missing beta-gamma-delta face) |
