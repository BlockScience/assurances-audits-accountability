# Audit Trails - Desk Reference

Audit trails verify complete assurance coverage for a chart's vertices using the **F = V - 1 invariant**.

---

## The Invariant: F = V - 1

Every assurance audit chart must satisfy:

```
Faces = Vertices - 1
```

**Why -1?** The root vertex (`b0:root`) provides assurance but is not itself assured by any face. Every other vertex requires exactly one assurance face.

**Example:** boundary-complex has 5 vertices (4 docs + root), so needs 4 assurance faces:
```
F = V - 1
4 = 5 - 1 ✓
```

---

## Running an Audit

```bash
python scripts/audit_assurance_chart.py charts/<name>/<name>.md
```

**Output for PASS:**
```
# Audit Trail for c:boundary-complex

**Status:** PASS
**Coverage:** 100.0% (4/4 vertices)
**Invariant:** F = V - 1: 4 = 5 - 1 ✓

**Boundary Anchoring:** ✅ b2:spec-spec, b2:guidance-guidance

## Vertex Assurance Results

- ✅ `b0:root` (Root vertex - provides assurance, not assured itself)
- ✅ `v:guidance:guidance` → b2:guidance-guidance
- ✅ `v:guidance:spec` → f:assurance:spec-guidance
- ✅ `v:spec:guidance` → f:assurance:guidance-spec
- ✅ `v:spec:spec` → b2:spec-spec
```

**Output for FAIL:**
```
**Status:** FAIL
**Coverage:** 75.0% (3/4 vertices)
**Invariant:** F = V - 1: 3 = 5 - 1 ✗

## Vertex Assurance Results

- ✅ `b0:root` (Root vertex)
- ✅ `v:spec:spec` → b2:spec-spec
- ✅ `v:guidance:guidance` → b2:guidance-guidance
- ❌ `v:spec:guidance` (NO ASSURANCE FACE)
- ✅ `v:guidance:spec` → f:assurance:spec-guidance
```

---

## Existing Audit Trail Charts

| Chart | Status | V | F | Invariant |
|-------|--------|---|---|-----------|
| `boundary-complex` | PASS | 5 | 4 | 4 = 5-1 ✓ |
| `chart-types-audit` | PASS | 14 | 13 | 13 = 14-1 ✓ |

Location: `charts/<name>/<name>-audit-trail.md`

---

## Chart Structure Requirements

For the audit tool to work, the chart must be type `chart/assurance_audit` with:

```yaml
type: chart/assurance_audit
extends: chart
id: c:<name>
assurance_requirements:
  all_vertices_assured: true
  root_vertex: b0:root

elements:
  vertices:
    - b0:root
    - v:spec:spec
    - v:guidance:guidance
    # ... all vertices to audit
  edges:
    # coupling, verification, validation edges
  faces:
    - b2:spec-spec
    - b2:guidance-guidance
    - f:assurance:*
    # one face per non-root vertex
```

---

## Boundary Anchoring

The audit checks that all assurance traces back to `b0:root`:

1. **Self-referential vertices** (SS, GG) use **boundary faces** (b2):
   - `v:spec:spec` → `b2:spec-spec` → `b0:root`
   - `v:guidance:guidance` → `b2:guidance-guidance` → `b0:root`

2. **Other vertices** use **standard assurance faces**:
   - `v:spec:guidance` → `f:assurance:guidance-spec` → depends on SS, GG being assured

The boundary complex (SS, SG, GS, GG) forms the **assurance kernel** - everything traces back through it.

---

## Topology Interpretation

| Metric | Meaning |
|--------|---------|
| **V** | Total vertices being audited (including root) |
| **F** | Total assurance faces |
| **F = V - 1** | Complete coverage (every non-root vertex has one face) |
| **F < V - 1** | Missing assurance faces (gaps in coverage) |
| **F > V - 1** | Over-assurance (redundant faces, not necessarily bad) |

---

## Common Issues

**"Vertex has no assurance face"**
- Missing `f:assurance:*` or `b2:*` face for that vertex
- Check the chart's `elements.faces` list

**"Face references non-existent vertex"**
- Face's target vertex not in chart's vertex list
- Add missing vertex or fix face definition

**"Invariant check failed"**
- Count mismatch between faces and vertices
- Usually means missing faces for some vertices

---

## Generating Audit Trail Files

After running audit, save to file:

```bash
python scripts/audit_assurance_chart.py charts/boundary-complex/boundary-complex.md \
  > charts/boundary-complex/boundary-complex-audit-trail.md
```

The audit trail becomes a versioned artifact showing assurance status at a point in time.

---

## Quick Reference

```bash
# Audit a chart
python scripts/audit_assurance_chart.py charts/<name>/<name>.md

# Verify chart structure first
python scripts/verify_chart.py charts/<name>/<name>.md --root .

# Check topology (different from assurance audit)
python scripts/topology.py charts/<name>/<name>.md --root .
```

**Invariant to remember:** `F = V - 1` (faces = vertices minus root)
