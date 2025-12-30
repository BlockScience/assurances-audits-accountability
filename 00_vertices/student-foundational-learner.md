---
type: vertex/student
extends: vertex/actor
id: v:student:foundational-learner
name: Foundational Learner
description: Student who has completed simplicial-complex-fundamentals and possesses fundamental knowledge of simplicial complexes
tags:
  - vertex
  - actor
  - student
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
domain: knowledge-complexes
---

# Foundational Learner

## Purpose

This student represents a learner who has completed the foundational module ([[v:learning-module:simplicial-complex-fundamentals]]) and now possesses [[v:skill:simplicial-complex-fundamentals]]. This is the first learning state transition in the knowledge complex educational journey.

## Actor Identity

The Foundational Learner is a student who has progressed from the initial beginner state ([[v:student:knowledge-complex-learner]]) by completing the first learning module. This learner now has concrete understanding of simplicial complex topology and can progress to intermediate modules that require this foundation.

This is a **learning state vertex** - a snapshot of student skill accumulation after completing specific module(s), not a specific individual person.

## Capabilities

- **Learn systematically**: Can progress through structured learning modules building on prerequisites
- **Possess and acquire skills**: Has acquired simplicial-complex-fundamentals skill through module completion
- **Study learning modules**: Can engage with intermediate modules that require foundational knowledge
- **Participate in learning paths**: Can follow syllabus sequences requiring foundational prerequisites

## Properties

- **Skills (`vertex/skill`)**: Possesses simplicial-complex-fundamentals
- **Learning status**: Has completed simplicial-complex-fundamentals module
- **Proficiency levels**: Beginner level with foundational knowledge

## Learning Context

This student has completed the first module in the knowledge complex learning journey and is prepared for intermediate topics. The learner understands:

- **Simplicial complex topology**: Vertices, edges, faces as knowledge structures
- **Euler characteristic**: χ = V - E + F formula and topological interpretation
- **Chart documents**: Can read and understand knowledge complex charts

The learner is ready to study:
- Verification and validation patterns
- Chart creation and design
- Advanced topological concepts

## Prerequisite Skills

**Possessed Skills:**
- **[[v:skill:simplicial-complex-fundamentals]]**: Understanding of vertices, edges, faces, and Euler characteristic

**Acquisition:** Gained through completing [[v:learning-module:simplicial-complex-fundamentals]]

## Learning Goals

The Foundational Learner aims to acquire additional skills through further study:

- **[[v:skill:verification-patterns]]**: Understanding template-based verification (requires foundational knowledge)
- **[[v:skill:chart-creation]]**: Creating custom charts for knowledge domains
- **[[v:skill:validation-patterns]]**: Human review and quality assessment processes

## Examples

This learning state can be instantiated as:

- **Any student after completing simplicial-complex-fundamentals**: Generic progression from knowledge-complex-learner
- **First milestone in syllabus**: Students reach this state before branching to different intermediate paths
- **Prerequisite state for intermediate modules**: Required starting point for modules needing foundational knowledge

## Relationships

This student participates in the following relationship patterns:

### has-skill Edges

```yaml
# Student possesses foundational skill
type: edge/has-skill
source: v:student:foundational-learner
target: v:skill:simplicial-complex-fundamentals
```

### studies Edges

```yaml
# Student can study intermediate modules
type: edge/studies
source: v:student:foundational-learner
target: v:learning-module:verification-fundamentals
```

### transitions-to Edge (from previous state)

```yaml
# Transition from beginner to foundational learner
type: edge/transitions-to
source: v:student:knowledge-complex-learner
target: v:student:foundational-learner
```

### completion Face (how this state was reached)

```yaml
# Completion of foundational module created this state
type: face/completion
vertices:
  - v:student:knowledge-complex-learner  # initial state (no skills)
  - v:learning-module:simplicial-complex-fundamentals  # completed module
  - v:student:foundational-learner  # resulting state (has skill)
```

### prerequisite Faces

```yaml
# Student with foundational skill can study intermediate modules
type: face/prerequisite
vertices:
  - v:student:foundational-learner
  - v:skill:simplicial-complex-fundamentals
  - v:learning-module:verification-fundamentals
```

## Constraints

- Must have completed simplicial-complex-fundamentals module (or equivalent)
- Must possess simplicial-complex-fundamentals skill (validated by completion face)
- Represents discrete learning state (skill set snapshot), not individual person
- Skills are supermodular (this state has all skills from previous state PLUS new skills)

## Skill Accumulation

**Skill set computation:**
```
knowledge-complex-learner.skills = {} (empty set)
simplicial-complex-fundamentals.develops = {simplicial-complex-fundamentals}

foundational-learner.skills = {} ∪ {simplicial-complex-fundamentals}
                              = {simplicial-complex-fundamentals}

Cardinality: |foundational-learner.skills| = 1 >= |knowledge-complex-learner.skills| = 0 ✓
```

---

**Note:** This student represents the first learning state transition in the knowledge complex educational journey. It demonstrates skill accumulation through module completion following the completion face pattern (student-before, module, student-after).
