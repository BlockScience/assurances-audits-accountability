# Module 08: Team Coordination

**Learning Journey: Knowledge Complexes**
**Module:** 08 of 10
**Skill Developed:** Team Coordination

## Learning Goals

By the end of this module, you will be able to:

1. Extend the type system with new domain-specific vertex types
2. Create actor and property vertex hierarchies for organizational modeling
3. Define team, staff, and role vertex types with proper inheritance
4. Build edge types for team membership and qualifications
5. Construct coordination charts with assignment faces
6. Model RACI (Responsible, Accountable, Consulted, Informed) patterns

## Prerequisites

Before starting this module, you should have completed:

- **Module 07:** Reference & Reuse
- **Skills Required:** Doc-kit pattern usage, systematic document creation

You should be familiar with:
- Creating documents using doc-kit patterns
- The boundary complex and assurance structure
- Type hierarchies and inheritance in typed simplicial complexes
- Spec-guidance pairs for defining new document types

## Module Roadmap

This module begins the **organizational modeling journey** - a three-module sequence (08-09-10) that culminates in the chief-engineer terminal state.

We'll learn to:
1. Extend the type system with domain-specific types
2. Model organizational structures as typed simplicial complexes
3. Build coordination charts capturing team responsibilities
4. Apply the doc-kit patterns from Module 07 to create new types

---

## Section 1: Type Extension Fundamentals

**Time:** 60 minutes

### Why Extend Types?

The boundary complex gives us foundational types:
- `vertex/spec`, `vertex/guidance` for documentation
- `edge/verification`, `edge/validation`, `edge/coupling` for assurance
- `face/assurance` for quality testimony

But organizations need domain-specific types:
- **Actors**: Teams, staff, roles
- **Properties**: Skills, responsibilities, qualifications
- **Relationships**: Membership, assignment, qualification

Type extension lets us create these while maintaining compatibility with existing assurance infrastructure.

### Inheritance Pattern

Every extended type inherits from a base type:

```yaml
---
type: vertex/actor
extends: vertex
id: v:spec:actor
name: Spec for Actor
description: Defines actor vertices representing entities that can take action
---
```

The `extends: vertex` line creates inheritance:
- Actor vertices are vertices (satisfy all vertex requirements)
- Actor vertices have additional requirements (can take actions)
- Assurance infrastructure works for actors (inherited from vertex)

### Spec-Guidance Pairs for New Types

Creating a new type requires:

1. **Spec document** - Structural requirements for the type
2. **Guidance document** - Quality criteria for instances
3. **Coupling edge** - Pairs the spec and guidance
4. **Template** - For template-based verification

### The Actor-Property Hierarchy

We'll build a two-branch hierarchy:

```
vertex (base)
├── actor (can take action)
│   ├── team (organizational unit)
│   ├── staff (individual)
│   └── role (function)
└── property (describes actors)
    ├── skill (capability)
    ├── responsibility (duty)
    └── qualification (credential)
```

**Actors** represent entities that can act:
- Teams (Engineering, QA, Operations)
- Staff (Alice, Bob, Charlie)
- Roles (Tech Lead, QA Engineer, DevOps)

**Properties** describe actors:
- Skills (Python programming, Code review)
- Responsibilities (Deploy to production, Approve PRs)
- Qualifications (AWS Certified, PhD)

### Exercise 1.1: Examine Existing Type Extensions

**Task:** Study how chart types extend the base types.

```bash
# Look at how chart extends vertex
cat 00_vertices/spec-for-chart.md | head -50

# Compare with base vertex spec
cat 00_vertices/spec-for-spec.md | head -50
```

**Questions:**
1. What fields does chart add beyond base vertex?
2. How does inheritance work in the frontmatter?
3. What additional sections does chart spec require?
4. How would you apply this pattern to actor types?

---

## Section 2: Creating Actor Vertex Types

**Time:** 90 minutes

### Actor Base Type

First, we create the actor base type that all organizational entities inherit from.

**Spec structure (spec-for-actor.md):**
```yaml
---
type: vertex/spec
extends: vertex/doc
id: v:spec:actor
name: Spec for Actor
description: Defines actor vertices - entities that can take actions in an organization
---

# Spec for Actor

## Purpose

Actors are vertices representing entities with agency...

## Frontmatter Schema

Required fields:
- `type: vertex/actor/*` - Specific actor subtype
- `extends: vertex/actor` - Inherits from actor
- `id: v:actor:*` - Actor identifier
- `name` - Human-readable name
- `capabilities` - List of actions this actor can perform

## Body Structure

### Identity
Who or what is this actor?

### Capabilities
What can this actor do?

### Constraints
What limits this actor's agency?
```

### Team Type

Teams are actors representing organizational units.

**Key characteristics:**
- Have members (staff or sub-teams)
- Have collective responsibilities
- Can be nested (team contains sub-teams)

**Spec excerpt:**
```yaml
type: vertex/actor/team
extends: vertex/actor
members:
  - v:actor:staff:alice
  - v:actor:staff:bob
responsibilities:
  - Deploy to production
  - Maintain documentation
```

### Staff Type

Staff are actors representing individual people.

**Key characteristics:**
- Have roles (current function)
- Have qualifications (credentials)
- Have skills (capabilities)

**Spec excerpt:**
```yaml
type: vertex/actor/staff
extends: vertex/actor
name: Alice
roles:
  - v:actor:role:tech-lead
qualifications:
  - v:property:qualification:aws-certified
skills:
  - v:property:skill:python
  - v:property:skill:code-review
```

### Role Type

Roles are actors representing functions (not people).

**Key characteristics:**
- Define expected responsibilities
- Define required qualifications
- Can be held by multiple staff

**Spec excerpt:**
```yaml
type: vertex/actor/role
extends: vertex/actor
name: Tech Lead
responsibilities:
  - Code review
  - Architecture decisions
required_qualifications:
  - v:property:qualification:senior-developer
```

### Exercise 2.1: Design an Actor Hierarchy

**Task:** Design actor types for a small engineering team.

**Elements to define:**
1. One team vertex (e.g., "Platform Team")
2. Two staff vertices (team members)
3. Two role vertices (functions they perform)

**Sketch the frontmatter for each, including:**
- type and extends fields
- id and name
- Relationships (members, roles, skills)

---

## Section 3: Property Vertex Types

**Time:** 60 minutes

### Property Base Type

Properties describe actors without having agency themselves.

**Key distinction:**
- Actors DO things
- Properties DESCRIBE actors

**Property subtypes:**
- **Skill** - Capability an actor possesses
- **Responsibility** - Duty an actor must fulfill
- **Qualification** - Credential an actor holds

### Skill Type

```yaml
type: vertex/property/skill
extends: vertex/property
id: v:property:skill:code-review
name: Code Review
description: Ability to review and provide feedback on code changes
level: expert  # beginner, intermediate, expert
domain: software-engineering
```

### Responsibility Type

```yaml
type: vertex/property/responsibility
extends: vertex/property
id: v:property:responsibility:deploy-production
name: Deploy to Production
description: Responsible for production deployment decisions
scope: platform  # team, department, organization
accountability: primary  # primary, shared, supporting
```

### Qualification Type

```yaml
type: vertex/property/qualification
extends: vertex/property
id: v:property:qualification:aws-certified
name: AWS Certified Solutions Architect
description: Cloud infrastructure certification
issuer: Amazon Web Services
validity: 3 years
```

### Connecting Actors to Properties

Properties connect to actors via edges:

```
Staff --[has-skill]--> Skill
Staff --[holds-responsibility]--> Responsibility
Staff --[has-qualification]--> Qualification
Role --[requires-skill]--> Skill
Role --[requires-qualification]--> Qualification
```

### Exercise 3.1: Define Properties for Your Actors

**Task:** Create property vertices for the actors you designed in Exercise 2.1.

**Define:**
1. Two skills relevant to the team
2. Two responsibilities the team handles
3. One qualification required for a role

---

## Section 4: Coordination Edge Types

**Time:** 60 minutes

### Edges for Organizational Modeling

We need edge types to connect actors and properties:

| Edge Type | Source | Target | Meaning |
|-----------|--------|--------|---------|
| member | team | staff/team | Team membership |
| holds-role | staff | role | Current function |
| has-skill | actor | skill | Capability |
| has-qualification | staff | qualification | Credential |
| requires-skill | role | skill | Skill requirement |
| assigned | role | responsibility | Role-responsibility link |

### Member Edge

```yaml
type: edge/member
extends: edge
id: e:member:platform-team:alice
v1: v:actor:team:platform-team
v2: v:actor:staff:alice
membership_type: full-time  # full-time, part-time, contractor
start_date: 2024-01-15
```

### Holds-Role Edge

```yaml
type: edge/holds-role
extends: edge
id: e:holds-role:alice:tech-lead
v1: v:actor:staff:alice
v2: v:actor:role:tech-lead
start_date: 2024-03-01
scope: platform-team
```

### Assigned Edge

```yaml
type: edge/assigned
extends: edge
id: e:assigned:tech-lead:deploy-production
v1: v:actor:role:tech-lead
v2: v:property:responsibility:deploy-production
raci: responsible  # responsible, accountable, consulted, informed
```

### Exercise 4.1: Build Edge Structure

**Task:** Create edges connecting your actors and properties.

**Define:**
1. Member edges for team membership
2. Holds-role edges for staff functions
3. Assigned edges for role responsibilities

---

## Section 5: Building a Coordination Chart

**Time:** 90 minutes

### What is a Coordination Chart?

A **coordination chart** is a typed simplicial complex that models:
- Who is responsible for what (RACI)
- Team structure and membership
- Role qualifications and assignments

### Chart Structure

```yaml
---
type: chart/coordination
extends: chart
id: c:platform-team-coordination
name: Platform Team Coordination Chart
description: Models platform team responsibilities and assignments

elements:
  vertices:
    # Actors
    - v:actor:team:platform-team
    - v:actor:staff:alice
    - v:actor:staff:bob
    - v:actor:role:tech-lead
    - v:actor:role:engineer
    # Properties
    - v:property:responsibility:deploy-production
    - v:property:responsibility:code-review
    - v:property:skill:kubernetes

  edges:
    # Membership
    - e:member:platform-team:alice
    - e:member:platform-team:bob
    # Roles
    - e:holds-role:alice:tech-lead
    - e:holds-role:bob:engineer
    # Assignments
    - e:assigned:tech-lead:deploy-production
    - e:assigned:engineer:code-review

  faces:
    # Assignment faces (actor, role, responsibility)
    - f:assignment:alice:tech-lead:deploy-production
    - f:assignment:bob:engineer:code-review
---
```

### Assignment Faces

Assignment faces are triangles that link:
- A staff member
- Their role
- A responsibility

```
         alice
          /\
         /  \
  member/    \holds-role
       /      \
      /        \
platform-team   tech-lead
               /
              /assigned
             /
     deploy-production
```

The face `(alice, tech-lead, deploy-production)` represents:
- Alice holds the tech-lead role
- Tech-lead is assigned deploy-production responsibility
- Therefore Alice is responsible for deploy-production

### RACI Modeling

RACI assignments appear as face properties:

| RACI | Meaning | Face Type |
|------|---------|-----------|
| R | Responsible - Does the work | f:assignment/responsible |
| A | Accountable - Approves/owns | f:assignment/accountable |
| C | Consulted - Provides input | f:assignment/consulted |
| I | Informed - Kept up to date | f:assignment/informed |

### Exercise 5.1: Complete Your Coordination Chart

**Task:** Build a complete coordination chart for your team.

**Include:**
1. All actor vertices (team, staff, roles)
2. All property vertices (skills, responsibilities)
3. All connecting edges (member, holds-role, assigned)
4. Assignment faces with RACI types

**Verify:**
```bash
python scripts/verify_chart.py your-chart.md --root .
python scripts/topology.py your-chart.md --root .
```

---

## Summary

### Key Takeaways

1. **Type Extension Creates Domain-Specific Types**
   - Inherit from base types (vertex, edge, face)
   - Add domain-specific fields and requirements
   - Maintain compatibility with assurance infrastructure

2. **Actor-Property Hierarchy Models Organizations**
   - Actors: team, staff, role (have agency)
   - Properties: skill, responsibility, qualification (describe actors)
   - Clear separation enables systematic modeling

3. **Edges Connect Actors and Properties**
   - member, holds-role for team structure
   - has-skill, has-qualification for capabilities
   - assigned for responsibility allocation

4. **Coordination Charts Capture RACI**
   - Assignment faces link staff-role-responsibility
   - RACI types on faces model accountability
   - Charts provide complete responsibility picture

5. **Doc-Kit Patterns Enable Systematic Extension**
   - Use Module 07 skills for creating new types
   - Spec-guidance pairs for each type
   - Templates for verification

### Skill Checklist

You should now be able to:

- Extend the type system with domain-specific vertex types
- Create actor and property hierarchies
- Define team, staff, and role vertices
- Build edge types for organizational relationships
- Construct coordination charts with assignment faces
- Model RACI patterns using face types

### What's Next

In **Module 09: Resource Management**, you'll learn to:

- Add resource and function vertices to organizational models
- Create flow edges (operates, produces, consumes)
- Build management charts showing resource dependencies
- Model cross-team resource flows

The coordination skills from this module prepare you for resource flow analysis.

---

## Section 6: The Learning Journey Structure

**Time:** 30 minutes

### How This Module Fits the Learning Path

This module is part of the **organizational modeling journey** (Modules 08-10). Let's examine how it fits into the typed simplicial complex that models the learning journey itself.

### Entry State: Document Architect

You enter this module as a [[v:student:document-architect]] with 5-7 skills:
- `simplicial-complex-fundamentals` (Module 01)
- `typed-simplicial-complexes` (Module 02)
- `verification-validation` (Module 04)
- `assurance-audits` (Module 05)
- `reference-reuse` (Module 07)
- Optional: `composing-typed-simplicial-complexes` (Module 03)
- Optional: `document-composition` (Module 06)

### Prerequisite Validation

The prerequisite face validates your readiness:

```
        document-architect
              /\
             /  \
  has-skill /    \ studies
           /      \
          /        \
  reference-reuse   team-coordination
           \        /
            \      /
      requires-skill
```

This triangle [[f:prerequisite:document-architect:reference-reuse:team-coordination]] validates:
- You possess the reference-reuse skill
- The module requires that skill
- Therefore you can study this module

### Exit State: Coordination Architect

After completing this module, you transition to [[v:student:coordination-architect]] with 6-8 skills:

**Skill gained:** [[v:skill:team-coordination]]

The completion face [[f:completion:document-architect:team-coordination:coordination-architect]] represents this transition:

```
    document-architect
           /\
          /  \
  studies/    \transitions-to
        /      \
       /        \
team-coordination  coordination-architect
        \        /
         \      /
          advances
```

### Skill Attribution

The skill-gain face [[f:skill-gain:coordination-architect:team-coordination:team-coordination]] shows causal attribution:

- The module [[v:learning-module:team-coordination]] develops the skill
- The student [[v:student:coordination-architect]] now possesses it
- The edge [[e:develops-skill:team-coordination:team-coordination]] connects them

### Topology of This Module's Chart

The learning journey chart for Module 08 has:
- **Vertices (V):** 5 (2 students + 2 skills + 1 module)
- **Edges (E):** 7 (has-skill, requires-skill, develops-skill, studies, transitions-to, advances, has-skill)
- **Faces (F):** 3 (prerequisite, completion, skill-gain)
- **Euler Characteristic:** χ = V - E + F = 5 - 7 + 3 = 1 ✓

See the full chart: [[c:learning-journey-module-08]]

### Exercise 6.1: Trace Your Learning Path

**Task:** Map your personal learning path through the modules.

1. List which optional modules you completed (03, 06)
2. Count your current skill total
3. Identify which prerequisite faces you've satisfied
4. Calculate how many skills you'll have after Module 10

---

## Section 7: Worked Example - Platform Team Coordination

**Time:** 45 minutes

### Scenario

Build a complete coordination chart for a Platform Team with:
- 1 team (Platform Team)
- 3 staff members (Alice, Bob, Charlie)
- 2 roles (Tech Lead, SRE)
- 3 responsibilities (Deploy, Monitor, Document)

### Step 1: Define Vertices

**Team vertex:**
```yaml
---
type: vertex/actor/team
extends: vertex/actor
id: v:actor:team:platform
name: Platform Team
description: Infrastructure and platform engineering team
members:
  - v:actor:staff:alice
  - v:actor:staff:bob
  - v:actor:staff:charlie
---
```

**Staff vertices:**
```yaml
# Alice - Tech Lead
---
type: vertex/actor/staff
extends: vertex/actor
id: v:actor:staff:alice
name: Alice
roles:
  - v:actor:role:tech-lead
---

# Bob - SRE
---
type: vertex/actor/staff
extends: vertex/actor
id: v:actor:staff:bob
name: Bob
roles:
  - v:actor:role:sre
---

# Charlie - SRE
---
type: vertex/actor/staff
extends: vertex/actor
id: v:actor:staff:charlie
name: Charlie
roles:
  - v:actor:role:sre
---
```

**Role vertices:**
```yaml
# Tech Lead role
---
type: vertex/actor/role
extends: vertex/actor
id: v:actor:role:tech-lead
name: Tech Lead
responsibilities:
  - Code review
  - Architecture decisions
  - Deployment approval
---

# SRE role
---
type: vertex/actor/role
extends: vertex/actor
id: v:actor:role:sre
name: Site Reliability Engineer
responsibilities:
  - Monitoring
  - Incident response
  - Infrastructure automation
---
```

### Step 2: Define Edges

**Member edges (3):**
```yaml
e:member:platform:alice    # Alice is member of Platform
e:member:platform:bob      # Bob is member of Platform
e:member:platform:charlie  # Charlie is member of Platform
```

**Holds-role edges (3):**
```yaml
e:holds-role:alice:tech-lead   # Alice holds Tech Lead role
e:holds-role:bob:sre           # Bob holds SRE role
e:holds-role:charlie:sre       # Charlie holds SRE role
```

**Includes edges (2):**
```yaml
e:includes:platform:tech-lead  # Platform includes Tech Lead role
e:includes:platform:sre        # Platform includes SRE role
```

### Step 3: Define Assignment Faces

**RACI assignments:**

| Staff | Role | Responsibility | RACI |
|-------|------|----------------|------|
| Alice | Tech Lead | Deploy | Accountable |
| Bob | SRE | Deploy | Responsible |
| Charlie | SRE | Monitor | Responsible |
| Alice | Tech Lead | Monitor | Consulted |
| Bob | SRE | Document | Informed |

**Face definitions:**
```yaml
f:assignment:alice:tech-lead:deploy    # type: accountable
f:assignment:bob:sre:deploy            # type: responsible
f:assignment:charlie:sre:monitor       # type: responsible
f:assignment:alice:tech-lead:monitor   # type: consulted
f:assignment:bob:sre:document          # type: informed
```

### Step 4: Verify Topology

**Count elements:**
- Vertices: 1 team + 3 staff + 2 roles + 3 responsibilities = **9 vertices**
- Edges: 3 member + 3 holds-role + 2 includes + (assignment edges) = **~12 edges**
- Faces: 5 assignment faces = **5 faces**

**Calculate Euler characteristic:**
- χ = V - E + F = 9 - 12 + 5 = 2

The χ = 2 indicates a sphere-like topology, which is expected for a well-connected coordination chart.

### Step 5: Visualize

```bash
# Export and visualize
python scripts/export_chart_direct.py charts/platform-coordination/platform-coordination.md charts/platform-coordination/platform-coordination.json --root .
python scripts/visualize_chart.py charts/platform-coordination/platform-coordination.json
```

**Expected visualization:**
- Team vertex at center
- Staff vertices around it (connected by member edges)
- Role vertices nearby (connected by holds-role and includes)
- Responsibility vertices (connected by assigned edges)
- Triangular faces showing complete RACI assignments

---

## Self-Assessment

### Concept Check

Answer these questions to verify your understanding:

**Level 1: Recall**
1. What is the difference between an actor and a property?
2. Name the three actor subtypes introduced in this module.
3. What does the `extends` field in YAML frontmatter do?
4. What three boundary edges does an assignment face require?

**Level 2: Understanding**
5. Why do we separate actors (who do things) from properties (descriptions)?
6. How does type inheritance enable reuse of assurance infrastructure?
7. What organizational relationship does a member edge represent?
8. Why must exactly one person be Accountable in RACI?

**Level 3: Application**
9. Given a new organization type (e.g., "Committee"), which base type would it extend?
10. Design the edges needed to model "Staff reports to Manager" relationship.
11. How would you modify the coordination chart to add a third team?
12. What topology change would you expect if two teams share some staff?

**Level 4: Analysis**
13. Analyze what happens to the Euler characteristic when you add a new assignment face.
14. Compare the coordination chart to the boundary complex - what patterns are similar?
15. How could you detect "missing accountability" from the chart topology?
16. What would a cycle in the member edges indicate about the organization?

### Practical Skills Verification

Complete these tasks to demonstrate skill acquisition:

- [ ] Created actor vertex type extending vertex
- [ ] Created property vertex type extending vertex
- [ ] Created team, staff, role subtypes
- [ ] Defined member, holds-role, includes edges
- [ ] Defined assignment face with boundary constraints
- [ ] Built complete RACI chart with multiple teams
- [ ] Verified chart passes topology checks
- [ ] Generated and interpreted visualization

---

## Assessment

### Final Exercise: Complete Coordination Chart

**Task:** Build a complete coordination chart for a 3-person team.

**Requirements:**

1. **Vertices** (40 points)
   - 1 team vertex
   - 3 staff vertices
   - 2 role vertices
   - 3 responsibility vertices
   - 2 skill vertices

2. **Edges** (30 points)
   - Member edges for all staff
   - Holds-role edges for role assignments
   - Assigned edges for responsibilities
   - Has-skill edges for capabilities

3. **Faces** (20 points)
   - Assignment faces with RACI types
   - At least 4 assignment faces

4. **Verification** (10 points)
   - Chart passes verify_chart.py
   - Topology is valid (χ = 1)

**Deliverables:**
- Chart file in `charts/your-coordination/`
- Brief write-up (150-200 words) explaining the team structure

---

## Additional Resources

### Scripts Reference

```bash
# Verify chart structure
python scripts/verify_chart.py charts/<chart>/<chart>.md --root .

# Analyze topology
python scripts/topology.py charts/<chart>/<chart>.md --root .

# Export for visualization
python scripts/export_chart_direct.py charts/<chart>/<chart>.md charts/<chart>/<chart>.json --root .
```

### Key Concepts for Review

1. **Type Extension**: Adding domain-specific types via inheritance
2. **Actor Types**: team, staff, role - entities with agency
3. **Property Types**: skill, responsibility, qualification - descriptions
4. **Coordination Edge Types**: member, holds-role, assigned, has-skill
5. **Assignment Faces**: Triangles linking staff-role-responsibility
6. **RACI**: Responsible, Accountable, Consulted, Informed patterns

---

**Module 08 Complete**

You've learned how to extend the type system for organizational modeling, create actor and property hierarchies, and build coordination charts with RACI assignment patterns. This prepares you for resource flow modeling in Module 09.
