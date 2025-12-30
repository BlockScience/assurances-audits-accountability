# Module 05: Concrete Assurance Audits

## Learning Objectives

By the end of this module, learners will be able to:
1. Construct assurance audit charts using the backtracking algorithm
2. Apply the invariant F = V - 1 to verify chart correctness
3. Trace how concrete documents depend on type specs/guidances which depend on the boundary complex
4. Understand why the boundary complex is called "boundary" - it's where the recursion terminates

## Prerequisites

- Module 01-04: Understanding of vertices, edges, faces, and the boundary complex
- Familiarity with verification edges (document → spec) and validation edges (document → guidance)
- Understanding of assurance faces as triangles (verification + validation + coupling)

---

## The Core Insight: Every Document Needs Assurance

When we have a concrete document in our knowledge complex, we need to *assure* it - verify it meets its spec and validate it follows its guidance. But this creates a recursive problem:

> To assure document D, we need spec S and guidance G.
> But S and G are also documents - who assures *them*?

This is where the **backtracking algorithm** comes in.

---

## The Backtracking Algorithm

### Setup

We maintain two sets:
- **needs_assurance**: vertices that don't yet have an assurance face
- **assured**: vertices that have been assigned an assurance face

### The Loop

```
1. Start with your target vertices in needs_assurance
2. While there are non-boundary vertices in needs_assurance:
   a. Pick a vertex V that needs assurance
   b. Create its assurance face (verification + validation + coupling)
   c. Move V to assured
   d. The face introduces spec S and guidance G
   e. If S not in assured, add S to needs_assurance
   f. If G not in assured, add G to needs_assurance
3. When only boundary complex vertices remain in needs_assurance:
   Add the boundary complex (root + 4 faces) to close everything
```

### Why It Terminates

Every vertex eventually traces back to the boundary complex:
- Concrete charts → type specs/guidances → foundational specs/guidances → boundary complex
- The boundary complex (SS, SG, GS, GG) is special - it uses the root vertex to resolve self-reference

---

## Worked Example: Assuring a Tetrahedron Chart

Let's trace through assuring `c:test-tetrahedron`, a chart of type `chart`.

### Step 1: Initialize

```
needs_assurance = {c:test-tetrahedron}
assured = {}
vertices = {c:test-tetrahedron}
faces = {}
```

### Step 2: Assure the Tetrahedron

To assure `c:test-tetrahedron`:
- **Verification target**: What spec does a chart verify against? → `v:spec:chart`
- **Validation target**: What guidance does a chart validate against? → `v:guidance:chart`
- **Create face**: `f:assurance:test-tetrahedron`

```
needs_assurance = {v:spec:chart, v:guidance:chart}
assured = {c:test-tetrahedron}
vertices = {c:test-tetrahedron, v:spec:chart, v:guidance:chart}
faces = {f:assurance:test-tetrahedron}
```

**Count: 3 vertices, 1 face**

### Step 3: Assure spec-for-chart

To assure `v:spec:chart`:
- **Verification target**: All specs verify against → `v:spec:spec`
- **Validation target**: All specs validate against → `v:guidance:spec`
- **Create face**: `f:assurance:chart-spec`

```
needs_assurance = {v:guidance:chart, v:spec:spec, v:guidance:spec}
assured = {c:test-tetrahedron, v:spec:chart}
vertices += {v:spec:spec, v:guidance:spec}
faces += {f:assurance:chart-spec}
```

**Count: 5 vertices, 2 faces**

### Step 4: Assure guidance-for-chart

To assure `v:guidance:chart`:
- **Verification target**: All guidances verify against → `v:spec:guidance`
- **Validation target**: All guidances validate against → `v:guidance:guidance`
- **Create face**: `f:assurance:chart-guidance`

```
needs_assurance = {v:spec:spec, v:guidance:spec, v:spec:guidance, v:guidance:guidance}
assured = {c:test-tetrahedron, v:spec:chart, v:guidance:chart}
vertices += {v:spec:guidance, v:guidance:guidance}
faces += {f:assurance:chart-guidance}
```

**Count: 7 vertices, 3 faces**

### Step 5: Recognize the Boundary

Now `needs_assurance` contains only: `{v:spec:spec, v:guidance:spec, v:spec:guidance, v:guidance:guidance}`

These are exactly the **boundary complex vertices**! The algorithm recognizes this and adds the boundary complex:

- Add `b0:root` (the anchor vertex)
- Add 4 boundary faces:
  - `b2:spec-spec` (assures SS via root)
  - `b2:guidance-guidance` (assures GG via root)
  - `f:assurance:spec-guidance` (assures SG)
  - `f:assurance:guidance-spec` (assures GS)

**Final count: 8 vertices, 7 faces**

### The Invariant Holds

$$F = V - 1$$
$$7 = 8 - 1$$ ✓

Every vertex except `b0:root` has exactly one face that assures it.

---

## Adding More Charts: The Pattern Emerges

### Adding a Syllabus Chart

Starting from the tetrahedron base (8V, 7F), add `c:learning-journey-module-01`:

| Step | Action | New Vertices | New Faces |
|------|--------|--------------|-----------|
| 1 | Assure module-01 | c:learning-journey-module-01 | f:assurance:learning-journey-module-01 |
| 2 | Need v:spec:syllabus | v:spec:syllabus | f:assurance:syllabus-spec |
| 3 | Need v:guidance:syllabus | v:guidance:syllabus | f:assurance:syllabus-guidance |
| 4 | syllabus-spec needs SS, GS | (already have them) | - |
| 5 | syllabus-guidance needs SG, GG | (already have them) | - |

**Net change: +3 vertices, +3 faces**
**New total: 11 vertices, 10 faces** (invariant holds: 10 = 11 - 1)

### Adding an Assurance Audit Chart

Same pattern - add `c:chart-types-audit`:

| Step | Action | New Vertices | New Faces |
|------|--------|--------------|-----------|
| 1 | Assure chart-types-audit | c:chart-types-audit | f:assurance:chart-types-audit |
| 2 | Need v:spec:assurance_audit | v:spec:assurance_audit | f:assurance:assurance_audit-spec |
| 3 | Need v:guidance:assurance_audit | v:guidance:assurance_audit | f:assurance:assurance_audit-guidance |
| 4 | These depend on SS, GS, SG, GG | (already have them) | - |

**Net change: +3 vertices, +3 faces**
**New total: 14 vertices, 13 faces** (invariant holds: 13 = 14 - 1)

---

## Why "Boundary" Complex?

The boundary complex gets its name because it's the **boundary of the recursion**:

1. Every assurance chain eventually reaches it
2. It cannot be assured by "normal" means (SS can't verify against itself without paradox)
3. The root vertex `b0:root` provides the axiomatic anchor
4. It's the topological boundary of the assurance structure

Think of it like the axioms in a mathematical system - you have to start *somewhere*, and the boundary complex is that starting point.

---

## The Chart-Types-Audit Chart

This module's chart (`c:chart-types-audit`) demonstrates the full pattern with three concrete charts:

- `c:test-tetrahedron` (type: chart)
- `c:learning-journey-module-01` (type: syllabus)
- `c:chart-types-audit` (type: assurance_audit)

### Final Structure

| Element | Count |
|---------|-------|
| Vertices | 14 |
| Edges | 34 |
| Faces | 13 |
| Euler characteristic (χ) | -7 |

### Vertex Breakdown

| Category | Vertices | Count |
|----------|----------|-------|
| Root | b0:root | 1 |
| Boundary complex | SS, SG, GS, GG | 4 |
| Chart type | v:spec:chart, v:guidance:chart | 2 |
| Syllabus type | v:spec:syllabus, v:guidance:syllabus | 2 |
| Assurance_audit type | v:spec:assurance_audit, v:guidance:assurance_audit | 2 |
| Concrete charts | c:test-tetrahedron, c:learning-journey-module-01, c:chart-types-audit | 3 |
| **Total** | | **14** |

### Face Breakdown

| Category | Faces | Count |
|----------|-------|-------|
| Boundary faces | b2:spec-spec, b2:guidance-guidance | 2 |
| Cross-domain assurance | f:assurance:spec-guidance, f:assurance:guidance-spec | 2 |
| Chart type assurance | f:assurance:chart-spec, f:assurance:chart-guidance | 2 |
| Syllabus type assurance | f:assurance:syllabus-spec, f:assurance:syllabus-guidance | 2 |
| Assurance_audit type assurance | f:assurance:assurance_audit-spec, f:assurance:assurance_audit-guidance | 2 |
| Concrete chart assurance | f:assurance:test-tetrahedron, f:assurance:learning-journey-module-01, f:assurance:chart-types-audit | 3 |
| **Total** | | **13** |

Every vertex except root has exactly one assurance face. **F = V - 1 = 13 = 14 - 1** ✓

---

## Key Takeaways

1. **Backtracking finds dependencies**: Start with what you want to assure, recursively discover what's needed
2. **The invariant F = V - 1**: Every vertex (except root) gets exactly one assurance face
3. **Boundary complex terminates recursion**: It's where all assurance chains eventually lead
4. **Adding new chart types is predictable**: Each new type adds +3V, +3F (concrete + spec + guidance)
5. **Shared dependencies reduce duplication**: Multiple charts can share the same type specs/guidances

---

## Exercises

1. **Trace the algorithm**: Given `c:my-new-chart` of type `syllabus`, trace through the backtracking algorithm step by step. What vertices and faces are created?

2. **Predict the counts**: If we add a fourth chart type (say, `persona`), what would the new V, F counts be? (Hint: +3V, +3F from current)

3. **Verify the invariant**: For any assurance audit chart, explain why F must always equal V - 1.

4. **Find the root**: In the visualization, identify `b0:root` and trace the boundary edges that connect it to SS, SG, GS, and GG.

---

## Verification Commands

```bash
# Generate the chart structure
python scripts/generate_assurance_audit_elements.py \
  c:test-tetrahedron \
  c:learning-journey-module-01 \
  c:chart-types-audit

# Verify the invariant
# Output should show: F = V - 1 (13 = 14 - 1)
```

---

## Next Module

Module 06 will explore **chart composition** - how multiple charts can be combined while preserving topological invariants.
