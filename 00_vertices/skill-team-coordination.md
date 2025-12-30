---
type: vertex/skill
extends: vertex/property
id: v:skill:team-coordination
name: Team Coordination
description: Understanding coordination charts with staff, team, and role vertices for modeling organizational responsibility structures like RACI
tags:
  - vertex
  - property
  - skill
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
domain: knowledge-complexes
level: advanced
---

# Team Coordination

## Purpose

This skill defines the capability to design and analyze coordination charts that model organizational responsibility structures. It represents mastery of extending the type system with actor and property subtypes, creating coordination-specific edges and faces, and building concrete coordination charts like RACI matrices.

## Property Definition

A **team coordination** understanding is a learnable capability encompassing:
- **Type extension:** Creating new vertex types by extending actor (team, staff) and property (role)
- **Coordination chart type:** Charts composed exclusively of staff, team, and role vertices
- **Coordination edges:** member (staff→team), qualified (staff→role), includes (team→role)
- **Assignment faces:** (staff, role, team) bounded by member + qualified + includes edges
- **RACI pattern:** Modeling responsibility matrices with responsible, accountable, consulted, informed roles
- **Constraint enforcement:** Exactly one accountable per team, appropriate overlap patterns
- **Topological visibility:** Using chart structure to reveal coordination patterns and resource contention

This skill is abstract until possessed by an actor (student), at which point it represents concrete knowledge and capability.

## Acquisition

This skill is **learned** through study and practice:
- Completing the [[v:learning-module:team-coordination]] module
- Extending vertex type to create actor and property subtypes
- Creating spec and guidance pairs for team, staff, and role types
- Defining coordination-specific edge types (member, qualified, includes)
- Defining assignment face type with proper boundary constraints
- Building a concrete RACI coordination chart
- Visualizing and interpreting coordination topology
- Committing new type definitions to the registry

## Applicable Actors

This skill can be possessed by:
- **`vertex/student`**: Students engaged in knowledge complex education
- **`vertex/actor`**: Any actor learning about organizational modeling and coordination structures

Rationale: This is a learnable capability appropriate for any actor who understands reference/reuse patterns and needs to model organizational responsibility structures.

## Learning Outcomes

After acquiring this skill, a learner can:

1. **Extend the type system** (create new vertex types from actor and property bases)
2. **Create spec-guidance pairs** (write compliant specs and guidances for new types)
3. **Design coordination edges** (define member, qualified, includes with proper semantics)
4. **Define assignment faces** (create faces with correct boundary edge requirements)
5. **Build RACI charts** (model responsibility matrices with 4 roles, multiple staff and teams)
6. **Enforce constraints** (exactly 1 accountable per team, appropriate overlap)
7. **Visualize coordination** (generate and interpret coordination chart visualizations)
8. **Commit to registry** (add new type definitions following established patterns)

## Prerequisite Skills

**Required:**
- [[v:skill:reference-reuse]] - Must understand doc-kit pattern for creating reusable type definitions

**Background (helpful but not required):**
- Experience with RACI matrices or responsibility assignment
- Understanding of organizational structures
- Familiarity with role-based access control concepts

## Enables

Possessing this skill enables:

- **Organizational modeling**: Can represent team structures and responsibility assignments
- **Coordination analysis**: Can identify overlap, contention, and gaps in responsibility
- **Type system extension**: Can create new domain-specific vertex types
- **Chart type creation**: Can define new chart types with specific vertex constraints
- **Resource management preparation**: Foundation for adding resource/function modeling (Module 09)

## Assessment Methods

Skill possession can be assessed through:

1. **Type Extension:** Create actor and property vertex types with spec-guidance pairs
2. **Subtype Creation:** Create team, staff, role subtypes with proper inheritance
3. **Edge Definition:** Define member, qualified, includes edges with correct semantics
4. **Face Definition:** Define assignment face with proper boundary constraints
5. **RACI Chart:** Build coordination chart with 4 roles, 5 staff, 2 teams
6. **Constraint Validation:** Verify exactly 1 accountable per team
7. **Visualization:** Generate and interpret coordination chart topology
8. **Registry Commit:** Add new types to registry following patterns

**Standard:** 80% accuracy on exercises and assessments demonstrates skill possession.

## Examples

**Students possessing this skill:**
- `v:student:coordination-architect` - Has completed team-coordination module

**Usage in prerequisite faces:**
```yaml
type: face/prerequisite
vertices:
  - v:student:document-architect  # has reference-reuse skill
  - v:skill:reference-reuse  # prerequisite
  - v:learning-module:team-coordination  # requires this skill
```

**Usage in skill-gain faces:**
```yaml
type: face/skill-gain
vertices:
  - v:student:coordination-architect  # possesses this skill after completion
  - v:learning-module:team-coordination  # develops this skill
  - v:skill:team-coordination  # this skill
```

## Constraints

- Must be acquired through learning (not inherent)
- Requires reference-reuse as prerequisite (builds on type extension patterns)
- Cannot be possessed without completing learning process (module or equivalent study)
- Should be validated through assessment before considering possessed
- Coordination charts must satisfy topological constraints (proper face boundaries)

## Real-World Applications

This skill enables understanding of:

- **RACI matrices**: Responsibility assignment in project management
- **RACI matrices**: Responsibility assignment in project management
- **Organizational charts**: Team structures and reporting relationships
- **Role-based systems**: Access control and permission modeling
- **Resource allocation**: Understanding who does what across teams
- **Coordination overhead**: Visualizing where coordination complexity concentrates

---

**Note:** This skill is the first of three organizational modeling skills (team-coordination → resource-management → organizational-design-analysis). It establishes the foundation for modeling people, teams, and responsibilities before adding resource flows in Module 09.
