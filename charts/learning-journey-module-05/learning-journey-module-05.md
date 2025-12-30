---
type: chart/syllabus
extends: chart
id: c:learning-journey-module-05
name: Learning Journey - Module 05
description: Fifth module in learning journey teaching assurance triangles, assurance network auditing, and boundary complex self-referential foundations

# Chart construction metadata
constructed_by: "Claude Sonnet 4.5"
construction_method: assisted
construction_date: 2025-12-28T00:00:00Z

# Chart purpose
purpose: Demonstrate skill accumulation for Module 5 (assurance & audits) building on Module 4, teaching complete assurance networks and boundary complex understanding
scope: One module (assurance-audits) with 1 prerequisite skill and 1 developed skill, showing student state transition from verification-learner to assurance-learner (fork point)

# Learning path metadata
learning_path:
  entry_state: v:student:verification-learner
  exit_states:
    - v:student:assurance-learner

prerequisites:
  entry_skills:
    - v:skill:verification-validation

outcomes:
  developed_skills:
    - v:skill:assurance-audits

# Elements comprising this chart
elements:
  vertices:
    - v:student:verification-learner
    - v:skill:verification-validation
    - v:skill:assurance-audits
    - v:learning-module:assurance-audits
    - v:student:assurance-learner
  edges:
    - e:has-skill:verification-learner:verification-validation
    - e:requires-skill:assurance-audits:verification-validation
    - e:develops-skill:assurance-audits:assurance-audits
    - e:studies:verification-learner:assurance-audits
    - e:transitions-to:verification-learner:assurance-learner
    - e:advances:assurance-audits:assurance-learner
    - e:has-skill:assurance-learner:assurance-audits
  faces:
    - f:prerequisite:verification-learner:verification-validation:assurance-audits
    - f:completion:verification-learner:assurance-audits:assurance-learner
    - f:skill-gain:assurance-learner:assurance-audits:assurance-audits

tags:
  - chart
  - syllabus
  - learning-journey
  - module-05
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Learning Journey - Module 05

Fifth module in the learning journey completing the assurance foundation with networks and boundary complex.

## Purpose

This chart validates the learning journey framework for Module 5 by demonstrating:
1. **Single prerequisite validation** via one prerequisite face (student must have verification-validation skill)
2. **Skill accumulation to 4 skills** via completion face (supermodular growth from 3 to 4 skills)
3. **State transitions** via student vertices representing discrete learning states
4. **Assurance network skill development** through triangle construction and auditing
5. **Fork point creation** where assurance-learner can proceed to Module 06 or Module 07

## Structure

### Vertices (5)

**Students (2 learning states):**
- [verification-learner](../../00_vertices/student-verification-learner.md) - Entry state with 3 skills
- [assurance-learner](../../00_vertices/student-assurance-learner.md) - State after completing Module 5 with 4 skills (fork point)

**Skills (2):**
- [verification-validation](../../00_vertices/skill-verification-validation.md) - Entry prerequisite from Module 4
- [assurance-audits](../../00_vertices/skill-assurance-audits.md) - Developed by Module 5

**Module (1):**
- [assurance-audits](../../00_vertices/learning-module-assurance-audits.md) - Module teaching assurance networks and boundary complex

### Edges (7)

**has-skill edges (2):**
- verification-learner → verification-validation (entry skill)
- assurance-learner → assurance-audits (newly acquired)

**requires-skill edge (1):**
- assurance-audits → verification-validation

**develops-skill edge (1):**
- assurance-audits → assurance-audits

**Learning edges (3):**
- studies: verification-learner → assurance-audits
- transitions-to: verification-learner → assurance-learner
- advances: assurance-audits → assurance-learner

### Faces (3)

**Prerequisite face (1):** Validates single input condition
- (verification-learner, verification-validation, assurance-audits)

**Completion face (1):** Represents state transition
- (verification-learner, assurance-audits, assurance-learner)

**Skill-gain face (1):** Represents skill acquisition
- (assurance-learner, assurance-audits, assurance-audits)

## Topological Properties

- **Vertices:** V = 5
- **Edges:** E = 7
- **Faces:** F = 3
- **Euler Characteristic:** χ = V - E + F = 5 - 7 + 3 = 1

**Interpretation:**
- χ = 1 indicates topologically complete structure (sphere-like)
- Three faces create complete validation structure: 1 prerequisite + 1 completion + 1 skill-gain
- Same topology as Module 4 (single prerequisite pattern)

## Learning Path Structure

### Entry Point
- **Initial State:** verification-learner
- **Entry Skills:** verification-validation (possessed from Module 4)

### Module Sequence

**Module:** assurance-audits
- **Prerequisites:** verification-validation (single prerequisite)
- **Develops:** assurance-audits
- **Input States:** verification-learner
- **Output States:** assurance-learner

### Exit Point
- **Completion State:** assurance-learner (fork point)
- **Total Skills Gained:** assurance-audits (1 new skill)
- **Cumulative Skills:** simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation, assurance-audits (4 total)

## Constraint Validation

### Prerequisite Constraints

For completion face (verification-learner, assurance-audits, assurance-learner):

**Prerequisite (quality assurance):**
- **Prerequisite face exists?** ✓ (verification-learner, verification-validation, assurance-audits)
- **Student has required skill?** ✓ (verification-learner has verification-validation)
- **Module requires that skill?** ✓ (assurance-audits requires verification-validation)

**All prerequisites validated** ✓

### Skill Accumulation Constraints

For completion face:
```
verification-learner.skills = {simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation}
assurance-audits.develops = {assurance-audits}

assurance-learner.skills = {
  simplicial-complex-fundamentals,
  typed-simplicial-complexes,
  verification-validation,
  assurance-audits
}

Validation:
- assurance-learner.skills ⊇ verification-learner.skills? ✓ (supermodular)
- assurance-learner.skills = verification-learner.skills ∪ module.develops? ✓
- |assurance-learner.skills| ≥ |verification-learner.skills|? ✓ (4 ≥ 3)
```

### Skill Attribution Constraints

For skill-gain face (assurance-learner, assurance-audits, assurance-audits):
- **Module develops the skill?** ✓ (develops-skill edge exists)
- **Student has the skill?** ✓ (has-skill edge exists)
- **Completion face exists?** ✓ (advances edge from completion)
- **Causal relationship valid?** ✓

### Acyclic Progression Constraint

- **transitions-to edges form DAG?** ✓ (knowledge-complex-newcomer → foundational → intermediate → verification → assurance, no cycles)
- **No student transitions to state with fewer skills?** ✓ (0 → 1 → 2 → 3 → 4 skills, monotonic)

## Expected Tool Behavior

### Verification

```bash
# Build cache
python scripts/build_cache.py

# Verify chart structure
python scripts/verify_chart.py charts/learning-journey-module-05/learning-journey-module-05.md --root .

# Analyze topology
python scripts/topology.py charts/learning-journey-module-05/learning-journey-module-05.md --root .
```

**Expected output:**
- All vertices, edges, faces parse correctly ✓
- All boundary edges exist for faces ✓
- Topology: V=5, E=7, F=3, χ=1 ✓

### Visualization

```bash
# Export to JSON
python scripts/export_chart_direct.py charts/learning-journey-module-05/learning-journey-module-05.md charts/learning-journey-module-05/learning-journey-module-05.json --root .

# Generate specialized syllabus visualization
python scripts/visualize_syllabus.py charts/learning-journey-module-05/learning-journey-module-05.json
```

**Expected output:** Interactive HTML file (`charts/learning-journey-module-05/learning-journey-module-05.html`) with:

- **Color-coded vertices:** Students (blue), Skills (green), Module (purple)
- **Color-coded edges:** Relationship types (has-skill, requires-skill, develops-skill, studies, transitions-to, advances)
- **Color-coded faces:** Prerequisite (orange), Completion (blue), Skill-gain (dark green)
- **Interactive legends:** Vertex types, edge types, face types with descriptions
- **Topology info:** V=5, E=7, F=3, χ=1 with learning path metadata
- **3D navigation:** Rotate, zoom, pan to inspect Module 5 structure

**Visual validation:**
- One orange prerequisite triangle validates verification-learner has verification-validation skill
- Blue completion triangle shows state transition (verification → assurance)
- Green skill-gain triangle shows assurance-audits skill acquisition
- Clear progression: entry (3 skills) → module → exit (4 skills, fork point)

## Module 5 Pedagogical Design

This chart represents the **assurance network completion module** where students learn to combine verification, validation, and coupling into complete assurance triangles:

**Teaching Approach:**
- **30% assurance triangle construction**: Combining three edges into coherent faces
- **30% assurance auditing**: Using `audit_assurance_chart.py` for network validation
- **30% boundary complex**: Understanding self-referential foundations and root anchoring
- **10% kernel pattern**: Recognizing SS-GS, SG-GG as foundational pairs

**Key Insight:** Students complete the assurance foundation by learning how individual quality checks combine into network-level quality testimony, with boundary complex resolving circular dependencies.

## Fork Point Significance

**Module 5 exit state (assurance-learner) is a critical fork point:**

- **Path 1 to Module 06 (document-composition):**
  - Requires: assurance-audits + composing-typed-simplicial-complexes (dual prerequisites)
  - Students must have taken Module 3 before Module 6
  - Gains: document-composition skill

- **Path 2 to Module 07 (reference-reuse):**
  - Requires: assurance-audits only (single prerequisite)
  - Students can skip Module 3 if taking this path
  - Gains: reference-reuse skill

- **Both paths lead to:** document-architect terminal state (convergence)

**Fork design enables multiple learning paths:**
- Linear path: 01 → 02 → 04 → 05 → 07 (skips composition)
- Full path: 01 → 02 → 03 → 04 → 05 → 06 (requires composition)
- Complete path: 01 → 02 → 03 → 04 → 05 → {06, 07} (both advanced modules)

---

**Note:** This chart completes the assurance foundation and creates the fork point for advanced modules. The assurance-learner state enables two parallel paths to document-architect, giving students flexibility in their learning journey.
