---
type: face/completion
vertices:
  - v:student:<student-before>
  - v:learning-module:<module-name>
  - v:student:<student-after>
edges:
  - e:studies:<student-before>:<module-name>
  - e:transitions-to:<student-before>:<student-after>
  - e:advances:<module-name>:<student-after>
orientation: oriented
id: f:completion:<student-before>:<module-name>:<student-after>
name: Completion triangle - <student-before> completes <module-name> becoming <student-after>
description: <student-before> completes <module-name>, transitioning to <student-after> with expanded skill set
tags:
  - face
  - completion
  - state-transition
version: 1.0.0
created: <ISO-8601 datetime>
modified: <ISO-8601 datetime>
---

# Completion Triangle: <student-before> completes <module-name> becoming <student-after>

## Purpose

This face represents a **learning state transition** where student **<student-before>** completes module **<module-name>** and transitions to **<student-after>** with an expanded skill set. The completion face is the core topological structure for learning journeys, encoding module completion and skill accumulation.

## Face Type

**Face Type:** completion (2-simplex / triangle)

**Dimension:** 2 (connects 3 vertices)

**Boundary Edges:**
1. `e:studies:<student-before>:<module-name>` - Student engages with module
2. `e:transitions-to:<student-before>:<student-after>` - State transition
3. Edge from module to student-after (could be implicit or explicit edge like `e:produces:<module-name>:<student-after>`)

## Vertices

The completion triangle connects three vertices representing a learning state transition:

1. **Student-before vertex:** `v:student:<student-before>` - Initial learning state
2. **Learning-module vertex:** `v:learning-module:<module-name>` - Completed module
3. **Student-after vertex:** `v:student:<student-after>` - Resulting learning state

## Meaning

This face encodes the **fundamental learning transition**:

```
student-before + module → student-after

Where:
  student-after.skills = student-before.skills ∪ module.develops-skills
```

The triangle represents:
- **Input state:** student-before with initial skill set
- **Transformation:** module completion
- **Output state:** student-after with expanded skill set

## Local Constraint (Validation Rule)

The completion face is **valid** if and only if:

1. **Prerequisite satisfaction:** student-before.skills ⊇ module.requires-skills
   - Student must have ALL skills required by the module
   - Validated via prerequisite faces or skill intersection check

2. **Skill accumulation:** student-after.skills = student-before.skills ∪ module.develops-skills
   - New state has all old skills PLUS skills developed by module
   - Supermodular growth

3. **Cardinality:** |student-after.skills| ≥ |student-before.skills|
   - Monotonically increasing skill count
   - Equality only if module develops no new skills (rare)

## Topological Structure

```
                v:learning-module:<module-name>
                          /\
                         /  \
                studies /    \ (edge to student-after)
                       /      \
                      /        \
                     /          \
                    /  TRIANGLE  \
                   /  (this face) \
                  /                \
                 /                  \
                /____________________\
    v:student:<student-before>   v:student:<student-after>
                  transitions-to
```

The face is the **filled triangle** representing the complete state transition.

## Examples

**Foundational Module (Zero Prerequisites):**
```yaml
type: face/completion
vertices:
  - v:student:knowledge-complex-learner  # No skills initially
  - v:learning-module:simplicial-complex-fundamentals
  - v:student:foundational-learner       # Has simplicial-complex-fundamentals

# Validation:
# - student-before.skills = {} (no prerequisites required)
# - module.requires-skills = {}
# - module.develops-skills = {simplicial-complex-fundamentals}
# - student-after.skills = {} ∪ {simplicial-complex-fundamentals} = {simplicial-complex-fundamentals}
# ✅ Valid
```

**Intermediate Module (With Prerequisites):**
```yaml
type: face/completion
vertices:
  - v:student:foundational-learner       # Has {simplicial-complex-fundamentals}
  - v:learning-module:verification-fundamentals
  - v:student:intermediate-learner       # Has {simplicial-complex-fundamentals, verification-patterns}

# Validation:
# - student-before.skills = {simplicial-complex-fundamentals}
# - module.requires-skills = {simplicial-complex-fundamentals}
# - module.develops-skills = {verification-patterns}
# - Prerequisite check: {simplicial-complex-fundamentals} ⊇ {simplicial-complex-fundamentals} ✅
# - student-after.skills = {simplicial-complex-fundamentals} ∪ {verification-patterns}
# ✅ Valid
```

**Multiple Modules to Same Target (Branching Paths):**
```yaml
# Path A: Module 2a
type: face/completion
vertices:
  - v:student:intermediate-learner
  - v:learning-module:advanced-topology
  - v:student:advanced-learner

# Path B: Module 2b (different module, same target state)
type: face/completion
vertices:
  - v:student:intermediate-learner
  - v:learning-module:chart-design
  - v:student:advanced-learner

# Both paths lead to same advanced-learner state
# (if modules develop same skills or skills are unioned correctly)
```

## Skill Computation

Given a completion face:

```python
def compute_student_after_skills(student_before, module):
    """Compute student-after skill set from completion."""
    # Get student-before skills
    before_skills = get_has_skill_targets(student_before)

    # Get module developed skills
    developed_skills = get_develops_skill_targets(module)

    # Supermodular union
    after_skills = before_skills | developed_skills

    return after_skills

# Validation
def validate_completion_face(student_before, module, student_after):
    """Validate completion face satisfies constraints."""
    # Check prerequisite satisfaction
    before_skills = get_has_skill_targets(student_before)
    required_skills = get_requires_skill_targets(module)
    assert before_skills >= required_skills, "Prerequisites not satisfied"

    # Check skill accumulation
    developed_skills = get_develops_skill_targets(module)
    after_skills = get_has_skill_targets(student_after)
    expected_skills = before_skills | developed_skills
    assert after_skills == expected_skills, "Skill accumulation incorrect"

    # Check monotonicity
    assert len(after_skills) >= len(before_skills), "Skill count decreased"

    return True
```

## Learning Path Chains

Completion faces chain together to form **learning paths**:

```
Face 1: (beginner, module-1, intermediate-1)
Face 2: (intermediate-1, module-2, intermediate-2)
Face 3: (intermediate-2, module-3, master)

Path: beginner → module-1 → intermediate-1 → module-2 → intermediate-2 → module-3 → master
```

Each face adds skills, creating supermodular growth along the path.

## Syllabus Chart Structure

A **syllabus chart** contains:
- **Vertices:** Student states (discrete snapshots), modules, skills
- **Edges:** has-skill, requires-skill, develops-skill, studies, transitions-to
- **Faces:** prerequisite (input validation), completion (state transitions)

Completion faces are the **core structure** of syllabi, representing all valid learning progressions.

## Constraints

- Must reference exactly 3 vertices (triangle)
- Vertex order convention: [student-before, module, student-after]
- All three vertices must exist
- All three boundary edges should exist
- student-before ≠ student-after (different states)
- **Local constraint:** student-before.skills ⊇ module.requires-skills (validated)
- **Local constraint:** student-after.skills = student-before.skills ∪ module.develops-skills (deterministic)

## Invalid Completion Face Examples

**Missing Prerequisites:**
```yaml
vertices:
  - v:student:beginner  # skills = {}
  - v:learning-module:advanced-topology  # requires {fundamentals, intermediate}
  - v:student:advanced  # skills = {fundamentals, intermediate, advanced}

❌ INVALID - beginner lacks prerequisites!
```

**Skill Loss:**
```yaml
vertices:
  - v:student:intermediate  # skills = {A, B, C}
  - v:learning-module:specialization  # develops {D}
  - v:student:specialist  # skills = {A, D}  (lost B and C!)

❌ INVALID - skills cannot be lost!
```

**Incorrect Skill Accumulation:**
```yaml
vertices:
  - v:student:beginner  # skills = {A}
  - v:learning-module:module-1  # develops {B, C}
  - v:student:intermediate  # skills = {A, B}  (missing C!)

❌ INVALID - student-after must have ALL developed skills!
```

## Verification

This face can be verified using:

```bash
python scripts/verify_template_based.py 02_faces/<face-file>.md --templates templates
```

Chart-level verification can check completion face validity:

```bash
python scripts/verify_chart.py charts/<syllabus>/<syllabus>.md
```

---

**Note:** This template defines the completion face (triangle) representing learning state transitions through module completion. Completion faces are the fundamental structure of learning journeys, encoding skill accumulation through supermodular growth. Local constraints ensure prerequisites are satisfied and skills accumulate correctly, while the topology encodes valid learning paths through the syllabus.
