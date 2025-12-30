# Module 03 - Composing Typed Simplicial Complexes: Building from Parts

Welcome to Module 3! You've learned about simplicial complexes (Module 1) and semantic types (Module 2). Now you'll discover how to **compose** charts—combining multiple simplicial complexes into larger structures through **identification** (also called pasting).

In this module, you'll combine the Module 1 and Module 2 syllabus charts you've already studied, creating a unified chart that represents your complete learning journey. This hands-on approach makes composition concrete: you'll work with charts you already understand.

## What You'll Learn

By the end of this module, you'll be able to:

- Identify shared vertices, edges, and faces across multiple typed simplicial complexes
- Perform set union operations while avoiding duplication of shared elements
- Verify type consistency across composition boundaries
- Calculate the Euler characteristic for composed structures
- Explain the semantics of identification and why pasting preserves topological meaning
- Create composite charts from modular components

## Prerequisites

This module assumes you've completed Modules 1 and 2 and possess:

- Understanding of vertices, edges, faces, and the Euler characteristic
- Ability to read chart documents and calculate χ
- Understanding of semantic types and type constraints
- Familiarity with the Module 1 and Module 2 syllabus charts

## Section 1: Why Compose Charts?

### The Modularity Challenge

You've now studied two separate learning modules, each with its own syllabus chart:

- **Module 1 chart**: knowledge-complex-newcomer → foundational-learner (1 skill gained)
- **Module 2 chart**: foundational-learner → intermediate-learner (1 skill gained)

But these charts aren't truly separate—they're connected! Module 2 **starts where Module 1 ends**. The `foundational-learner` vertex appears in BOTH charts:

- In Module 1: It's the **exit state** (student after completing Module 1)
- In Module 2: It's the **entry state** (student before starting Module 2)

This is the same student state, not two different states. When we treat them as separate, we lose information about the continuous learning journey.

**Question:** What if we want to represent the complete journey from newcomer → foundational → intermediate in a single chart?

**Answer:** We need to **compose** the two charts by **identifying** the shared vertex.

### What Is Identification?

**Identification** (or **pasting**) is the operation of declaring that certain elements in separate complexes are actually the same element. When we identify elements:

1. **Shared elements appear once** in the composed structure (not duplicated)
2. **Connections are preserved** (edges and faces remain intact)
3. **Types must match** (you can't identify elements of different types)

**Intuition:** Think of two puzzle pieces that share an edge. When you connect them, the shared edge doesn't duplicate—it becomes a single edge connecting both pieces.

### Exercise 1: Conceptual Warmup

Before working with actual charts, consider this simple example:

**Chart A:**
- Vertices: {a, b, c}
- Edges: {(a→b), (b→c)}
- Faces: none

**Chart B:**
- Vertices: {c, d, e}
- Edges: {(c→d), (d→e)}
- Faces: none

**Question 1:** If we identify vertex `c` (it appears in both charts), how many vertices are in the composed chart?

**Question 2:** What about edges?

**Answers:**

1. **Vertices:** Chart A has 3, Chart B has 3, but `c` is shared. Total: 3 + 3 - 1 = **5 vertices** {a, b, c, d, e}
2. **Edges:** Chart A has 2, Chart B has 2, no edges are shared. Total: 2 + 2 = **4 edges**

**Key Insight:** Union with identification means counting each shared element **exactly once**.

## Section 2: Identifying Shared Elements

Now let's identify the shared elements between the Module 1 and Module 2 syllabus charts.

### Step 1: Load the Charts

```bash
# Module 1 chart
cat charts/learning-journey-module-01/learning-journey-module-01.md

# Module 2 chart
cat charts/learning-journey-module-02/learning-journey-module-02.md
```

### Step 2: List the Elements

**Module 1 elements:**

Vertices (5):
- `v:student:knowledge-complex-learner`
- `v:skill:sets-and-graphs`
- `v:skill:simplicial-complex-fundamentals`
- `v:learning-module:simplicial-complex-fundamentals`
- `v:student:foundational-learner`

Edges (7):
- `e:has-skill:knowledge-complex-learner:sets-and-graphs`
- `e:requires-skill:simplicial-complex-fundamentals:sets-and-graphs`
- `e:develops-skill:simplicial-complex-fundamentals:simplicial-complex-fundamentals`
- `e:studies:knowledge-complex-learner:simplicial-complex-fundamentals`
- `e:transitions-to:knowledge-complex-learner:foundational-learner`
- `e:advances:simplicial-complex-fundamentals:foundational-learner`
- `e:has-skill:foundational-learner:simplicial-complex-fundamentals`

Faces (3):
- `f:prerequisite:knowledge-complex-learner:sets-and-graphs:simplicial-complex-fundamentals`
- `f:completion:knowledge-complex-learner:simplicial-complex-fundamentals:foundational-learner`
- `f:skill-gain:foundational-learner:simplicial-complex-fundamentals:simplicial-complex-fundamentals`

**Module 2 elements:**

Vertices (5):
- `v:student:foundational-learner`
- `v:skill:simplicial-complex-fundamentals`
- `v:skill:typed-simplicial-complexes`
- `v:learning-module:typed-simplicial-complexes`
- `v:student:intermediate-learner`

Edges (7):
- `e:has-skill:foundational-learner:simplicial-complex-fundamentals`
- `e:requires-skill:typed-simplicial-complexes:simplicial-complex-fundamentals`
- `e:develops-skill:typed-simplicial-complexes:typed-simplicial-complexes`
- `e:studies:foundational-learner:typed-simplicial-complexes`
- `e:transitions-to:foundational-learner:intermediate-learner`
- `e:advances:typed-simplicial-complexes:intermediate-learner`
- `e:has-skill:intermediate-learner:typed-simplicial-complexes`

Faces (3):
- `f:prerequisite:foundational-learner:simplicial-complex-fundamentals:typed-simplicial-complexes`
- `f:completion:foundational-learner:typed-simplicial-complexes:intermediate-learner`
- `f:skill-gain:intermediate-learner:typed-simplicial-complexes:typed-simplicial-complexes`

### Step 3: Identify Shared Elements (Find the Intersection)

Compare the element lists. Which elements appear in **both** charts? This is the **intersection** operation.

**Shared Vertices (V_module1 ∩ V_module2):**
- `v:student:foundational-learner` ✓ (exit of Module 1, entry of Module 2)
- `v:skill:simplicial-complex-fundamentals` ✓ (developed in Module 1, required by Module 2)

Count: |V_module1 ∩ V_module2| = 2 shared vertices

**Shared Edges (E_module1 ∩ E_module2):**
- `e:has-skill:foundational-learner:simplicial-complex-fundamentals` ✓ (shows foundational-learner possesses the skill)

Count: |E_module1 ∩ E_module2| = 1 shared edge

**Shared Faces (F_module1 ∩ F_module2):**
- None (prerequisite and completion faces are module-specific)

Count: |F_module1 ∩ F_module2| = 0 shared faces

**Critical Insight:** These intersection elements are the **pasting points**—the elements we'll identify as "the same" when we combine the charts. Finding the intersection FIRST is essential before we can correctly construct the union.

### Exercise 2: Verify Shared Elements

**Task:** Manually verify each shared element by checking both chart documents.

1. Open `charts/learning-journey-module-01/learning-journey-module-01.md`
2. Search for `foundational-learner` — where does it appear?
3. Open `charts/learning-journey-module-02/learning-journey-module-02.md`
4. Search for `foundational-learner` — where does it appear?
5. Repeat for `simplicial-complex-fundamentals`

**Reflection Questions:**

1. Why is `foundational-learner` shared but `knowledge-complex-newcomer` is not?
2. Why is `simplicial-complex-fundamentals` shared but `typed-simplicial-complexes` is not?
3. Why is the `has-skill` edge shared but the `studies` edges are not?

**Answers:**

1. `foundational-learner` is the transition point between modules; `knowledge-complex-newcomer` only appears in Module 1
2. `simplicial-complex-fundamentals` is developed in Module 1 and required by Module 2; `typed-simplicial-complexes` is only in Module 2
3. The `has-skill` edge connects two shared vertices with the same relationship; `studies` edges connect to different modules

**Key Takeaway:** Elements are shared when they have **identical IDs** across charts and represent the **same semantic entity**.

## Section 3: Set Union and Deduplication

Now we'll combine the element lists using **set union**, counting shared elements exactly once. This is the heart of **identification** (pasting): we find the **intersection** first (elements to identify/paste on), then construct the **union** without duplicates.

### The Intersection-Union Process

The composition process has two critical steps for each element type:

1. **Find the intersection** (A ∩ B): Identify which elements appear in BOTH charts with identical IDs
2. **Construct the union** (A ∪ B): Combine all elements, counting intersection elements exactly once

**Key Insight:** The elements in the **intersection** are the ones we're **identifying** or **pasting on**. These are the "glue points" where the two charts connect.

**Formula:** |A ∪ B| = |A| + |B| - |A ∩ B|

The subtraction prevents double-counting the identified elements.

### Vertex Union

**Step 1: Find intersection (V_module1 ∩ V_module2)**

Compare the vertex lists element by element:

- Module 1 has: knowledge-complex-learner, sets-and-graphs, simplicial-complex-fundamentals, simplicial-complex-fundamentals-module, foundational-learner
- Module 2 has: foundational-learner, simplicial-complex-fundamentals, typed-simplicial-complexes, typed-simplicial-complexes-module, intermediate-learner

**Intersection (shared vertices):**
```
V_module1 ∩ V_module2 = {foundational-learner, simplicial-complex-fundamentals}
```

These 2 vertices are the **identification points** (pasting points).

**Step 2: Construct union (V_module1 ∪ V_module2)**

Combine all vertices, counting intersection elements once:

```
V_combined = V_module1 ∪ V_module2
           = {knowledge-complex-learner, sets-and-graphs, simplicial-complex-fundamentals,
              simplicial-complex-fundamentals-module, foundational-learner,
              typed-simplicial-complexes, typed-simplicial-complexes-module, intermediate-learner}
```

**Count:**
- |V_module1| = 5
- |V_module2| = 5
- |V_module1 ∩ V_module2| = 2 (identified elements)
- |V_combined| = 5 + 5 - 2 = **8 vertices**

**Verification:** Count the deduplicated set above: 8 vertices ✓

### Edge Union

**Step 1: Find intersection (E_module1 ∩ E_module2)**

Compare edge IDs element by element:

**Intersection (shared edges):**
```
E_module1 ∩ E_module2 = {e:has-skill:foundational-learner:simplicial-complex-fundamentals}
```

Only 1 edge is shared—this edge connects two shared vertices (both endpoints are in the vertex intersection).

**Step 2: Construct union (E_module1 ∪ E_module2)**

```
E_combined = E_module1 ∪ E_module2
```

**Count:**
- |E_module1| = 7
- |E_module2| = 7
- |E_module1 ∩ E_module2| = 1 (identified edge)
- |E_combined| = 7 + 7 - 1 = **13 edges**

### Face Union

**Step 1: Find intersection (F_module1 ∩ F_module2)**

Compare face IDs element by element:

**Intersection (shared faces):**
```
F_module1 ∩ F_module2 = ∅ (empty set)
```

No faces are shared! Prerequisite and completion faces are module-specific.

**Step 2: Construct union (F_module1 ∪ F_module2)**

```
F_combined = F_module1 ∪ F_module2
```

**Count:**
- |F_module1| = 3
- |F_module2| = 3
- |F_module1 ∩ F_module2| = 0 (no identified faces)
- |F_combined| = 3 + 3 - 0 = **6 faces**

### Interactive Exercise: Explore the Data

The composition has been computed using our automated tool. You can examine the actual data:

**JSON files:**
```bash
# View Module 1 chart data
cat charts/learning-journey-module-01/learning-journey-module-01.json

# View Module 2 chart data
cat charts/learning-journey-module-02/learning-journey-module-02.json

# View composed chart data (generated by compose_charts.py)
cat charts/composition-demo/module-composition-computed.json
```

The composed chart JSON contains a `composition` section showing exactly which elements were identified:

```json
"composition": {
  "method": "identification",
  "shared_vertices": ["v:skill:simplicial-complex-fundamentals", "v:student:foundational-learner"],
  "shared_edges": ["e:has-skill:foundational-learner:simplicial-complex-fundamentals"],
  "shared_faces": []
}
```

**3D Visualizations:**

Open these HTML files in your browser to see the structures:

1. `learning-journey-module-01.html` — Module 1 (standalone)
2. `learning-journey-module-02.html` — Module 2 (standalone)
3. `module-composition-computed.html` — Combined chart (composition result)

**Exercise:** In the visualizations, can you spot the shared vertices? Look for `foundational-learner` and `simplicial-complex-fundamentals`—they appear in all three visualizations but are counted only once in the composed chart.

### Using the Automated Composition Tool

The composition you're studying was generated using `compose_charts.py`, an automated tool that implements the formal intersection-union process.

**How it works:**

1. **Loads both source charts** (JSON format)
2. **Finds intersections** for vertices, edges, and faces by comparing IDs
3. **Constructs unions** counting shared elements exactly once
4. **Verifies type consistency** for all shared elements
5. **Outputs composed chart** with full metadata and visualization-ready format

**Try it yourself:**

```bash
# Compose Module 1 + Module 2
python scripts/compose_charts.py \
  charts/learning-journey-module-01/learning-journey-module-01.json \
  charts/learning-journey-module-02/learning-journey-module-02.json \
  charts/composition-demo/my-composition.json

# The script will output:
# - Shared vertices count
# - Shared edges count
# - Shared faces count
# - Combined topology (V, E, F, χ)
```

**What you'll see:**

```
Loading charts...
Chart 1: Learning Journey - Module 01
  V=5, E=7, F=3
Chart 2: Learning Journey - Module 02
  V=5, E=7, F=3

Identifying shared elements...
  Shared vertices: 2
    - v:skill:simplicial-complex-fundamentals
    - v:student:foundational-learner
  Shared edges: 1
    - e:has-skill:foundational-learner:simplicial-complex-fundamentals
  Shared faces: 0

Performing set union...
  Composed: V=8, E=13, F=6, χ=1
```

This demonstrates the **intersection-first, then union** process in action!

**Challenge:** Can you read the `compose_charts.py` source code and identify where it computes the intersections? Look for the `find_shared_elements()` function.

### Exercise 3: Calculate Combined Topology

Now calculate the Euler characteristic for the combined chart:

```
V = 8 vertices
E = 13 edges
F = 6 faces

χ = V - E + F = ?
```

**Answer:** χ = 8 - 13 + 6 = **1**

**Compare to individual charts:**

- Module 1: χ = 5 - 7 + 3 = 1
- Module 2: χ = 5 - 7 + 3 = 1
- Combined: χ = 8 - 13 + 6 = 1

**Why does χ stay the same?** All three charts (Module 1, Module 2, and their composition) have χ = 1, indicating they are all topologically complete, sphere-like structures. The composition preserves the topological completeness because the pasting is done along a shared vertex (foundational-learner) and shared skill, maintaining the overall connectivity pattern.

## Section 4: Type Consistency Validation

Before declaring composition valid, we must verify that **shared elements have identical types** across both charts.

### Rule: Type Consistency Across Boundaries

**For every shared element, the type annotations must match exactly.**

If chart A says vertex `x` has type `student` and chart B says vertex `x` has type `skill`, the composition is **invalid** (type conflict).

### Verify Shared Vertex Types

**Vertex 1: `v:student:foundational-learner`**

Module 1:
```yaml
# Referenced in edges/faces but not explicitly typed in Module 1 chart
# Type inferred from ID prefix: v:student:*
Type: student ✓
```

Module 2:
```yaml
vertices:
  - v:student:foundational-learner
Type: student ✓
```

**Type check:** student = student ✓ **Valid**

**Vertex 2: `v:skill:simplicial-complex-fundamentals`**

Module 1:
```yaml
vertices:
  - v:skill:simplicial-complex-fundamentals
Type: skill ✓
```

Module 2:
```yaml
vertices:
  - v:skill:simplicial-complex-fundamentals
Type: skill ✓
```

**Type check:** skill = skill ✓ **Valid**

### Verify Shared Edge Types

**Edge: `e:has-skill:foundational-learner:simplicial-complex-fundamentals`**

Module 1:
```yaml
edges:
  - e:has-skill:foundational-learner:simplicial-complex-fundamentals
Source: v:student:foundational-learner (type: student)
Target: v:skill:simplicial-complex-fundamentals (type: skill)
Edge type: has-skill ✓
```

Module 2:
```yaml
edges:
  - e:has-skill:foundational-learner:simplicial-complex-fundamentals
Source: v:student:foundational-learner (type: student)
Target: v:skill:simplicial-complex-fundamentals (type: skill)
Edge type: has-skill ✓
```

**Type check:**
- Edge type: has-skill = has-skill ✓
- Source type: student = student ✓
- Target type: skill = skill ✓

**Valid**

### Exercise 4: Type Violation Detection

Consider this hypothetical scenario:

**Chart A:**
```yaml
vertices:
  - v:student:alice
edges:
  - e:has-skill:alice:python
    source: v:student:alice
    target: v:skill:python
```

**Chart B:**
```yaml
vertices:
  - v:skill:alice  # WRONG TYPE!
edges:
  - e:teaches:bob:alice
    source: v:teacher:bob
    target: v:skill:alice
```

**Question:** Can we identify the `alice` vertices and compose these charts?

**Answer:** **No!** Type conflict:
- Chart A says `alice` is type `student`
- Chart B says `alice` is type `skill`

The same ID cannot have two different types. This composition is invalid.

**Key Principle:** Type consistency is non-negotiable. If types don't match, you cannot identify the elements.

## Section 5: Topological Recalculation

After composition, we must verify that **boundary relationships** remain intact.

### Boundary Preservation Principle

**Every face must have all its boundary edges present in the composed edge set.**

Let's verify this for the combined Module 1+2 chart.

### Check Module 1 Faces

**Face 1:** `f:prerequisite:knowledge-complex-learner:sets-and-graphs:simplicial-complex-fundamentals`

Boundary edges required:
1. `e:has-skill:knowledge-complex-learner:sets-and-graphs` ✓ (in Module 1)
2. `e:requires-skill:simplicial-complex-fundamentals:sets-and-graphs` ✓ (in Module 1)
3. `e:studies:knowledge-complex-learner:simplicial-complex-fundamentals` ✓ (in Module 1)

**All present in combined chart? Yes** ✓

**Face 2:** `f:completion:knowledge-complex-learner:simplicial-complex-fundamentals:foundational-learner`

Boundary edges required:
1. `e:studies:knowledge-complex-learner:simplicial-complex-fundamentals` ✓
2. `e:transitions-to:knowledge-complex-learner:foundational-learner` ✓
3. `e:advances:simplicial-complex-fundamentals:foundational-learner` ✓

**All present in combined chart? Yes** ✓

**Face 3:** `f:skill-gain:foundational-learner:simplicial-complex-fundamentals:simplicial-complex-fundamentals`

Boundary edges required:
1. `e:has-skill:foundational-learner:simplicial-complex-fundamentals` ✓ (SHARED EDGE - also in Module 2)
2. `e:develops-skill:simplicial-complex-fundamentals:simplicial-complex-fundamentals` ✓
3. `e:advances:simplicial-complex-fundamentals:foundational-learner` ✓

**All present in combined chart? Yes** ✓

### Check Module 2 Faces

**Face 4:** `f:prerequisite:foundational-learner:simplicial-complex-fundamentals:typed-simplicial-complexes`

Boundary edges required:
1. `e:has-skill:foundational-learner:simplicial-complex-fundamentals` ✓ (SHARED EDGE - also in Module 1)
2. `e:requires-skill:typed-simplicial-complexes:simplicial-complex-fundamentals` ✓
3. `e:studies:foundational-learner:typed-simplicial-complexes` ✓

**All present in combined chart? Yes** ✓

**Face 5:** `f:completion:foundational-learner:typed-simplicial-complexes:intermediate-learner`

Boundary edges required:
1. `e:studies:foundational-learner:typed-simplicial-complexes` ✓
2. `e:transitions-to:foundational-learner:intermediate-learner` ✓
3. `e:advances:typed-simplicial-complexes:intermediate-learner` ✓

**All present in combined chart? Yes** ✓

**Face 6:** `f:skill-gain:intermediate-learner:typed-simplicial-complexes:typed-simplicial-complexes`

Boundary edges required:
1. `e:has-skill:intermediate-learner:typed-simplicial-complexes` ✓
2. `e:develops-skill:typed-simplicial-complexes:typed-simplicial-complexes` ✓
3. `e:advances:typed-simplicial-complexes:intermediate-learner` ✓

**All present in combined chart? Yes** ✓

### Summary of Boundary Verification

All **6 faces** in the composed chart have complete boundaries:
- **Module 1:** 3 faces (prerequisite, completion, skill-gain)
- **Module 2:** 3 faces (prerequisite, completion, skill-gain)
- **Total:** 6 faces, all boundaries intact ✓

### Exercise 5: Broken Boundaries

**Hypothetical scenario:** What if we forgot to include an edge in the composition?

Suppose we accidentally omitted `e:has-skill:foundational-learner:simplicial-complex-fundamentals` from the combined chart.

**Question:** Which faces would break?

**Answer:**
- Module 1's completion face would break (needs this edge as a boundary)
- Module 2's prerequisite face would break (needs this edge as a boundary)

**Result:** Two faces would have incomplete boundaries → **topologically invalid**

**Key Insight:** You can't cherry-pick elements during composition. If you include a face, you MUST include ALL its boundary edges.

## Section 6: Understanding Identification Semantics

Why does identification preserve meaning? Let's explore the semantics.

### The Shared Student State

In Module 1, `foundational-learner` represents:
- A student who has completed Module 1
- Possesses `simplicial-complex-fundamentals`
- Ready to study more advanced topics

In Module 2, `foundational-learner` represents:
- A student entering Module 2
- Possesses `simplicial-complex-fundamentals` (prerequisite)
- Will study typed complexes

**Are these the same student state?** **Yes!**

The exit condition of Module 1 is EXACTLY the entry condition of Module 2. They describe the same learning state. Identifying them is not just valid—it's **necessary** to represent the continuous journey.

### The Shared Skill

`simplicial-complex-fundamentals` in Module 1:
- Developed as the outcome of Module 1
- Possessed by `foundational-learner`

`simplicial-complex-fundamentals` in Module 2:
- Required as a prerequisite for Module 2
- Possessed by `foundational-learner`

**Are these the same skill?** **Yes!**

The skill developed in Module 1 IS the skill required by Module 2. Duplicating it would be semantically wrong.

### The Shared Edge

`e:has-skill:foundational-learner:simplicial-complex-fundamentals` appears in both charts because:

- Module 1 establishes this relationship (student acquires skill)
- Module 2 depends on this relationship (prerequisite validation)

This is the **same relationship**, not two separate relationships. Identifying it maintains semantic coherence.

### Exercise 6: Identification Decision Making

For each pair below, decide: Should these elements be identified (same element) or kept separate (different elements)?

**Pair 1:**
- Chart A: `v:person:alice` (type: person, age: 25)
- Chart B: `v:person:alice` (type: person, age: 30)

**Pair 2:**
- Chart A: `v:skill:python-basics` (level: beginner)
- Chart B: `v:skill:python-advanced` (level: advanced)

**Pair 3:**
- Chart A: `e:works-at:alice:company-X`
- Chart B: `e:works-at:alice:company-X`

**Answers:**

1. **Identify** (if Alice's age changed over time, this represents the same person at different times—depends on temporal model)
2. **Keep separate** (different skill levels = different skills)
3. **Identify** (same relationship, should not duplicate)

## Self-Assessment

Test your understanding:

**Conceptual Questions:**

1. What is the difference between "union" and "union with identification"?

2. Why must shared elements have matching types?

3. If Chart A has χ = 0 and Chart B has χ = 1, can you predict the χ of the composed chart? Why or why not?

4. What happens to boundary relationships during composition?

**Applied Skills:**

5. Given two charts with shared vertices {x, y} and no shared edges, calculate |V_combined|, |E_combined| if |V_A| = 5, |E_A| = 7, |V_B| = 4, |E_B| = 6.

6. Verify type consistency for a shared edge connecting two shared vertices across two charts.

7. Detect which faces would break if a specific boundary edge were omitted from a composition.

**Critical Thinking:**

8. Can you compose three charts simultaneously (A + B + C)? What challenges might arise?

9. If Chart A and Chart B share no elements (disjoint), is their composition meaningful? What would χ be?

10. Design a composition where identification creates a new topological hole that didn't exist in either source chart.

## Practice Problems

### Problem 1: Small Composition

**Chart A:**
- Vertices: {v:a, v:b, v:c}
- Edges: {(a→b), (b→c)}

**Chart B:**
- Vertices: {v:c, v:d}
- Edges: {(c→d)}

Identify shared elements, perform union, calculate V, E, χ (no faces).

### Problem 2: Type Validation

You're composing two organizational charts:

**Org Chart 1:**
```yaml
vertices:
  - v:person:bob (type: employee)
  - v:role:engineer (type: role)
edges:
  - e:has-role:bob:engineer
```

**Org Chart 2:**
```yaml
vertices:
  - v:person:bob (type: employee)
  - v:project:compiler (type: project)
edges:
  - e:works-on:bob:compiler
```

1. Which elements are shared?
2. Are types consistent?
3. What is the combined chart's structure?

### Problem 3: Boundary Preservation

**Chart A:**
- Vertices: {v:x, v:y, v:z}
- Edges: {(x→y), (y→z), (x→z)}
- Faces: {f:(x,y,z)}

**Chart B:**
- Vertices: {v:z, v:w}
- Edges: {(z→w)}
- Faces: none

Compose by identifying `v:z`. Does the face `f:(x,y,z)` remain valid?

## Next Steps

Congratulations! You now understand composition through identification.

### Immediate Practice

1. **Create the combined Module 1+2 chart:** Write the complete chart document with all deduplicated elements

2. **Visualize the composition:** Generate 3D visualizations of Module 1, Module 2, and the combined chart—compare their structures

3. **Explore Module 3's chart:** The Module 3 syllabus chart shows YOUR learning journey through composition

### Continuing Your Learning

Consider these advanced topics:

- **Module 4: Verification and Validation** — Learn to systematically verify composed structures
- **Categorical Composition:** Explore pushouts and colimits as general composition operations
- **Hierarchical Composition:** Build large charts from many small modular components

### Deeper Exploration

- **Identification in Topology:** Study how mathematicians use identification to construct new spaces
- **Modular System Design:** Apply composition principles to software architecture
- **Knowledge Graph Integration:** Use identification to merge knowledge from multiple sources

## Glossary

**Boundary Preservation:** Property that all edges forming a face's boundary remain present after composition

**Composition:** The operation of combining multiple simplicial complexes into a single structure

**Deduplication:** Counting shared elements exactly once during union operations

**Identification (Pasting):** Declaring that elements in separate complexes are actually the same element

**Set Union:** Combining element sets while preserving uniqueness (A ∪ B)

**Shared Element:** An element with identical ID appearing in multiple charts being composed

**Type Consistency:** Requirement that shared elements have matching type annotations across composition boundaries

---

**Module 3 Complete!** You've learned how to compose typed simplicial complexes through identification. This completes the foundational trilogy (structure + types + composition). You're now ready for advanced work in verification, validation, assurance, and modular chart design.
