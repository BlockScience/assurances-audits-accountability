---
type: chart/organization
extends: chart
id: c:org:composed-org-chart
name: Composed Organization Chart
description: Complete organizational chart composing coordination and management views to show staff, roles, responsibilities, functions, and resources
tags:
  - chart
  - organization
  - composed
  - complete
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z

# Chart construction metadata
constructed_by: "Claude (LLM-assisted)"
construction_method: assisted
construction_date: 2025-12-29T00:00:00Z

# Chart purpose
purpose: Provide complete organizational view by composing coordination (who does what) and management (what flows where) charts
scope: Full organizational model - teams, staff, roles, responsibilities, functions, resources

# Organization-specific metadata
organization_type: composed
organization_scope:
  teams:
    - v:actor:team:platform
    - v:actor:team:product
  primary_focus: Complete organizational topology with people and resources

composition_metadata:
  source_charts:
    - c:org:raci-coordination-chart
    - c:org:resource-management-chart
  shared_vertices:
    - v:actor:team:platform
    - v:actor:team:product
  emergent_edges: []

# Elements comprising this chart
elements:
  vertices:
    # Teams (SHARED - appear in both source charts)
    - v:actor:team:platform
    - v:actor:team:product
    # Staff (from coordination)
    - v:actor:staff:alice
    - v:actor:staff:bob
    - v:actor:staff:charlie
    - v:actor:staff:dana
    - v:actor:staff:evan
    # Roles (from coordination)
    - v:actor:role:tech-lead
    - v:actor:role:sre
    - v:actor:role:senior-developer
    - v:actor:role:developer
    # Responsibilities (from coordination)
    - v:property:responsibility:deploy
    - v:property:responsibility:monitor
    - v:property:responsibility:build
    # Functions (from management)
    - v:function:build
    - v:function:test
    - v:function:deploy
    # Resources (from management)
    - v:resource:source-code
    - v:resource:built-artifact
    - v:resource:tested-code
    - v:resource:running-service
  edges:
    # === COORDINATION EDGES ===
    # Member edges (staff → team)
    - e:member:platform:alice
    - e:member:platform:bob
    - e:member:platform:charlie
    - e:member:product:dana
    - e:member:product:evan
    # Holds-role edges (staff → role)
    - e:holds-role:alice:tech-lead
    - e:holds-role:bob:sre
    - e:holds-role:charlie:sre
    - e:holds-role:dana:senior-developer
    - e:holds-role:evan:developer
    # Includes edges (team → role)
    - e:includes:platform:tech-lead
    - e:includes:platform:sre
    - e:includes:product:senior-developer
    - e:includes:product:developer
    # Assigned edges (role → responsibility)
    - e:assigned:tech-lead:deploy:a
    - e:assigned:sre:deploy:r
    - e:assigned:tech-lead:monitor:a
    - e:assigned:sre:monitor:r
    - e:assigned:senior-developer:build:a
    - e:assigned:developer:build:r
    # Direct RACI edges (staff → responsibility) - completes assignment face triangles
    - e:accountable:alice:deploy
    - e:accountable:alice:monitor
    - e:accountable:dana:build
    - e:responsible:bob:deploy
    - e:responsible:charlie:deploy
    - e:responsible:bob:monitor
    - e:responsible:charlie:monitor
    - e:responsible:evan:build
    # === MANAGEMENT EDGES ===
    # Operates edges (team → function)
    - e:operates:product:build
    - e:operates:product:test
    - e:operates:platform:deploy
    # Consumes edges (function → resource)
    - e:consumes:build:source-code
    - e:consumes:test:built-artifact
    - e:consumes:deploy:tested-code
    # Produces edges (function → resource)
    - e:produces:build:built-artifact
    - e:produces:test:tested-code
    - e:produces:deploy:running-service
  faces:
    # === ASSIGNMENT FACES (from coordination) ===
    # Deploy assignments
    - f:assignment:alice:tech-lead:deploy
    - f:assignment:bob:sre:deploy
    - f:assignment:charlie:sre:deploy
    # Monitor assignments
    - f:assignment:alice:tech-lead:monitor
    - f:assignment:bob:sre:monitor
    - f:assignment:charlie:sre:monitor
    # Build assignments
    - f:assignment:dana:senior-developer:build
    - f:assignment:evan:developer:build
---

# Chart: Composed Organization Chart

This chart provides a complete organizational view by composing the coordination chart (who does what) with the management chart (what flows where), connected through shared team vertices.

## Why This Chart Exists

**Motivation:** Neither coordination nor management charts alone provide complete organizational visibility. By composing them through shared team vertices, we see the full picture: who is accountable for what, and how resources flow through the organization.

**Context:** Module 10 introduces chart composition - combining charts that share vertices to reveal emergent structure. This chart demonstrates that technique with the practical example of organizational modeling.

**Intended Use:**
- Strategic planning: Complete view for restructuring decisions
- Dependency analysis: Trace from staff through teams to resource flows
- Audit: Verify accountability covers all functions
- Training: Demonstrate Module 10 composition concepts

## What This Chart Contains

### Scope Definition

**Included:**
- Everything from coordination chart: teams, staff, roles, responsibilities, RACI
- Everything from management chart: teams, functions, resources, flows
- Shared vertices: Platform Team, Product Team

**Excluded:**
- Emergent edges (could be added to show staff-function paths)
- Faces (no triangular relationships modeled yet)
- Higher-level organizational hierarchy

**Boundaries:**
- Two teams, complete staff-to-resource path visibility
- One level of team hierarchy

### Element Summary

**Vertices (21):**
- 2 teams (shared)
- 5 staff
- 4 roles
- 3 responsibilities
- 3 functions
- 4 resources

**Edges (37):**
- 28 from coordination (5 member + 5 holds-role + 4 includes + 6 assigned + 8 direct RACI)
- 9 from management (3 operates + 3 consumes + 3 produces)

**Faces (8):** 8 assignment faces from coordination (3 deploy + 3 monitor + 2 build)

**Dimension:** 2 (includes faces)

## How This Chart Was Constructed

**Construction Method:** assisted

**Process:**
1. Identified source charts (coordination, management)
2. Identified shared vertices (Platform Team, Product Team)
3. Verified shared vertices have consistent properties
4. Combined all vertices (union)
5. Combined all edges (union)
6. Verified no edge conflicts
7. Looked for emergent relationships (none added this version)
8. Computed combined topology

**Constructor:** Claude (LLM-assisted)

**Date Constructed:** 2025-12-29

**Quality Assurance:**
- Verified shared vertices are identical in both sources
- Verified no edge ID conflicts
- Computed topology for combined structure
- Identified integration point (teams bridge coordination and management)

## Composition Structure

### Shared Vertices

The composition pastes the two charts along shared team vertices:

```
COORDINATION CHART                    MANAGEMENT CHART

staff ----+                                 +---- functions
          |                                 |
          v                                 v
roles ----+--> [PLATFORM TEAM] <----+------+
                                    |
                    [PRODUCT TEAM] -+----->+---- resources
          ^                                 ^
          |                                 |
responsibilities                        produces/consumes
```

### Bridge Structure

Teams appear in both charts with different edges:

**In Coordination:** team ← member ← staff, team → includes → role
**In Management:** team → operates → function

This creates paths from staff through teams to functions, even though no explicit staff-function edge exists.

### Implicit Paths Revealed

Through composition, we can trace:

| Path | Meaning |
|------|---------|
| Alice → Platform → Deploy function | Alice's team operates Deploy |
| Bob → Platform → Deploy function | Bob's team operates Deploy |
| Dana → Product → Build function | Dana's team operates Build |
| Tech Lead → Deploy (responsibility) ↔ Deploy (function) | Accountability aligns with operation |

## Vertices (0-Cells)

### Shared Vertices (Teams)

| ID | Name | Coordination Role | Management Role |
|----|------|-------------------|-----------------|
| v:actor:team:platform | Platform Team | 3 staff, 2 roles | Operates Deploy |
| v:actor:team:product | Product Team | 2 staff, 2 roles | Operates Build, Test |

**Total:** 2 teams (shared between charts)

### Coordination-Only Vertices

**Staff (5):** Alice, Bob, Charlie (Platform); Dana, Evan (Product)

**Roles (4):** Tech Lead, SRE (Platform); Senior Developer, Developer (Product)

**Responsibilities (3):** Deploy, Monitor, Build

**Total:** 12 vertices from coordination

### Management-Only Vertices

**Functions (3):** Build, Test, Deploy

**Resources (4):** Source Code, Built Artifact, Tested Code, Running Service

**Total:** 7 vertices from management

## Edges (1-Cells)

### Coordination Edges (28)

| Category | Edges | Count |
|----------|-------|-------|
| Member | staff → team | 5 |
| Holds-role | staff → role | 5 |
| Includes | team → role | 4 |
| Assigned | role → responsibility | 6 |
| Direct RACI | staff → responsibility | 8 |

### Management Edges (9)

| Category | Edges | Count |
|----------|-------|-------|
| Operates | team → function | 3 |
| Consumes | function → resource | 3 |
| Produces | function → resource | 3 |

**Total:** 37 edges

## Chart Properties

### Topological Properties

- **Vertices (V):** 21
- **Edges (E):** 37
- **Faces (F):** 8
- **Euler Characteristic:** χ = V - E + F = 21 - 37 + 8 = -8
- **Connected:** Yes (via shared team vertices)
- **Dimension:** 2 (includes faces)

### Composition Properties

- **Shared Vertices:** 2 (teams)
- **Edges from Coordination:** 28
- **Edges from Management:** 9
- **Edge Conflicts:** 0
- **Emergent Edges:** 0 (could add staff-function paths)

### Structural Properties

- **Connectivity:** Single connected component
- **Bipartite Substructures:** Staff-Team, Team-Function, Role-Responsibility
- **Bridge Vertices:** Platform Team, Product Team (removal disconnects charts)

## Organizational Analysis

### Structure Summary

| Category | Count | From |
|----------|-------|------|
| Teams | 2 | Shared |
| Staff | 5 | Coordination |
| Roles | 4 | Coordination |
| Responsibilities | 3 | Coordination |
| Functions | 3 | Management |
| Resources | 4 | Management |

**Total:** 21 vertices, 37 edges

### Complete Accountability-Operation Map

| Responsibility | Accountable (Person) | Function | Operating Team |
|----------------|---------------------|----------|----------------|
| Deploy | Alice (Tech Lead) | Deploy | Platform |
| Monitor | Alice (Tech Lead) | - | Platform |
| Build | Dana (Senior Developer) | Build | Product |

**Insight:** Deploy responsibility and Deploy function are both on Platform Team with Alice accountable. This is well-aligned. The "Build" responsibility maps to the "Build" function, also well-aligned.

### Cross-Team Integration Point

**The Critical Handoff:**

```
Product Team                              Platform Team
(Dana accountable for Build)              (Alice accountable for Deploy)
           |                                      |
           v                                      v
    [Build function]                       [Deploy function]
           |                                      ^
           v                                      |
    [Test function]                              |
           |                                      |
           +-----> [tested-code] -----------------+
                   (handoff artifact)
```

The `tested-code` resource is where Product's accountability ends and Platform's begins. This is the critical integration point.

### Path Analysis

From staff to running service:

| Staff | Path to Running Service |
|-------|------------------------|
| Alice | Alice → Platform → Deploy → running-service |
| Bob | Bob → Platform → Deploy → running-service |
| Charlie | Charlie → Platform → Deploy → running-service |
| Dana | Dana → Product → Build → ... → tested-code → Deploy → running-service |
| Evan | Evan → Product → Build → ... → tested-code → Deploy → running-service |

**Insight:** All staff connect to running-service, but Product staff require cross-team path through tested-code.

## Constraint Validation

### Composition Constraints

- ✓ **Shared vertices consistent:** Teams have same ID in both source charts
- ✓ **No edge conflicts:** No edge appears in both charts with different properties
- ✓ **Connected:** Single component (teams bridge the charts)

### RACI-Function Alignment

- ✓ **Deploy:** Accountable (Alice) is on team (Platform) that operates function (Deploy)
- ✓ **Build:** Accountable (Dana) is on team (Product) that operates function (Build)
- ⚠️ **Monitor:** No corresponding function in this chart

### Cross-Team Dependencies

- ✓ **tested-code handoff:** Product produces, Platform consumes
- ✓ **Path exists:** Product staff can trace to deployment output

## Verification

### Structural Verification

```bash
# Verify chart structure
python scripts/verify_chart.py charts/composed-org-chart/composed-org-chart.md

# Analyze topology
python scripts/topology.py charts/composed-org-chart/composed-org-chart.md

# Run Hodge analysis (if exported to JSON)
python scripts/export_chart_direct.py charts/composed-org-chart/composed-org-chart.md
python scripts/hodge_analysis.py charts/composed-org-chart/composed-org-chart.json
```

**Expected Result:** ✓ Valid simplicial complex (1-skeleton)

**Checks:**
- All referenced vertices exist
- All edges have valid source/target
- Element counts match
- Single connected component

## Interpretation

**What This Chart Reveals:**

1. **Complete staff-to-output path:** Every person connects to the running service
2. **Accountability-operation alignment:** RACI matches function ownership for Deploy and Build
3. **Clear handoff point:** Tested-code is the integration artifact

**Key Observations:**

- Alice is critical: accountable for Deploy (responsibility) and on team that operates Deploy (function)
- Product team has longer path to output (requires cross-team handoff)
- Teams are the "glue" - they bridge people (coordination) to work (management)

**Emergent Insights from Composition:**

- Without composition, you can't see that Alice's accountability for Deploy maps to the Deploy function her team operates
- Without composition, you can't trace Dana's work through to the running service
- Composition reveals the organization as a unified system

**Implications:**

- Restructuring must consider both views (moving staff affects accountability AND operation)
- Bottleneck analysis needs composition (Alice is critical in both dimensions)
- Incident response traces through the complete path

**Limitations:**

- No faces to capture triangular constraints
- Emergent edges not explicitly modeled (staff-function paths are implicit)
- Monitoring function not modeled

## Related Charts

| Chart | Relationship | Notes |
|-------|--------------|-------|
| [[c:org:raci-coordination-chart]] | Source | Provides coordination vertices and edges |
| [[c:org:resource-management-chart]] | Source | Provides management vertices and edges |

---

**Note:** This chart demonstrates the composition pattern from Module 10. By pasting coordination and management charts along shared team vertices, we see the complete organizational topology.
