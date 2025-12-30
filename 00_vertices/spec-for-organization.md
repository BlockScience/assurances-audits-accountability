---
type: vertex/spec
extends: vertex/doc
id: v:spec:organization
name: Specification for Organization Charts
description: Defines the structure and constraints for organization chart type documents representing teams, roles, resources, and their relationships
tags:
  - vertex
  - spec
  - chart-type
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
dependencies:
  - v:spec:chart
---

# Specification for Organization Charts

## Purpose

This specification defines the **organization chart type** - a specialized chart representing organizational structure through actors (teams, staff, roles), properties (skills, responsibilities), resources (functions, artifacts), and their relationships.

Organization charts encode organizational topology as simplicial complexes where:
- **Vertices** represent actors (teams, staff, roles), properties (skills, responsibilities), resources (functions, artifacts, infrastructure)
- **Edges** represent relationships (membership, assignment, operation, production, consumption)
- **Faces** represent constraints (RACI assignments, resource dependencies, cross-team flows)

## Document Type

**Type:** `chart/organization`

**Extends:** `chart/chart` (inherits all chart requirements plus organization-specific constraints)

## Chart Subtypes

Organization charts come in three primary variants:

| Subtype | Focus | Key Vertices | Key Edges | Key Faces |
|---------|-------|--------------|-----------|-----------|
| **Coordination** | People & responsibilities | team, staff, role | member, holds-role, assigned | assignment (RACI) |
| **Management** | Resources & flows | team, function, resource | operates, produces, consumes | dependency, flow |
| **Composed** | Complete organization | All of above | All of above | All of above |

## Required Frontmatter Fields

All fields from `chart/chart` specification PLUS:

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| `type` | string | Must be `chart/organization` | Yes |
| `extends` | string | Must be `chart` | Yes |
| `organization_type` | enum | One of: `coordination`, `management`, `composed` | Yes |
| `organization_scope` | object | Defines organizational boundaries | Yes |
| `organization_scope.teams` | list[string] | Team vertex IDs included | Yes |
| `organization_scope.primary_focus` | string | Main purpose of this chart | Yes |

### Coordination-Specific Fields

For `organization_type: coordination`:

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| `coordination_metadata` | object | Coordination chart details | Yes |
| `coordination_metadata.staff_count` | int | Number of staff vertices | Yes |
| `coordination_metadata.role_count` | int | Number of role vertices | Yes |
| `coordination_metadata.raci_coverage` | string | Description of RACI completeness | Yes |

### Management-Specific Fields

For `organization_type: management`:

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| `management_metadata` | object | Management chart details | Yes |
| `management_metadata.function_count` | int | Number of function vertices | Yes |
| `management_metadata.resource_count` | int | Number of resource vertices | Yes |
| `management_metadata.flow_description` | string | Description of primary flows | Yes |

### Composed-Specific Fields

For `organization_type: composed`:

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| `composition_metadata` | object | Composition details | Yes |
| `composition_metadata.source_charts` | list[string] | Chart IDs being composed | Yes |
| `composition_metadata.shared_vertices` | list[string] | Vertices shared across charts | Yes |
| `composition_metadata.emergent_edges` | list[string] | New edges discovered in composition | No |

### Example Frontmatter

```yaml
---
type: chart/organization
extends: chart
id: c:org:platform-team-coordination
name: Platform Team Coordination Chart
description: Coordination chart showing Platform Team structure and responsibilities

# Chart construction metadata
constructed_by: "Claude (LLM-assisted)"
construction_method: assisted
construction_date: 2025-12-29T00:00:00Z

# Chart purpose
purpose: Document team structure and RACI responsibilities for the Platform Team
scope: Platform Team members, roles, and responsibility assignments

# Organization-specific metadata
organization_type: coordination
organization_scope:
  teams:
    - v:actor:team:platform
  primary_focus: Team structure and RACI accountability

coordination_metadata:
  staff_count: 3
  role_count: 2
  raci_coverage: "Complete for deployment and monitoring responsibilities"

# Elements comprising this chart
elements:
  vertices: [...]
  edges: [...]
  faces: [...]

tags:
  - chart
  - organization
  - coordination
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
---
```

## Required Body Sections

All sections from `chart/chart` specification PLUS organization-specific sections:

### 1. Purpose (from chart spec)

### 2. Organization Structure (ENHANCED)

Must document vertices, edges, and faces with **organization-specific categorization**:

#### Vertices (categorized by domain type)

**Actors:**
- Teams - organizational units
- Staff - individual people
- Roles - functional positions

**Properties (coordination only):**
- Skills - capabilities
- Responsibilities - assigned duties

**Resources (management only):**
- Functions - operational capabilities
- Resources - artifacts, infrastructure, capabilities consumed/produced

#### Edges (categorized by relationship type)

**Coordination Edges:**
- `member` - staff → team (membership)
- `holds-role` - staff → role (position)
- `includes` - team → role (role definition)
- `assigned` - role → responsibility (duty assignment)
- `has-skill` - staff → skill (capability possession)

**Management Edges:**
- `operates` - team → function (operational control)
- `produces` - function → resource (output)
- `consumes` - function → resource (input)
- `owns` - team → resource (ownership)

**Cross-Cutting Edges:**
- `depends-on` - resource → resource (dependency)
- `requires` - function → skill (capability requirement)

#### Faces (categorized by semantic type)

**Assignment Faces (coordination):**
- Pattern: `(staff, role, responsibility)`
- RACI types: Responsible, Accountable, Consulted, Informed
- Constraint: Exactly one Accountable per responsibility

**Dependency Faces (management):**
- Pattern: `(team, resource, team)` for cross-team dependencies
- Pattern: `(function, resource, function)` for functional chains

**Flow Faces (management):**
- Pattern: `(team, function, resource)` for production
- Pattern: `(resource, function, team)` for consumption

### 3. Topological Properties (from chart spec)

Must calculate and document V, E, F, and χ

### 4. Organizational Analysis (NEW - required for organization charts)

Must document organizational insights:

```markdown
## Organizational Analysis

### Structure Summary
- **Teams:** [count] organizational units
- **Staff:** [count] individuals (coordination only)
- **Roles:** [count] functional positions (coordination only)
- **Functions:** [count] operational capabilities (management only)
- **Resources:** [count] assets managed (management only)

### Key Relationships
[Document the most important structural relationships]

### Accountability Coverage (coordination)
[Document RACI completeness - are all responsibilities assigned?]

### Resource Flow Analysis (management)
[Document critical paths, bottlenecks, cross-team dependencies]

### Topology Interpretation
[Connect χ and structural properties to organizational meaning]
```

### 5. Constraint Validation (NEW - required for organization charts)

Must validate and document compliance with organizational constraints:

```markdown
## Constraint Validation

### RACI Constraints (coordination)
- ✓ Every responsibility has exactly one Accountable
- ✓ At least one Responsible per responsibility
- ✓ No orphan roles (every role assigned to someone)

### Resource Flow Constraints (management)
- ✓ No cycles in primary production chain
- ✓ All consumed resources have producers
- ✓ Critical path identified

### Composition Constraints (composed)
- ✓ Shared vertices have consistent properties
- ✓ No conflicting edges from source charts
- ✓ Emergent edges documented
```

### 6. Expected Tool Behavior (from chart spec)

## Local Constraint Rules

Organization charts MUST satisfy these local constraints:

### Vertex Type Constraints

1. **Team vertices** (`vertex/actor/team`):
   - Must have `members` list (may be empty for stub teams)
   - Must have `responsibilities` list (may be empty)

2. **Staff vertices** (`vertex/actor/staff`):
   - Must have `roles` list (may be empty)
   - Must belong to at least one team (member edge exists)

3. **Role vertices** (`vertex/actor/role`):
   - Must have `responsibilities` list
   - Must be included in at least one team

4. **Function vertices** (`vertex/function`):
   - Must have `operated_by` field (team reference)
   - Must have `inputs` and `outputs` lists

5. **Resource vertices** (`vertex/resource`):
   - Must have `resource_type` (capability, artifact, infrastructure)
   - Must have `owner` field (team reference)

### Edge Type Constraints

**Coordination Edges:**

1. **member edges** (staff → team):
   - Source must be staff vertex
   - Target must be team vertex
   - Creates membership relationship

2. **holds-role edges** (staff → role):
   - Source must be staff vertex
   - Target must be role vertex
   - Staff can hold multiple roles

3. **includes edges** (team → role):
   - Source must be team vertex
   - Target must be role vertex
   - Role can be included in multiple teams

4. **assigned edges** (role → responsibility):
   - Source must be role vertex
   - Target must be responsibility vertex
   - Must have `raci_type` property (R, A, C, or I)

**Management Edges:**

5. **operates edges** (team → function):
   - Source must be team vertex
   - Target must be function vertex
   - Creates operational control relationship

6. **produces edges** (function → resource):
   - Source must be function vertex
   - Target must be resource vertex
   - Creates output relationship

7. **consumes edges** (function → resource):
   - Source must be function vertex
   - Target must be resource vertex
   - May have `blocking` property (true if blocking dependency)

### Face Type Constraints

**Assignment Faces (coordination):**
- Pattern: `(staff, role, responsibility)`
- Boundary edges: holds-role, assigned, (implicit staff→responsibility)
- RACI constraint: Exactly one A per responsibility across all faces

**Production Faces (management):**
- Pattern: `(team, function, resource)`
- Boundary edges: operates, produces, owns
- Represents team producing resource via function

**Consumption Faces (management):**
- Pattern: `(team, function, resource)`
- Boundary edges: operates, consumes, (uses or dependency edge)
- Represents team consuming resource via function

**Cross-Team Dependency Faces (management):**
- Pattern: `(team-producer, resource, team-consumer)`
- Captures handoff points between teams
- Critical for identifying integration points

### Composition Constraints (for composed charts)

1. **Shared Vertex Consistency:**
   - Team vertices appearing in both coordination and management charts must have identical `id` and consistent properties
   - Merging preserves all edges from both source charts

2. **No Edge Conflicts:**
   - Same edge ID cannot have different source/target in different charts
   - Conflicting relationships must be resolved before composition

3. **Emergent Edge Documentation:**
   - New meaningful relationships discovered through composition should be documented
   - Example: Staff operates function (via team membership)

## Quality Criteria

A well-formed organization chart:

1. **Completeness:** All actors have relationships; no orphan vertices
2. **Consistency:** RACI rules satisfied; flows are acyclic
3. **Validity:** All local constraints satisfied
4. **Meaningful:** Topology reflects actual organizational structure
5. **Maintainable:** Clear scope boundaries; documented assumptions

## Anti-Patterns

### Multiple Accountables

```yaml
# INVALID: Two people accountable for same responsibility
f:assignment:alice:lead:deploy  # raci_type: A
f:assignment:bob:manager:deploy # raci_type: A
❌ Violates single-accountable constraint
```

### Orphan Resources

```yaml
# INVALID: Resource with no producer
v:resource:artifact-x
# No produces edge to artifact-x
❌ Resource has no source
```

### Circular Dependencies

```yaml
# INVALID: Cycle in resource dependencies
function-A consumes resource-X
function-B produces resource-X
function-B consumes resource-Y
function-A produces resource-Y
❌ Circular dependency chain
```

### Inconsistent Composition

```yaml
# INVALID: Same team, different members
# In coordination chart:
team:platform.members = [alice, bob]
# In management chart:
team:platform.members = [alice, charlie]
❌ Conflicting team definition
```

## Verification

Organization charts can be verified using:

```bash
# Standard chart verification
python scripts/verify_chart.py charts/<org-chart>/<org-chart>.md

# Topology analysis
python scripts/topology.py charts/<org-chart>/<org-chart>.md

# RACI validation (if implemented)
python scripts/validate_raci.py charts/<org-chart>/<org-chart>.md
```

## Visualization

**Required:** Organization charts MUST include visualization with semantic color coding.

### Recommended Visualizer

```bash
# Export chart to JSON
python scripts/export_chart_direct.py charts/<org-chart>/<org-chart>.md

# Generate interactive visualization
python scripts/visualize_chart.py charts/<org-chart>/<org-chart>.json
```

### Color Coding Convention

**Coordination Charts:**
- Teams: Blue
- Staff: Green
- Roles: Purple
- Responsibilities: Orange

**Management Charts:**
- Teams: Blue
- Functions: Purple
- Resources: Green (artifacts), Yellow (infrastructure), Cyan (capabilities)

**Composed Charts:**
- Shared vertices (teams): Blue with highlight
- Coordination-only vertices: Warm colors
- Management-only vertices: Cool colors

---

**Note:** This specification extends chart/chart with organization-specific structure and constraints. Organization charts model real-world organizational topology through typed simplicial complexes, enabling formal analysis of team structure, accountability, and resource flows.
