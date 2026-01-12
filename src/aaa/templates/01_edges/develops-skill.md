---
type: edge/develops-skill
source: v:learning-module:<module-name>
target: v:skill:<skill-name>
source_type: vertex/learning-module
target_type: vertex/skill
orientation: directed
id: e:develops-skill:<module-name>:<skill-name>
name: <module-name> develops skill <skill-name>
description: <module-name> teaches and develops <skill-name> capability
tags:
  - edge
  - develops-skill
  - learning-outcome
version: 1.0.0
created: <ISO-8601 datetime>
modified: <ISO-8601 datetime>
---

# <module-name> develops skill <skill-name>

## Purpose

This edge represents that the learning module **<module-name>** develops (teaches) the skill **<skill-name>** as a learning outcome. The develops-skill relationship connects modules to the skills students gain by completing them.

## Relationship Type

**Edge Type:** develops-skill (learning outcome)

**Direction:** learning-module → skill (module develops skill)

**Participants:**
- **Source:** `v:learning-module:<module-name>` (the module that teaches)
- **Target:** `v:skill:<skill-name>` (the skill that is developed)

## Meaning

This edge indicates that `<module-name>` teaches `<skill-name>` as a learning outcome. Students who complete this module gain this skill, transitioning to a new learning state with an expanded skill set.

This represents the **output signature** of the module:
- **Input:** requires-skill edges (prerequisites)
- **Output:** develops-skill edges (learning outcomes)

## Skill Accumulation Pattern

This edge enables **supermodular skill accumulation**:

```
student-after.skills = student-before.skills ∪ module.develops-skills

Where module.develops-skills = {all skills with develops-skill edges from module}
```

The skill set grows (supermodular) through module completion, and the cardinality is monotonically increasing.

## Examples

**Foundational Module (Develops First Skills):**
```yaml
# Module develops foundational skills from zero prerequisites
source: v:learning-module:simplicial-complex-fundamentals
target: v:skill:simplicial-complex-fundamentals
# Students gain this skill by completing the module
```

**Intermediate Module (Develops Advanced Skills):**
```yaml
# Module develops new skills building on prerequisites
source: v:learning-module:verification-fundamentals
target: v:skill:verification-patterns
# Students who already have prerequisites gain this skill
```

**Module with Multiple Outcomes:**
```yaml
# Multiple develops-skill edges for multiple learning outcomes
source: v:learning-module:advanced-topology
target: v:skill:homology-theory

source: v:learning-module:advanced-topology
target: v:skill:topological-analysis
# Students gain ALL skills the module develops
```

## Participation in Faces

develops-skill edges participate in **completion faces**:

```yaml
type: face/completion
vertices:
  - v:student:<student-before>        # initial learning state
  - v:learning-module:<module-name>   # develops-skill edge source
  - v:student:<student-after>         # new learning state
```

The completion face represents:
- student-before completes module
- module develops skills (this edge)
- student-after has student-before.skills ∪ module.develops-skills

## Module Signature Pattern

**Complete Module Signature:**

```yaml
Module: v:learning-module:example

Input (Prerequisites):
  requires-skill → v:skill:prerequisite-A
  requires-skill → v:skill:prerequisite-B

Output (Learning Outcomes):
  develops-skill → v:skill:outcome-X
  develops-skill → v:skill:outcome-Y

Signature: (prerequisite-A, prerequisite-B) → (outcome-X, outcome-Y)
```

Students must have input skills, gain output skills.

## Constraints

- Source MUST be a learning-module vertex (v:learning-module:*)
- Target MUST be a skill vertex (v:skill:*)
- Each module-skill pair should have at most one develops-skill edge
- Skill must be defined (skill vertex should exist)
- Module must be defined (learning-module vertex should exist)
- Developed skill should NOT also be a required skill for the same module (module doesn't teach what it requires)

## Anti-Pattern: Circular Development

**Invalid:**
```
Module A develops Skill X (needed for Module B)
Module B develops Skill Y (needed for Module A)
Both modules require each other's outputs as inputs
❌ CIRCULAR DEPENDENCY
```

**Valid:**
```
Module A (foundational) develops Skill X
Module B requires Skill X, develops Skill Y
Module C requires Skill Y, develops Skill Z
✅ Valid linear progression
```

## Skill Set Computation

Given a completion face (student-before, module, student-after):

```python
# Compute student-after skills
student_after_skills = (
    student_before_skills
    | module_develops_skills  # Set union (supermodular)
)

# Cardinality is monotonically increasing
assert len(student_after_skills) >= len(student_before_skills)
```

## Verification

This edge can be verified using:

```bash
python scripts/verify_template_based.py 01_edges/<edge-file>.md --templates templates
```

---

**Note:** This template defines the develops-skill relationship representing module learning outcomes. It is essential for computing student skill set transitions and forms the output signature of learning modules. Together with requires-skill (input signature), it defines the complete module transformation: input-skills → module → output-skills.
