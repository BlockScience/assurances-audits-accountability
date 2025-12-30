---
type: chart/syllabus
extends: chart
id: c:learning-journey-module-03
name: Learning Journey - Module 03
description: Third module in learning journey teaching composition of typed simplicial complexes through identification (pasting) operations

# Chart construction metadata
constructed_by: "Claude Sonnet 4.5"
construction_method: assisted
construction_date: 2025-12-28T00:00:00Z

# Chart purpose
purpose: Demonstrate skill accumulation for Module 3 (composition) building on Modules 1 and 2, teaching identification as the fundamental operation for combining charts
scope: One module (composing-typed-simplicial-complexes) with 2 prerequisite skills and 1 developed skill, showing student state transition from intermediate to compositional

# Learning path metadata
learning_path:
  entry_state: v:student:intermediate-learner
  exit_states:
    - v:student:compositional-learner

prerequisites:
  entry_skills:
    - v:skill:simplicial-complex-fundamentals
    - v:skill:typed-simplicial-complexes

outcomes:
  developed_skills:
    - v:skill:composing-typed-simplicial-complexes

# Elements comprising this chart
elements:
  vertices:
    - v:student:intermediate-learner
    - v:skill:simplicial-complex-fundamentals
    - v:skill:typed-simplicial-complexes
    - v:skill:composing-typed-simplicial-complexes
    - v:learning-module:composing-typed-simplicial-complexes
    - v:student:compositional-learner
  edges:
    - e:has-skill:intermediate-learner:simplicial-complex-fundamentals
    - e:has-skill:intermediate-learner:typed-simplicial-complexes
    - e:requires-skill:composing-typed-simplicial-complexes:simplicial-complex-fundamentals
    - e:requires-skill:composing-typed-simplicial-complexes:typed-simplicial-complexes
    - e:develops-skill:composing-typed-simplicial-complexes:composing-typed-simplicial-complexes
    - e:studies:intermediate-learner:composing-typed-simplicial-complexes
    - e:transitions-to:intermediate-learner:compositional-learner
    - e:advances:composing-typed-simplicial-complexes:compositional-learner
    - e:has-skill:compositional-learner:composing-typed-simplicial-complexes
  faces:
    - f:prerequisite:intermediate-learner:simplicial-complex-fundamentals:composing-typed-simplicial-complexes
    - f:prerequisite:intermediate-learner:typed-simplicial-complexes:composing-typed-simplicial-complexes
    - f:completion:intermediate-learner:composing-typed-simplicial-complexes:compositional-learner
    - f:skill-gain:compositional-learner:composing-typed-simplicial-complexes:composing-typed-simplicial-complexes

tags:
  - chart
  - syllabus
  - learning-journey
  - module-03
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Learning Journey - Module 03

Third module in the learning journey completing the foundational trilogy with composition and identification.

## Purpose

This chart validates the learning journey framework for Module 3 by demonstrating:
1. **Dual prerequisite validation** via two prerequisite faces (student must have both foundational and typing skills)
2. **Skill accumulation to 3 skills** via completion face (supermodular growth from 2 to 3 skills)
3. **State transitions** via student vertices representing discrete learning states
4. **Compositional skill development** through identification/pasting operations
5. **Completion of foundational trilogy** enabling advanced work in verification, validation, and assurance

## Structure

### Vertices (6)

**Students (2 learning states):**
- [intermediate-learner](../../00_vertices/student-intermediate-learner.md) - Entry state with 2 skills (foundational + typing)
- [compositional-learner](../../00_vertices/student-compositional-learner.md) - State after completing Module 3 with 3 skills

**Skills (3):**
- [simplicial-complex-fundamentals](../../00_vertices/skill-simplicial-complex-fundamentals.md) - Entry prerequisite from Module 1
- [typed-simplicial-complexes](../../00_vertices/skill-typed-simplicial-complexes.md) - Entry prerequisite from Module 2
- [composing-typed-simplicial-complexes](../../00_vertices/skill-composing-typed-simplicial-complexes.md) - Developed by Module 3

**Module (1):**
- [composing-typed-simplicial-complexes](../../00_vertices/learning-module-composing-typed-simplicial-complexes.md) - Module teaching identification and pasting

### Edges (11)

**has-skill edges (5):**
- intermediate-learner → simplicial-complex-fundamentals (entry skill 1)
- intermediate-learner → typed-simplicial-complexes (entry skill 2)
- compositional-learner → simplicial-complex-fundamentals (carried over)
- compositional-learner → typed-simplicial-complexes (carried over)
- compositional-learner → composing-typed-simplicial-complexes (newly acquired)

**requires-skill edges (2):**
- composing-typed-simplicial-complexes → simplicial-complex-fundamentals
- composing-typed-simplicial-complexes → typed-simplicial-complexes

**develops-skill edge (1):**
- composing-typed-simplicial-complexes → composing-typed-simplicial-complexes

**Learning edges (3):**
- studies: intermediate-learner → composing-typed-simplicial-complexes
- transitions-to: intermediate-learner → compositional-learner
- advances: composing-typed-simplicial-complexes → compositional-learner

### Faces (4)

**Prerequisite faces (2):** Validate dual input conditions
- (intermediate-learner, simplicial-complex-fundamentals, composing-typed-simplicial-complexes)
- (intermediate-learner, typed-simplicial-complexes, composing-typed-simplicial-complexes)

**Completion face (1):** Represents state transition
- (intermediate-learner, composing-typed-simplicial-complexes, compositional-learner)

**Skill-gain face (1):** Represents skill acquisition
- (compositional-learner, composing-typed-simplicial-complexes, composing-typed-simplicial-complexes)

## Topological Properties

- **Vertices:** V = 6
- **Edges:** E = 11
- **Faces:** F = 4
- **Euler Characteristic:** χ = V - E + F = 6 - 11 + 4 = -1

**Interpretation:**
- χ = -1 indicates more complex structure than previous modules due to dual prerequisites
- Four faces create complete validation structure: 2 prerequisites + 1 completion + 1 skill-gain
- Negative χ reflects richer constraint network with two prerequisite paths

## Learning Path Structure

### Entry Point
- **Initial State:** intermediate-learner
- **Entry Skills:** simplicial-complex-fundamentals, typed-simplicial-complexes (both possessed from Modules 1 and 2)

### Module Sequence

**Module:** composing-typed-simplicial-complexes
- **Prerequisites:** simplicial-complex-fundamentals AND typed-simplicial-complexes (dual prerequisites)
- **Develops:** composing-typed-simplicial-complexes
- **Input States:** intermediate-learner
- **Output States:** compositional-learner

### Exit Point
- **Completion State:** compositional-learner
- **Total Skills Gained:** composing-typed-simplicial-complexes (1 new skill)
- **Cumulative Skills:** simplicial-complex-fundamentals, typed-simplicial-complexes, composing-typed-simplicial-complexes (3 total)

## Constraint Validation

### Prerequisite Constraints

For completion face (intermediate-learner, composing-typed-simplicial-complexes, compositional-learner):

**Prerequisite 1 (fundamentals):**
- **Prerequisite face exists?** ✓ (intermediate-learner, simplicial-complex-fundamentals, composing-typed-simplicial-complexes)
- **Student has required skill?** ✓ (intermediate-learner has simplicial-complex-fundamentals)
- **Module requires that skill?** ✓ (composing-typed-simplicial-complexes requires simplicial-complex-fundamentals)

**Prerequisite 2 (typing):**
- **Prerequisite face exists?** ✓ (intermediate-learner, typed-simplicial-complexes, composing-typed-simplicial-complexes)
- **Student has required skill?** ✓ (intermediate-learner has typed-simplicial-complexes)
- **Module requires that skill?** ✓ (composing-typed-simplicial-complexes requires typed-simplicial-complexes)

**All prerequisites validated** ✓

### Skill Accumulation Constraints

For completion face:
```
intermediate-learner.skills = {simplicial-complex-fundamentals, typed-simplicial-complexes}
composing-typed-simplicial-complexes.develops = {composing-typed-simplicial-complexes}

compositional-learner.skills = {
  simplicial-complex-fundamentals,
  typed-simplicial-complexes,
  composing-typed-simplicial-complexes
}

Validation:
- compositional-learner.skills ⊇ intermediate-learner.skills? ✓ (supermodular)
- compositional-learner.skills = intermediate-learner.skills ∪ module.develops? ✓
- |compositional-learner.skills| ≥ |intermediate-learner.skills|? ✓ (3 ≥ 2)
```

### Skill Attribution Constraints

For skill-gain face (compositional-learner, composing-typed-simplicial-complexes, composing-typed-simplicial-complexes):
- **Module develops the skill?** ✓ (develops-skill edge exists)
- **Student has the skill?** ✓ (has-skill edge exists)
- **Completion face exists?** ✓ (advances edge from completion)
- **Causal relationship valid?** ✓

### Acyclic Progression Constraint

- **transitions-to edges form DAG?** ✓ (knowledge-complex-newcomer → foundational → intermediate → compositional, no cycles)
- **No student transitions to state with fewer skills?** ✓ (0 → 1 → 2 → 3 skills, monotonic)

## Expected Tool Behavior

### Verification

```bash
# Build cache
python scripts/build_cache.py

# Verify chart structure
python scripts/verify_chart.py charts/learning-journey-module-03/learning-journey-module-03.md --root .

# Analyze topology
python scripts/topology.py charts/learning-journey-module-03/learning-journey-module-03.md --root .
```

**Expected output:**
- All vertices, edges, faces parse correctly ✓
- All boundary edges exist for faces ✓
- Topology: V=6, E=11, F=4, χ=-1 ✓

### Visualization

```bash
# Export to JSON
python scripts/export_chart_direct.py charts/learning-journey-module-03/learning-journey-module-03.md charts/learning-journey-module-03/learning-journey-module-03.json --root .

# Generate specialized syllabus visualization
python scripts/visualize_syllabus.py charts/learning-journey-module-03/learning-journey-module-03.json
```

**Expected output:** Interactive HTML file (`charts/learning-journey-module-03/learning-journey-module-03.html`) with:

- **Color-coded vertices:** Students (blue), Skills (green), Module (purple)
- **Color-coded edges:** Relationship types (has-skill, requires-skill, develops-skill, studies, transitions-to, advances)
- **Color-coded faces:** Prerequisite (orange, two instances), Completion (blue), Skill-gain (dark green)
- **Interactive legends:** Vertex types, edge types, face types with descriptions
- **Topology info:** V=6, E=11, F=4, χ=-1 with learning path metadata
- **3D navigation:** Rotate, zoom, pan to inspect Module 3 structure

**Visual validation:**
- Two orange prerequisite triangles validate intermediate-learner has both required skills
- Blue completion triangle shows state transition (intermediate → compositional)
- Green skill-gain triangle shows composition skill acquisition
- Clear progression: entry (2 skills) → module → exit (3 skills)

## Module 3 Pedagogical Design

This chart represents the **final foundational module** where students learn to compose simplicial complexes through identification:

**Teaching Approach:**
- **50% identification mechanics**: Students learn to identify shared elements across charts
- **30% composition operations**: Students perform set union and verify type consistency
- **20% practical application**: Students create the combined Module 1+2 chart

**Key Insight:** Students combine the very charts they completed in Modules 1 and 2, making composition concrete and immediately relevant. This completes the foundational trilogy, preparing students for advanced work.

## Path Dependency Note

**Module 3 has a path dependency fork with Module 4 (verification/validation):**

- Module 3 requires: simplicial-complex-fundamentals + typed-simplicial-complexes
- Module 4 requires: simplicial-complex-fundamentals + typed-simplicial-complexes
- Module 3 and Module 4 are **independent**: students could study in either order

This fork will be revealed when the full syllabus chart is constructed, showing multiple valid learning paths through the curriculum.

---

**Note:** This chart completes the foundational trilogy (Module 1: structure, Module 2: types, Module 3: composition). The compositional-learner state possesses all three foundational skills and is ready for advanced modules on verification, validation, assurance, and chart design.
