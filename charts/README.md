# Charts

Named collections of vertices, edges, and faces forming coherent subcomplexes within the knowledge complex.

**Navigation:** [[../README|Home]] | [[../NAVIGATION|Navigation Hub]] | [[../00_vertices/README|Vertices]] | [[../01_edges/README|Edges]] | [[../02_faces/README|Faces]]

---

## Summary

| Chart | Purpose | Vertices | Faces |
|-------|---------|----------|-------|
| [[incose-paper-assurance/incose-paper-assurance\|incose-paper-assurance]] | INCOSE paper dual assurance | 24 | 23 |
| [[boundary-complex/boundary-complex\|boundary-complex]] | Foundation layer | 5 | 4 |
| [[test-tetrahedron/test-tetrahedron\|test-tetrahedron]] | Test fixture | 4 | 3 |

---

## Purpose

Charts serve multiple functions:
- **Visualization** - Define what should be visualized together
- **Analysis** - Scope for topological analysis and metrics
- **Documentation** - Communicate structure and relationships
- **Testing** - Regression test baselines for tooling

## Chart Structure

### Frontmatter

```yaml
type: chart/chart
id: c:<name>
name: <Chart Name>
elements:
  vertices:
    - v:<id-1>
    - v:<id-2>
  edges:
    - e:<id-1>
    - e:<id-2>
  faces:
    - f:<id-1>
tags:
  - chart
version: 1.0.0
created: YYYY-MM-DDTHH:MM:SSZ
modified: YYYY-MM-DDTHH:MM:SSZ
```

### Body

Markdown documentation explaining:
- Purpose and scope of the chart
- Structure and topology
- Expected tool behavior
- Visualization suggestions

## Existing Charts

### incose-paper-assurance

**Location:** `charts/incose-paper-assurance/`

**Purpose:** Complete assurance network for the INCOSE IS 2026 paper submission with dual assurance (base + self-demonstration)

**Structure:**

- 24 vertices (5 boundary + 4 INCOSE types + 8 supporting doc types + 4 instances + 1 paper + 2 self-demo)
- 23 faces (dual assurance for paper)
- V - F = 1 invariant satisfied

**Special Property:** Self-demonstrating - the paper exists as a vertex in its own assurance chart

**Files:**

- `incose-paper-assurance.md` - Assurance audit chart document
- `incose-paper-assurance.json` - Parsed chart data
- `incose-paper-assurance.html` - Interactive 3D visualization (layered architecture)

**Usage:**
```bash
# Run assurance audit
python scripts/audit_assurance_chart.py charts/incose-paper-assurance/incose-paper-assurance.md

# Export and visualize
python scripts/export_chart_direct.py charts/incose-paper-assurance/incose-paper-assurance.md
python scripts/visualize_assured_signed.py charts/incose-paper-assurance/incose-paper-assurance.json
```

### boundary-complex

**Location:** `charts/boundary-complex/`

**Purpose:** Foundation layer showing self-referential spec and guidance vertices

**Structure:**

- 5 vertices (root, SS, SG, GS, GG)
- 12 edges
- 4 faces (2 boundary, 2 standard assurance)

**Special Property:** Contains the self-referential foundations (spec-for-spec assures itself)

### test-tetrahedron

**Location:** `charts/test-tetrahedron/`

**Purpose:** Minimal test chart for validating toolchain

**Structure:**
- 4 vertices (alpha, beta, gamma, delta)
- 6 edges (complete graph K₄)
- 3 faces (deliberately missing beta-gamma-delta)

**Special Property:** Topological hole for testing hole detection

**Files:**
- `test-tetrahedron.md` - Assured chart document
- `test-tetrahedron.json` - Parsed chart data for visualization
- `test-tetrahedron.html` - Interactive 3D visualization (RED, GREEN, BLUE faces)

**Usage:**
```bash
# Verify chart structure
python scripts/verify_chart.py charts/test-tetrahedron/test-tetrahedron.md

# Export to JSON for visualization
python scripts/export_chart_direct.py charts/test-tetrahedron/test-tetrahedron.md

# Generate interactive 3D visualization
python scripts/visualize_chart.py charts/test-tetrahedron/test-tetrahedron.json

# Analyze topology
python scripts/topology.py charts/test-tetrahedron/test-tetrahedron.md
```

**Expected Results:**
- ✓ Valid simplicial complex
- ✓ Detects 1 hole (missing face beta-gamma-delta)
- ✓ Euler characteristic χ = 1
- ✓ Visualization shows RED, GREEN, BLUE faces (yellow face missing)

## Creating Charts

### 1. Choose Scope

Decide what elements to include:
- **Feature charts** - Elements for specific feature
- **Process charts** - States and transitions
- **Organization charts** - Actors and relationships
- **Boundary charts** - Foundational elements

### 2. Use Template

Copy `templates/charts/chart.md` and fill in:
- Chart ID and metadata
- Element arrays (vertices, edges, faces)
- Documentation

### 3. Verify Structure

Run verification:
```bash
python scripts/verify_chart.py charts/your-chart.md
```

Checks:
- All referenced elements exist in cache
- Edges have valid vertex boundaries
- Faces have valid edge boundaries
- Forms valid simplicial complex

### 4. Analyze Topology

Optional topological analysis:
```bash
python scripts/topology.py charts/your-chart.md
```

Reports:
- Euler characteristic
- Holes (missing faces)
- Connectivity

## Chart Properties

### Valid Simplicial Complex

A chart is valid if:
1. **Element existence** - All referenced vertices/edges/faces exist
2. **Edge boundaries** - Every edge's source and target are in the chart
3. **Face boundaries** - Every face's boundary edges are in the chart
4. **Boundary matching** - Face vertices match edge endpoints

### Topological Properties

Charts can be analyzed for:
- **Euler characteristic** - χ = V - E + F
- **Holes** - Missing faces in cycles
- **Connectivity** - Number of components
- **Dimension** - Highest dimensional cells

## Visualization

Charts define what to visualize. Common formats:

### Graphviz (DOT)

```bash
# Generate from chart (if implemented)
python scripts/visualize.py charts/your-chart.md --format dot > chart.dot
dot -Tpng chart.dot > chart.png
```

### D3.js Force-Directed Graph

```bash
# Export to JSON for D3
python scripts/export_chart.py charts/your-chart.md --format d3 > chart.json
```

### Hasse Diagram

For hierarchical charts, use Hasse diagram layout.

## Cache Dependency

Charts depend on `complex.json` cache:

```bash
# Build cache from all elements
python scripts/build_cache.py

# Cache contains:
# - All vertices with metadata
# - All edges with source/target
# - All faces with boundaries
```

The cache enables:
- Fast element lookup
- Boundary verification
- Topology analysis

## Best Practices

### Chart Naming

- Use descriptive names: `boundary-complex`, `auth-feature`, `org-structure`
- Use hyphens for multi-word names
- Keep names short but meaningful

### Element Selection

- Include all elements needed for coherent picture
- Don't include unnecessary elements
- Document why elements are included/excluded

### Documentation

- Explain purpose and scope
- Document special properties
- Include expected tool results
- Add visualization suggestions

### Versioning

- Bump version when elements change
- Update modified timestamp
- Document changes in commit messages

## Testing Charts

### Regression Tests

Charts serve as regression test baselines:
```bash
# Test that chart still verifies
python scripts/verify_chart.py charts/test-tetrahedron.md

# Test that topology is correct
python scripts/topology.py charts/test-tetrahedron.md | grep "Holes: 1"
```

### Deliberate Holes

Test charts can include deliberate issues:
- **test-tetrahedron.md** - Missing face for hole detection
- Add more test charts for edge cases

## Common Issues

### "Vertex not found in cache"

**Cause:** Cache out of date or vertex doesn't exist

**Fix:**
```bash
# Rebuild cache
python scripts/build_cache.py

# Or check if vertex exists
ls 00_vertices/v-id.md
```

### "Edge boundary not in chart"

**Cause:** Chart references edge but not its endpoint vertices

**Fix:** Add missing vertices to chart or remove edge

### "Face boundary not in chart"

**Cause:** Chart references face but not its boundary edges

**Fix:** Add missing edges (and their vertices) to chart

## Future Enhancements

Potential additions:
- Chart composition (union, intersection)
- Chart validation (structural requirements)
- Chart templates (common patterns)
- Automated visualization generation
- Interactive exploration tools

---

## Chart Directory Contents

### incose-paper-assurance/

| File | Description |
|------|-------------|
| [[incose-paper-assurance/incose-paper-assurance\|incose-paper-assurance.md]] | Main assurance audit chart |
| [[incose-paper-assurance/incose-paper-assurance-audit-trail\|incose-paper-assurance-audit-trail.md]] | Audit trail record |
| `incose-paper-assurance.json` | Exported chart data |
| `incose-paper-assurance.html` | Interactive 3D visualization |

### boundary-complex/

| File | Description |
|------|-------------|
| [[boundary-complex/boundary-complex\|boundary-complex.md]] | Foundation layer chart |
| [[boundary-complex/boundary-complex-audit-trail\|boundary-complex-audit-trail.md]] | Audit trail record |
| [[boundary-complex/TEACHING-GUIDE\|TEACHING-GUIDE.md]] | Educational guide |
| `boundary-complex.json` | Exported chart data |
| `boundary-complex.html` | Interactive visualization |

### test-tetrahedron/

| File | Description |
|------|-------------|
| [[test-tetrahedron/test-tetrahedron\|test-tetrahedron.md]] | Minimal test fixture |
| [[test-tetrahedron/TEACHING-GUIDE\|TEACHING-GUIDE.md]] | Educational guide |
| `test-tetrahedron.json` | Exported chart data |
| `test-tetrahedron.html` | Interactive visualization |

---

## Related Directories

| Directory | Description |
|-----------|-------------|
| [[../00_vertices/README\|Vertices]] | The nodes that charts reference |
| [[../01_edges/README\|Edges]] | The relationships that charts include |
| [[../02_faces/README\|Faces]] | The triangles that charts contain |
| [[../templates/README\|Templates]] | Type definitions including chart template |
| [[../scripts/README\|Scripts]] | Tools for verification and visualization |
