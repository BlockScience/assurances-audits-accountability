---
type: chart/syllabus
extends: chart
id: c:learning-journey-module-06
name: Learning Journey - Module 06
description: Sixth module in learning journey teaching compositional document architecture using Obsidian embeds, typed subsections, and PPP framework

# Chart construction metadata
constructed_by: "Claude Sonnet 4.5"
construction_method: assisted
construction_date: 2025-12-28T00:00:00Z

# Chart purpose
purpose: Demonstrate skill accumulation for Module 6 (document composition) building on Modules 3 and 5, teaching compositional architectures with systematic assurance workflows
scope: One module (document-composition) with 2 prerequisite skills (dual) and 1 developed skill, showing student state transition from assurance-learner to document-architect (convergence point)

# Learning path metadata
learning_path:
  entry_state: v:student:assurance-learner
  exit_states:
    - v:student:document-architect

prerequisites:
  entry_skills:
    - v:skill:assurance-audits
    - v:skill:composing-typed-simplicial-complexes

outcomes:
  developed_skills:
    - v:skill:document-composition

# Elements comprising this chart
elements:
  vertices:
    - v:student:assurance-learner
    - v:skill:assurance-audits
    - v:skill:composing-typed-simplicial-complexes
    - v:skill:document-composition
    - v:learning-module:document-composition
    - v:student:document-architect
  edges:
    - e:has-skill:assurance-learner:assurance-audits
    - e:has-skill:assurance-learner:composing-typed-simplicial-complexes
    - e:requires-skill:document-composition:assurance-audits
    - e:requires-skill:document-composition:composing-typed-simplicial-complexes
    - e:develops-skill:document-composition:document-composition
    - e:studies:assurance-learner:document-composition
    - e:transitions-to:assurance-learner:document-architect
    - e:advances:document-composition:document-architect
    - e:has-skill:document-architect:document-composition
  faces:
    - f:prerequisite:assurance-learner:assurance-audits:document-composition
    - f:prerequisite:assurance-learner:composing-typed-simplicial-complexes:document-composition
    - f:completion:assurance-learner:document-composition:document-architect
    - f:skill-gain:document-architect:document-composition:document-composition

tags:
  - chart
  - syllabus
  - learning-journey
  - module-06
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Learning Journey - Module 06

Sixth module in the learning journey introducing compositional document architecture (one of two paths to document-architect).

## Purpose

This chart validates the learning journey framework for Module 6 by demonstrating:
1. **Dual prerequisite validation** via two prerequisite faces (student must have both assurance-audits AND composing-typed-simplicial-complexes)
2. **Skill accumulation to 6 skills** via completion face (supermodular growth from 5 to 6 skills)
3. **State transitions** via student vertices representing discrete learning states
4. **Compositional architecture skill development** through Obsidian embeds and PPP framework
5. **Convergence point creation** where Module 06 path merges with Module 07 path at document-architect

## Structure

### Vertices (6)

**Students (2 learning states):**
- [assurance-learner](../../00_vertices/student-assurance-learner.md) - Entry state with 5 skills (fork point, includes composing skill from Module 3)
- [document-architect](../../00_vertices/student-document-architect.md) - Terminal state with 6 skills (convergence point)

**Skills (3):**
- [assurance-audits](../../00_vertices/skill-assurance-audits.md) - Entry prerequisite 1 from Module 5
- [composing-typed-simplicial-complexes](../../00_vertices/skill-composing-typed-simplicial-complexes.md) - Entry prerequisite 2 from Module 3
- [document-composition](../../00_vertices/skill-document-composition.md) - Developed by Module 6

**Module (1):**
- [document-composition](../../00_vertices/learning-module-document-composition.md) - Module teaching compositional document architecture

### Edges (9)

**has-skill edges (3):**
- assurance-learner → assurance-audits (entry skill 1)
- assurance-learner → composing-typed-simplicial-complexes (entry skill 2)
- document-architect → document-composition (newly acquired)

**requires-skill edges (2):**
- document-composition → assurance-audits
- document-composition → composing-typed-simplicial-complexes

**develops-skill edge (1):**
- document-composition → document-composition

**Learning edges (3):**
- studies: assurance-learner → document-composition
- transitions-to: assurance-learner → document-architect
- advances: document-composition → document-architect

### Faces (4)

**Prerequisite faces (2):** Validate dual input conditions
- (assurance-learner, assurance-audits, document-composition)
- (assurance-learner, composing-typed-simplicial-complexes, document-composition)

**Completion face (1):** Represents state transition
- (assurance-learner, document-composition, document-architect)

**Skill-gain face (1):** Represents skill acquisition
- (document-architect, document-composition, document-composition)

## Topological Properties

- **Vertices:** V = 6
- **Edges:** E = 9
- **Faces:** F = 4
- **Euler Characteristic:** χ = V - E + F = 6 - 9 + 4 = 1

**Interpretation:**
- χ = 1 indicates topologically complete structure (sphere-like)
- Four faces create complete validation structure: 2 prerequisites + 1 completion + 1 skill-gain
- More complex than Modules 4 and 5 due to dual prerequisites

## Learning Path Structure

### Entry Point
- **Initial State:** assurance-learner (fork point)
- **Entry Skills:** assurance-audits (from Module 5), composing-typed-simplicial-complexes (from Module 3)
- **Total entry skills:** 5 (fundamentals, types, composition, verification-validation, assurance-audits)

### Module Sequence

**Module:** document-composition
- **Prerequisites:** assurance-audits AND composing-typed-simplicial-complexes (dual prerequisites)
- **Develops:** document-composition
- **Input States:** assurance-learner (with composition skill)
- **Output States:** document-architect (convergence point)

### Exit Point
- **Completion State:** document-architect (convergence point, terminal state)
- **Total Skills Gained:** document-composition (1 new skill)
- **Cumulative Skills:** simplicial-complex-fundamentals, typed-simplicial-complexes, composing-typed-simplicial-complexes, verification-validation, assurance-audits, document-composition (6 total)

## Constraint Validation

### Prerequisite Constraints

For completion face (assurance-learner, document-composition, document-architect):

**Prerequisite 1 (assurance):**
- **Prerequisite face exists?** ✓ (assurance-learner, assurance-audits, document-composition)
- **Student has required skill?** ✓ (assurance-learner has assurance-audits)
- **Module requires that skill?** ✓ (document-composition requires assurance-audits)

**Prerequisite 2 (composition):**
- **Prerequisite face exists?** ✓ (assurance-learner, composing-typed-simplicial-complexes, document-composition)
- **Student has required skill?** ✓ (assurance-learner has composing-typed-simplicial-complexes)
- **Module requires that skill?** ✓ (document-composition requires composing-typed-simplicial-complexes)

**All prerequisites validated** ✓

### Skill Accumulation Constraints

For completion face:
```
assurance-learner.skills = {
  simplicial-complex-fundamentals,
  typed-simplicial-complexes,
  composing-typed-simplicial-complexes,
  verification-validation,
  assurance-audits
}
document-composition.develops = {document-composition}

document-architect.skills = {
  simplicial-complex-fundamentals,
  typed-simplicial-complexes,
  composing-typed-simplicial-complexes,
  verification-validation,
  assurance-audits,
  document-composition
}

Validation:
- document-architect.skills ⊇ assurance-learner.skills? ✓ (supermodular)
- document-architect.skills = assurance-learner.skills ∪ module.develops? ✓
- |document-architect.skills| ≥ |assurance-learner.skills|? ✓ (6 ≥ 5)
```

### Skill Attribution Constraints

For skill-gain face (document-architect, document-composition, document-composition):
- **Module develops the skill?** ✓ (develops-skill edge exists)
- **Student has the skill?** ✓ (has-skill edge exists)
- **Completion face exists?** ✓ (advances edge from completion)
- **Causal relationship valid?** ✓

### Acyclic Progression Constraint

- **transitions-to edges form DAG?** ✓ (assurance-learner → document-architect, no cycles)
- **No student transitions to state with fewer skills?** ✓ (5 → 6 skills, monotonic)

## Expected Tool Behavior

### Verification

```bash
# Build cache
python scripts/build_cache.py

# Verify chart structure
python scripts/verify_chart.py charts/learning-journey-module-06/learning-journey-module-06.md --root .

# Analyze topology
python scripts/topology.py charts/learning-journey-module-06/learning-journey-module-06.md --root .
```

**Expected output:**
- All vertices, edges, faces parse correctly ✓
- All boundary edges exist for faces ✓
- Topology: V=6, E=9, F=4, χ=1 ✓

### Visualization

```bash
# Export to JSON
python scripts/export_chart_direct.py charts/learning-journey-module-06/learning-journey-module-06.md charts/learning-journey-module-06/learning-journey-module-06.json --root .

# Generate specialized syllabus visualization
python scripts/visualize_syllabus.py charts/learning-journey-module-06/learning-journey-module-06.json
```

**Expected output:** Interactive HTML file (`charts/learning-journey-module-06/learning-journey-module-06.html`) with:

- **Color-coded vertices:** Students (blue), Skills (green), Module (purple)
- **Color-coded edges:** Relationship types (has-skill, requires-skill, develops-skill, studies, transitions-to, advances)
- **Color-coded faces:** Prerequisite (orange, two instances), Completion (blue), Skill-gain (dark green)
- **Interactive legends:** Vertex types, edge types, face types with descriptions
- **Topology info:** V=6, E=9, F=4, χ=1 with learning path metadata
- **3D navigation:** Rotate, zoom, pan to inspect Module 6 structure

**Visual validation:**
- Two orange prerequisite triangles validate assurance-learner has both required skills
- Blue completion triangle shows state transition (assurance → document-architect)
- Green skill-gain triangle shows document-composition skill acquisition
- Clear progression: entry (5 skills) → module → exit (6 skills, convergence)

## Module 6 Pedagogical Design

This chart represents the **compositional architecture module** where students learn to design modular documentation with systematic assurance:

**Teaching Approach:**
- **20% compositional problem**: Understanding limitations of monolithic documents
- **20% Obsidian embeds & typed subsections**: Syntax and semantics of composition
- **30% PPP framework**: Persona-Purpose-Protocol worked example
- **20% compilation workflow**: Using `compile_document.py` deterministically
- **10% assurance workflow**: Assure components → compile → assure compound

**Key Insight:** Students apply composition operations from Module 3 and assurance workflows from Module 5 to design modular document systems where components are independently assured and then systematically composed.

## Convergence Point Significance

**Module 6 exit state (document-architect) is a convergence point:**

- **Path 1 (via Module 06):**
  - Requires: Modules 03 + 05 (composition + assurance)
  - Gains: document-composition skill
  - Total skills: 6

- **Path 2 (via Module 07):**
  - Requires: Module 05 only (assurance)
  - Gains: reference-reuse skill
  - Total skills: 5

- **Both paths (complete):**
  - Requires: Modules 03 + 05, then both 06 and 07
  - Gains: both document-composition and reference-reuse
  - Total skills: 7

**Convergence enables multiple completion strategies:**
- Minimum path: Skip Module 06, take Module 07 (5 skills)
- Composition path: Take Module 06, skip Module 07 (6 skills)
- Complete path: Take both Module 06 and Module 07 (7 skills)

---

**Note:** This chart demonstrates the dual prerequisite pattern (requires both assurance AND composition understanding) and creates one of two paths to the terminal document-architect state. Students reaching document-architect via Module 06 have mastered compositional document architecture.
