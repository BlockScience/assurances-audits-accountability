# Hodge Decomposition and Edge PageRank

This document provides a desk reference for understanding and interpreting Hodge decomposition and edge PageRank analysis on simplicial complexes.

## Overview

When a simplicial complex becomes too large or intricate for visual inspection, algebraic topology provides rigorous analysis tools. Hodge decomposition and edge PageRank reveal structural properties that visualization cannot:

- **Which edges are structurally critical?**
- **Where do information flows converge?**
- **What topological features exist in the complex?**

## The Edge Laplacian

The edge Laplacian L₁ captures how edges relate to both vertices (below) and faces (above):

```
L₁ = ∂₁ D₀⁻¹ ∂₁* + D₁⁻¹ ∂₂* ∂₂
     └─────────┘   └─────────┘
     down-Laplacian  up-Laplacian
```

Where:
- **∂₁**: Boundary operator from edges to vertices (source/target)
- **∂₂**: Boundary operator from faces to edges (boundary edges)
- **D₀**: Diagonal matrix of vertex degrees
- **D₁**: Diagonal matrix of edge degrees (incident faces)

The down-Laplacian measures how edges connect through shared vertices. The up-Laplacian measures how edges connect through shared faces.

## Edge PageRank

For each edge e, we compute a personalized PageRank vector:

```
PR(e) = (βI + L₁)⁻¹ χₑ
```

Where:
- **β**: Jumping parameter (default 0.1), controls locality vs global spread
- **χₑ**: Indicator vector for edge e (1 at position e, 0 elsewhere)

The PageRank vector PR(e) measures how influence from edge e spreads through the complex. Edges with high PageRank values are "close" to e in the Laplacian sense.

### Interpreting β

| β value | Behavior |
|---------|----------|
| Small (0.01) | Influence spreads far, global patterns dominate |
| Medium (0.1) | Balance between local and global (recommended) |
| Large (1.0) | Influence stays local, neighborhood effects dominate |

## Hodge Decomposition

Every edge vector (including PageRank vectors) decomposes into three orthogonal components:

```
v = gradient + circular + harmonic
```

### Gradient Component

**What it is:** Flow that comes from vertices. The gradient of a potential function on vertices.

**Mathematical form:** Projection onto image of ∂₁*

**Interpretation in charts:**
- Edges with high gradient flow act as **structural bridges**
- They connect regions of the complex through vertex pathways
- Removing them would disconnect vertex-level structure

**Example edges:** `transitions-to` edges connecting student states, `requires-skill` edges linking modules to prerequisites

### Circular Component

**What it is:** Flow around faces. Curl or rotational flow.

**Mathematical form:** Projection onto image of ∂₂

**Interpretation in charts:**
- Edges with high circular flow mark **confluence zones**
- Multiple faces share these edges as boundaries
- Information from different faces converges here

**Example edges:** In learning journeys, typically zero because the structure is acyclic (no circular dependencies)

### Harmonic Component

**What it is:** Flow that is both divergence-free and curl-free. Represents topological features.

**Mathematical form:** Kernel of L₁ (null space of edge Laplacian)

**Interpretation in charts:**
- Edges with high harmonic flow mark **topological cycles**
- They represent "holes" in the simplicial complex
- Harmonic forms correspond to homology classes

**Example edges:** `studies` and `has-skill` edges in learning journeys carry harmonic flow because they participate in the triangular face structure

## Influence Measures

For each edge's PageRank vector, we compute four influence measures:

| Measure | Formula | Interpretation |
|---------|---------|----------------|
| **Penetration** | ‖v‖₂ | Overall influence strength. High values = important edge. |
| **Absolute Influence** | ‖v‖₁ | Total magnitude. Measures raw influence capacity. |
| **Spread** | ‖v‖₂ / ‖v‖₁ | Concentration vs diffusion. High = focused influence. |
| **Relative Influence** | Σv | Signed sum. Positive = net excitation, negative = net inhibition. |

### Which Measure to Use

- **Finding critical edges:** Use penetration (L2 norm)
- **Finding high-capacity edges:** Use absolute influence (L1 norm)
- **Finding focused vs diffuse edges:** Use spread ratio
- **Finding excitatory vs inhibitory edges:** Use relative influence

## Reading the Analysis Output

Example output:

```
Hodge Decomposition (global):
  Gradient:  18.2%
  Circular:  0.0%
  Harmonic:  81.8%
```

**Interpretation:**
- 18.2% of edge flow comes from vertex potentials (structural bridging)
- 0.0% circular flow (no cyclic dependencies - expected for DAG-like structures)
- 81.8% harmonic flow (rich topological structure with many faces)

### Top Edges by Component

**Gradient (Structural Bridges):**
```
1. e:develops-skill:composing-typed-simplicial-complexes:...   2.601781
```
This edge is critical for connecting the skill development structure.

**Circular (Confluence Zones):**
```
1. e:has-skill:knowledge-complex-learner:sets-and-graphs   0.000000
```
Zero circular flow throughout indicates acyclic structure.

**Harmonic (Topological Cycles):**
```
1. e:studies:management-architect:organizational-topology   8.418259
```
This edge participates in the face structure defining the learning path.

## Practical Applications

### 1. Identifying Critical Dependencies

Edges with high gradient flow are structural bridges. Removing or modifying them affects vertex-level connectivity:

```bash
python scripts/hodge_analysis.py chart.json --top 5
# Look at "Top Edges by Gradient Flow"
```

### 2. Finding Topological Features

High harmonic flow indicates edges participating in topological cycles (homology):

```bash
# Compare harmonic percentages across charts
# Higher harmonic % = richer topological structure
```

### 3. Validating Acyclic Structure

Circular component should be zero for DAG-like structures (learning paths, dependency graphs):

```bash
# If Circular > 0%, investigate for unintended cycles
```

### 4. Comparing Chart Complexity

| Chart Type | Expected Pattern |
|------------|------------------|
| Linear chain | High gradient, low harmonic |
| Rich face structure | High harmonic, moderate gradient |
| Cyclic dependencies | Non-zero circular |
| Tree structure | Pure gradient, zero harmonic |

## Tool Usage

### Basic Analysis

```bash
python scripts/hodge_analysis.py charts/<chart>/<chart>.json
```

### With Options

```bash
python scripts/hodge_analysis.py chart.json --top 15 --beta 0.1 --quiet
```

| Option | Default | Purpose |
|--------|---------|---------|
| `--top N` | 10 | Number of top edges to display per category |
| `--beta X` | 0.1 | PageRank jumping parameter |
| `--quiet` | false | Suppress solver warnings |

### Prerequisite: Export to JSON

The analyzer requires JSON format. Export from markdown first:

```bash
python scripts/export_chart_direct.py chart.md chart.json --root .
python scripts/hodge_analysis.py chart.json
```

## Mathematical Background

### Boundary Operators

The boundary operators form a chain complex:

```
        ∂₂         ∂₁
Faces ────→ Edges ────→ Vertices
```

Key property: ∂₁ ∘ ∂₂ = 0 (boundary of a boundary is empty)

### Hodge Theorem

For the edge Laplacian L₁, the Hodge theorem guarantees:

```
Edge space = im(∂₁*) ⊕ im(∂₂) ⊕ ker(L₁)
              gradient  circular  harmonic
```

These three subspaces are orthogonal and span the entire edge space.

### Connection to Homology

The harmonic subspace ker(L₁) is isomorphic to the first homology group H₁. Each independent harmonic form represents a "hole" in the complex - a cycle that cannot be filled by faces.

## Common Patterns

### Learning Journey Charts

- **High harmonic (70-90%)**: Rich face structure from prerequisite/completion/skill-gain triangles
- **Moderate gradient (10-30%)**: Structural edges like `transitions-to` and `requires-skill`
- **Zero circular**: Acyclic progression (students don't loop back)

### Assurance Charts

- **Balanced gradient/harmonic**: Mix of structural verification edges and assurance face structure
- **Zero circular**: No circular dependencies in assurance chain

### Organizational Charts

- **Variable**: Depends on whether structure is hierarchical (high gradient) or networked (high harmonic)
- **Possible circular**: Matrix organizations may have circular reporting

---

## See Also

- [Module 10: Organizational Topology](../learning/module-10.md) - Practical application of Hodge analysis
- [Charts vs Documents](charts-vs-documents.md) - Understanding chart structure
- [scripts/hodge_analysis.py](../../scripts/hodge_analysis.py) - Implementation source
