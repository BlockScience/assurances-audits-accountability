---
type: chart/organization
extends: chart
id: c:org:resource-management-chart
name: Resource Management Chart
description: Management chart showing resource flows through functions operated by Platform and Product teams
tags:
  - chart
  - organization
  - management
  - pipeline
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z

# Chart construction metadata
constructed_by: "Claude (LLM-assisted)"
construction_method: assisted
construction_date: 2025-12-29T00:00:00Z

# Chart purpose
purpose: Document resource flows through the deployment pipeline operated by Platform and Product teams
scope: Two teams, 3 functions, 4 resources, with production and consumption flows

# Organization-specific metadata
organization_type: management
organization_scope:
  teams:
    - v:actor:team:platform
    - v:actor:team:product
  primary_focus: Deployment pipeline resource flows

management_metadata:
  function_count: 3
  resource_count: 4
  flow_description: "Linear pipeline: source code → build → test → deploy → running service"

# Elements comprising this chart
elements:
  vertices:
    # Teams
    - v:actor:team:platform
    - v:actor:team:product
    # Functions
    - v:function:build
    - v:function:test
    - v:function:deploy
    # Resources
    - v:resource:source-code
    - v:resource:built-artifact
    - v:resource:tested-code
    - v:resource:running-service
  edges:
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
  faces: []
---

# Chart: Resource Management Chart

This chart documents the resource flows through the deployment pipeline, showing how functions transform resources and which teams operate each function.

## Why This Chart Exists

**Motivation:** To formalize resource flows and identify cross-team dependencies in the deployment pipeline. Understanding who produces what and who consumes it reveals integration points and bottlenecks.

**Context:** The coordination chart shows who is accountable; this chart shows what resources flow between teams. Together they provide complete organizational visibility.

**Intended Use:**
- Capacity planning: Identify bottlenecks in resource production
- Dependency analysis: Find cross-team handoff points
- Incident response: Trace resource failures through the pipeline
- Training: Demonstrate Module 09 management chart concepts

## What This Chart Contains

### Scope Definition

**Included:**
- Two teams: Platform and Product
- Three functions: Build, Test, Deploy
- Four resources: Source Code, Built Artifact, Tested Code, Running Service
- Operates, produces, and consumes edges

**Excluded:**
- Staff and role vertices (see coordination chart)
- RACI assignments (see coordination chart)
- Monitoring and infrastructure management functions

**Boundaries:**
- Deployment pipeline only (not development or operations)
- Function level (not individual steps within functions)

### Element Summary

**Vertices (9):** 2 teams + 3 functions + 4 resources

**Edges (9):** 3 operates + 3 consumes + 3 produces

**Faces (0):** No faces defined (pure 1-skeleton)

**Dimension:** 1 (edges only)

## How This Chart Was Constructed

**Construction Method:** assisted

**Process:**
1. Identified teams from coordination chart (Platform, Product)
2. Defined deployment pipeline functions (Build, Test, Deploy)
3. Identified resources at each pipeline stage
4. Created operates edges (team → function)
5. Created consumes edges (function → resource input)
6. Created produces edges (function → resource output)
7. Verified linear flow (no cycles)
8. Identified cross-team handoff (tested-code: Product → Platform)

**Constructor:** Claude (LLM-assisted)

**Date Constructed:** 2025-12-29

**Quality Assurance:**
- Verified each resource has at least one producer
- Verified each consumption has a matching production
- Checked for cycles (none found - linear pipeline)
- Identified critical path and cross-team dependency

## Vertices (0-Cells)

### Teams

| ID | Name | Type | Functions Operated |
|----|------|------|-------------------|
| v:actor:team:platform | Platform Team | team | Deploy |
| v:actor:team:product | Product Team | team | Build, Test |

**Total:** 2 teams

### Functions

| ID | Name | Input | Output | Operated By |
|----|------|-------|--------|-------------|
| v:function:build | Build | Source Code | Built Artifact | Product |
| v:function:test | Test | Built Artifact | Tested Code | Product |
| v:function:deploy | Deploy | Tested Code | Running Service | Platform |

**Total:** 3 functions

### Resources

| ID | Name | Type | Producer | Consumer |
|----|------|------|----------|----------|
| v:resource:source-code | Source Code | artifact | (external) | Build |
| v:resource:built-artifact | Built Artifact | artifact | Build | Test |
| v:resource:tested-code | Tested Code | artifact | Test | Deploy |
| v:resource:running-service | Running Service | infrastructure | Deploy | (monitored) |

**Total:** 4 resources

## Edges (1-Cells)

### Operates Edges (team → function)

| ID | Team | Function |
|----|------|----------|
| e:operates:product:build | Product Team | Build |
| e:operates:product:test | Product Team | Test |
| e:operates:platform:deploy | Platform Team | Deploy |

**Total:** 3 operates edges

### Consumes Edges (function → resource)

| ID | Function | Resource | Blocking |
|----|----------|----------|----------|
| e:consumes:build:source-code | Build | Source Code | Yes |
| e:consumes:test:built-artifact | Test | Built Artifact | Yes |
| e:consumes:deploy:tested-code | Deploy | Tested Code | Yes |

**Total:** 3 consumes edges

### Produces Edges (function → resource)

| ID | Function | Resource |
|----|----------|----------|
| e:produces:build:built-artifact | Build | Built Artifact |
| e:produces:test:tested-code | Test | Tested Code |
| e:produces:deploy:running-service | Deploy | Running Service |

**Total:** 3 produces edges

## Chart Properties

### Topological Properties

- **Vertices (V):** 9
- **Edges (E):** 9
- **Faces (F):** 0
- **Euler Characteristic:** χ = V - E + F = 9 - 9 + 0 = 0
- **Connected:** Yes (via operates and flow edges)
- **Dimension:** 1 (pure 1-skeleton, no faces)
- **Acyclic:** Yes (linear pipeline)

### Structural Properties

- **Completeness:** All functions have operators, all resources have producers
- **Pipeline Structure:** Linear chain with no branches
- **Cross-Team Boundary:** Between Test (Product) and Deploy (Platform)
- **Critical Path:** source-code → build → test → deploy → running-service

### Pipeline Flow Diagram

```
Product Team                        Platform Team
     |                                   |
     v                                   v
[source-code] --> [Build] --> [built-artifact]
                                   |
                                   v
                              [Test] --> [tested-code]
                                              |
                        =====================|===============
                        Cross-Team Handoff   |
                        =====================|===============
                                              v
                                         [Deploy] --> [running-service]
```

## Organizational Analysis

### Structure Summary

- **Teams:** 2 organizational units operating the pipeline
- **Functions:** 3 pipeline stages
- **Resources:** 4 artifacts/infrastructure at each stage

### Key Relationships

1. **Product Team** operates 2/3 of the pipeline (Build, Test)
2. **Platform Team** operates the final critical stage (Deploy)
3. **Tested Code** is the cross-team handoff artifact

### Resource Flow Analysis

**Critical Path:**
source-code → build → built-artifact → test → tested-code → deploy → running-service

**Bottleneck Risk:**
- Single path with no parallelism
- Any function failure blocks downstream
- Cross-team handoff at tested-code

**Cross-Team Dependencies:**
- Product produces tested-code
- Platform consumes tested-code for deployment
- This is the **integration point** where teams must coordinate

### Topology Interpretation

The Euler characteristic χ = 0 indicates a balanced structure (equal vertices and edges). The linear pipeline has:
- No cycles (acyclic)
- No faces (no triangular relationships modeled)
- Single connected component

## Constraint Validation

### Resource Flow Constraints

- ✓ **Source Code:** Has consumer (Build)
- ✓ **Built Artifact:** Has producer (Build) and consumer (Test)
- ✓ **Tested Code:** Has producer (Test) and consumer (Deploy)
- ✓ **Running Service:** Has producer (Deploy)
- ✓ No cycles in production chain
- ✓ All consumed resources have producers

### Structural Constraints

- ✓ All functions have exactly one operating team
- ✓ All blocking dependencies documented
- ✓ Cross-team handoff identified (tested-code)

## Verification

### Structural Verification

```bash
# Verify chart structure
python scripts/verify_chart.py charts/resource-management-chart/resource-management-chart.md

# Analyze topology
python scripts/topology.py charts/resource-management-chart/resource-management-chart.md
```

**Expected Result:** ✓ Valid simplicial complex (1-skeleton)

**Checks:**
- All referenced vertices exist
- All edges have valid source/target
- Element counts match

## Interpretation

**What This Chart Reveals:**

1. **Linear pipeline:** Simple flow with no parallelism
2. **Clear ownership:** Product owns early stages, Platform owns deployment
3. **Single handoff:** Tested-code is the only cross-team artifact

**Key Observations:**

- Product Team is responsible for most of the pipeline (Build + Test)
- Platform Team has the critical final step (Deploy)
- Tested-code is the integration point - if Product fails to produce it, Platform is blocked

**Implications:**

- Capacity planning should focus on the cross-team handoff
- Incident response must trace through the entire pipeline
- Parallelization opportunities limited in current design

**Limitations:**

- No faces to capture triangular dependencies
- Monitoring and operations not modeled
- No visibility into who specifically operates (see coordination chart)

## Related Charts

| Chart | Relationship | Notes |
|-------|--------------|-------|
| [[c:org:raci-coordination-chart]] | Complements | Shows who is accountable/responsible |
| [[c:org:composed-org-chart]] | Extends | Combines coordination and management views |

---

**Note:** This chart demonstrates the management chart pattern from Module 09. For complete organizational modeling, compose with the coordination chart to see staff-function relationships.
