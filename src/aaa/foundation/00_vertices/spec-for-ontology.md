---
type: vertex/spec
extends: doc
id: v:spec:ontology
name: Specification for Ontology Documents
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2026-01-11T00:00:00Z
modified: 2026-01-11T00:00:00Z
description: Defines structural requirements for knowledge complex type ontology documents
schema_type: yaml
strictness: required
---

# Specification for Ontology Documents

## Purpose Statement

An ontology document defines the type system for a knowledge complex. It specifies what vertex types, edge types, face types, and chart types exist; how they inherit from each other; what constraints apply to their construction; and what local rules govern topologically adjacent simplices. Charts are vertices that contain collections of simplices forming valid sub-complexes; they serve both as construction scaffolds (scoping addition of new simplices) and as analytical views (assurance audits, dependency chains, requirements traceability). Ontologies are foundational infrastructure that all other documents in a knowledge complex depend upon.

## Structural Requirements

### Required Frontmatter Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `type` | string | Must be `vertex/ontology` | `vertex/ontology` |
| `extends` | string | Must be `doc` | `doc` |
| `id` | string | Unique identifier with prefix `v:ontology:` | `v:ontology:base` |
| `name` | string | Human-readable ontology name | `Base Ontology for Knowledge Complexes` |
| `tags` | array | Must include `[vertex, doc, ontology]` | `[vertex, doc, ontology]` |
| `version` | string | Semantic version | `1.0.0` |
| `created` | datetime | ISO 8601 creation timestamp | `2026-01-11T00:00:00Z` |
| `modified` | datetime | ISO 8601 last modification | `2026-01-11T00:00:00Z` |
| `description` | string | Brief description of ontology scope | `Foundational types for accountability` |
| `extends_ontology` | string or null | ID of parent ontology, or null for root | `v:ontology:base` or `null` |
| `vertex_type_count` | integer | Number of vertex types defined | `12` |
| `edge_type_count` | integer | Number of edge types defined | `15` |
| `face_type_count` | integer | Number of face types defined | `10` |
| `local_rule_count` | integer | Number of local rules defined | `8` |
| `chart_type_count` | integer | Number of chart types defined | `3` |

### Required Body Sections

| Section | Purpose |
|---------|---------|
| `## Purpose` | Describe what domain this ontology covers and why it exists |
| `## Vertex Types` | Define all 0-simplex types with inheritance hierarchy |
| `## Edge Types` | Define all 1-simplex types with endpoint constraints |
| `## Face Types` | Define all 2-simplex types with boundary and local rules |
| `## Chart Types` | Define chart types (vertices containing simplex collections) |
| `## Local Rules` | Define constraints on topologically adjacent simplices |
| `## Extension Points` | Describe how application ontologies can extend this one |

## Format Constraints

### Vertex Type Definition Format

Each vertex type must be defined with:

```yaml
### <type-name>

**ID Pattern:** `v:<type>:<name>`
**Extends:** <parent-type or 'vertex'>
**Tags:** [vertex, <parent-tags...>, <type>]

**Purpose:** <why this type exists>

**Required Fields:**
| Field | Type | Description |
|-------|------|-------------|
| <field> | <type> | <description> |

**Constraints:**
- <constraint 1>
- <constraint 2>
```

### Edge Type Definition Format

Each edge type must be defined with:

```yaml
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
| Field | Type | Description |
|-------|------|-------------|
| source | string | Source vertex ID |
| target | string | Target vertex ID |
| <additional fields> | <type> | <description> |
```

### Face Type Definition Format

Each face type must be defined with:

```yaml
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
| Field | Type | Description |
|-------|------|-------------|
| boundary_edges | array | IDs of 3 boundary edges |
| boundary_vertices | array | IDs of 3 boundary vertices |
```

### Local Rule Definition Format

Each local rule must be defined with:

```yaml
### <rule-name>

**Rule Type:** <edge-endpoint | face-boundary | face-adjacency | star | degree>
**Constraint Class:** <syntactic | semantic>
**Scope:** <what simplices this rule applies to>
**Constraint:** <formal constraint expression>

**Verification:**
<how to verify this rule is satisfied>

**Example:**
<concrete example of rule application>
```

**Rule Types:**

- `edge-endpoint`: Constraints on vertex types connected by edges
- `face-boundary`: Constraints on edge types forming face boundaries
- `face-adjacency`: Constraints on faces sharing edges
- `star`: Constraints on edges incident to a vertex
- `degree`: Constraints on in/out-degree of vertices for specific edge types

**Constraint Classes:**

- `syntactic`: Structure/type compliance, machine-checkable without context
- `semantic`: Meaning/dependency compliance, may require broader context

### Chart Type Definition Format

Each chart type must be defined with:

```yaml
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
- <requirement 1: e.g., "all edges must connect vertices within the chart">
- <requirement 2: e.g., "all face boundaries must be edges within the chart">
- <requirement 3: e.g., "chart must form a valid simplicial complex">

**Local Rules:**
- <chart-specific local rule 1>
- <chart-specific local rule 2>

**Exit Criteria:** (required for module and runbook charts)
<when execution of this chart is complete - typically: all output documents have assurance faces>

**Required Fields:**
| Field | Type | Description |
|-------|------|-------------|
| vertices | array | IDs of member vertices |
| edges | array | IDs of member edges |
| faces | array | IDs of member faces |
| <additional fields> | <type> | <description> |
```

## Schema Definition

### Ontology Document Schema

```yaml
# Frontmatter schema
type: vertex/ontology
extends: doc
id: v:ontology:<name>  # name in kebab-case
name: string  # human-readable
tags:
  - vertex
  - doc
  - ontology
  # additional tags allowed
version: semver
created: iso8601
modified: iso8601
description: string
extends_ontology: string | null  # v:ontology:<parent> or null
vertex_type_count: integer >= 0
edge_type_count: integer >= 0
face_type_count: integer >= 0
local_rule_count: integer >= 0
chart_type_count: integer >= 0
```

### Type Definition Schema

```yaml
# Schema for individual type definitions
type_definition:
  name: string  # type name in kebab-case
  id_pattern: string  # e.g., "v:<type>:<name>"
  extends: string  # parent type
  tags: array[string]  # inheritance chain
  purpose: string  # why this type exists
  required_fields: array[field_definition]
  constraints: array[string]  # type-specific constraints

field_definition:
  name: string
  type: string  # string, integer, array, datetime, etc.
  description: string
  required: boolean
  default: any  # optional default value
```

### Local Rule Schema

```yaml
# Schema for local rule definitions
local_rule:
  name: string  # rule name
  type: enum[edge-endpoint, face-boundary, face-adjacency, star, degree]
  constraint_class: enum[syntactic, semantic]  # NEW: classification of constraint
  scope: string  # what this rule applies to
  constraint: string  # formal constraint expression
  verification: string  # how to verify
  example: string  # concrete example
```

### Chart Type Schema

```yaml
# Schema for chart type definitions
chart_type:
  name: string  # chart type name in kebab-case
  id_pattern: string  # e.g., "c:<type>:<name>"
  extends: string  # must be "chart" or a chart subtype
  tags: array[string]  # must include [vertex, chart, <type>]
  purpose: string  # why this chart type exists
  use_cases:
    construction: string  # how chart scaffolds simplex addition
    analysis: string  # how chart enables inspection
  membership_constraints:
    vertices:
      types: array[string]  # allowed vertex types
      cardinality: string  # e.g., "1..*", "3", "0..*"
    edges:
      types: array[string]  # allowed edge types
      cardinality: string
    faces:
      types: array[string]  # allowed face types
      cardinality: string
  coherence_requirements: array[string]  # e.g., "edges connect chart vertices"
  local_rules: array[string]  # chart-specific constraints
  required_fields: array[field_definition]
```

## Version-Assurance Semantics

The `version` field follows semantic versioning with assurance implications:

| Change Type | Version Bump | Required Action |
|-------------|--------------|-----------------|
| Typo, formatting | X.Y.Z+1 | Reverification only |
| Content update | X.Y+1.0 | Revalidation required |
| Breaking change | X+1.0.0 | New assurance chain |

**Implications:**

- **Patch (Z+1)**: Minor corrections that don't change meaning. Existing validations remain valid; only reverification needed to confirm structure.
- **Minor (Y+1)**: Content changes that affect quality assessment. Existing validations must be redone by qualified signers.
- **Major (X+1)**: Breaking changes that alter document identity. Treated as an entirely new document requiring full assurance from scratch.

Documents referencing a changed document must update their references when the major version changes.

## Extension Mechanism

### Creating Application Ontologies

An application ontology extends a base ontology by:

1. **Setting `extends_ontology`** to the parent ontology ID
2. **Inheriting all types** from the parent (do not redefine)
3. **Adding new types** that specialize or complement parent types
4. **Adding new local rules** that further constrain the complex
5. **Preserving parent local rules** (cannot weaken, only strengthen)

### ID Naming Convention

Simplex IDs follow a package-like naming convention:

```
<dimension>:<namespace>:<name>
```

Where:
- **dimension** = `v` (vertex), `e` (edge), `f` (face), or `c` (chart)
- **namespace** = type namespace (like a package name)
- **name** = unique identifier within that namespace

**Namespace Hierarchy:**

| Level | Pattern | Example | Who Defines |
|-------|---------|---------|-------------|
| Base | `<dim>:<type>:<name>` | `v:spec:ontology` | Base ontology only |
| Application | `<dim>:<domain>.<type>:<name>` | `v:brand.audience:enterprise` | Application ontologies |
| Instance | `<dim>:<type>:<name>` or `<dim>:<domain>.<type>:<name>` | `v:spec:my-api` | Documents |

The base ontology reserves **root-level type namespaces** (no dot). Application ontologies must use **dotted namespaces** like software packages.

### Reserved Namespaces (Base Ontology)

| Namespace | Dimension | Reserved For |
|-----------|-----------|--------------|
| **Document Namespaces** | | |
| `spec` | v | Structural requirements |
| `guidance` | v | Quality criteria |
| `ontology` | v | Type system definitions |
| `doc` | v | Generic documents |
| `module` | v | Typed I/O transformations |
| **Actor Namespaces** | | |
| `actor` | v | Abstract actors |
| `signer` | v | Signing actors |
| **RBAC Namespaces** | | |
| `role` | v | Organizational positions |
| `authority` | v | Permissions |
| **Assurance Namespaces** | | |
| `verification` | e | Deterministic checks |
| `validation` | e | Human assessments |
| `coupling` | e | Spec-guidance alignment |
| `assurance` | f | Complete attestation |
| `signature` | f | Qualified validation |
| `b2` | f | Bootstrap boundary |
| **Signature Namespaces** | | |
| `signs` | e | Attestation events |
| `qualifies` | e | Credentials |
| **RBAC Edge Namespaces** | | |
| `has-role` | e | Role assignment |
| `conveys` | e | Authority grant |
| `requires-authority` | e | Permission requirement |
| **Module I/O Namespaces** | | |
| `precedes` | e | Module ordering |
| `feeds` | e | Concrete input |
| `yields` | e | Concrete output |
| `input` | f | Input type specification |
| `output` | f | Output type specification |
| `input-satisfaction` | f | Concrete input proof |
| `output-satisfaction` | f | Concrete output proof |
| `module-signature` | f | Module output validation |
| **Document Relationship Namespaces** | | |
| `inherits` | e | Type specialization |
| `instantiates` | e | Type instantiation |
| **Execution Namespaces** | | |
| `execution` | v | State transition events |
| `executes` | e | Links execution to module |
| `follows` | e | Causal ordering (DAG) |
| `consumes` | e | Execution input |
| `produces` | e | Execution output |
| `execution-step` | f | State transition proof |
| **Chart Namespaces** | | |
| `audit` | c | Verification charts |
| `module` | c | Module I/O charts |
| `runbook` | c | Module sequence charts |
| `execution-trace` | c | Causal history (DAG) |
| **RBAC Face Namespaces** | | |
| `authorization` | f | Authority derivation |

### Application Namespace Convention

Application ontologies extend base by adding **dotted namespaces**:

```
<dim>:<domain>.<type>:<name>
```

Where `<domain>` is a unique application identifier (like a package name).

**Examples:**

| Application | Namespace Pattern | Example IDs |
|-------------|-------------------|-------------|
| Brand Management | `brand.<type>` | `v:brand.audience:enterprise`, `e:brand.resonates:tech-innovators` |
| API Documentation | `api.<type>` | `v:api.endpoint:users-list`, `f:api.request-response:get-users` |
| Software Dev | `dev.<type>` | `v:dev.component:auth-service`, `e:dev.depends-on:database` |
| Legal Compliance | `legal.<type>` | `v:legal.regulation:gdpr`, `f:legal.compliance:data-retention` |

**Importing Application Ontologies:**

When an application ontology sets `extends_ontology: v:ontology:base`, it:
1. Inherits all base types (uses root namespaces)
2. Adds new types in its dotted namespace
3. Cannot define types in reserved root namespaces

This is analogous to:
```python
from base_ontology import *  # All base types available
# Define new types in your namespace
brand.audience = ...
brand.resonates = ...
```

### Core Local Rules

The ontology's semantics are defined by local rules. These are the foundational rules for the base ontology:

| Rule | Type | Constraint |
|------|------|------------|
| Module qualification requires output qualifications | star | `qualifies(signer, module)` requires `qualifies(signer, g)` for every guidance `g` in module's output faces |
| Signature face requires guidance qualification | star | `f:signature:(doc, guidance, signer)` requires `qualifies(signer, guidance)` in signer's star |
| Module-signature shares edge with signature | face-adjacency | `f:module-signature:` must share `e:signs:` edge with `f:signature:` face |
| Signature shares edge with assurance | face-adjacency | `f:signature:` must share `e:validation:` edge with `f:assurance:` face |
| Assurance requires b2 anchor | face-adjacency | `f:assurance:` must be adjacent to `f:b2:` sharing `e:coupling:` edge |
| Output satisfaction requires output type | face-adjacency | `f:output-satisfaction:` must share edges with `f:output:` in module chart |
| Input satisfaction requires input type | face-adjacency | `f:input-satisfaction:` must share edges with `f:input:` in module chart |

These rules form a **dense kernel**: module qualification cascades to output qualifications, which cascade to signature faces, which cascade to assurance faces, which anchor to b2 bootstrap faces.

### Extension Example

```yaml
# Application ontology frontmatter
type: vertex/ontology
id: v:ontology:brand
extends_ontology: v:ontology:base
vertex_type_count: 3
edge_type_count: 2
face_type_count: 1
```

```markdown
## Vertex Types

### brand.audience

**ID Pattern:** `v:brand.audience:<name>`
**Extends:** vertex
**Tags:** [vertex, brand.audience]

**Purpose:** Target audience segment for brand content.

### brand.theme

**ID Pattern:** `v:brand.theme:<name>`
**Extends:** vertex
**Tags:** [vertex, brand.theme]

**Purpose:** Content theme aligned with brand identity.

### brand.post (extends doc)

**ID Pattern:** `v:brand.post:<name>`
**Extends:** doc
**Tags:** [vertex, doc, brand.post]

**Purpose:** Social media content targeting specific audiences.

## Edge Types

### brand.resonates

**ID Pattern:** `e:brand.resonates:<name>`
**Extends:** edge
**Tags:** [edge, brand.resonates]

**Purpose:** Audience connects emotionally with theme.

**Endpoint Constraints:**
| Property | Constraint |
|----------|------------|
| source_type | brand.audience |
| target_type | brand.theme |
| direction | directed |

## Face Types

### brand.alignment

**ID Pattern:** `f:brand.alignment:<name>`
**Extends:** face
**Tags:** [face, brand.alignment]

**Purpose:** Proves content aligns theme with target audience.

**Boundary Specification:**
| Vertex | Type Constraint |
|--------|-----------------|
| v1 | brand.post |
| v2 | brand.theme |
| v3 | brand.audience |
```

## Example Instance

See [[ontology-base]] for the foundational ontology that defines core types for accountability, traceability, and auditing.

## Appendices

### Appendix A: JSON Schema (Informative)

For tooling integration, the ontology structure can be expressed as JSON Schema:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Knowledge Complex Ontology Schema",
  "definitions": {
    "vertex": {
      "type": "object",
      "required": ["type", "id", "name", "tags"],
      "properties": {
        "type": {"type": "string", "pattern": "^vertex/"},
        "id": {"type": "string", "pattern": "^v:"},
        "name": {"type": "string"},
        "tags": {
          "type": "array",
          "items": {"type": "string"},
          "contains": {"const": "vertex"}
        }
      }
    },
    "edge": {
      "type": "object",
      "required": ["type", "id", "source", "target"],
      "properties": {
        "type": {"type": "string", "pattern": "^edge/"},
        "id": {"type": "string", "pattern": "^e:"},
        "source": {"type": "string", "pattern": "^v:"},
        "target": {"type": "string", "pattern": "^v:"}
      }
    },
    "face": {
      "type": "object",
      "required": ["type", "id", "boundary_vertices", "boundary_edges"],
      "properties": {
        "type": {"type": "string", "pattern": "^face/"},
        "id": {"type": "string", "pattern": "^f:"},
        "boundary_vertices": {
          "type": "array",
          "items": {"type": "string", "pattern": "^v:"},
          "minItems": 3,
          "maxItems": 3
        },
        "boundary_edges": {
          "type": "array",
          "items": {"type": "string", "pattern": "^e:"},
          "minItems": 3,
          "maxItems": 3
        }
      }
    },
    "chart": {
      "type": "object",
      "required": ["type", "id", "vertices", "edges", "faces"],
      "properties": {
        "type": {"type": "string", "pattern": "^chart/"},
        "id": {"type": "string", "pattern": "^c:"},
        "vertices": {"type": "array", "items": {"type": "string", "pattern": "^v:"}},
        "edges": {"type": "array", "items": {"type": "string", "pattern": "^e:"}},
        "faces": {"type": "array", "items": {"type": "string", "pattern": "^f:"}}
      }
    }
  }
}
```

This schema is informative; the authoritative definition is the markdown specification above.

---

**Note:** This specification defines what ontology documents must contain. The [[guidance-for-ontology]] provides quality criteria for evaluating ontology design.
