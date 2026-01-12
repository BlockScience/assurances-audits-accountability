---
type: face/skill-gain
vertices:
  - v:student:<student-after>
  - v:learning-module:<module-name>
  - v:skill:<skill-name>
edges:
  - e:advances:<module-name>:<student-after>
  - e:has-skill:<student-after>:<skill-name>
  - e:develops-skill:<module-name>:<skill-name>
orientation: oriented
id: f:skill-gain:<student-after>:<module-name>:<skill-name>
name: Skill-gain triangle - <student-after> gains <skill-name> from <module-name>
description: <student-after> gains <skill-name> through completing <module-name>
tags:
  - face
  - skill-gain
  - acquisition
version: 1.0.0
created: <ISO-8601 datetime>
modified: <ISO-8601 datetime>
---

# Skill-Gain Triangle: <student-after> gains <skill-name> from <module-name>

## Purpose

This face represents **skill acquisition** where student **<student-after>** gains skill **<skill-name>** through completing module **<module-name>**. The skill-gain face is a causal structure encoding that module completion causes skill acquisition.

## Face Type

**Face Type:** skill-gain (2-simplex / triangle)

**Dimension:** 2 (connects 3 vertices)

**Boundary Edges:**
1. `e:advances:<module-name>:<student-after>` - Module advances to student state
2. `e:has-skill:<student-after>:<skill-name>` - Student possesses skill
3. `e:develops-skill:<module-name>:<skill-name>` - Module develops skill

## Vertices

The skill-gain triangle connects three vertices representing skill acquisition:

1. **Student-after vertex:** `v:student:<student-after>` - Resulting learning state
2. **Learning-module vertex:** `v:learning-module:<module-name>` - Completed module
3. **Skill vertex:** `v:skill:<skill-name>` - Acquired skill

## Meaning

This face encodes the **causal relationship of skill acquisition**:

```
Module completion → Student gains skill

Where:
  module develops skill (develops-skill edge)
  module advances student (advances edge)
  student has skill (has-skill edge)

∴ Completing module CAUSES student to acquire skill
```

The triangle represents:
- **Module output:** Module develops this skill
- **State advancement:** Module advances learner to new state
- **Skill possession:** New state possesses the developed skill
- **Causality:** The completion causes the acquisition

## Topological Structure

```
                v:learning-module:<module-name>
                          /\
                         /  \
              advances  /    \ develops-skill
                       /      \
                      /        \
                     /          \
                    /  SKILL-GAIN \
                   /      FACE      \
                  /                  \
                 /____________________\
    v:student:<student-after>   v:skill:<skill-name>
                    has-skill
```

The face is the **filled triangle** representing the causal skill acquisition.

## Examples

**Single Skill Acquisition:**
```yaml
type: face/skill-gain
vertices:
  - v:student:foundational-learner
  - v:learning-module:simplicial-complex-fundamentals
  - v:skill:simplicial-complex-fundamentals

# Causality:
# - Module develops simplicial-complex-fundamentals
# - Module advances to foundational-learner
# - Foundational-learner has simplicial-complex-fundamentals
# ∴ Completing module causes skill acquisition
```

**Multiple Skill Acquisitions:**
```yaml
# If module develops multiple skills, create multiple skill-gain faces

# Face 1: Gain skill A
type: face/skill-gain
vertices:
  - v:student:intermediate-learner
  - v:learning-module:advanced-topics
  - v:skill:skill-A

# Face 2: Gain skill B
type: face/skill-gain
vertices:
  - v:student:intermediate-learner
  - v:learning-module:advanced-topics
  - v:skill:skill-B

# Each developed skill gets its own skill-gain face
```

## Semantic Distinction from Other Face Types

**Prerequisite face:** `(student-before, skill, module)`
- Validates **input condition** (student HAS skill module REQUIRES)
- Checks prerequisite satisfaction
- Uses edges: has-skill, requires-skill, studies

**Completion face:** `(student-before, module, student-after)`
- Represents **state transition** through module completion
- Shows learning progression
- Uses edges: studies, transitions-to, advances

**Skill-gain face:** `(student-after, module, skill)` ← THIS FACE
- Represents **skill acquisition** from module completion
- Shows causal relationship: completion → gain
- Uses edges: advances, has-skill, develops-skill

## Relationship to Completion Face

The skill-gain face is **complementary** to the completion face:

**Completion face shows:** student-before → module → student-after (WHO)
**Skill-gain face shows:** student-after ← module → skill (WHAT)

Together they encode:
- **WHO transitions:** student-before becomes student-after (completion)
- **WHAT is gained:** student-after gains developed skills (skill-gain)

For a module that develops N skills, you have:
- **1 completion face** (state transition)
- **N skill-gain faces** (one per developed skill)

## Local Constraint (Validation Rule)

The skill-gain face is **valid** if and only if:

1. **Module develops skill:** `develops-skill` edge exists from module to skill
2. **Module advances student:** `advances` edge exists from module to student-after
3. **Student has skill:** `has-skill` edge exists from student-after to skill
4. **Consistency:** All edges in boundary exist and connect the 3 vertices in a closed triangle

## Skill Accumulation Validation

Given a skill-gain face, we can verify:

```python
def validate_skill_gain(student_after, module, skill):
    """Validate skill-gain face represents valid acquisition."""

    # Check module develops this skill
    developed_skills = get_develops_skill_targets(module)
    assert skill in developed_skills, "Module must develop this skill"

    # Check student-after has this skill
    student_skills = get_has_skill_targets(student_after)
    assert skill in student_skills, "Student-after must have this skill"

    # Check advances edge exists (from completion face)
    advances_edges = get_advances_edges(module)
    assert student_after in [e.target for e in advances_edges], "Module must advance to this student"

    return True
```

## Chart Structure Pattern

For a learning journey with one module developing one skill:

```
Vertices: student-before, module, student-after, skill
Edges: studies, transitions-to, advances, develops-skill, has-skill (+ others)
Faces:
  - Prerequisite faces (if module has prerequisites)
  - Completion face: (student-before, module, student-after)
  - Skill-gain face: (student-after, module, skill)
```

The completion and skill-gain faces work together to fully represent the learning transformation.

## Multiple Modules Pattern

For a learning journey with multiple modules:

```
Module 1 develops Skill A:
  - Completion face 1: (beginner, module-1, intermediate)
  - Skill-gain face 1: (intermediate, module-1, skill-A)

Module 2 develops Skill B:
  - Completion face 2: (intermediate, module-2, advanced)
  - Skill-gain face 2: (advanced, module-2, skill-B)
```

Each module completion creates:
- 1 completion face (state transition)
- N skill-gain faces (N = number of skills developed)

## Constraints

- Must reference exactly 3 vertices (triangle)
- Vertex order convention: [student-after, module, skill]
- All three vertices must exist
- All three boundary edges must exist
- **Causal constraint:** Module must develop the skill (develops-skill edge)
- **Possession constraint:** Student-after must have the skill (has-skill edge)
- **Advancement constraint:** Module must advance to student-after (advances edge from completion face)

## Invalid Skill-Gain Face Examples

**Module doesn't develop skill:**
```yaml
vertices:
  - v:student:advanced-learner
  - v:learning-module:intro-module
  - v:skill:expert-skill

# Module develops: basic-skill
# Face claims: expert-skill
❌ INVALID - module doesn't develop this skill!
```

**Student doesn't have skill:**
```yaml
vertices:
  - v:student:intermediate-learner  # has skills: A, B
  - v:learning-module:module-1  # develops: C
  - v:skill:skill-C

# But intermediate-learner.skills = {A, B} (missing C!)
❌ INVALID - student must have the skill!
```

**No advances edge:**
```yaml
vertices:
  - v:student:random-learner
  - v:learning-module:some-module
  - v:skill:some-skill

# No completion face with advances edge to random-learner
❌ INVALID - module must advance to this student (from completion face)!
```

## Verification

This face can be verified using:

```bash
python scripts/verify_template_based.py 02_faces/<face-file>.md --templates templates
```

Chart-level verification can check skill-gain face validity:

```bash
python scripts/verify_chart.py charts/<syllabus>/<syllabus>.md
```

---

**Note:** This template defines the skill-gain face representing causal skill acquisition through module completion. Skill-gain faces complement completion faces by encoding WHAT skills are gained (not just WHO transitions). Together they provide a complete picture of learning journeys: state transitions (completion) + skill acquisitions (skill-gain).
