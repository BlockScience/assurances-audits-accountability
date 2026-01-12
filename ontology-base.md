---
type: vertex/ontology
extends: doc
id: v:ontology:base
name: Base Ontology for Knowledge Complexes
tags:
  - vertex
  - doc
  - ontology
version: 1.0.0
created: 2026-01-11T00:00:00Z
modified: 2026-01-11T00:00:00Z
description: Foundational type ontology for accountability, traceability, and auditing in knowledge complexes
extends_ontology: null
vertex_type_count: 10
edge_type_count: 13
face_type_count: 9
local_rule_count: 12
chart_type_count: 3
---

# Base Ontology for Knowledge Complexes

## Purpose

This ontology defines the foundational type system for knowledge complexes focused on accountability, traceability, and auditing. It establishes the primitive types from which application-specific ontologies are built through extension.

The ontology covers three interlocking systems:

1. **Role-Based Access Control (RBAC)**: Who can do what - actors, roles, authorities, and their relationships
2. **Modules & Runbooks**: Typed I/O transformations and their chains - specs for work products and the processes that produce them
3. **Document Assurance**: Verification, validation, and signatures - the accountability infrastructure that makes documents trustworthy

Every authorization, transformation, or attestation is expressed as a **face (triangle)**. Faces are the atomic units of meaning. Local rules on faces enable compositional verification - checking each simplex locally guarantees global coherence.

## Vertex Types

### Abstract Base Type

#### vertex

**ID Pattern:** `v:<type>:<name>`
**Extends:** (root type)
**Tags:** [vertex]

**Purpose:** The abstract root of all vertex types. All vertices in a knowledge complex are typed, and all types inherit from this base.

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| type | string | The vertex type (e.g., `vertex/doc`, `vertex/spec`) |
| id | string | Unique identifier with prefix `v:<type>:` |
| name | string | Human-readable name |
| tags | array | Type inheritance chain starting with `vertex` |

**Constraints:**

- ID must be unique within the knowledge complex
- Tags must include complete inheritance chain
- Type must match a defined vertex type in the ontology

### Document Types

#### doc

**ID Pattern:** `v:doc:<name>`
**Extends:** vertex
**Tags:** [vertex, doc]

**Purpose:** Content artifacts - things that get authored, verified, validated, and assured. Documents are the primary work products in a knowledge complex.

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| type | string | Must be `vertex/doc` or subtype |
| extends | string | Parent type (must be `doc` or a doc subtype) |
| version | string | Semantic version |
| created | datetime | ISO 8601 creation timestamp |
| modified | datetime | ISO 8601 last modification |
| description | string | Brief description of document purpose |

**Constraints:**

- Must have verification edge to its governing spec
- Should have validation edge to its governing guidance (for assured docs)

#### spec

**ID Pattern:** `v:spec:<name>`
**Extends:** doc
**Tags:** [vertex, doc, spec]

**Purpose:** Structural requirements for a document type. Specs define WHAT structure a document must have - the deterministic, machine-checkable constraints.

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| type | string | Must be `vertex/spec` |
| extends | string | Must be `doc` |
| schema_type | string | Schema format (yaml, json, markdown) |
| strictness | string | Enforcement level (required, recommended, optional) |

**Constraints:**

- Must be coupled to a guidance document via coupling edge
- Defines required frontmatter fields and body sections

#### guidance

**ID Pattern:** `v:guidance:<name>`
**Extends:** doc
**Tags:** [vertex, doc, guidance]

**Purpose:** Quality criteria for a document type. Guidances define HOW WELL a document should be written - the qualitative, human-judged aspects.

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| type | string | Must be `vertex/guidance` |
| extends | string | Must be `doc` |
| criteria | array | List of quality criteria names |
| rubric | string | Assessment scale (e.g., excellent/good/needs-improvement) |

**Constraints:**

- Must be coupled to a spec document via coupling edge
- Signers validating against this guidance must have qualifies edge to it

#### ontology

**ID Pattern:** `v:ontology:<name>`
**Extends:** doc
**Tags:** [vertex, doc, ontology]

**Purpose:** Type system definitions for a knowledge complex. Ontologies define what vertex, edge, face, and chart types exist and how they relate.

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| type | string | Must be `vertex/ontology` |
| extends | string | Must be `doc` |
| extends_ontology | string or null | Parent ontology ID or null for root |
| vertex_type_count | integer | Number of vertex types defined |
| edge_type_count | integer | Number of edge types defined |
| face_type_count | integer | Number of face types defined |
| local_rule_count | integer | Number of local rules defined |
| chart_type_count | integer | Number of chart types defined |

**Constraints:**

- Type counts must match actual definitions in document body
- If extending another ontology, cannot redefine parent types
- Extension can only add types and strengthen (not weaken) local rules

### Actor Types

#### actor

**ID Pattern:** `v:actor:<name>`
**Extends:** vertex
**Tags:** [vertex, actor]

**Purpose:** Entities that can act in the system. Actors can hold roles, exercise authorities, and participate in workflows.

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| type | string | Must be `vertex/actor` or subtype |
| extends | string | Must be `vertex` or actor subtype |

**Constraints:**

- Abstract type - use concrete subtypes like signer

#### signer

**ID Pattern:** `v:signer:<name>`
**Extends:** actor
**Tags:** [vertex, actor, signer]

**Purpose:** Actor with verified identity who can sign documents. Signers create accountability by attaching their identity to validation edges.

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| type | string | Must be `vertex/signer` |
| extends | string | Must be `actor` |
| identity | string | Verified identity (email, GPG key, etc.) |

**Constraints:**

- Must have qualifies edge to each guidance they sign validations against
- Signs edges must include timestamp and commit hash

### Organizational Types

#### role

**ID Pattern:** `v:role:<name>`
**Extends:** vertex
**Tags:** [vertex, role]

**Purpose:** Organizational position that conveys authorities. Roles are the intermediate layer between actors and authorities in RBAC.

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| type | string | Must be `vertex/role` |
| extends | string | Must be `vertex` |
| description | string | What this role represents |

**Constraints:**

- Must have at least one conveys edge to an authority
- Actors receive role via has-role edge

**Examples:** `v:role:approver`, `v:role:author`, `v:role:architect`

#### authority

**ID Pattern:** `v:authority:<name>`
**Extends:** vertex
**Tags:** [vertex, authority]

**Purpose:** Permission to perform specific actions. Authorities are the atomic units of access control - what a role allows an actor to do.

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| type | string | Must be `vertex/authority` |
| extends | string | Must be `vertex` |
| action | string | What action this authority permits |
| scope | string | What this authority applies to |

**Constraints:**

- Conveyed by roles via conveys edge
- Required by actions via requires-authority edge

**Examples:** `v:authority:validate-against:guidance-X`, `v:authority:approve-module:M`

### Module Type

#### module

**ID Pattern:** `v:module:<name>`
**Extends:** doc
**Tags:** [vertex, doc, module]

**Purpose:** Typed I/O transformation specification. A module defines a process with explicit input and output type requirements. Modules are self-referential - they are charts that contain themselves as a vertex.

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| type | string | Must be `vertex/module` |
| extends | string | Must be `doc` |
| input_count | integer | Number of input type specifications |
| output_count | integer | Number of output type specifications |

**Constraints:**

- Must have at least one input face (`f:input:`)
- Must have at least one output face (`f:output:`)
- Signers qualified for this module must be qualified for ALL output guidances

## Edge Types

### Assurance Edges

#### verification

**ID Pattern:** `e:verification:<name>`
**Extends:** edge
**Tags:** [edge, verification]

**Purpose:** Deterministic structural check. A verification edge attests that a document passes all machine-checkable requirements defined by its spec.

**Endpoint Constraints:**

| Property | Constraint |
|----------|------------|
| source_type | doc (or any doc subtype) |
| target_type | spec |
| direction | directed |

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| source | string | Document vertex ID |
| target | string | Spec vertex ID |
| verifier | string | Tool or process that performed verification |
| result | string | pass or fail |
| timestamp | datetime | When verification was performed |

#### validation

**ID Pattern:** `e:validation:<name>`
**Extends:** edge
**Tags:** [edge, validation]

**Purpose:** Human quality assessment. A validation edge attests that a qualified signer has judged a document meets the quality criteria defined by its guidance.

**Endpoint Constraints:**

| Property | Constraint |
|----------|------------|
| source_type | doc (or any doc subtype) |
| target_type | guidance |
| direction | directed |

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| source | string | Document vertex ID |
| target | string | Guidance vertex ID |
| validator | string | Signer vertex ID |
| assessment | object | Scores per criterion |
| timestamp | datetime | When validation was performed |

#### coupling

**ID Pattern:** `e:coupling:<name>`
**Extends:** edge
**Tags:** [edge, coupling]

**Purpose:** Semantic alignment between spec and guidance. A coupling edge declares that a spec and guidance document together govern a document type.

**Endpoint Constraints:**

| Property | Constraint |
|----------|------------|
| source_type | spec |
| target_type | guidance |
| direction | undirected |

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| source | string | Spec vertex ID |
| target | string | Guidance vertex ID |
| governed_type | string | Document type this pair governs |

### Signature/Accountability Edges

#### signs

**ID Pattern:** `e:signs:<name>`
**Extends:** edge
**Tags:** [edge, signs]

**Purpose:** Attestation event. A signs edge records that a signer has attached their identity to a document, creating accountability.

**Endpoint Constraints:**

| Property | Constraint |
|----------|------------|
| source_type | signer |
| target_type | doc (or any doc subtype) |
| direction | directed |

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| source | string | Signer vertex ID |
| target | string | Document vertex ID |
| timestamp | datetime | When signature was created |
| commit_hash | string | Git commit hash at signing time |

#### qualifies

**ID Pattern:** `e:qualifies:<name>`
**Extends:** edge
**Tags:** [edge, qualifies]

**Purpose:** Credential authorizing validation. A qualifies edge records that a signer has the expertise, role, delegation, or certification to validate against a particular guidance or execute a particular module.

**Endpoint Constraints:**

| Property | Constraint |
|----------|------------|
| source_type | signer |
| target_type | guidance OR module |
| direction | directed |

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| source | string | Signer vertex ID |
| target | string | Guidance or Module vertex ID |
| credential_type | string | expertise, delegation, certification, role |
| granted_by | string | Authority that granted this qualification |
| valid_from | datetime | When qualification became valid |

### RBAC Edges

#### has-role

**ID Pattern:** `e:has-role:<name>`
**Extends:** edge
**Tags:** [edge, has-role]

**Purpose:** Actor holds organizational position. Links an actor to a role they occupy.

**Endpoint Constraints:**

| Property | Constraint |
|----------|------------|
| source_type | actor (or any actor subtype) |
| target_type | role |
| direction | directed |

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| source | string | Actor vertex ID |
| target | string | Role vertex ID |
| granted_by | string | Authority that assigned this role |
| valid_from | datetime | When role assignment began |

#### conveys

**ID Pattern:** `e:conveys:<name>`
**Extends:** edge
**Tags:** [edge, conveys]

**Purpose:** Role grants permission. Links a role to the authorities it bestows on actors holding that role.

**Endpoint Constraints:**

| Property | Constraint |
|----------|------------|
| source_type | role |
| target_type | authority |
| direction | directed |

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| source | string | Role vertex ID |
| target | string | Authority vertex ID |

#### requires-authority

**ID Pattern:** `e:requires-authority:<name>`
**Extends:** edge
**Tags:** [edge, requires-authority]

**Purpose:** Action requires permission. Links an action or document to the authority needed to perform or approve it.

**Endpoint Constraints:**

| Property | Constraint |
|----------|------------|
| source_type | vertex (any action-representing vertex) |
| target_type | authority |
| direction | directed |

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| source | string | Action vertex ID |
| target | string | Authority vertex ID |

### Module I/O Edges

#### precedes

**ID Pattern:** `e:precedes:<name>`
**Extends:** edge
**Tags:** [edge, precedes]

**Purpose:** Module ordering in runbook. Establishes that one module must complete before another can begin.

**Endpoint Constraints:**

| Property | Constraint |
|----------|------------|
| source_type | module |
| target_type | module |
| direction | directed |

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| source | string | Prior module vertex ID |
| target | string | Subsequent module vertex ID |

#### feeds

**ID Pattern:** `e:feeds:<name>`
**Extends:** edge
**Tags:** [edge, feeds]

**Purpose:** Concrete input provision. Links an actual input document to a module it satisfies input requirements for.

**Endpoint Constraints:**

| Property | Constraint |
|----------|------------|
| source_type | doc (or any doc subtype) |
| target_type | module |
| direction | directed |

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| source | string | Input document vertex ID |
| target | string | Module vertex ID |
| satisfies_input | string | Which input type specification this satisfies |

#### yields

**ID Pattern:** `e:yields:<name>`
**Extends:** edge
**Tags:** [edge, yields]

**Purpose:** Concrete output production. Links a module to an actual output document it produced.

**Endpoint Constraints:**

| Property | Constraint |
|----------|------------|
| source_type | module |
| target_type | doc (or any doc subtype) |
| direction | directed |

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| source | string | Module vertex ID |
| target | string | Output document vertex ID |
| satisfies_output | string | Which output type specification this satisfies |

### Document Relationship Edges

#### inherits

**ID Pattern:** `e:inherits:<name>`
**Extends:** edge
**Tags:** [edge, inherits]

**Purpose:** Domain specialization. Links a spec to a parent spec it extends. Separate from assurance DAG - this is for type hierarchy.

**Endpoint Constraints:**

| Property | Constraint |
|----------|------------|
| source_type | spec |
| target_type | spec |
| direction | directed |

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| source | string | Child spec vertex ID |
| target | string | Parent spec vertex ID |

#### instantiates

**ID Pattern:** `e:instantiates:<name>`
**Extends:** edge
**Tags:** [edge, instantiates]

**Purpose:** Document is instance of type. Links a document to the spec that defines its type.

**Endpoint Constraints:**

| Property | Constraint |
|----------|------------|
| source_type | doc (or any doc subtype) |
| target_type | spec |
| direction | directed |

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| source | string | Document vertex ID |
| target | string | Spec vertex ID |

## Face Types

### Assurance Faces

#### assurance

**ID Pattern:** `f:assurance:<name>`
**Extends:** face
**Tags:** [face, assurance]

**Purpose:** Complete document attestation. An assurance face proves a document has both passed structural verification AND received qualified human validation.

**Boundary Specification:**

| Vertex | Type Constraint |
|--------|-----------------|
| v1 | doc (the assured document) |
| v2 | spec (its governing spec) |
| v3 | guidance (its governing guidance) |

| Edge | Type | Connects |
|------|------|----------|
| e1 | verification | v1 → v2 |
| e2 | validation | v1 → v3 |
| e3 | coupling | v2 ↔ v3 |

**Local Rules:**

- Must be adjacent to a b2 face sharing the coupling edge
- Must be adjacent to a signature face sharing the validation edge

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| boundary_edges | array | IDs of [verification, validation, coupling] edges |
| boundary_vertices | array | IDs of [doc, spec, guidance] vertices |

#### signature

**ID Pattern:** `f:signature:<name>`
**Extends:** face
**Tags:** [face, signature]

**Purpose:** Qualified validation attestation. A signature face proves that a specific signer with verified qualifications signed a validation.

**Boundary Specification:**

| Vertex | Type Constraint |
|--------|-----------------|
| v1 | doc (the validated document) |
| v2 | guidance (the quality criteria) |
| v3 | signer (the qualified validator) |

| Edge | Type | Connects |
|------|------|----------|
| e1 | validation | v1 → v2 |
| e2 | qualifies | v3 → v2 |
| e3 | signs | v3 → v1 |

**Local Rules:**

- Signer's star must contain qualifies edge to the guidance
- Must share validation edge with an assurance face

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| boundary_edges | array | IDs of [validation, qualifies, signs] edges |
| boundary_vertices | array | IDs of [doc, guidance, signer] vertices |

#### b2

**ID Pattern:** `f:b2:<name>`
**Extends:** face
**Tags:** [face, b2]

**Purpose:** Bootstrap boundary face. Anchors assurance network to root trust. B2 faces are self-referential - specs and guidances assuring themselves.

**Boundary Specification:**

| Vertex | Type Constraint |
|--------|-----------------|
| v1 | spec or guidance (the bootstrap document) |
| v2 | spec (spec-for-spec or spec-for-guidance) |
| v3 | guidance (guidance-for-spec or guidance-for-guidance) |

| Edge | Type | Connects |
|------|------|----------|
| e1 | verification | v1 → v2 |
| e2 | validation | v1 → v3 |
| e3 | coupling | v2 ↔ v3 |

**Local Rules:**

- Forms boundary of assurance network (no further ancestry required)
- Must anchor at least one assurance face via shared coupling edge

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| boundary_edges | array | IDs of boundary edges |
| boundary_vertices | array | IDs of boundary vertices |
| anchor_type | string | `spec-spec` or `guidance-guidance` |

### RBAC Faces

#### authorization

**ID Pattern:** `f:authorization:<name>`
**Extends:** face
**Tags:** [face, authorization]

**Purpose:** Actor authority derivation. Proves that an actor has a specific authority through their role assignment.

**Boundary Specification:**

| Vertex | Type Constraint |
|--------|-----------------|
| v1 | actor (or signer) |
| v2 | role |
| v3 | authority |

| Edge | Type | Connects |
|------|------|----------|
| e1 | has-role | v1 → v2 |
| e2 | conveys | v2 → v3 |
| e3 | (derived) | v1 → v3 (actor has authority) |

**Local Rules:**

- The authority must match action requirements for permissions to be valid
- Actor-authority derivation is transitive through role

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| boundary_edges | array | IDs of [has-role, conveys, derived] edges |
| boundary_vertices | array | IDs of [actor, role, authority] vertices |

### Module I/O Faces

#### input

**ID Pattern:** `f:input:<name>`
**Extends:** face
**Tags:** [face, input]

**Purpose:** Module input type specification. Defines that a module requires input conforming to a particular spec, assessed against a particular guidance.

**Boundary Specification:**

| Vertex | Type Constraint |
|--------|-----------------|
| v1 | spec (input type spec) |
| v2 | guidance (input quality guidance) |
| v3 | module (the module requiring this input) |

| Edge | Type | Connects |
|------|------|----------|
| e1 | coupling | v1 ↔ v2 |
| e2 | verification | v3 → v1 (module references input spec) |
| e3 | validation | v3 → v2 (module references input guidance) |

**Local Rules:**

- Edges point INTO the module (input direction)
- Reuses assurance triangle pattern for type specification

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| boundary_edges | array | IDs of boundary edges |
| boundary_vertices | array | IDs of [spec, guidance, module] vertices |
| input_name | string | Name of this input slot |

#### output

**ID Pattern:** `f:output:<name>`
**Extends:** face
**Tags:** [face, output]

**Purpose:** Module output type specification. Defines that a module produces output conforming to a particular spec, assessed against a particular guidance.

**Boundary Specification:**

| Vertex | Type Constraint |
|--------|-----------------|
| v1 | module (the module producing this output) |
| v2 | spec (output type spec) |
| v3 | guidance (output quality guidance) |

| Edge | Type | Connects |
|------|------|----------|
| e1 | verification | v1 → v2 (module references output spec) |
| e2 | validation | v1 → v3 (module references output guidance) |
| e3 | coupling | v2 ↔ v3 |

**Local Rules:**

- Edges point FROM the module (output direction)
- Reuses assurance triangle pattern for type specification
- Signer qualified for module must be qualified for this output's guidance

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| boundary_edges | array | IDs of boundary edges |
| boundary_vertices | array | IDs of [module, spec, guidance] vertices |
| output_name | string | Name of this output slot |

#### input-satisfaction

**ID Pattern:** `f:input-satisfaction:<name>`
**Extends:** face
**Tags:** [face, input-satisfaction]

**Purpose:** Concrete input provision. Proves that an actual document satisfies a module's input type requirements.

**Boundary Specification:**

| Vertex | Type Constraint |
|--------|-----------------|
| v1 | doc (concrete input document) |
| v2 | spec (input type spec from f:input) |
| v3 | module |

| Edge | Type | Connects |
|------|------|----------|
| e1 | verification | v1 → v2 |
| e2 | (from f:input) | v3 → v2 |
| e3 | feeds | v1 → v3 |

**Local Rules:**

- Must share edges with corresponding f:input face in module chart
- Input document must pass verification against input spec

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| boundary_edges | array | IDs of boundary edges |
| boundary_vertices | array | IDs of [doc, spec, module] vertices |
| satisfies_input | string | Which f:input face this satisfies |

#### output-satisfaction

**ID Pattern:** `f:output-satisfaction:<name>`
**Extends:** face
**Tags:** [face, output-satisfaction]

**Purpose:** Concrete output production. Proves that a module produced an actual document satisfying its output type requirements.

**Boundary Specification:**

| Vertex | Type Constraint |
|--------|-----------------|
| v1 | module |
| v2 | spec (output type spec from f:output) |
| v3 | doc (concrete output document) |

| Edge | Type | Connects |
|------|------|----------|
| e1 | (from f:output) | v1 → v2 |
| e2 | verification | v3 → v2 |
| e3 | yields | v1 → v3 |

**Local Rules:**

- Must share edges with corresponding f:output face in module chart
- Output document must pass verification against output spec

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| boundary_edges | array | IDs of boundary edges |
| boundary_vertices | array | IDs of [module, spec, doc] vertices |
| satisfies_output | string | Which f:output face this satisfies |

#### module-signature

**ID Pattern:** `f:module-signature:<name>`
**Extends:** face
**Tags:** [face, module-signature]

**Purpose:** Qualified signer validated module output. Proves that a signer qualified for the module validated a specific output document.

**Boundary Specification:**

| Vertex | Type Constraint |
|--------|-----------------|
| v1 | doc (output document) |
| v2 | module |
| v3 | signer |

| Edge | Type | Connects |
|------|------|----------|
| e1 | yields | v2 → v1 |
| e2 | qualifies | v3 → v2 |
| e3 | signs | v3 → v1 |

**Local Rules:**

- Must share signs edge with f:signature face for the output document
- Signer must be qualified for the module (which requires all output guidance qualifications)

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| boundary_edges | array | IDs of [yields, qualifies, signs] edges |
| boundary_vertices | array | IDs of [doc, module, signer] vertices |

## Chart Types

### audit

**ID Pattern:** `c:audit:<name>`
**Extends:** chart
**Tags:** [vertex, chart, audit]

**Purpose:** Charts that verify local rules and system invariants. Audit charts enable inspection of assurance networks, dependency chains, and coherence properties.

**Use Cases:**

- **Construction:** Scaffolds verification of new assurance faces by showing what edges are needed
- **Analysis:** Enables inspection of assurance coverage ("are all docs assured?"), accountability chains, and gap identification

**Membership Constraints:**

| Simplex Dimension | Type Constraints | Cardinality |
|-------------------|------------------|-------------|
| vertices | doc, spec, guidance, signer | 1..* |
| edges | verification, validation, coupling, signs, qualifies | 0..* |
| faces | assurance, signature, b2 | 0..* |

**Coherence Requirements:**

- All edges must connect vertices within the chart
- All face boundaries must be edges within the chart
- Chart must form a valid simplicial complex

**Local Rules:**

- Assurance faces ≥ document vertices (every doc should be assured)
- All assurance faces must trace to a b2 anchor

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| vertices | array | IDs of member vertices |
| edges | array | IDs of member edges |
| faces | array | IDs of member faces |
| audit_type | string | Type of audit (assurance, coverage, accountability) |

### module

**ID Pattern:** `c:module:<name>`
**Extends:** chart
**Tags:** [vertex, chart, module]

**Purpose:** I/O specification for a typed transformation. Module charts are self-referential - they contain the module vertex itself plus its input/output neighborhood.

**Use Cases:**

- **Construction:** Scaffolds definition of new modules by showing required input/output faces
- **Analysis:** Enables inspection of module type signatures, qualification requirements, and I/O dependencies

**Membership Constraints:**

| Simplex Dimension | Type Constraints | Cardinality |
|-------------------|------------------|-------------|
| vertices | module (self), spec, guidance | 3..* |
| edges | verification, validation, coupling | 3..* |
| faces | input, output | 1..* each |

**Coherence Requirements:**

- Must contain exactly one module vertex (self-reference)
- All input faces point INTO the module vertex
- All output faces point FROM the module vertex
- All edges must connect vertices within the chart

**Local Rules:**

- At least one input face required
- At least one output face required
- Module qualification requires all output guidance qualifications

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| vertices | array | IDs of member vertices (including self) |
| edges | array | IDs of member edges |
| faces | array | IDs of member faces |
| input_faces | array | IDs of f:input faces |
| output_faces | array | IDs of f:output faces |

### runbook

**ID Pattern:** `c:runbook:<name>`
**Extends:** chart
**Tags:** [vertex, chart, runbook]

**Purpose:** Chained sequence of modules with typed I/O dependencies. Runbooks encode multi-step workflows where each module's output becomes the next module's input.

**Use Cases:**

- **Construction:** Scaffolds definition of workflows by showing module ordering and I/O chaining
- **Analysis:** Enables inspection of workflow dependencies, bottlenecks, and completion status

**Membership Constraints:**

| Simplex Dimension | Type Constraints | Cardinality |
|-------------------|------------------|-------------|
| vertices | module (2+), spec, guidance | 4..* |
| edges | precedes, verification, validation, coupling | 1..* |
| faces | input, output | per module |

**Coherence Requirements:**

- All edges must connect vertices within the chart
- All face boundaries must be edges within the chart
- Output spec of module N must equal input spec of module N+1 (chaining)
- precedes edges must form a directed acyclic graph

**Local Rules:**

- No cycles in precedes edges (DAG requirement)
- Chained I/O: one module's output type = next module's input type
- First module has external inputs; last module has external outputs

**Required Fields:**

| Field | Type | Description |
|-------|------|-------------|
| vertices | array | IDs of member vertices |
| edges | array | IDs of member edges |
| faces | array | IDs of member faces |
| modules | array | Ordered list of module vertex IDs |
| precedes_edges | array | IDs of ordering edges |

## Local Rules

### Module Qualification Cascade

**Rule Type:** star
**Scope:** qualifies edges from signer to module
**Constraint:** `qualifies(signer, module)` requires `qualifies(signer, g)` for every guidance `g` in module's output faces

**Verification:**

1. Find all `f:output` faces in the module's chart
2. Extract the guidance vertex from each output face
3. Verify signer has `qualifies` edge to each such guidance

**Example:**

Module M has two output faces:
- `f:output:M-report` with guidance `v:guidance:report`
- `f:output:M-summary` with guidance `v:guidance:summary`

For signer S to have `qualifies(S, M)`, S must also have:
- `qualifies(S, v:guidance:report)`
- `qualifies(S, v:guidance:summary)`

### Signature Face Requires Guidance Qualification

**Rule Type:** star
**Scope:** signature faces
**Constraint:** `f:signature:(doc, guidance, signer)` requires `qualifies(signer, guidance)` in signer's star

**Verification:**

1. Extract signer vertex from signature face
2. Extract guidance vertex from signature face
3. Verify existence of qualifies edge from signer to guidance

**Example:**

For signature face `f:signature:(doc-X, guidance-Y, signer-Z)`:
- Check that edge `e:qualifies:Z-to-Y` exists
- If missing, signature face is invalid

### Module-Signature Shares Edge with Signature

**Rule Type:** face-adjacency
**Scope:** module-signature faces
**Constraint:** `f:module-signature:` must share `e:signs:` edge with `f:signature:` face

**Verification:**

1. Find the signs edge in module-signature face boundary
2. Find signature face containing same signs edge
3. Verify both faces exist and share the edge

**Example:**

`f:module-signature:(doc, module, signer)` contains `e:signs:(signer → doc)`
`f:signature:(doc, guidance, signer)` also contains `e:signs:(signer → doc)`
They share the signs edge, proving the signer validated both as module output and against guidance.

### Signature Shares Edge with Assurance

**Rule Type:** face-adjacency
**Scope:** signature faces
**Constraint:** `f:signature:` must share `e:validation:` edge with `f:assurance:` face

**Verification:**

1. Find the validation edge in signature face boundary
2. Find assurance face containing same validation edge
3. Verify both faces exist and share the edge

**Example:**

`f:signature:(doc, guidance, signer)` contains `e:validation:(doc → guidance)`
`f:assurance:(doc, spec, guidance)` also contains `e:validation:(doc → guidance)`
They share the validation edge, connecting signature accountability to document assurance.

### Assurance Requires B2 Anchor

**Rule Type:** face-adjacency
**Scope:** assurance faces
**Constraint:** `f:assurance:` must be adjacent to `f:b2:` sharing `e:coupling:` edge

**Verification:**

1. Find the coupling edge in assurance face boundary
2. Trace coupling edges until reaching a b2 face
3. Verify chain terminates at b2 (no infinite regress)

**Example:**

`f:assurance:(doc-X, spec-Y, guidance-Z)` contains `e:coupling:(spec-Y ↔ guidance-Z)`
Trace: spec-Y is assured by `f:assurance:(spec-Y, spec-for-spec, guidance-for-spec)`
Continue until reaching `f:b2:spec-spec` which is self-anchoring.

### Output Satisfaction Requires Output Type

**Rule Type:** face-adjacency
**Scope:** output-satisfaction faces
**Constraint:** `f:output-satisfaction:` must share edges with `f:output:` in module chart

**Verification:**

1. Extract module from output-satisfaction face
2. Find module's chart
3. Find f:output face that matches the output type
4. Verify shared edges (module→spec relationship)

**Example:**

`f:output-satisfaction:(module-M, spec-X, doc-D)` requires:
- `f:output:(module-M, spec-X, guidance-G)` exists in module-M's chart
- They share the module→spec relationship

### Input Satisfaction Requires Input Type

**Rule Type:** face-adjacency
**Scope:** input-satisfaction faces
**Constraint:** `f:input-satisfaction:` must share edges with `f:input:` in module chart

**Verification:**

1. Extract module from input-satisfaction face
2. Find module's chart
3. Find f:input face that matches the input type
4. Verify shared edges (spec→module relationship)

**Example:**

`f:input-satisfaction:(doc-D, spec-X, module-M)` requires:
- `f:input:(spec-X, guidance-G, module-M)` exists in module-M's chart
- They share the spec→module relationship

### Edge Endpoint Type Compliance

**Rule Type:** edge-endpoint
**Scope:** all edges
**Constraint:** Edge source and target must match type constraints defined for that edge type

**Verification:**

1. Get edge type from edge's type field
2. Look up endpoint constraints for that type in ontology
3. Verify source vertex type matches source_type constraint
4. Verify target vertex type matches target_type constraint

**Example:**

Edge `e:verification:doc-X-to-spec-Y`:
- source: `v:doc:X` (type: vertex/doc)
- target: `v:spec:Y` (type: vertex/spec)
- Constraint: source_type=doc, target_type=spec
- Valid because doc is a doc subtype and spec is a spec

### Face Boundary Closure

**Rule Type:** face-boundary
**Scope:** all faces
**Constraint:** Face boundary edges must form a closed triangle connecting exactly three vertices

**Verification:**

1. Extract three boundary edges from face
2. Verify each edge connects two of the three boundary vertices
3. Verify edges form closed cycle: e1 connects v1-v2, e2 connects v2-v3, e3 connects v1-v3

**Example:**

`f:assurance:(doc, spec, guidance)`:
- e1: verification connects doc→spec
- e2: validation connects doc→guidance
- e3: coupling connects spec↔guidance
- Triangle closes: doc connects to spec and guidance, spec connects to guidance

### Authorization Chain Validity

**Rule Type:** star
**Scope:** authorization faces
**Constraint:** For an actor to have an authority, there must exist a complete authorization face

**Verification:**

1. For permission check: find authorization face (actor, role, authority)
2. Verify has-role edge from actor to role
3. Verify conveys edge from role to authority
4. Complete face proves actor has authority

**Example:**

Can signer S validate against guidance G?
1. Need authority `v:authority:validate:G`
2. Find role R where `e:conveys:(R → validate:G)`
3. Verify `e:has-role:(S → R)`
4. If `f:authorization:(S, R, validate:G)` exists, S can validate against G

### Runbook DAG Requirement

**Rule Type:** edge-endpoint
**Scope:** precedes edges in runbook charts
**Constraint:** Precedes edges must form a directed acyclic graph (no cycles)

**Verification:**

1. Collect all precedes edges in runbook
2. Perform topological sort
3. If sort fails (cycle detected), runbook is invalid

**Example:**

Valid: M1 → M2 → M3 (linear chain)
Valid: M1 → M2, M1 → M3, M2 → M4, M3 → M4 (diamond)
Invalid: M1 → M2 → M3 → M1 (cycle)

### Runbook I/O Chaining

**Rule Type:** face-adjacency
**Scope:** consecutive modules in runbook
**Constraint:** Prior module's output type must match subsequent module's input type

**Verification:**

1. For each precedes edge (M1 → M2)
2. Find M1's output faces and M2's input faces
3. Verify at least one output spec from M1 equals an input spec of M2

**Example:**

M1 outputs to `v:spec:conceptual-architecture`
M2 inputs from `v:spec:conceptual-architecture`
Chaining valid because output type matches input type.

## Extension Points

### ID Naming Convention

Simplex IDs follow a package-like naming convention:

```
<dimension>:<namespace>:<name>
```

Where:

- **dimension** = `v` (vertex), `e` (edge), `f` (face), or `c` (chart)
- **namespace** = type namespace (like a package name)
- **name** = unique identifier within that namespace

The base ontology reserves **root-level namespaces** (no dot). Application ontologies must use **dotted namespaces** like software packages.

### How to Create Application Ontologies

An application ontology extends this base ontology by:

1. **Setting `extends_ontology`** to `v:ontology:base`
2. **Inheriting all types** from base (do not redefine base types)
3. **Adding new types** using dotted namespace prefixes (e.g., `brand.audience`)
4. **Adding new local rules** that further constrain (cannot weaken base rules)
5. **Documenting extensions** with reference to base for inherited behavior

### Reserved Namespaces (Base Ontology)

The following root-level namespaces are reserved by the base ontology:

| Namespace | Dimension | Reserved For |
|-----------|-----------|--------------|
| `spec`, `guidance`, `ontology`, `doc`, `module` | v | Document types |
| `actor`, `signer` | v | Actor types |
| `role`, `authority` | v | RBAC types |
| `verification`, `validation`, `coupling` | e | Assurance edges |
| `signs`, `qualifies` | e | Signature edges |
| `has-role`, `conveys`, `requires-authority` | e | RBAC edges |
| `precedes`, `feeds`, `yields` | e | Module I/O edges |
| `inherits`, `instantiates` | e | Document relationship edges |
| `assurance`, `signature`, `b2` | f | Assurance faces |
| `authorization` | f | RBAC face |
| `input`, `output`, `input-satisfaction`, `output-satisfaction`, `module-signature` | f | Module faces |
| `audit`, `module`, `runbook` | c | Chart types |

### Application Namespace Convention

Application ontologies add types using **dotted namespaces**:

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

This is analogous to importing software packages:

```python
from base_ontology import *  # All base types available
# Define new types in your namespace
brand.audience = ...
brand.resonates = ...
```

### Extension Guidelines

1. Use dotted namespaces for all new types (e.g., `brand.audience`, not `audience`)
2. Choose a unique domain prefix for your application
3. Inherit from appropriate base types (e.g., new doc types extend doc)
4. Document purpose and constraints for each new type
5. Add local rules only to strengthen, never weaken base rules
6. Ensure new face types have valid boundary specifications
7. Test that extended ontology composes correctly with base

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
```

---

**Note:** This is the foundational ontology for knowledge complexes. Application-specific ontologies should extend this base using the extension mechanism documented above. See [[spec-for-ontology]] for structural requirements and [[guidance-for-ontology]] for quality criteria.
