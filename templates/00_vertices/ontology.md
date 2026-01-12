---
type: vertex/ontology
extends: doc
id: v:ontology:<name>
name: <Name>
tags:
  - vertex
  - doc
  - ontology
version: <Version>
created: YYYY-MM-DDTHH:MM:SSZ
modified: YYYY-MM-DDTHH:MM:SSZ
description: <Brief description of ontology scope>
extends_ontology: <v:ontology:parent or null>
vertex_type_count: <count>
edge_type_count: <count>
face_type_count: <count>
local_rule_count: <count>
chart_type_count: <count>
---

# <Name>

## Purpose

[Describe what domain this ontology covers and why it exists. If extending another ontology, reference the parent and explain what this extension adds.]

## Vertex Types

[Define all 0-simplex types with inheritance hierarchy. Organize by category.]

### <type-name>

**ID Pattern:** `v:<type>:<name>`
**Extends:** <parent-type or 'vertex'>
**Tags:** [vertex, <parent-tags...>, <type>]

**Purpose:** <why this type exists>

**Required Fields:**

| Name | Data Type | Description |
|------|-----------|-------------|
| <field> | <type> | <description> |

**Constraints:**

- <constraint 1>
- <constraint 2>

## Edge Types

[Define all 1-simplex types with endpoint constraints. Group by semantic category.]

### <type-name>

**ID Pattern:** `e:<type>:<name>`
**Extends:** edge
**Tags:** [edge, <type>]

**Purpose:** <why this edge type exists>

**Endpoint Constraints:**

| Property | Constraint |
|----------|------------|
| source_type | <allowed vertex types> |
| target_type | <allowed vertex types> |
| direction | directed or undirected |

**Required Fields:**

| Name | Data Type | Description |
|------|-----------|-------------|
| source | string | Source vertex ID |
| target | string | Target vertex ID |

## Face Types

[Define all 2-simplex types with boundary specifications.]

### <type-name>

**ID Pattern:** `f:<type>:<name>`
**Extends:** face
**Tags:** [face, <type>]

**Purpose:** <why this face type exists>

**Boundary Specification:**

| Vertex | Type Constraint |
|--------|-----------------|
| v1 | <allowed types> |
| v2 | <allowed types> |
| v3 | <allowed types> |

| Edge | Type | Connects |
|------|------|----------|
| e1 | <edge-type> | v1 → v2 |
| e2 | <edge-type> | v2 → v3 |
| e3 | <edge-type> | v1 → v3 |

**Local Rules:**

- <local rule 1>
- <local rule 2>

**Required Fields:**

| Name | Data Type | Description |
|------|-----------|-------------|
| boundary_edges | array | IDs of 3 boundary edges |
| boundary_vertices | array | IDs of 3 boundary vertices |

## Chart Types

[Define chart types that serve as construction scaffolds and analytical views.]

### <type-name>

**ID Pattern:** `c:<type>:<name>`
**Extends:** chart
**Tags:** [vertex, chart, <type>]

**Purpose:** <why this chart type exists>

**Use Cases:**

- **Construction:** <how this chart type scaffolds new simplex addition>
- **Analysis:** <how this chart type enables inspection or interpretation>

**Membership Constraints:**

| Simplex Dimension | Type Constraints | Cardinality |
|-------------------|------------------|-------------|
| vertices | <allowed vertex types> | <min..max or *> |
| edges | <allowed edge types> | <min..max or *> |
| faces | <allowed face types> | <min..max or *> |

**Coherence Requirements:**

- All edges must connect vertices within the chart
- All face boundaries must be edges within the chart
- Chart must form a valid simplicial complex

**Local Rules:**

- <chart-specific local rule 1>
- <chart-specific local rule 2>

**Exit Criteria:** (required for module and runbook charts)

<when execution of this chart is complete - typically: all output documents have assurance faces, validated by qualified signers>

**Required Fields:**

| Name | Data Type | Description |
|------|-----------|-------------|
| vertices | array | IDs of member vertices |
| edges | array | IDs of member edges |
| faces | array | IDs of member faces |

## Local Rules

[Define constraints on topologically adjacent simplices. Organize by rule type.]

### <rule-name>

**Rule Type:** <edge-endpoint | face-boundary | face-adjacency | star>
**Scope:** <what simplices this rule applies to>
**Constraint:** <formal constraint expression>

**Verification:**

<how to verify this rule is satisfied>

**Example:**

<concrete example of rule application>

## Extension Points

[Describe how application ontologies can extend this one.]

### Reserved Prefixes

[List prefixes reserved by this ontology]

### Extension Guidelines

1. Set `extends_ontology` to this ontology's ID
2. Inherit all types from parent (do not redefine)
3. Add new types using `v:app:`, `e:app:`, `f:app:`, `c:app:` prefixes
4. Add new local rules that further constrain (cannot weaken parent rules)
5. Document extensions with reference to parent for inherited types

---

**Note:** This ontology defines types for [domain]. See [[spec-for-ontology]] for structural requirements and [[guidance-for-ontology]] for quality criteria.
