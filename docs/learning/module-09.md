# Module 09: Resource Management

**Learning Journey: Knowledge Complexes**
**Module:** 09 of 10
**Skill Developed:** Resource Management

## Learning Goals

By the end of this module, you will be able to:

1. Create resource and function vertex types for operational modeling
2. Define flow edges: operates, produces, consumes
3. Build management charts showing resource dependencies
4. Model cross-team resource flows and dependencies
5. Identify critical resource paths and bottlenecks
6. Compare coordination charts vs management charts

## Prerequisites

Before starting this module, you should have completed:

- **Module 08:** Team Coordination
- **Skills Required:** Type extension, coordination chart construction, actor-property modeling

You should be familiar with:
- Extending the type system with domain-specific types
- Building coordination charts with assignment faces
- Actor (team, staff, role) and property (skill, responsibility) types
- RACI patterns for responsibility modeling

## Module Roadmap

This module adds **operational structure** to the organizational models from Module 08.

Coordination charts answer "who is responsible for what."
Management charts answer "what resources flow where."

We'll learn to:
1. Create resource and function vertex types
2. Define flow edges showing how resources move
3. Build management charts with dependency faces
4. Identify where coordination and management concerns intersect

---

## Section 1: From Coordination to Management

**Time:** 45 minutes

### Coordination vs Management

**Coordination** focuses on people and responsibilities:
- Who does what?
- Who approves what?
- Who needs to be informed?

**Management** focuses on resources and flows:
- What resources are needed?
- Where do resources come from?
- How do resources flow between teams?

### The Bridge: Teams as Shared Context

Teams appear in both charts:
- In coordination charts: teams have members and responsibilities
- In management charts: teams operate functions and consume resources

This shared vertex (team) will enable **chart composition** in Module 10.

### Why Resource Modeling Matters

Organizations fail when:
- Resource dependencies are unclear
- Bottlenecks aren't visible
- Cross-team flows aren't coordinated

Management charts make these patterns explicit.

### Exercise 1.1: Identify Resource Dependencies

**Task:** For the team you modeled in Module 08, list:

1. What resources does your team produce?
   - (e.g., deployed services, documentation, code reviews)

2. What resources does your team consume?
   - (e.g., infrastructure, API access, design specs)

3. Who provides those resources?
   - (e.g., Platform team, Security team, Design team)

---

## Section 2: Resource and Function Vertex Types

**Time:** 60 minutes

### Resource Vertex Type

Resources are things that can be produced, consumed, or transformed.

```yaml
---
type: vertex/resource
extends: vertex
id: v:resource:api-access
name: API Access
description: Authenticated access to production API
resource_type: capability  # capability, artifact, infrastructure
availability: on-demand  # on-demand, scheduled, limited
owner: v:actor:team:platform
---
```

**Resource subtypes:**
- **Capability**: Something that can be done (API access, deployment ability)
- **Artifact**: Something produced (documentation, code, reports)
- **Infrastructure**: Something hosted (servers, databases, networks)

### Function Vertex Type

Functions are operations that transform resources.

```yaml
---
type: vertex/function
extends: vertex
id: v:function:deploy-service
name: Deploy Service
description: Deploy a service to production environment
operated_by: v:actor:team:platform
inputs:
  - v:resource:tested-code
  - v:resource:deployment-config
outputs:
  - v:resource:running-service
---
```

**Key aspects:**
- Functions have inputs (consumed resources)
- Functions have outputs (produced resources)
- Functions are operated by teams or roles

### Modeling a Pipeline

Consider a deployment pipeline:

```
tested-code ─────┐
                 │
                 v
deployment-config ──> [deploy-service] ──> running-service
                           │
                           │ operated by
                           v
                      platform-team
```

**Vertices:**
- Resources: tested-code, deployment-config, running-service
- Function: deploy-service
- Actor: platform-team

### Exercise 2.1: Define Resources and Functions

**Task:** For your Module 08 team, define:

1. Two resource vertices your team produces
2. Two resource vertices your team consumes
3. One function vertex that transforms inputs to outputs

---

## Section 3: Flow Edge Types

**Time:** 60 minutes

### Three Flow Edge Types

| Edge Type | Source | Target | Meaning |
|-----------|--------|--------|---------|
| operates | actor | function | Team/role runs this function |
| produces | function | resource | Function creates this resource |
| consumes | function | resource | Function requires this resource |

### Operates Edge

Links actors to functions they perform:

```yaml
type: edge/operates
extends: edge
id: e:operates:platform:deploy-service
v1: v:actor:team:platform
v2: v:function:deploy-service
capacity: 10/day  # How often can they run this?
sla: 4 hours      # Response time commitment
```

### Produces Edge

Links functions to resources they create:

```yaml
type: edge/produces
extends: edge
id: e:produces:deploy-service:running-service
v1: v:function:deploy-service
v2: v:resource:running-service
reliability: 99.9%
latency: 15 minutes
```

### Consumes Edge

Links functions to resources they require:

```yaml
type: edge/consumes
extends: edge
id: e:consumes:deploy-service:tested-code
v1: v:function:deploy-service
v2: v:resource:tested-code
required: true  # Can function proceed without this?
blocking: true  # Does absence block the function?
```

### Complete Flow Pattern

```
platform-team ──[operates]──> deploy-service
                                   │
                    ┌──[consumes]──┤──[consumes]──┐
                    │              │              │
                    v              │              v
              tested-code          │      deployment-config
                                   │
                                   └──[produces]──> running-service
```

### Exercise 3.1: Build Flow Edges

**Task:** Create flow edges for your resources and functions.

**Define:**
1. Operates edge linking your team to your function
2. Consumes edges for each input resource
3. Produces edges for each output resource

---

## Section 4: Resource Dependency Faces

**Time:** 60 minutes

### Dependency Face Structure

Dependency faces are triangles that show resource relationships:

**Pattern 1: Production Dependency**
```
(team, function, produced-resource)
```
The team operates a function that produces a resource.

**Pattern 2: Consumption Dependency**
```
(team, function, consumed-resource)
```
The team operates a function that consumes a resource.

**Pattern 3: Cross-Team Dependency**
```
(team-a, resource, team-b)
```
Team A produces a resource that Team B consumes.

### Modeling Cross-Team Dependencies

Consider two teams:
- **Platform Team**: Produces infrastructure, API access
- **Product Team**: Consumes API access, produces features

```yaml
# Cross-team dependency face
type: face/dependency
extends: face
id: f:dependency:product-api-platform
vertices:
  - v:actor:team:product
  - v:resource:api-access
  - v:actor:team:platform
dependency_type: cross-team
criticality: high
```

This face represents:
- Product team needs API access
- Platform team provides API access
- There's a cross-team dependency

### Why Dependencies Create "Tangled" Topology

Unlike hierarchies (trees), resource dependencies create **cycles** and **meshes**:

```
Platform ──> API Access ──> Product
    ^                          │
    │                          v
    └──── Feature Requests ────┘
```

Teams become **peers with mutual needs**, not hierarchical subordinates.

The faces that cross team boundaries reveal **critical coordination points**.

### Exercise 4.1: Identify Cross-Team Dependencies

**Task:** Model a cross-team dependency.

**Define:**
1. A resource your team produces
2. Another team that consumes it
3. A cross-team dependency face

---

## Section 5: Building a Management Chart

**Time:** 90 minutes

### Management Chart Structure

```yaml
---
type: chart/management
extends: chart
id: c:deployment-pipeline-management
name: Deployment Pipeline Management Chart
description: Models resource flows through deployment pipeline

elements:
  vertices:
    # Actors (shared with coordination chart)
    - v:actor:team:platform
    - v:actor:team:product

    # Functions
    - v:function:build-service
    - v:function:test-service
    - v:function:deploy-service

    # Resources
    - v:resource:source-code
    - v:resource:tested-code
    - v:resource:deployment-config
    - v:resource:running-service

  edges:
    # Operates edges
    - e:operates:product:build-service
    - e:operates:product:test-service
    - e:operates:platform:deploy-service

    # Flow edges
    - e:consumes:build-service:source-code
    - e:produces:build-service:built-artifact
    - e:consumes:test-service:built-artifact
    - e:produces:test-service:tested-code
    - e:consumes:deploy-service:tested-code
    - e:consumes:deploy-service:deployment-config
    - e:produces:deploy-service:running-service

  faces:
    # Production dependencies
    - f:dependency:product:build-service:built-artifact
    - f:dependency:product:test-service:tested-code
    - f:dependency:platform:deploy-service:running-service

    # Cross-team dependency
    - f:dependency:product:tested-code:platform
---
```

### Comparing with Coordination Chart

**Coordination Chart** (Module 08):
- Focus: Who is responsible for deployment?
- Vertices: team, staff, role, responsibility
- Faces: Assignment faces (RACI)

**Management Chart** (Module 09):
- Focus: What resources flow through deployment?
- Vertices: team, function, resource
- Faces: Dependency faces (flows)

**Shared Vertex:** Team (appears in both)

### Critical Resource Paths

The management chart reveals critical paths:

```
source-code → build → test → deploy → running-service
```

If any step fails, the pipeline stops. This is a **critical path**.

**Identifying bottlenecks:**
- Which function has the most consumes edges? (most dependencies)
- Which resource has the most produces edges? (most impact)
- Which team operates the most functions? (highest load)

### Exercise 5.1: Complete Your Management Chart

**Task:** Build a management chart for your deployment or operational pipeline.

**Include:**
1. Team vertices (shared with coordination chart)
2. Function vertices for key operations
3. Resource vertices for inputs and outputs
4. Flow edges (operates, consumes, produces)
5. Dependency faces

**Verify:**
```bash
python scripts/verify_chart.py charts/your-management/your-management.md --root .
python scripts/topology.py charts/your-management/your-management.md --root .
```

---

## Summary

### Key Takeaways

1. **Management Charts Model Resource Flows**
   - Resources: Things produced, consumed, transformed
   - Functions: Operations that transform resources
   - Flows: How resources move between functions

2. **Flow Edges Capture Operational Dependencies**
   - operates: Actor → Function (who runs what)
   - produces: Function → Resource (what's created)
   - consumes: Function → Resource (what's needed)

3. **Dependency Faces Show Critical Relationships**
   - Production dependencies (team-function-resource)
   - Consumption dependencies (function-resource-requirement)
   - Cross-team dependencies (team-resource-team)

4. **Tangled Topology Reveals Reality**
   - Resource dependencies create meshes, not trees
   - Teams become peers with mutual needs
   - Cross-team faces mark coordination points

5. **Teams Bridge Coordination and Management**
   - Shared team vertices enable chart composition
   - Module 10 will compose coordination + management charts

### Skill Checklist

You should now be able to:

- Create resource and function vertex types
- Define flow edges (operates, produces, consumes)
- Build dependency faces for resource relationships
- Construct management charts showing resource flows
- Identify cross-team dependencies and critical paths
- Compare coordination vs management chart purposes

### What's Next

In **Module 10: Organizational Topology**, you'll learn to:

- Compose coordination and management charts
- Apply Hodge decomposition to analyze edge flows
- Use edge PageRank to find structurally important edges
- Analyze organizations too complex for visualization
- Achieve the chief-engineer terminal state

---

## Section 6: The Learning Journey Structure

**Time:** 30 minutes

### How This Module Fits the Learning Path

This is the second module in the **organizational modeling journey** (Modules 08-09-10). It builds on coordination charts to add operational resource flow modeling.

### Entry State: Coordination Architect

You enter this module as a [[v:student:coordination-architect]] with 6-8 skills:

- `simplicial-complex-fundamentals` (Module 01)
- `typed-simplicial-complexes` (Module 02)
- `verification-validation` (Module 04)
- `assurance-audits` (Module 05)
- `reference-reuse` (Module 07)
- `team-coordination` (Module 08) - the prerequisite for this module
- Optional: `composing-typed-simplicial-complexes` (Module 03)
- Optional: `document-composition` (Module 06)

### Prerequisite Validation

The prerequisite face validates your readiness:

```
      coordination-architect
              /\
             /  \
  has-skill /    \ studies
           /      \
          /        \
 team-coordination  resource-management
           \        /
            \      /
      requires-skill
```

This triangle [[f:prerequisite:coordination-architect:team-coordination:resource-management]] validates:

- You possess the team-coordination skill from Module 08
- This module requires that skill
- Therefore you can study this module

### Exit State: Management Architect

After completing this module, you transition to [[v:student:management-architect]] with 7-9 skills:

**Skill gained:** [[v:skill:resource-management]]

The completion face [[f:completion:coordination-architect:resource-management:management-architect]] represents this transition:

```
  coordination-architect
           /\
          /  \
  studies/    \transitions-to
        /      \
       /        \
resource-management  management-architect
        \        /
         \      /
          advances
```

### Skill Attribution

The skill-gain face [[f:skill-gain:management-architect:resource-management:resource-management]] shows causal attribution:

- The module [[v:learning-module:resource-management]] develops the skill
- The student [[v:student:management-architect]] now possesses it
- The edge [[e:develops-skill:resource-management:resource-management]] connects them

### Topology of This Module's Chart

The learning journey chart for Module 09 has:

- **Vertices (V):** 5 (2 students + 2 skills + 1 module)
- **Edges (E):** 7 (has-skill, requires-skill, develops-skill, studies, transitions-to, advances, has-skill)
- **Faces (F):** 3 (prerequisite, completion, skill-gain)
- **Euler Characteristic:** χ = V - E + F = 5 - 7 + 3 = 1 ✓

See the full chart: [[c:learning-journey-module-09]]

### Exercise 6.1: Trace Your Path to Chief Engineer

**Task:** Map the remaining path to the terminal state.

1. What skills do you have after this module?
2. What additional skill(s) does Module 10 require?
3. What two skills does Module 10 develop?
4. What is the terminal state called?

---

## Section 7: Worked Example - Deployment Pipeline

**Time:** 45 minutes

### Scenario

Build a complete management chart for a deployment pipeline with:

- 2 teams (Product Team, Platform Team)
- 3 functions (Build, Test, Deploy)
- 4 resources (Source Code, Built Artifact, Tested Code, Running Service)

### Step 1: Define Resource Vertices

```yaml
# Source Code - input to the pipeline
---
type: vertex/resource
extends: vertex
id: v:resource:source-code
name: Source Code
resource_type: artifact
owner: v:actor:team:product
---

# Built Artifact - intermediate product
---
type: vertex/resource
extends: vertex
id: v:resource:built-artifact
name: Built Artifact
resource_type: artifact
owner: v:actor:team:product
---

# Tested Code - verified intermediate
---
type: vertex/resource
extends: vertex
id: v:resource:tested-code
name: Tested Code
resource_type: artifact
owner: v:actor:team:product
---

# Running Service - final output
---
type: vertex/resource
extends: vertex
id: v:resource:running-service
name: Running Service
resource_type: infrastructure
owner: v:actor:team:platform
---
```

### Step 2: Define Function Vertices

```yaml
# Build function
---
type: vertex/function
extends: vertex
id: v:function:build
name: Build Service
operated_by: v:actor:team:product
inputs:
  - v:resource:source-code
outputs:
  - v:resource:built-artifact
---

# Test function
---
type: vertex/function
extends: vertex
id: v:function:test
name: Test Service
operated_by: v:actor:team:product
inputs:
  - v:resource:built-artifact
outputs:
  - v:resource:tested-code
---

# Deploy function
---
type: vertex/function
extends: vertex
id: v:function:deploy
name: Deploy Service
operated_by: v:actor:team:platform
inputs:
  - v:resource:tested-code
outputs:
  - v:resource:running-service
---
```

### Step 3: Define Flow Edges

**Operates edges (3):**

```yaml
e:operates:product:build    # Product team operates Build
e:operates:product:test     # Product team operates Test
e:operates:platform:deploy  # Platform team operates Deploy
```

**Consumes edges (3):**

```yaml
e:consumes:build:source-code       # Build consumes Source Code
e:consumes:test:built-artifact     # Test consumes Built Artifact
e:consumes:deploy:tested-code      # Deploy consumes Tested Code
```

**Produces edges (3):**

```yaml
e:produces:build:built-artifact    # Build produces Built Artifact
e:produces:test:tested-code        # Test produces Tested Code
e:produces:deploy:running-service  # Deploy produces Running Service
```

### Step 4: Identify the Cross-Team Handoff

The critical cross-team dependency is:

```
Product team ──[operates]──> Test ──[produces]──> tested-code
                                                      │
                                                      v
Platform team ──[operates]──> Deploy ──[consumes]──┘
```

This is where Product hands off to Platform. A face captures this:

```yaml
type: face/dependency
id: f:dependency:product-tested-code-platform
vertices:
  - v:actor:team:product
  - v:resource:tested-code
  - v:actor:team:platform
dependency_type: cross-team
```

### Step 5: Visualize the Pipeline

```
                    [Build] ──produces──> built-artifact
                       │                      │
            operates   │                      │ consumes
                       │                      v
  product-team ────────┼─────────────────> [Test] ──produces──> tested-code
                       │                                            │
                                                                    │ consumes
                                                                    v
  platform-team ──operates──> [Deploy] ──produces──> running-service
```

### Step 6: Calculate Topology

**Count elements:**

- Vertices: 2 teams + 3 functions + 4 resources = **9 vertices**
- Edges: 3 operates + 3 consumes + 3 produces = **9 edges**
- Faces: Production + consumption + cross-team faces = **~4 faces**

**Calculate Euler characteristic:**

- χ = V - E + F = 9 - 9 + 4 = 4

The high χ value reflects a relatively sparse face structure. Adding more dependency faces would lower χ toward 1.

---

## Section 8: Comparing Coordination and Management Charts

**Time:** 30 minutes

### Side-by-Side Comparison

| Aspect | Coordination Chart | Management Chart |
|--------|-------------------|------------------|
| **Focus** | People & responsibilities | Resources & flows |
| **Primary vertices** | staff, team, role | function, resource, team |
| **Key edges** | member, holds-role, assigned | operates, produces, consumes |
| **Key faces** | assignment (RACI) | dependency (flows) |
| **Question answered** | Who is accountable? | What resources flow? |
| **Topology pattern** | Role-based hierarchy | Resource-based mesh |

### The Team Bridge

Teams appear in both chart types:

**In Coordination Chart:**

```yaml
team:platform
├── member: alice, bob
├── includes: tech-lead, sre
└── assignment faces for RACI
```

**In Management Chart:**

```yaml
team:platform
├── operates: deploy-service
├── dependency on: tested-code (from product)
└── produces: running-service
```

This shared vertex enables composition in Module 10.

### When to Use Each Chart Type

**Use Coordination Charts when:**

- Designing reporting structures
- Assigning accountability (RACI)
- Onboarding new team members
- Auditing responsibility coverage

**Use Management Charts when:**

- Analyzing resource bottlenecks
- Planning capacity
- Identifying cross-team dependencies
- Optimizing operational flows

**Use Both (Composed) when:**

- Complete organizational design
- Holistic dependency analysis
- Restructuring decisions
- Strategic planning

---

## Self-Assessment

### Concept Check

Answer these questions to verify your understanding:

**Level 1: Recall**

1. What are the three flow edge types introduced in this module?
2. What is the difference between a resource and a function?
3. Name the three resource subtypes (capability, artifact, infrastructure).
4. What does an operates edge connect?

**Level 2: Understanding**

5. Why do resource dependencies create "tangled" topology rather than hierarchies?
6. How does a cross-team dependency face reveal coordination requirements?
7. What does the "consumes" edge's `blocking: true` property mean?
8. Why are teams the "bridge" between coordination and management charts?

**Level 3: Application**

9. Given a new pipeline step, how would you add it to the management chart?
10. Design the edges needed to model "Function A depends on Function B" relationship.
11. How would you identify the bottleneck function in a management chart?
12. What topology change would you expect if you add a parallel path?

**Level 4: Analysis**

13. Compare the Euler characteristic of a linear pipeline (no branches) vs a branching pipeline.
14. How could you detect "circular dependencies" from the chart topology?
15. What would a high number of consumes edges on one function indicate?
16. How does the tangled topology of management charts differ from the boundary complex?

### Practical Skills Verification

Complete these tasks to demonstrate skill acquisition:

- [ ] Created resource vertex type with subtypes
- [ ] Created function vertex type with inputs/outputs
- [ ] Defined operates, produces, consumes edges
- [ ] Defined dependency faces for resource relationships
- [ ] Built complete management chart with cross-team flow
- [ ] Identified critical path through the pipeline
- [ ] Verified chart passes topology checks
- [ ] Generated and interpreted visualization

---

## Assessment

### Final Exercise: Complete Management Chart

**Task:** Build a management chart for a multi-team resource pipeline.

**Requirements:**

1. **Vertices** (40 points)
   - 2 team vertices
   - 3 function vertices
   - 4 resource vertices

2. **Edges** (30 points)
   - operates edges for all functions
   - consumes and produces edges for all flows
   - At least 8 flow edges total

3. **Faces** (20 points)
   - Dependency faces for key relationships
   - At least 1 cross-team dependency face
   - At least 3 dependency faces total

4. **Verification** (10 points)
   - Chart passes verify_chart.py
   - Valid topology (χ = 1)

**Deliverables:**
- Management chart file in `charts/your-management/`
- Brief write-up (150-200 words) identifying critical paths

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

1. **Resource Types**: capability, artifact, infrastructure
2. **Function**: Operation with inputs and outputs
3. **Flow Edges**: operates, produces, consumes
4. **Dependency Faces**: Production, consumption, cross-team
5. **Critical Path**: Sequence where any failure blocks the pipeline
6. **Tangled Topology**: Mesh-like dependencies vs hierarchies

---

**Module 09 Complete**

You've learned how to model resource flows with management charts, create function and resource vertices, define flow edges, and identify cross-team dependencies. This prepares you for chart composition and Hodge analysis in Module 10.
