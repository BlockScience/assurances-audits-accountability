---
type: edge/has-skill
source: v:student:<student-name>
target: v:skill:<skill-name>
source_type: vertex/student
target_type: vertex/skill
orientation: directed
id: e:has-skill:<student-name>:<skill-name>
name: <student-name> has skill <skill-name>
description: <student-name> possesses <skill-name> capability
tags:
  - edge
  - has-skill
  - relationship
version: 1.0.0
created: <ISO-8601 datetime>
modified: <ISO-8601 datetime>
---

# <student-name> has skill <skill-name>

## Purpose

This edge represents that the student **<student-name>** possesses the skill **<skill-name>**. The has-skill relationship connects students (actors) to skills (properties), creating a concrete reference to an abstract capability.

## Relationship Type

**Edge Type:** has-skill (possession)

**Direction:** student → skill (student possesses skill)

**Participants:**
- **Source:** `v:student:<student-name>` (the student who has the skill)
- **Target:** `v:skill:<skill-name>` (the skill that is possessed)

## Meaning

This edge indicates that `<student-name>` has acquired and currently possesses `<skill-name>`. This could be:
- A prerequisite skill the student already has (enabling module study)
- A skill the student has learned (achievement during learning journey)
- A skill verified through assessment

## Property Possession Pattern

This edge follows the **property possession pattern**:

- **Property as referent (abstract):** The skill `<skill-name>` is an abstract capability definition
- **Possession as reference (concrete):** This edge creates a concrete instance where `<student-name>` possesses that skill
- The skill becomes "real" for this student through this possession relationship

## Examples

**Prerequisite Possession:**
```yaml
# Student has prerequisite skill needed for a module
source: v:student:knowledge-complex-learner
target: v:skill:simplicial-complex-fundamentals
# This enables studying modules that require this skill
```

**Acquired Skill:**
```yaml
# Student has learned a new skill
source: v:student:alice-researcher
target: v:skill:chart-creation
# This achievement unlocks new learning opportunities
```

## Participation in Faces

has-skill edges participate in **prerequisite faces**:

```yaml
type: face/prerequisite
vertices:
  - v:student:<student-name>          # has-skill edge source
  - v:skill:<skill-name>              # has-skill edge target
  - v:learning-module:<module-name>   # requires-skill edge source
```

This triangle means: **Student with skill can study module requiring that skill**

## Constraints

- Source MUST be a student vertex (v:student:*)
- Target MUST be a skill vertex (v:skill:*)
- Each student-skill pair should have at most one has-skill edge
- Skill must be defined (skill vertex should exist)
- Student must be defined (student vertex should exist)

## Verification

This edge can be verified using:

```bash
python scripts/verify_template_based.py 01_edges/<edge-file>.md --templates templates
```

---

**Note:** This template defines the has-skill relationship between students and skills. It follows the property possession pattern where the abstract skill becomes concrete through possession by a specific student.
