# Charts vs Chart Documents

**Date:** 2025-12-27
**Topic:** Conceptual distinction between charts (mathematical objects) and chart documents (vertices)

---

## The Distinction

### Charts (Mathematical Objects)

**What they are:**
- Simplicial complexes composed of vertices, edges, and faces
- Mathematical structures with topological properties
- The subject of analysis (Euler characteristic, holes, connectivity)
- NOT vertices in the knowledge complex

**Example:**
The test tetrahedron IS a simplicial complex with:
- 4 vertices: alpha, beta, gamma, delta
- 6 edges: all pairs connected (K₄)
- 3 faces: alpha-beta-gamma, alpha-beta-delta, alpha-gamma-delta
- 1 hole: missing face beta-gamma-delta

**ID Prefix:** Charts themselves don't have IDs in the knowledge complex

### Chart Documents (Vertices)

**What they are:**
- Markdown files that DESCRIBE charts
- Vertices that extend doc type
- Documents ABOUT charts
- Subject to assurance (verification, validation, assurance faces)

**Example:**
The test-tetrahedron chart document `c:test-tetrahedron` IS a vertex that:
- Located at `charts/test-tetrahedron/test-tetrahedron.md`
- Has `type: chart/chart` and `extends: doc`
- Contains frontmatter describing the chart
- Can be verified against spec-for-charts
- Can be validated against guidance-for-charts
- Can participate in assurance faces

**ID Prefix:** `c:` (for chart document)

---

## Why This Matters

### Type System Clarity

**Correct Statement:**
- "The chart document `c:test-tetrahedron` is a vertex that extends doc"

**Incorrect Statement:**
- "The chart is a vertex" (charts are not vertices!)

### Assurance Framework

**What Gets Assured:**
- The **chart document** (the markdown file describing a chart)
- We verify the document has required structure
- We validate the document meets quality criteria
- We attest the document is trustworthy

**What Doesn't Get Assured:**
- The **chart** (the mathematical simplicial complex)
- We can verify the chart forms a valid simplicial complex
- But this is a different kind of verification (mathematical, not documentary)

### Edge Types

**Verification Edge:**
- Source: `c:test-tetrahedron` (chart document - a vertex)
- Target: `v:spec:chart` (spec document - a vertex)
- Source Type: `vertex/doc/chart`
- Target Type: `vertex/doc/spec`

**NOT:**
- Source: "the chart" (not a vertex!)
- Source Type: `chart/chart` (this is the type field value, not the source_type)

---

## Analogies

### Similar Patterns in Knowledge Complex

**Spec Documents vs The Things They Specify:**
- `v:spec:spec` is a vertex (document) that specifies specifications
- The specification itself (as a concept) is not a vertex
- We verify spec documents against spec-for-spec
- We don't "verify specifications" in the abstract

**Guidance Documents vs The Practices They Guide:**
- `v:guidance:spec` is a vertex (document) providing guidance
- The best practices themselves are not vertices
- We validate guidance documents against guidance-for-guidance
- We don't "validate guidance" in the abstract

**Chart Documents vs The Charts They Describe:**
- `c:test-tetrahedron` is a vertex (document) describing a chart
- The simplicial complex itself is not a vertex
- We verify chart documents against spec-for-charts
- We analyze charts mathematically with topology.py

---

## File Organization Reflects This

### Chart Documents (Vertices)

**Location:** `charts/test-tetrahedron/test-tetrahedron.md`
**Purpose:** Document describing the chart
**Type:** `vertex/doc/chart`
**Participates In:**
- Verification edges (against spec-for-charts)
- Validation edges (against guidance-for-charts)
- Assurance faces (complete assurance triangle)

### Chart Data (Derived Artifacts)

**Location:** `charts/test-tetrahedron/test-tetrahedron.json`
**Purpose:** Parsed representation of chart for visualization
**Not A Vertex:** This is data, not a document subject to assurance

### Chart Visualization (Derived Artifacts)

**Location:** `charts/test-tetrahedron/test-tetrahedron.html`
**Purpose:** Interactive 3D rendering of the chart
**Not A Vertex:** This is a visual artifact, not a document subject to assurance

---

## Implications for Development

### When Creating Verification Edges

**DO:**
```yaml
source: c:test-tetrahedron        # Chart document (vertex)
target: v:spec:chart              # Spec document (vertex)
source_type: vertex/doc/chart     # Full inheritance chain
target_type: vertex/doc/spec      # Full inheritance chain
```

**DON'T:**
```yaml
source: c:test-tetrahedron
target: v:spec:chart
source_type: chart/chart          # This is type field value, not source_type!
target_type: vertex/spec          # Inconsistent inheritance notation
```

### When Writing Documentation

**DO:**
- "The chart document verifies against spec-for-charts"
- "The chart (mathematical object) has Euler characteristic χ = 1"
- "Chart documents extend doc and can participate in assurance"

**DON'T:**
- "The chart is a vertex" (charts are not vertices!)
- "The chart verifies" (chart documents verify, not charts)
- "Charts can be assured" (chart documents can be assured)

### When Building Tools

**Distinguish:**
- **verify_chart.py** - Verifies chart (mathematical object) is valid simplicial complex
- **verify_template_based.py** - Verifies chart document (vertex) meets structural requirements
- First is mathematical verification
- Second is documentary verification

---

## Summary

| Aspect | Charts | Chart Documents |
|--------|--------|-----------------|
| **What** | Mathematical simplicial complexes | Markdown files describing charts |
| **Are they vertices?** | NO | YES (extend doc) |
| **ID prefix** | N/A | `c:` |
| **Type** | N/A | `vertex/doc/chart` (extends `chart/chart`) |
| **Location** | Described in files | `charts/<name>/<name>.md` |
| **Verification** | Mathematical (topology.py) | Documentary (verify_template_based.py) |
| **Assurance** | Not applicable | Full assurance framework applies |
| **Examples** | K₄, tetrahedron, boundary complex | `c:test-tetrahedron` |

**Key Insight:** Chart documents are vertices that extend doc. Charts (the mathematical objects) are what those documents describe. We assure documents, not mathematical structures.

---

**Reference:** This distinction is documented in:
- `01_edges/verification-test-tetrahedron.md` (Important Conceptual Note)
- `02_faces/assurance-test-tetrahedron.md` (Important Conceptual Note)
- This document

**Status:** Clarified 2025-12-27 after merge block revealed type confusion
