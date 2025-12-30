# Organization Chart Plan (UX Test)

**Status:** Planned for Future UX Testing
**Complexity:** Medium-High
**Dependencies:** Actor vertex types, Role/Responsibility typing

## Purpose

Demonstrate knowledge complex capabilities for modeling organizational structures with actors, roles, responsibilities, and accountability relationships. Serves as UX test for non-document vertex types.

## Why This Is Important

**Current State:** Knowledge complex focuses on document vertices (specs, guidance, personas, etc.)

**Extension Test:** Can we model:
- People (actors/individuals)
- Teams (groups of actors)
- Roles (responsibilities assigned to actors)
- Reporting structures (edges between actors)
- RACI matrices (responsibility assignment)
- Accountability chains

**UX Questions:**
- How do users interact with org chart elements?
- What queries do users want to run?
- How does visualization work for non-document graphs?
- Can we integrate with real org systems (LDAP, HR databases)?

## Vertex Types Needed

### actor/individual

```yaml
type: vertex/actor/individual
id: a:person:<username>
name: <Full Name>
email: <email>
github: <username>  # optional
roles:
  - r:role:<role-id>
team: g:team:<team-id>
```

### actor/group

```yaml
type: vertex/actor/group
extends: vertex/actor
id: g:team:<team-name>
name: <Team Name>
members:
  - a:person:<username1>
  - a:person:<username2>
lead: a:person:<lead-username>
```

### property/role

```yaml
type: vertex/property/role
id: r:role:<role-name>
name: <Role Title>
responsibilities:
  - <responsibility 1>
  - <responsibility 2>
accountabilities:
  - <what this role is accountable for>
```

## Edge Types Needed

### edge/reports_to

```yaml
type: edge/reports_to
source: a:person:<employee>
target: a:person:<manager>
orientation: directed
relationship: reporting_line
```

### edge/responsible_for

```yaml
type: edge/responsible_for
source: a:person:<person> | g:team:<team>
target: v:doc:<document> | property/artifact:<artifact>
orientation: directed
raci_role: Responsible | Accountable | Consulted | Informed
```

### edge/delegates_to

```yaml
type: edge/delegates_to
source: a:person:<delegator>
target: a:person:<delegate>
artifact: <what is being delegated>
orientation: directed
```

## Chart Example: Knowledge Complex Team

```yaml
type: chart/org_chart
id: c:org:knowledge-complex-team
name: Knowledge Complex Development Team
purpose: Map team structure and responsibilities for knowledge complex project
```

### Vertices

**People:**
- a:person:mzargham - Chief Engineer
- a:person:claude - AI Assistant
- a:person:future-contributor-1 - Future team member

**Teams:**
- g:team:core - Core development team
- g:team:documentation - Documentation team

**Roles:**
- r:role:chief-engineer - Strategic decisions, final approvals
- r:role:ai-assistant - Documentation, verification, preparation
- r:role:contributor - Implementation, testing

### Edges

**Reporting Structure:**
- e:reports_to:claude:mzargham (AI assistant reports to chief engineer)
- e:reports_to:contributor-1:mzargham

**Responsibilities:**
- e:responsible_for:mzargham:v:spec:* (RACI: Accountable for all specs)
- e:responsible_for:claude:verification-edges (RACI: Responsible for verification edges)
- e:responsible_for:claude:validation-prep (RACI: Responsible for validation prep)

**Delegation:**
- e:delegates_to:mzargham:claude:artifact:documentation (Delegates documentation to Claude)

## Face Types Needed

### face/raci_matrix

Shows responsibility assignment for a set of artifacts across team:

```yaml
type: face/raci_matrix
vertices: [actors, artifacts]
edges: [responsible_for edges with RACI annotations]
matrix:
  - artifact: v:spec:persona
    responsible: a:person:claude
    accountable: a:person:mzargham
    consulted: []
    informed: [g:team:core]
```

## Visualization Requirements

**Hierarchical Layout:**
- Chief engineer at top
- Direct reports below
- Teams as clustered groups

**RACI Matrix:**
- Rows = Artifacts
- Columns = People/Teams
- Cells = R/A/C/I indicators

**Responsibility Graph:**
- Nodes = People + Artifacts
- Edges = responsible_for relationships
- Color coded by RACI role

## UX Test Questions

1. **Creation:**
   - How do users add new team members?
   - How do users assign responsibilities?
   - Can we import from existing systems?

2. **Querying:**
   - "Who is responsible for spec-for-persona?"
   - "What is Claude responsible for?"
   - "Show me all Accountable roles for mzargham"
   - "Which artifacts have no owner?"

3. **Visualization:**
   - How to render org hierarchy?
   - How to show RACI matrix readably?
   - Interactive exploration?

4. **Integration:**
   - Can we sync with GitHub teams?
   - Can we validate that code owners match RACI?
   - Can we generate CODEOWNERS from org chart?

5. **Assurance:**
   - How do we verify org chart completeness?
   - How do we validate responsibility assignments?
   - Can we check for accountability gaps?

## Implementation Phases

### Phase 1: Types and Templates
- [ ] Create actor/individual spec and template
- [ ] Create actor/group spec and template
- [ ] Create property/role spec and template
- [ ] Create edge/reports_to spec and template
- [ ] Create edge/responsible_for spec and template

### Phase 2: Example Org Chart
- [ ] Create example people vertices
- [ ] Create example team vertices
- [ ] Create example role vertices
- [ ] Create reporting structure edges
- [ ] Create responsibility edges
- [ ] Create c:org:knowledge-complex-team chart

### Phase 3: Tooling
- [ ] Extend verify_chart.py for org charts
- [ ] Create visualize_org_chart.py
- [ ] Create generate_raci_matrix.py
- [ ] Create query_responsibilities.py

### Phase 4: UX Testing
- [ ] Test with real users
- [ ] Collect feedback on usability
- [ ] Iterate on vertex/edge types
- [ ] Refine visualization approaches

## Connection to Current Work

**Uses existing infrastructure:**
- Vertex/Edge/Face model
- Chart verification
- Assurance framework (can we assure org structures?)

**Extends into new domain:**
- People/teams instead of documents
- Organizational relationships instead of document relationships
- RACI instead of verification/validation

**Benefits:**
- Proves knowledge complex is general-purpose
- Provides concrete accountability mapping
- Enables org-aware tooling (who to ping for reviews, etc.)

## Deferred to Future

This org chart work is intentionally deferred because:
1. Didactic starter repo focuses on document types
2. Actor/role types need design iteration
3. UX patterns need testing with real users
4. Visualization requirements are complex

But planning it now ensures:
- Type system is extensible to non-documents
- Chart infrastructure supports different domains
- We know what's coming and can design accordingly

---

**Note:** This plan captures the vision for org chart support without committing to immediate implementation. It's a stake in the ground for future capability.
