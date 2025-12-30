---
type: vertex/student
extends: vertex/actor
id: v:student:management-architect
name: Management Architect
description: Student who has completed Module 09 (resource-management) and can design management charts modeling organizational resource flows
tags:
  - vertex
  - actor
  - student
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
domain: knowledge-complexes
---

# Management Architect

## Purpose

This student represents a learner who has completed Module 09 [[v:learning-module:resource-management]] and can now design management charts that model organizational resource flows. This learning state builds on coordination-architect by adding the ability to model functions, resources, and their flow relationships across teams.

## Actor Identity

The Management Architect is a student who has progressed from the coordination-architect state ([[v:student:coordination-architect]]) by completing Module 09. This learner can create resource and function vertex types, define flow edges (operates, produces, consumes), and build management charts that reveal cross-team resource dependencies and peer relationships.

This is a **learning state vertex** - a snapshot of student skill accumulation after completing Module 09, not a specific individual person.

**Skill Path:** This state is reached by completing:
- Modules 01-02 (fundamentals) + Module 04-05 (verification/assurance) + Module 07 (reference-reuse) + Module 08 (team-coordination) + Module 09 (resource-management)
- Optional: Module 03 (composition) and/or Module 06 (document-composition)

## Capabilities

- **Learn systematically**: Has completed learning journey through Module 09
- **Possess and acquire skills**: Has acquired 7-9 skills through module completion (cumulative)
- **Model resource flows**: Can create resource and function vertices
- **Define flow edges**: Can create operates, produces, consumes edges
- **Build management charts**: Can architect charts with teams, functions, resources
- **Identify dependencies**: Can find resource flows that cross team boundaries
- **Recognize peer relationships**: Can identify mutual dependencies between teams
- **Visualize operations**: Can generate and interpret management chart topology
- **All previous capabilities**: Type extension, coordination charts, doc-kits, assurance, etc.

## Properties

- **Skills (`vertex/skill`)**: Possesses 7-9 skills depending on path taken
  - **Core (6 skills minimum)**: simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation, assurance-audits, reference-reuse, team-coordination
  - **Module 09 skill**: resource-management
  - **Optional from Module 03**: composing-typed-simplicial-complexes
  - **Optional from Module 06**: document-composition
- **Learning status**: Has completed Module 09 (resource-management)
- **Proficiency levels**: Advanced level with operational modeling capability

## Learning Context

This student has completed 7+ modules in the knowledge complex learning journey. The learner understands all previous concepts PLUS:

**From Module 09 (resource management):**
- Resource vertices: Things that flow between functions
- Function vertices: Operations with inputs and outputs
- Operates edge: (team→function) with 1:1 constraint
- Produces edge: (function→resource) for outputs
- Consumes edge: (function→resource) for inputs
- Resource dependency faces: Cross-team resource flow representations
- Tangled topology: How mutual dependencies create rich structures
- Peer relationships: Teams that depend on each other's outputs
- Management chart type: Charts with teams, functions, resources

## Prerequisite Skills

**Possessed Skills (minimum path):**
- **[[v:skill:simplicial-complex-fundamentals]]**: Understanding of vertices, edges, faces, and Euler characteristic
- **[[v:skill:typed-simplicial-complexes]]**: Understanding of semantic types and type-driven constraints
- **[[v:skill:verification-validation]]**: Understanding of structural verification and qualitative validation
- **[[v:skill:assurance-audits]]**: Understanding of assurance triangles and network auditing
- **[[v:skill:reference-reuse]]**: Understanding of doc-kit pattern and registry maintenance
- **[[v:skill:team-coordination]]**: Understanding of coordination charts and organizational modeling
- **[[v:skill:resource-management]]**: Understanding of management charts and resource flows

**Additional Skills (optional paths):**
- **[[v:skill:composing-typed-simplicial-complexes]]**: From Module 03 (required for Module 10)
- **[[v:skill:document-composition]]**: From Module 06

**Acquisition Path (critical):**
1. Module 01 → simplicial-complex-fundamentals
2. Module 02 → typed-simplicial-complexes
3. Module 04 → verification-validation
4. Module 05 → assurance-audits
5. Module 07 → reference-reuse
6. Module 08 → team-coordination
7. Module 09 → resource-management
→ **management-architect** (7 skills minimum)

## Learning Goals

The Management Architect is prepared for:

- **Module 10**: Organizational topology analysis (composing charts, Hodge decomposition)
- **Advanced application**: Domain-specific management chart design
- **Chief Engineer terminal state**: Final learning destination

## Examples

This learning state can be instantiated as:

- **Students completing Module 09**: Those who completed resource-management after team-coordination
- **Minimum path students**: 7 skills (skipped Modules 03 and 06)
- **Full path students**: 9 skills (completed all modules 01-09)

## Relationships

This student participates in the following relationship patterns:

### has-skill Edges (7-9 depending on path)

```yaml
# Core skills (all paths)
type: edge/has-skill
source: v:student:management-architect
target: v:skill:simplicial-complex-fundamentals

type: edge/has-skill
source: v:student:management-architect
target: v:skill:typed-simplicial-complexes

type: edge/has-skill
source: v:student:management-architect
target: v:skill:verification-validation

type: edge/has-skill
source: v:student:management-architect
target: v:skill:assurance-audits

type: edge/has-skill
source: v:student:management-architect
target: v:skill:reference-reuse

type: edge/has-skill
source: v:student:management-architect
target: v:skill:team-coordination

type: edge/has-skill
source: v:student:management-architect
target: v:skill:resource-management

# Optional skills (Module 03)
type: edge/has-skill
source: v:student:management-architect
target: v:skill:composing-typed-simplicial-complexes

# Optional skills (Module 06)
type: edge/has-skill
source: v:student:management-architect
target: v:skill:document-composition
```

### transitions-to Edges (from previous state)

```yaml
# Transition from coordination-architect to management-architect
type: edge/transitions-to
source: v:student:coordination-architect
target: v:student:management-architect
```

### completion Faces (how this state was reached)

```yaml
# Completion of Module 09
type: face/completion
vertices:
  - v:student:coordination-architect  # initial state (6-8 skills)
  - v:learning-module:resource-management  # completed module
  - v:student:management-architect  # resulting state (7-9 skills)
```

### skill-gain Faces

```yaml
# Student gained resource-management skill
type: face/skill-gain
vertices:
  - v:student:management-architect  # possesses resource-management skill
  - v:learning-module:resource-management  # developed skill
  - v:skill:resource-management  # the skill gained
```

## Constraints

- Must have completed Module 09 (resource-management)
- Must possess at minimum: simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation, assurance-audits, reference-reuse, team-coordination, resource-management
- Represents discrete learning state (skill set snapshot), not individual person
- Skills are supermodular (this state has all skills from previous state PLUS new skills)
- Skill set varies based on optional modules taken (7-9 skills total)

## Skill Accumulation

**Skill set computation (minimum path):**
```
coordination-architect.skills = {
  simplicial-complex-fundamentals,
  typed-simplicial-complexes,
  verification-validation,
  assurance-audits,
  reference-reuse,
  team-coordination
}
resource-management.develops = {resource-management}

management-architect.skills = {
  simplicial-complex-fundamentals,
  typed-simplicial-complexes,
  verification-validation,
  assurance-audits,
  reference-reuse,
  team-coordination,
  resource-management
}

Cardinality: |management-architect.skills| = 7 >= |coordination-architect.skills| = 6 ✓
Supermodular: management-architect.skills ⊇ coordination-architect.skills ✓
```

**Skill set computation (full path with Modules 03 and 06):**
```
management-architect.skills (full) = {
  simplicial-complex-fundamentals,
  typed-simplicial-complexes,
  composing-typed-simplicial-complexes,
  verification-validation,
  assurance-audits,
  document-composition,
  reference-reuse,
  team-coordination,
  resource-management
}

Cardinality: |management-architect.skills| = 9 (if took all modules 01-09)
```

---

**Note:** This student represents the second organizational modeling learning state. It demonstrates extension of coordination capabilities into resource flow analysis. Students proceed to Module 10 (organizational-topology) to compose charts and apply Hodge analysis, reaching the chief-engineer terminal state.
