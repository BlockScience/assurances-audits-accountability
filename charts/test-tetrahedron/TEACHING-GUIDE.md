# Teaching Guide: Test Tetrahedron

**Stage 1: Introduction to Simplicial Complexes**

**Prerequisites:** None - this is the entry point

**Time Required:** 30-45 minutes

---

## Learning Objectives

By the end of this lesson, you will understand:

1. **What is a simplicial complex?** The fundamental building blocks (vertices, edges, faces)
2. **What makes a valid complex?** Boundary constraints and closure properties
3. **What is the Euler characteristic?** The topological invariant χ = V - E + F
4. **What are topological holes?** How missing faces create detectable gaps
5. **How to verify structure?** Using topology.py to detect holes

---

## What You're Looking At

The **test-tetrahedron** is the simplest possible non-trivial simplicial complex: a tetrahedron (4-sided pyramid) with one face deliberately removed.

### The Structure

**4 Vertices (0-cells):**
- [alpha.md](../../00_vertices/alpha.md) - First corner
- [beta.md](../../00_vertices/beta.md) - Second corner
- [gamma.md](../../00_vertices/gamma.md) - Third corner
- [delta.md](../../00_vertices/delta.md) - Fourth corner

**6 Edges (1-cells):** All possible pairs connected
- alpha ↔ beta
- alpha ↔ gamma
- alpha ↔ delta
- beta ↔ gamma
- beta ↔ delta
- gamma ↔ delta

**3 Faces (2-cells):** Only 3 of the 4 possible triangular faces
- ✓ Triangle(alpha, beta, gamma)
- ✓ Triangle(alpha, beta, delta)
- ✓ Triangle(alpha, gamma, delta)
- ✗ **MISSING:** Triangle(beta, gamma, delta) ← This is the hole!

---

## Key Concepts

### 1. Simplices (Singular: Simplex)

A **simplex** is the generalization of a triangle to arbitrary dimensions:

| Dimension | Name | Example | Boundary |
|-----------|------|---------|----------|
| 0 | Vertex | A single point | ∅ (empty) |
| 1 | Edge | Line segment | 2 vertices |
| 2 | Face | Triangle | 3 edges (which have 3 vertices) |
| 3 | Cell | Tetrahedron | 4 faces (which have 6 edges, 4 vertices) |

**Key Property:** The boundary of a simplex is itself made of lower-dimensional simplices.

### 2. Simplicial Complex

A **simplicial complex** is a collection of simplices where:

1. **Closure:** If a simplex is in the complex, all its faces (boundaries) must also be in the complex
2. **Intersection:** Any two simplices either don't intersect, or intersect in a common boundary element

**Example in test-tetrahedron:**
- Face(alpha, beta, gamma) is in the complex
- Therefore edges alpha-beta, beta-gamma, alpha-gamma MUST be in the complex ✓
- Therefore vertices alpha, beta, gamma MUST be in the complex ✓

### 3. Euler Characteristic

The **Euler characteristic** (χ, pronounced "kai" or "kye") is defined as:

**χ = V - E + F**

where:
- V = number of vertices
- E = number of edges
- F = number of faces

**For test-tetrahedron:**
- V = 4 (alpha, beta, gamma, delta)
- E = 6 (all pairs)
- F = 3 (only 3 of 4 triangles)
- **χ = 4 - 6 + 3 = 1**

**What does χ = 1 mean?**
- A complete tetrahedron (all 4 faces) would have χ = 2
- A sphere has χ = 2
- A torus (donut) has χ = 0
- Our incomplete tetrahedron has χ = 1, indicating **one topological hole**

The Euler characteristic is a **topological invariant** - it doesn't change if you bend, stretch, or deform the shape (but it does change if you tear or glue).

### 4. Topological Holes

A **topological hole** is a place where a face COULD exist (all its boundary edges are present) but DOESN'T exist.

**In test-tetrahedron:**
- We have edges: beta-gamma, gamma-delta, beta-delta
- These three edges form a complete triangle boundary
- But we don't have face(beta, gamma, delta)
- This missing face = **a hole in the structure**

**Why does this matter?**
Holes are meaningful! In different domains:
- **Organizations:** Unfilled positions (person qualified, team needs role, but no assignment)
- **Assurance:** Documentation gaps (document exists, spec exists, but no verification edge)
- **Workflows:** Missing approvals (all dependencies ready, but no sign-off)

---

## Teaching Moments

### Moment 1: The Complete Graph vs The Hole

**Observation:** All 6 possible edges exist (complete graph K₄), but only 3 of 4 possible faces exist.

**Question:** "If all the edges are there, why can't we just assume the face is there?"

**Answer:** Because simplicial complexes are **explicit, not implicit**. We only include what we explicitly list. This explicitness enables:
- Detection of gaps (what's missing matters!)
- Verification (can check completeness)
- Intentional design (holes may be deliberate)

### Moment 2: The Euler Characteristic Detects the Hole

**Observation:** χ = 1 instead of χ = 2

**Calculation:**
- Complete tetrahedron: V=4, E=6, F=4 → χ = 4-6+4 = 2
- Our tetrahedron: V=4, E=6, F=3 → χ = 4-6+3 = 1
- Difference: Δχ = -1 (one missing face)

**Insight:** The Euler characteristic **counts holes**! Each missing face decreases χ by 1.

### Moment 3: Verification Without Semantics

**Observation:** These vertices have no meaning - they're just labeled alpha, beta, gamma, delta.

**Question:** "Can we verify structure without knowing what the vertices represent?"

**Answer:** Yes! Topological verification is **purely structural**:
- Do edges connect vertices in the complex? ✓
- Do faces reference edges in the complex? ✓
- Do face vertices match edge boundaries? ✓
- Euler characteristic consistent? ✓

This separation of structure from semantics is powerful - we'll add semantics in Stage 2.

---

## Hands-On Exercises

### Exercise 1: Verify the Structure

Run the topology verification script:

```bash
python scripts/topology.py charts/test-tetrahedron/test-tetrahedron.md
```

**Expected Output:**
```
Chart: test-tetrahedron
Vertices (V): 4
Edges (E): 6
Faces (F): 3
Euler Characteristic (χ): 1

Topological Analysis:
- Expected χ for complete structure: 2
- Actual χ: 1
- Difference: -1
- Interpretation: 1 hole detected
```

**Question:** What happens to χ if you add the missing face?

### Exercise 2: Examine a Vertex

Open [00_vertices/alpha.md](../../00_vertices/alpha.md) and look at the frontmatter:

```yaml
---
type: vertex/test
extends: vertex
id: v:test:alpha
name: Test Vertex Alpha
description: First vertex of test tetrahedron
tags:
  - vertex
  - test
version: 1.0.0
created: 2025-12-27T14:30:00Z
modified: 2025-12-27T14:30:00Z
---
```

**Observations:**
- `type: vertex/test` - Even "generic" vertices have a type
- `extends: vertex` - Inheritance (we'll explore this in Stage 5)
- `id: v:test:alpha` - Unique identifier
- `tags` - Enables Obsidian queries
- Version and timestamps - Tracking

**Question:** What's the difference between `type` and `extends`?

### Exercise 3: Examine an Edge

Open [01_edges/alpha-beta.md](../../01_edges/alpha-beta.md):

```yaml
---
type: edge/test
extends: edge
id: e:test:alpha:beta
name: Test Edge Alpha-Beta
source: v:test:alpha
target: v:test:beta
source_type: vertex/test
target_type: vertex/test
orientation: undirected
---
```

**Key Fields:**
- `source` and `target` - The boundary vertices
- `source_type` and `target_type` - Type constraints (both must be vertex/test)
- `orientation: undirected` - No direction (beta→alpha is the same as alpha→beta)

**Question:** What would change if this edge was directed?

### Exercise 4: Examine a Face

Open [02_faces/alpha-beta-gamma.md](../../02_faces/alpha-beta-gamma.md):

```yaml
---
type: face/test
extends: face
id: f:test:alpha:beta:gamma
vertices: [v:test:alpha, v:test:beta, v:test:gamma]
edges: [e:test:alpha:beta, e:test:beta:gamma, e:test:alpha:gamma]
orientation: oriented
---
```

**Key Constraint:**
The vertices listed in `vertices` must be **exactly** the boundary of the edges listed in `edges`.

**Verification:**
- Edge alpha-beta has boundary {alpha, beta}
- Edge beta-gamma has boundary {beta, gamma}
- Edge alpha-gamma has boundary {alpha, gamma}
- Union: {alpha, beta, gamma} ✓ Matches `vertices`!

**Question:** What would happen if `edges` listed alpha-beta, beta-gamma, gamma-**delta**?

### Exercise 5: Add the Missing Face (Optional)

Create the missing face to complete the tetrahedron:

1. Copy [02_faces/alpha-beta-gamma.md](../../02_faces/alpha-beta-gamma.md) to `02_faces/beta-gamma-delta.md`
2. Update the frontmatter:
   - `id: f:test:beta:gamma:delta`
   - `vertices: [v:test:beta, v:test:gamma, v:test:delta]`
   - `edges: [e:test:beta:gamma, e:test:gamma:delta, e:test:beta:delta]`
3. Update [test-tetrahedron.md](test-tetrahedron.md) to include the new face
4. Run `python scripts/topology.py charts/test-tetrahedron/test-tetrahedron.md`

**Expected Result:** χ should change from 1 to 2 (no holes!)

**Restore:**
```bash
git restore 02_faces/beta-gamma-delta.md charts/test-tetrahedron/test-tetrahedron.md
```

---

## Common Questions

**Q: Why use a tetrahedron instead of a simpler example like a triangle?**

A: A single triangle (3 vertices, 3 edges, 1 face) has χ = 1, which is its natural state. To demonstrate a hole, we need a structure where something is **missing**. A tetrahedron with a missing face clearly shows the difference between "edges present" and "face present."

**Q: What's the difference between a graph and a simplicial complex?**

A: A graph has vertices and edges. A simplicial complex adds **faces** (and higher-dimensional cells). Faces capture ternary (3-way) and higher relationships that can't be represented by binary edges alone.

**Q: Are topological holes always bad?**

A: No! Holes can be:
- **Intentional:** Representing real gaps (unfilled positions, pending approvals)
- **Temporary:** Work in progress (documentation not yet complete)
- **Informative:** Highlighting what needs attention

The key is **detecting** holes so you can decide if they're intentional or problems.

**Q: Why is χ negative for some charts but positive here?**

A: The Euler characteristic depends on the topology:
- **Contractible spaces** (can shrink to a point): χ = 1
- **Spheres:** χ = 2
- **Tori (donuts):** χ = 0
- **Multiple holes:** χ decreases by 1 per hole
- **Complex structures:** Can have negative χ

Our tetrahedron-with-hole has χ = 1 (nearly contractible). The boundary-complex in Stage 3 has χ = -4 (much richer structure).

---

## Verification Commands

```bash
# Verify chart structure (run from repository root)
python scripts/verify_chart.py charts/test-tetrahedron/test-tetrahedron.md --root .

# Analyze topology
python scripts/topology.py charts/test-tetrahedron/test-tetrahedron.md

# Build cache and check overall structure
python scripts/build_cache.py
```

**Expected:** All verifications pass, topology reports χ = 1 with 1 hole.

---

## What's Next?

**You've learned:** Pure topological structure (vertices, edges, faces, holes, Euler characteristic)

**Next stage:** [Stage 2 - Typed Simplicial Complexes](../../docs/teaching-guides/02-typed-topology.md)

In Stage 2, you'll learn:
- How to add **semantic types** to vertices/edges/faces
- How **type inheritance** works (staff extends individual extends actor)
- How **typed edge boundaries** enforce constraints
- How organizational gaps appear as topological holes

**Preview:** Instead of generic alpha/beta/gamma vertices, you'll see Alice/Bob/Carol (staff), Frontend/Backend (teams), and Lead/Developer (roles). The topology will gain meaning!

---

## Additional Resources

- **File locations:**
  - Vertices: `00_vertices/{alpha,beta,gamma,delta}.md`
  - Edges: `01_edges/{alpha-beta,...}.md`
  - Faces: `02_faces/{alpha-beta-gamma,...}.md`
  - Chart: `charts/test-tetrahedron/test-tetrahedron.md`

- **Key scripts:**
  - `scripts/verify_chart.py` - Structural verification
  - `scripts/topology.py` - Euler characteristic and hole detection
  - `scripts/build_cache.py` - Parse all elements into complex.json

- **Concepts to review:**
  - Simplicial complex (Wikipedia: "Simplicial complex")
  - Euler characteristic (Wikipedia: "Euler characteristic")
  - Graph theory basics (if needed for understanding edges)

---

**Note:** This is a **teaching chart**, not a production example. The deliberately simple structure and intentional hole are pedagogical choices to help you understand fundamental concepts before moving to real-world applications.
