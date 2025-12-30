---
type: edge/studies
source: v:student:<student-name>
target: v:learning-module:<module-name>
source_type: vertex/student
target_type: vertex/learning-module
orientation: directed
id: e:studies:<student-name>:<module-name>
name: <student-name> studies <module-name>
description: <student-name> is engaged in learning <module-name>
tags:
  - edge
  - studies
  - learning
version: 1.0.0
created: <ISO-8601 datetime>
modified: <ISO-8601 datetime>
---

# <student-name> studies <module-name>

## Purpose

This edge represents that the student **<student-name>** is studying (or has studied) the learning module **<module-name>**. The studies relationship connects students to learning modules, indicating engagement in the learning process.

## Relationship Type

**Edge Type:** studies (learning engagement)

**Direction:** student → learning-module (student studies module)

**Participants:**
- **Source:** `v:student:<student-name>` (the student engaged in learning)
- **Target:** `v:learning-module:<module-name>` (the module being studied)

## Meaning

This edge indicates that `<student-name>` is engaged with `<module-name>`. This could represent:
- **Current study:** Student is actively working through the module
- **Completed study:** Student has finished the module (achieving learning objectives)
- **Planned study:** Student intends to study this module (in syllabus sequence)

## Learning Engagement Pattern

This edge follows the **learning engagement pattern**:

- Students engage with modules through the studies relationship
- Prerequisites should be satisfied before creating a studies edge (checked by prerequisite faces)
- Completion of a module may result in has-skill edges (student gains new skills)
- Syllabus charts organize studies edges in logical sequences

## Status Tracking (Optional)

While the studies edge itself doesn't track status, associated metadata could include:

- **Status:** not-started, in-progress, completed
- **Started:** timestamp when study began
- **Completed:** timestamp when study finished
- **Progress:** percentage complete or steps completed

(These would be in an extended studies edge if status tracking is needed)

## Examples

**Student Studying Module:**
```yaml
# Student actively engaged in module
source: v:student:knowledge-complex-learner
target: v:learning-module:simplicial-complex-fundamentals
# Student is working through this module
```

**Student Completed Module:**
```yaml
# Student has finished module
source: v:student:alice-researcher
target: v:learning-module:verification-fundamentals
# Completion led to acquiring new skills
```

**Syllabus Sequence:**
```yaml
# Student studies modules in syllabus order
source: v:student:knowledge-complex-learner
target: v:learning-module:fundamentals
# THEN (after completion):
source: v:student:knowledge-complex-learner
target: v:learning-module:intermediate-topics
# Sequential progression through syllabus
```

## Participation in Faces

studies edges participate in **prerequisite faces** indirectly:

```yaml
type: face/prerequisite
vertices:
  - v:student:<student-name>          # has-skill edge source, studies edge source
  - v:skill:<skill-name>              # has-skill target, requires-skill target
  - v:learning-module:<module-name>   # studies edge target, requires-skill source
```

The prerequisite face validates that the student can study the module:
- Student **has** prerequisite skill (has-skill edge)
- Module **requires** that skill (requires-skill edge)
- Student **studies** module (studies edge is valid)

## Constraints

- Source MUST be a student vertex (v:student:*)
- Target MUST be a learning-module vertex (v:learning-module:*)
- Each student-module pair may have multiple studies edges (if tracking attempts) OR one edge (if tracking single engagement)
- Module must be defined (learning-module vertex should exist)
- Student must be defined (student vertex should exist)
- **Prerequisite check:** Ideally, prerequisite faces should exist validating student has required skills

## Prerequisite Validation

**Invalid Study (Missing Prerequisite):**
```
Student: knowledge-complex-learner
  has-skill: [none]  # No skills yet

Module: advanced-chart-design
  requires-skill: chart-creation
  requires-skill: type-system-understanding

studies edge: knowledge-complex-learner → advanced-chart-design
❌ INVALID - student lacks prerequisites!
```

**Valid Study (Prerequisites Satisfied):**
```
Student: knowledge-complex-learner
  has-skill: chart-creation
  has-skill: type-system-understanding

Module: advanced-chart-design
  requires-skill: chart-creation
  requires-skill: type-system-understanding

studies edge: knowledge-complex-learner → advanced-chart-design
✅ VALID - all prerequisites satisfied
```

## Learning Progression

Studies edges enable tracking learning progression:

```
Time 0: Student studies Module A (foundational, no prerequisites)
  ↓
Time 1: Student completes Module A, gains Skill X (has-skill edge created)
  ↓
Time 2: Student studies Module B (requires Skill X - prerequisite satisfied)
  ↓
Time 3: Student completes Module B, gains Skill Y (has-skill edge created)
  ↓
...progression continues
```

## Verification

This edge can be verified using:

```bash
python scripts/verify_template_based.py 01_edges/<edge-file>.md --templates templates
```

---

**Note:** This template defines the studies relationship between students and learning modules. Studies edges indicate learning engagement and should ideally be validated by prerequisite faces ensuring students have required skills before studying modules.
