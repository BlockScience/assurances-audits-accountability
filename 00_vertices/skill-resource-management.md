---
type: vertex/skill
extends: vertex/property
id: v:skill:resource-management
name: Resource Management
description: Understanding management charts with resource, function, and team vertices for modeling organizational resource flows and operational dependencies
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

# Resource Management

## Purpose

This skill defines the capability to design and analyze management charts that model organizational resource flows. It represents mastery of extending the coordination type system with resource and function vertices, creating flow-specific edges, and building concrete management charts that reveal cross-team dependencies.

## Property Definition

A **resource management** understanding is a learnable capability encompassing:
- **Resource vertices:** Things that flow between functions (GUI, API, database, etc.)
- **Function vertices:** Operations with inputs and outputs that transform resources
- **Operates edge:** (team→function) with exactly 1 team per function constraint
- **Produces edge:** (function→resource) representing output
- **Consumes edge:** (function→resource) representing input
- **Resource dependency faces:** Capturing how resource flows cut across team boundaries
- **Tangled topology:** Understanding how input/output dependencies create rich structures
- **Peer team relationships:** Recognizing when teams have mutual dependencies

This skill is abstract until possessed by an actor (student), at which point it represents concrete knowledge and capability.

## Acquisition

This skill is **learned** through study and practice:
- Completing the [[v:learning-module:resource-management]] module
- Creating resource and function vertex types
- Defining operates, produces, consumes edges with proper semantics
- Defining resource dependency faces with correct boundary constraints
- Building a concrete management chart with 2 teams, 3 functions, 3 resources
- Visualizing and interpreting resource flow topology
- Identifying where resource dependencies cut across team boundaries

## Applicable Actors

This skill can be possessed by:
- **`vertex/student`**: Students engaged in knowledge complex education
- **`vertex/actor`**: Any actor learning about organizational resource flows and operational modeling

Rationale: This is a learnable capability appropriate for any actor who understands coordination charts and needs to model resource flows between organizational functions.

## Learning Outcomes

After acquiring this skill, a learner can:

1. **Create resource vertices** (define resources that flow between functions)
2. **Create function vertices** (define operations with inputs and outputs)
3. **Define operates edges** (team→function with 1:1 constraint)
4. **Define produces edges** (function→resource outputs)
5. **Define consumes edges** (function→resource inputs)
6. **Define resource dependency faces** (capture cross-team resource flows)
7. **Build management charts** (model teams, functions, resources with proper topology)
8. **Identify peer relationships** (recognize mutual team dependencies)
9. **Visualize resource flows** (generate and interpret management chart topology)

## Prerequisite Skills

**Required:**
- [[v:skill:team-coordination]] - Must understand coordination charts before adding resource flows

**Background (helpful but not required):**
- Experience with data flow diagrams
- Understanding of supply chain or production processes
- Familiarity with input-output modeling

## Enables

Possessing this skill enables:

- **Resource flow modeling**: Can represent how resources move through an organization
- **Dependency analysis**: Can identify critical resource dependencies between teams
- **Operational architecture**: Can design function-resource topologies
- **Cross-team visibility**: Can reveal where team boundaries are bridged by resource flows
- **Organizational topology preparation**: Foundation for Hodge analysis in Module 10

## Assessment Methods

Skill possession can be assessed through:

1. **Vertex Creation:** Create resource and function vertex types with spec-guidance pairs
2. **Edge Definition:** Define operates, produces, consumes edges with correct semantics
3. **Face Definition:** Define resource dependency face with proper boundary constraints
4. **Management Chart:** Build chart with 2 teams, 3 functions, 3 resources
5. **Constraint Validation:** Verify exactly 1 team operates each function
6. **Dependency Analysis:** Identify resource flows that cross team boundaries
7. **Peer Recognition:** Identify mutual dependencies between teams
8. **Visualization:** Generate and interpret management chart topology

**Standard:** 80% accuracy on exercises and assessments demonstrates skill possession.

## Examples

**Students possessing this skill:**
- `v:student:management-architect` - Has completed resource-management module

**Usage in prerequisite faces:**
```yaml
type: face/prerequisite
vertices:
  - v:student:coordination-architect  # has team-coordination skill
  - v:skill:team-coordination  # prerequisite
  - v:learning-module:resource-management  # requires this skill
```

**Usage in skill-gain faces:**
```yaml
type: face/skill-gain
vertices:
  - v:student:management-architect  # possesses this skill after completion
  - v:learning-module:resource-management  # develops this skill
  - v:skill:resource-management  # this skill
```

## Constraints

- Must be acquired through learning (not inherent)
- Requires team-coordination as prerequisite (builds on coordination chart patterns)
- Cannot be possessed without completing learning process (module or equivalent study)
- Should be validated through assessment before considering possessed
- Management charts must satisfy topological constraints (proper face boundaries)

## Real-World Applications

This skill enables understanding of:

- **Supply chains**: Resource flows between production stages
- **Data pipelines**: How data moves through processing functions
- **Service architectures**: API dependencies between teams
- **Production systems**: Input-output relationships in manufacturing
- **Cross-functional dependencies**: Where team coordination is required

---

**Note:** This skill is the second of three organizational modeling skills (team-coordination → resource-management → organizational-design-analysis). It adds resource flow modeling on top of team coordination, preparing for the capstone Module 10 where charts are composed and analyzed with Hodge decomposition.
