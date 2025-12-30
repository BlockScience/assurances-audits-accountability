---
type: vertex/student
extends: vertex/actor
id: v:student:coordination-architect
name: Coordination Architect
description: Student who has completed Module 08 (team-coordination) and can design coordination charts modeling organizational responsibility structures
tags:
  - vertex
  - actor
  - student
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
domain: knowledge-complexes
---

# Coordination Architect

## Purpose

This student represents a learner who has completed Module 08 [[v:learning-module:team-coordination]] and can now design coordination charts that model organizational responsibility structures. This learning state builds on the document-architect foundation by adding the ability to extend the type system and create domain-specific charts for organizational modeling.

## Actor Identity

The Coordination Architect is a student who has progressed from the document-architect state ([[v:student:document-architect]]) by completing Module 08. This learner can extend the type system to create new vertex types (actor, property, team, staff, role), define coordination-specific edges and faces, and build concrete coordination charts like RACI matrices.

This is a **learning state vertex** - a snapshot of student skill accumulation after completing Module 08, not a specific individual person.

**Skill Path:** This state is reached by completing:
- Modules 01-02 (fundamentals) + Module 04-05 (verification/assurance) + Module 07 (reference-reuse) + Module 08 (team-coordination)
- Optional: Module 03 (composition) and/or Module 06 (document-composition)

## Capabilities

- **Learn systematically**: Has completed learning journey through Module 08
- **Possess and acquire skills**: Has acquired 6-8 skills through module completion (cumulative)
- **Extend type system**: Can create new vertex types by extending actor and property
- **Design coordination charts**: Can architect charts with staff, team, role vertices
- **Define domain edges**: Can create member, qualified, includes edges with proper semantics
- **Define domain faces**: Can create assignment faces with correct boundary constraints
- **Build RACI charts**: Can model responsibility matrices with role constraints
- **Visualize organizations**: Can generate and interpret coordination chart topology
- **Maintain registries**: Can commit new type definitions to documentation registry

## Properties

- **Skills (`vertex/skill`)**: Possesses 6-8 skills depending on path taken
  - **Core (5 skills minimum)**: simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation, assurance-audits, reference-reuse
  - **Module 08 skill**: team-coordination
  - **Optional from Module 03**: composing-typed-simplicial-complexes
  - **Optional from Module 06**: document-composition
- **Learning status**: Has completed Module 08 (team-coordination)
- **Proficiency levels**: Advanced level with organizational modeling capability

## Learning Context

This student has completed 6+ modules in the knowledge complex learning journey. The learner understands all previous concepts PLUS:

**From Module 08 (team coordination):**
- Type extension: Creating actor and property base vertex types
- Subtype creation: Team and staff extending actor, role extending property
- Coordination edges: member (staff→team), qualified (staff→role), includes (team→role)
- Assignment faces: (staff, role, team) with boundary edge requirements
- Coordination chart type: Charts restricted to staff, team, role vertices
- RACI pattern: Modeling responsibility with 4 role types
- Constraint enforcement: Exactly 1 accountable per team
- Topological visibility: Using chart structure to reveal coordination patterns
- Registry commit: Adding new types following established patterns

## Prerequisite Skills

**Possessed Skills (minimum path):**
- **[[v:skill:simplicial-complex-fundamentals]]**: Understanding of vertices, edges, faces, and Euler characteristic
- **[[v:skill:typed-simplicial-complexes]]**: Understanding of semantic types and type-driven constraints
- **[[v:skill:verification-validation]]**: Understanding of structural verification and qualitative validation
- **[[v:skill:assurance-audits]]**: Understanding of assurance triangles and network auditing
- **[[v:skill:reference-reuse]]**: Understanding of doc-kit pattern and registry maintenance
- **[[v:skill:team-coordination]]**: Understanding of coordination charts and organizational modeling

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
→ **coordination-architect** (6 skills minimum)

## Learning Goals

The Coordination Architect is prepared for:

- **Module 09**: Resource management (adding resource, function vertices and flow modeling)
- **Module 10**: Organizational topology analysis (composing charts, Hodge decomposition)
- **Advanced application**: Domain-specific coordination chart design

## Examples

This learning state can be instantiated as:

- **Students completing Module 08**: Those who completed team-coordination after reference-reuse
- **Minimum path students**: 6 skills (skipped Modules 03 and 06)
- **Full path students**: 8 skills (completed all modules 01-08)

## Relationships

This student participates in the following relationship patterns:

### has-skill Edges (6-8 depending on path)

```yaml
# Core skills (all paths)
type: edge/has-skill
source: v:student:coordination-architect
target: v:skill:simplicial-complex-fundamentals

type: edge/has-skill
source: v:student:coordination-architect
target: v:skill:typed-simplicial-complexes

type: edge/has-skill
source: v:student:coordination-architect
target: v:skill:verification-validation

type: edge/has-skill
source: v:student:coordination-architect
target: v:skill:assurance-audits

type: edge/has-skill
source: v:student:coordination-architect
target: v:skill:reference-reuse

type: edge/has-skill
source: v:student:coordination-architect
target: v:skill:team-coordination

# Optional skills (Module 03)
type: edge/has-skill
source: v:student:coordination-architect
target: v:skill:composing-typed-simplicial-complexes

# Optional skills (Module 06)
type: edge/has-skill
source: v:student:coordination-architect
target: v:skill:document-composition
```

### transitions-to Edges (from previous state)

```yaml
# Transition from document-architect to coordination-architect
type: edge/transitions-to
source: v:student:document-architect
target: v:student:coordination-architect
```

### completion Faces (how this state was reached)

```yaml
# Completion of Module 08
type: face/completion
vertices:
  - v:student:document-architect  # initial state (5-7 skills)
  - v:learning-module:team-coordination  # completed module
  - v:student:coordination-architect  # resulting state (6-8 skills)
```

### skill-gain Faces

```yaml
# Student gained team-coordination skill
type: face/skill-gain
vertices:
  - v:student:coordination-architect  # possesses team-coordination skill
  - v:learning-module:team-coordination  # developed skill
  - v:skill:team-coordination  # the skill gained
```

## Constraints

- Must have completed Module 08 (team-coordination)
- Must possess at minimum: simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation, assurance-audits, reference-reuse, team-coordination
- Represents discrete learning state (skill set snapshot), not individual person
- Skills are supermodular (this state has all skills from previous state PLUS new skills)
- Skill set varies based on optional modules taken (6-8 skills total)

## Skill Accumulation

**Skill set computation (minimum path):**
```
document-architect.skills = {
  simplicial-complex-fundamentals,
  typed-simplicial-complexes,
  verification-validation,
  assurance-audits,
  reference-reuse
}
team-coordination.develops = {team-coordination}

coordination-architect.skills = {
  simplicial-complex-fundamentals,
  typed-simplicial-complexes,
  verification-validation,
  assurance-audits,
  reference-reuse,
  team-coordination
}

Cardinality: |coordination-architect.skills| = 6 >= |document-architect.skills| = 5 ✓
Supermodular: coordination-architect.skills ⊇ document-architect.skills ✓
```

**Skill set computation (full path with Modules 03 and 06):**
```
coordination-architect.skills (full) = {
  simplicial-complex-fundamentals,
  typed-simplicial-complexes,
  composing-typed-simplicial-complexes,
  verification-validation,
  assurance-audits,
  document-composition,
  reference-reuse,
  team-coordination
}

Cardinality: |coordination-architect.skills| = 8 (if took all modules 01-08)
```

---

**Note:** This student represents the first organizational modeling learning state. It demonstrates extension of document architecture capabilities into domain-specific organizational modeling. Students can proceed to Module 09 (resource-management) to add resource flow analysis, building toward the chief-engineer terminal state in Module 10.
