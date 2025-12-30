---
type: chart/organization
extends: chart
id: c:org:raci-coordination-chart
name: RACI Coordination Chart
description: Coordination chart showing team structure and RACI responsibility assignments for Platform and Product teams
tags:
  - chart
  - organization
  - coordination
  - raci
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z

# Chart construction metadata
constructed_by: "Claude (LLM-assisted)"
construction_method: assisted
construction_date: 2025-12-29T00:00:00Z

# Chart purpose
purpose: Document team structure and RACI responsibilities for Platform and Product teams
scope: Two teams (Platform, Product), 5 staff, 4 roles, 3 responsibilities with RACI assignments

# Organization-specific metadata
organization_type: coordination
organization_scope:
  teams:
    - v:actor:team:platform
    - v:actor:team:product
  primary_focus: Team structure and RACI accountability

coordination_metadata:
  staff_count: 5
  role_count: 4
  raci_coverage: "Complete RACI for deploy, monitor, and build responsibilities"

# Elements comprising this chart
elements:
  vertices:
    # Teams
    - v:actor:team:platform
    - v:actor:team:product
    # Staff
    - v:actor:staff:alice
    - v:actor:staff:bob
    - v:actor:staff:charlie
    - v:actor:staff:dana
    - v:actor:staff:evan
    # Roles
    - v:actor:role:tech-lead
    - v:actor:role:sre
    - v:actor:role:senior-developer
    - v:actor:role:developer
    # Responsibilities
    - v:property:responsibility:deploy
    - v:property:responsibility:monitor
    - v:property:responsibility:build
  edges:
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
    # Assigned edges (role → responsibility with RACI)
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
  faces:
    # Assignment faces (staff, role, responsibility) with RACI
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

# Chart: RACI Coordination Chart

This chart documents the organizational structure and RACI (Responsible, Accountable, Consulted, Informed) assignments for Platform and Product teams.

## Why This Chart Exists

**Motivation:** To formalize team structure and accountability for key responsibilities, enabling clear understanding of who does what and who is answerable.

**Context:** Organizations need clear accountability. RACI matrices provide this, but as text tables they lack structural verification. This chart encodes RACI as a typed simplicial complex, enabling formal verification of accountability rules.

**Intended Use:**
- Onboarding: New team members understand accountability structure
- Audit: Verify single-accountable rule is satisfied
- Planning: Identify gaps in responsibility coverage
- Training: Demonstrate Module 08 coordination chart concepts

## What This Chart Contains

### Scope Definition

**Included:**
- Two teams: Platform (ops) and Product (dev)
- All staff members of both teams
- All roles within both teams
- Three key responsibilities: Deploy, Monitor, Build
- RACI assignments for all responsibilities

**Excluded:**
- Cross-team collaboration edges (see composed chart)
- Resource and function vertices (see management chart)
- Higher-level organizational hierarchy

**Boundaries:**
- Focuses on staff-role-responsibility relationships
- One level of team hierarchy only

### Element Summary

**Vertices (14):** 2 teams + 5 staff + 4 roles + 3 responsibilities

**Edges (28):** 5 member + 5 holds-role + 4 includes + 6 assigned + 8 direct RACI (3 accountable + 5 responsible)

**Faces (8):** 3 deploy assignments + 3 monitor assignments + 2 build assignments

**Dimension:** 2 (includes faces)

## How This Chart Was Constructed

**Construction Method:** assisted

**Process:**
1. Defined team structure from Module 08 Platform Team example
2. Added Product Team for cross-team demonstration
3. Created staff vertices for each team member
4. Defined roles within each team
5. Created responsibility vertices for key activities
6. Built member edges (staff → team)
7. Built holds-role edges (staff → role)
8. Built includes edges (team → role)
9. Applied RACI assignments (assigned edges with raci_type)
10. Verified single-accountable rule for each responsibility

**Constructor:** Claude (LLM-assisted)

**Date Constructed:** 2025-12-29

**Quality Assurance:**
- Verified each responsibility has exactly one Accountable
- Verified each responsibility has at least one Responsible
- All staff are members of exactly one team
- All roles are included in their respective teams

## Vertices (0-Cells)

### Teams

| ID | Name | Type | Members |
|----|------|------|---------|
| v:actor:team:platform | Platform Team | team | Alice, Bob, Charlie |
| v:actor:team:product | Product Team | team | Dana, Evan |

**Total:** 2 teams

### Staff

| ID | Name | Role | Team |
|----|------|------|------|
| v:actor:staff:alice | Alice | Tech Lead | Platform |
| v:actor:staff:bob | Bob | SRE | Platform |
| v:actor:staff:charlie | Charlie | SRE | Platform |
| v:actor:staff:dana | Dana | Senior Developer | Product |
| v:actor:staff:evan | Evan | Developer | Product |

**Total:** 5 staff

### Roles

| ID | Name | Team | Primary Duty |
|----|------|------|--------------|
| v:actor:role:tech-lead | Tech Lead | Platform | Approval, architecture |
| v:actor:role:sre | SRE | Platform | Monitoring, deployment execution |
| v:actor:role:senior-developer | Senior Developer | Product | Feature design, code review |
| v:actor:role:developer | Developer | Product | Feature implementation, testing |

**Total:** 4 roles

### Responsibilities

| ID | Name | Accountable | Responsible |
|----|------|-------------|-------------|
| v:property:responsibility:deploy | Deploy to Production | Tech Lead (Alice) | SRE (Bob, Charlie) |
| v:property:responsibility:monitor | Monitor Services | Tech Lead (Alice) | SRE (Bob, Charlie) |
| v:property:responsibility:build | Build Application | Senior Developer (Dana) | Developer (Evan) |

**Total:** 3 responsibilities

## Edges (1-Cells)

### Member Edges (staff → team)

| ID | Staff | Team |
|----|-------|------|
| e:member:platform:alice | Alice | Platform Team |
| e:member:platform:bob | Bob | Platform Team |
| e:member:platform:charlie | Charlie | Platform Team |
| e:member:product:dana | Dana | Product Team |
| e:member:product:evan | Evan | Product Team |

**Total:** 5 member edges

### Holds-Role Edges (staff → role)

| ID | Staff | Role |
|----|-------|------|
| e:holds-role:alice:tech-lead | Alice | Tech Lead |
| e:holds-role:bob:sre | Bob | SRE |
| e:holds-role:charlie:sre | Charlie | SRE |
| e:holds-role:dana:senior-developer | Dana | Senior Developer |
| e:holds-role:evan:developer | Evan | Developer |

**Total:** 5 holds-role edges

### Includes Edges (team → role)

| ID | Team | Role |
|----|------|------|
| e:includes:platform:tech-lead | Platform | Tech Lead |
| e:includes:platform:sre | Platform | SRE |
| e:includes:product:senior-developer | Product | Senior Developer |
| e:includes:product:developer | Product | Developer |

**Total:** 4 includes edges

### Assigned Edges (role → responsibility with RACI)

| ID | Role | Responsibility | RACI |
|----|------|----------------|------|
| e:assigned:tech-lead:deploy:a | Tech Lead | Deploy | A |
| e:assigned:sre:deploy:r | SRE | Deploy | R |
| e:assigned:tech-lead:monitor:a | Tech Lead | Monitor | A |
| e:assigned:sre:monitor:r | SRE | Monitor | R |
| e:assigned:senior-developer:build:a | Senior Developer | Build | A |
| e:assigned:developer:build:r | Developer | Build | R |

**Total:** 6 assigned edges

### Direct RACI Edges (staff → responsibility)

| ID | Staff | Responsibility | RACI |
|----|-------|----------------|------|
| e:accountable:alice:deploy | Alice | Deploy | A |
| e:accountable:alice:monitor | Alice | Monitor | A |
| e:accountable:dana:build | Dana | Build | A |
| e:responsible:bob:deploy | Bob | Deploy | R |
| e:responsible:charlie:deploy | Charlie | Deploy | R |
| e:responsible:bob:monitor | Bob | Monitor | R |
| e:responsible:charlie:monitor | Charlie | Monitor | R |
| e:responsible:evan:build | Evan | Build | R |

**Total:** 8 direct RACI edges

## Faces (2-Cells)

### Assignment Faces (staff, role, responsibility)

| ID | Staff | Role | Responsibility | RACI |
|----|-------|------|----------------|------|
| f:assignment:alice:tech-lead:deploy | Alice | Tech Lead | Deploy | A |
| f:assignment:bob:sre:deploy | Bob | SRE | Deploy | R |
| f:assignment:charlie:sre:deploy | Charlie | SRE | Deploy | R |
| f:assignment:alice:tech-lead:monitor | Alice | Tech Lead | Monitor | A |
| f:assignment:bob:sre:monitor | Bob | SRE | Monitor | R |
| f:assignment:charlie:sre:monitor | Charlie | SRE | Monitor | R |
| f:assignment:dana:senior-developer:build | Dana | Senior Developer | Build | A |
| f:assignment:evan:developer:build | Evan | Developer | Build | R |

**Total:** 8 assignment faces

## Chart Properties

### Topological Properties

- **Vertices (V):** 14
- **Edges (E):** 28
- **Faces (F):** 8
- **Euler Characteristic:** χ = V - E + F = 14 - 28 + 8 = -6
- **Connected:** Yes (via team membership)
- **Dimension:** 2 (includes faces)

### Structural Properties

- **Completeness:** All staff assigned to teams, all roles have holders
- **RACI Coverage:** Complete for all 3 responsibilities
- **Single Accountable:** ✓ Each responsibility has exactly one A
- **Bipartite Structure:** Staff-Role and Role-Responsibility form bipartite subgraphs

## Organizational Analysis

### Structure Summary

- **Teams:** 2 organizational units (Platform, Product)
- **Staff:** 5 individuals across both teams
- **Roles:** 4 functional positions
- **Responsibilities:** 3 key activities with RACI

### Key Relationships

1. **Alice (Tech Lead)** is the accountability bottleneck for Platform - accountable for both Deploy and Monitor
2. **SRE role** is shared by Bob and Charlie - both responsible for Deploy and Monitor
3. **Product Team** has clean hierarchy: Dana (A) and Evan (R) for Build

### Accountability Coverage

| Responsibility | R | A | C | I |
|----------------|---|---|---|---|
| Deploy | SRE (Bob, Charlie) | Tech Lead (Alice) | - | - |
| Monitor | SRE (Bob, Charlie) | Tech Lead (Alice) | - | - |
| Build | Developer (Evan) | Senior Developer (Dana) | - | - |

**Gap Analysis:** C and I assignments not modeled. In a complete RACI, Product Team might be Consulted on Deploy, Platform Informed on Build.

### Topology Interpretation

The negative Euler characteristic (χ = -6) indicates the chart has more edges than a tree structure. This reflects:
- Multiple paths from staff to responsibilities (staff → role → responsibility)
- Role sharing (two SREs)
- Team/role/responsibility layered structure

## Constraint Validation

### RACI Constraints

- ✓ **Deploy:** One Accountable (Tech Lead)
- ✓ **Monitor:** One Accountable (Tech Lead)
- ✓ **Build:** One Accountable (Senior Developer)
- ✓ All responsibilities have at least one Responsible
- ✓ No orphan roles (every role has holder)

### Structural Constraints

- ✓ All staff are members of exactly one team
- ✓ All roles are included in their respective teams
- ✓ Staff hold roles appropriate to their team

## Verification

### Structural Verification

```bash
# Verify chart structure
python scripts/verify_chart.py charts/raci-coordination-chart/raci-coordination-chart.md

# Analyze topology
python scripts/topology.py charts/raci-coordination-chart/raci-coordination-chart.md
```

**Expected Result:** ✓ Valid simplicial complex (1-skeleton)

**Checks:**
- All referenced vertices exist
- All edges have valid source/target
- Element counts match

## Interpretation

**What This Chart Reveals:**

1. **Clear accountability lines:** Each responsibility has exactly one accountable party
2. **Role-based structure:** Accountability flows through roles, not directly to individuals
3. **Team isolation:** Platform and Product have no shared staff or roles (in this chart)

**Key Observations:**

- Alice is a potential bottleneck - accountable for all Platform responsibilities
- Two SREs share responsibility, providing redundancy
- Product Team has flatter structure (2 staff, 2 roles)

**Implications:**

- If Alice is unavailable, Platform accountability is blocked
- SRE on-call rotation is well-supported (either can fulfill R)
- Cross-team dependencies (Product → Platform for deploy) not captured here

**Limitations:**

- No C/I assignments modeled
- Cross-team collaboration not shown
- Resource flows not visible (see management chart)

## Related Charts

| Chart | Relationship | Notes |
|-------|--------------|-------|
| [[c:org:resource-management-chart]] | Complements | Shows resource flows for same teams |
| [[c:org:composed-org-chart]] | Extends | Combines coordination and management views |

---

**Note:** This chart demonstrates the coordination chart pattern from Module 08. For complete organizational modeling, compose with the management chart to see staff-function relationships.
