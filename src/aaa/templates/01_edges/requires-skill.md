---
type: edge/requires-skill
source: v:learning-module:<module-name>
target: v:skill:<skill-name>
source_type: vertex/learning-module
target_type: vertex/skill
orientation: directed
id: e:requires-skill:<module-name>:<skill-name>
name: <module-name> requires skill <skill-name>
description: <module-name> has prerequisite <skill-name>
tags:
  - edge
  - requires-skill
  - prerequisite
version: 1.0.0
created: <ISO-8601 datetime>
modified: <ISO-8601 datetime>
---

# <module-name> requires skill <skill-name>

## Purpose

This edge represents that the learning module **<module-name>** requires the skill **<skill-name>** as a prerequisite. The requires-skill relationship connects learning modules to the skills students must possess before beginning the module.

## Relationship Type

**Edge Type:** requires-skill (prerequisite requirement)

**Direction:** learning-module → skill (module requires skill)

**Participants:**
- **Source:** `v:learning-module:<module-name>` (the module with the requirement)
- **Target:** `v:skill:<skill-name>` (the skill that is required)

## Meaning

This edge indicates that `<module-name>` cannot be successfully studied without first possessing `<skill-name>`. This could be because:
- The module builds directly on concepts from that skill
- The module uses techniques that require that skill
- The module's exercises assume that skill is already mastered
- The module's pace assumes prerequisite knowledge

## Prerequisite Pattern

This edge defines **prerequisite requirements** for modules:

- Students without this skill should not attempt the module
- Syllabus charts use these edges to sequence modules appropriately
- Prerequisite faces connect students who have the skill to modules that require it
- The skill must be defined (skill vertex exists) for the requirement to be valid

## Examples

**Foundational Module:**
```yaml
# Module has no prerequisites
# No requires-skill edges for this module
```

**Intermediate Module:**
```yaml
# Module requires understanding of simplicial complexes
source: v:learning-module:verification-fundamentals
target: v:skill:simplicial-complex-fundamentals
# Students must have this skill before studying this module
```

**Advanced Module:**
```yaml
# Module requires multiple prerequisites (multiple requires-skill edges)
source: v:learning-module:advanced-chart-design
target: v:skill:chart-creation
# AND also:
source: v:learning-module:advanced-chart-design
target: v:skill:type-system-understanding
# Students need BOTH skills for this module
```

## Participation in Faces

requires-skill edges participate in **prerequisite faces**:

```yaml
type: face/prerequisite
vertices:
  - v:student:<student-name>          # has-skill edge source
  - v:skill:<skill-name>              # target of both edges
  - v:learning-module:<module-name>   # requires-skill edge source
```

This triangle means: **Student with skill can study module requiring that skill**

The prerequisite face "completes the circuit":
- Student **has** skill (has-skill edge)
- Module **requires** skill (requires-skill edge)
- Triangle: Student **can study** module (prerequisite satisfied)

## Constraints

- Source MUST be a learning-module vertex (v:learning-module:*)
- Target MUST be a skill vertex (v:skill:*)
- Each module-skill pair should have at most one requires-skill edge
- Skill must be defined (skill vertex should exist)
- Module must be defined (learning-module vertex should exist)
- Must not create circular dependencies (module A requires skill from module B requires skill from module A)

## Circular Dependency Check

**Invalid:**
```
Module A requires Skill X (gained from Module B)
Module B requires Skill Y (gained from Module A)
❌ CIRCULAR - learner can't start either module!
```

**Valid Linear Dependency:**
```
Module A (foundational) → teaches Skill X
Module B requires Skill X → teaches Skill Y
Module C requires Skill Y → teaches Skill Z
✅ Valid progression
```

**Valid Branching Dependency:**
```
Module A (foundational) → teaches Skill X
├─ Module B requires Skill X → teaches Skill Y
└─ Module C requires Skill X → teaches Skill Z
✅ Valid branching from foundation
```

## Verification

This edge can be verified using:

```bash
python scripts/verify_template_based.py 01_edges/<edge-file>.md --templates templates
```

---

**Note:** This template defines the requires-skill relationship between learning modules and prerequisite skills. Multiple requires-skill edges from the same module indicate multiple prerequisites that must ALL be satisfied.
