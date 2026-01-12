---
type: edge/transitions-to
source: v:student:<student-before>
target: v:student:<student-after>
source_type: vertex/student
target_type: vertex/student
orientation: directed
id: e:transitions-to:<student-before>:<student-after>
name: <student-before> transitions to <student-after>
description: <student-before> learning state transitions to <student-after> state through module completion
tags:
  - edge
  - transitions-to
  - state-transition
version: 1.0.0
created: <ISO-8601 datetime>
modified: <ISO-8601 datetime>
---

# <student-before> transitions to <student-after>

## Purpose

This edge represents a **learning state transition** where student **<student-before>** (initial state) transitions to **<student-after>** (new state) through completing a learning module. The transitions-to relationship connects student vertices representing discrete learning states in a learning journey.

## Relationship Type

**Edge Type:** transitions-to (state transition)

**Direction:** student → student (before state → after state)

**Participants:**
- **Source:** `v:student:<student-before>` (initial learning state)
- **Target:** `v:student:<student-after>` (new learning state with expanded skills)

## Meaning

This edge indicates that `<student-before>` has transitioned to `<student-after>` by completing one or more learning modules. The transition represents:

- **Skill accumulation:** student-after has all skills from student-before PLUS new skills
- **State progression:** advancement through learning journey
- **Irreversible learning:** students don't transition backward to states with fewer skills

## Learning State Model

**Students as Discrete States:**

In this model, student vertices represent **snapshots of learning state**, not individual people:
- `v:student:beginner` - State with minimal/no skills
- `v:student:intermediate-learner` - State after completing foundational modules
- `v:student:advanced-learner` - State after completing intermediate modules
- `v:student:master` - State with all skills from complete learning path

**State Transitions:**

```
beginner --[module A]--> intermediate --[module B]--> advanced --[module C]--> master
```

Each transition adds skills (supermodular accumulation).

## Skill Set Relationship

**Constraint:** student-after.skills ⊇ student-before.skills (superset)

```
student_after_skills = student_before_skills ∪ module_develops_skills
```

**Cardinality:** |student-after.skills| ≥ |student-before.skills| (monotonically increasing)

The skill set grows through state transitions.

## Examples

**Initial Transition (Zero to First Skills):**
```yaml
# Beginner completes first module, gains first skills
source: v:student:knowledge-complex-learner  # No prerequisites
target: v:student:foundational-learner       # Has simplicial-complex-fundamentals
# Transition through v:learning-module:simplicial-complex-fundamentals
```

**Intermediate Transition:**
```yaml
# Foundational learner advances to intermediate
source: v:student:foundational-learner
target: v:student:intermediate-learner
# Transition through v:learning-module:verification-fundamentals
```

**Branching Paths:**
```yaml
# Same initial state, different transitions (different module choices)
source: v:student:intermediate-learner
target: v:student:advanced-path-A

source: v:student:intermediate-learner
target: v:student:advanced-path-B
# Multiple valid learning paths from same state
```

## Participation in Faces

transitions-to edges participate in **completion faces**:

```yaml
type: face/completion
vertices:
  - v:student:<student-before>        # transitions-to edge source
  - v:learning-module:<module-name>   # completed module
  - v:student:<student-after>         # transitions-to edge target
```

The completion face connects:
1. Initial state (student-before)
2. Module completed
3. Resulting state (student-after)

The triangle represents the state transition caused by module completion.

## State Transition Graph

**Properties:**
- **Directed:** Transitions flow forward through learning journey
- **Acyclic:** No cycles (students don't regress to states with fewer skills)
- **Multiple paths possible:** Different module sequences can lead to same final state
- **Monotonic skill growth:** Each transition adds skills (never removes)

**Example Graph:**
```
        beginner
           |
      [complete M1]
           ↓
      intermediate-A ----[M2a]----> advanced-A
           |                            |
        [M2b]                        [M4a]
           ↓                            ↓
      intermediate-B ----[M3]----> master
                            ↑
                         [M4b]
                            |
                       advanced-B
```

Multiple paths from beginner → master, all valid.

## Constraints

- Source MUST be a student vertex (v:student:*)
- Target MUST be a student vertex (v:student:*)
- Source and target MUST be different students (no self-loops)
- Target skills MUST be superset of source skills (skill accumulation)
- Must not create cycles (acyclic directed graph)
- Each transition should correspond to completion face(s) showing which module(s) caused the transition

## Anti-Pattern: Skill Loss

**Invalid:**
```
student-before.skills = {A, B, C}
student-after.skills = {A, B}  # Lost skill C!
❌ INVALID - skills cannot be lost in transitions
```

**Valid:**
```
student-before.skills = {A, B}
student-after.skills = {A, B, C}  # Gained skill C
✅ VALID - supermodular accumulation
```

## Anti-Pattern: Cycles

**Invalid:**
```
student-A --transitions-to--> student-B
student-B --transitions-to--> student-C
student-C --transitions-to--> student-A
❌ CYCLE - invalid learning progression
```

**Valid:**
```
student-A --transitions-to--> student-B
student-B --transitions-to--> student-C
✅ Acyclic progression
```

## Computing State Transitions

Given completion face (student-before, module, student-after):

```python
# Verify transition validity
def validate_transition(student_before, module, student_after):
    # Check skill accumulation
    required_skills = student_before.skills | module.develops_skills
    assert student_after.skills == required_skills

    # Check monotonicity
    assert len(student_after.skills) >= len(student_before.skills)

    # Check superset
    assert student_before.skills.issubset(student_after.skills)

    return True
```

## Verification

This edge can be verified using:

```bash
python scripts/verify_template_based.py 01_edges/<edge-file>.md --templates templates
```

---

**Note:** This template defines the transitions-to relationship between student learning states. Students represent discrete snapshots of skill accumulation, and transitions model progression through learning journeys with supermodular skill growth. Each transition should be justified by completion face(s) showing which module(s) caused the state change.
