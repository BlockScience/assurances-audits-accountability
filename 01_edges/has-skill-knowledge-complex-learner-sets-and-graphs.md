---
type: edge/has-skill
source: v:student:knowledge-complex-learner
target: v:skill:sets-and-graphs
source_type: vertex/student
target_type: vertex/skill
orientation: directed
id: e:has-skill:knowledge-complex-learner:sets-and-graphs
name: knowledge-complex-learner has skill sets-and-graphs
description: knowledge-complex-learner possesses sets-and-graphs capability
tags:
  - edge
  - has-skill
  - relationship
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# knowledge-complex-learner has skill sets-and-graphs

## Purpose

This edge represents that the student **knowledge-complex-learner** possesses the skill **sets-and-graphs**. This is an entry prerequisite - the student arrives with this skill before beginning knowledge complex education.

## Relationship Type

**Edge Type:** has-skill (possession)

**Direction:** student → skill (student possesses skill)

**Participants:**
- **Source:** `v:student:knowledge-complex-learner` (the student who has the skill)
- **Target:** `v:skill:sets-and-graphs` (the skill that is possessed)

## Meaning

This edge indicates that `knowledge-complex-learner` has acquired `sets-and-graphs` prior to beginning knowledge complex studies. This is an **entry prerequisite** from general computer science background.

## Property Possession Pattern

This edge follows the **property possession pattern**:
- **Property as referent (abstract):** The skill `sets-and-graphs` is an abstract capability definition
- **Possession as reference (concrete):** This edge creates a concrete instance where knowledge-complex-learner possesses that skill

## Participation in Faces

This has-skill edge participates in **prerequisite face**:

```yaml
type: face/prerequisite
vertices:
  - v:student:knowledge-complex-learner  # has-skill edge source
  - v:skill:sets-and-graphs  # has-skill edge target
  - v:learning-module:simplicial-complex-fundamentals  # requires this skill
```

This triangle validates that student with this prerequisite skill can study the module.

---

**Note:** Entry prerequisite skill possessed before beginning curriculum.
