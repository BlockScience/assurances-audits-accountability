---
type: chart/assurance_audit
extends: chart
id: c:chart-types-audit
name: Chart Types Assurance Audit
description: Comprehensive assurance audit demonstrating complete assurance coverage for three concrete charts and their type dependencies

# Chart construction metadata
constructed_by: "mzargham"
construction_method: assisted
construction_date: 2025-12-28T00:00:00Z

# Chart purpose
purpose: Demonstrate the backtracking algorithm for assurance audits and validate the F = V - 1 invariant
scope: Three concrete charts (tetrahedron, syllabus, assurance_audit) with full dependency resolution to boundary complex

# Assurance audit specific metadata
audit_date: 2025-12-28T00:00:00Z
auditor: "mzargham"
audit_status: PASS
audit_coverage: 100% (13/13 non-root vertices assured)

# Assurance requirements
assurance_requirements:
  all_vertices_assured: true
  assurance_method: mixed
  minimum_assurance_level: ASSURED
  audit_targets:
    - c:test-tetrahedron
    - c:learning-journey-module-01
    - c:chart-types-audit

# Elements comprising this chart
elements:
  vertices:
    - b0:root
    - c:chart-types-audit
    - c:learning-journey-module-01
    - c:test-tetrahedron
    - v:guidance:assurance_audit
    - v:guidance:chart
    - v:guidance:guidance
    - v:guidance:spec
    - v:guidance:syllabus
    - v:spec:assurance_audit
    - v:spec:chart
    - v:spec:guidance
    - v:spec:spec
    - v:spec:syllabus
  edges:
    - b1:couples-GS-root
    - b1:couples-SG-root
    - b1:self-validation
    - b1:self-verification
    - e:coupling:assurance_audit
    - e:coupling:chart
    - e:coupling:guidance
    - e:coupling:spec
    - e:coupling:spec-guidance:guidance-spec
    - e:coupling:syllabus
    - e:validation:assurance_audit-guidance:guidance-guidance
    - e:validation:assurance_audit-spec:spec-guidance
    - e:validation:chart-guidance:guidance-guidance
    - e:validation:chart-spec:spec-guidance
    - e:validation:chart-types-audit:assurance_audit-guidance
    - e:validation:guidance-spec:guidance-guidance
    - e:validation:learning-journey-module-01:syllabus-guidance
    - e:validation:spec-guidance:guidance-spec
    - e:validation:spec-spec:guidance-spec
    - e:validation:syllabus-guidance:guidance-guidance
    - e:validation:syllabus-spec:spec-guidance
    - e:validation:test-tetrahedron:chart-guidance
    - e:verification:assurance_audit-guidance:guidance-spec
    - e:verification:assurance_audit-spec:spec-spec
    - e:verification:chart-guidance:guidance-spec
    - e:verification:chart-spec:spec-spec
    - e:verification:chart-types-audit:assurance_audit-spec
    - e:verification:guidance-guidance:spec-guidance
    - e:verification:guidance-spec:spec-guidance
    - e:verification:learning-journey-module-01:syllabus-spec
    - e:verification:spec-guidance:spec-spec
    - e:verification:syllabus-guidance:guidance-spec
    - e:verification:syllabus-spec:spec-spec
    - e:verification:test-tetrahedron:chart-spec
  faces:
    - b2:guidance-guidance
    - b2:spec-spec
    - f:assurance:assurance_audit-guidance
    - f:assurance:assurance_audit-spec
    - f:assurance:chart-guidance
    - f:assurance:chart-spec
    - f:assurance:chart-types-audit
    - f:assurance:guidance-spec
    - f:assurance:learning-journey-module-01
    - f:assurance:spec-guidance
    - f:assurance:syllabus-guidance
    - f:assurance:syllabus-spec
    - f:assurance:test-tetrahedron

tags:
  - chart
  - assurance_audit
  - module-05
  - backtracking
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Chart Types Assurance Audit

A comprehensive assurance audit demonstrating the backtracking algorithm for constructing assurance charts. This chart validates three concrete charts and traces their dependencies back to the boundary complex.

## Purpose

This chart serves as Module 05 in the learning journey, demonstrating:
1. **The backtracking algorithm** for discovering assurance dependencies
2. **The F = V - 1 invariant** (every vertex except root has exactly one assurance face)
3. **Dependency resolution** from concrete charts → type specs/guidances → boundary complex
4. **Why the boundary complex is called "boundary"** - it terminates the recursion

## Structure

### Vertices (14)

**Boundary Anchor (1):**
- `b0:root` - The axiomatic anchor (provides assurance, not assured itself)

**Boundary Complex (4):**
- `v:spec:spec` (SS) - Assured by `b2:spec-spec`
- `v:spec:guidance` (SG) - Assured by `f:assurance:spec-guidance`
- `v:guidance:spec` (GS) - Assured by `f:assurance:guidance-spec`
- `v:guidance:guidance` (GG) - Assured by `b2:guidance-guidance`

**Chart Type (2):**
- `v:spec:chart` - Assured by `f:assurance:chart-spec`
- `v:guidance:chart` - Assured by `f:assurance:chart-guidance`

**Syllabus Type (2):**
- `v:spec:syllabus` - Assured by `f:assurance:syllabus-spec`
- `v:guidance:syllabus` - Assured by `f:assurance:syllabus-guidance`

**Assurance Audit Type (2):**
- `v:spec:assurance_audit` - Assured by `f:assurance:assurance_audit-spec`
- `v:guidance:assurance_audit` - Assured by `f:assurance:assurance_audit-guidance`

**Concrete Charts (3):**
- `c:test-tetrahedron` - Assured by `f:assurance:test-tetrahedron`
- `c:learning-journey-module-01` - Assured by `f:assurance:learning-journey-module-01`
- `c:chart-types-audit` - Assured by `f:assurance:chart-types-audit`

### Edges (34)

**Boundary Edges (4):** Connect boundary complex to root
**Coupling Edges (6):** Spec-guidance pairs
**Verification Edges (12):** Document → spec relationships
**Validation Edges (12):** Document → guidance relationships

### Faces (13)

Each face assures exactly one vertex (except root which has no face):

| Vertex | Assurance Face |
|--------|----------------|
| v:spec:spec | b2:spec-spec |
| v:guidance:guidance | b2:guidance-guidance |
| v:spec:guidance | f:assurance:spec-guidance |
| v:guidance:spec | f:assurance:guidance-spec |
| v:spec:chart | f:assurance:chart-spec |
| v:guidance:chart | f:assurance:chart-guidance |
| v:spec:syllabus | f:assurance:syllabus-spec |
| v:guidance:syllabus | f:assurance:syllabus-guidance |
| v:spec:assurance_audit | f:assurance:assurance_audit-spec |
| v:guidance:assurance_audit | f:assurance:assurance_audit-guidance |
| c:test-tetrahedron | f:assurance:test-tetrahedron |
| c:learning-journey-module-01 | f:assurance:learning-journey-module-01 |
| c:chart-types-audit | f:assurance:chart-types-audit |

## Topological Properties

- **Vertices:** V = 14
- **Edges:** E = 34
- **Faces:** F = 13
- **Euler Characteristic:** χ = V - E + F = 14 - 34 + 13 = **-7**

**Key Invariant:** F = V - 1 → 13 = 14 - 1 ✓

## Backtracking Trace

Starting with targets `{c:test-tetrahedron, c:learning-journey-module-01, c:chart-types-audit}`:

1. **Assure tetrahedron** → needs chart spec/guidance → needs SS, GS, SG, GG
2. **Assure module-01** → needs syllabus spec/guidance → (SS, GS, SG, GG already present)
3. **Assure chart-types-audit** → needs assurance_audit spec/guidance → (SS, GS, SG, GG already present)
4. **Boundary complex reached** → add root + 4 boundary faces

Final: 14V, 13F with invariant preserved.

## Verification

```bash
# Generate and verify structure
python scripts/generate_assurance_audit_elements.py \
  c:test-tetrahedron \
  c:learning-journey-module-01 \
  c:chart-types-audit

# Expected output:
#   Vertices: 14
#   Edges: 34
#   Faces: 13
#   Euler characteristic (χ): -7
#   ✓ Invariant holds: F = V - 1 (13 = 14 - 1)
```

---

**Note:** See [TEACHING-GUIDE.md](./TEACHING-GUIDE.md) for detailed explanation of the backtracking algorithm and worked examples.
