---
type: vertex/doc
extends: doc
id: v:doc:logical-architecture-knowledge-complex-refactor
name: Logical Architecture - Knowledge Complex Framework Refactor
description: System components, interfaces, and component-function matrix for the knowledge complex framework refactor
tags:
  - vertex
  - doc
  - logical-architecture
version: 0.1.0
created: 2026-01-11T00:00:00Z
modified: 2026-01-11T00:00:00Z
system_name: Knowledge Complex Framework
scope: Internal-first deployment enabling systematic documentation with verification, validation, and assurance
functional_architecture_ref: v:doc:functional-architecture-knowledge-complex-refactor
component_count: 14
---

# Logical Architecture - Knowledge Complex Framework Refactor

## Purpose

This logical architecture defines HOW the knowledge complex framework is structured to perform its 24 functions. The document specifies 14 technology-agnostic components organized into 6 component areas, with clear responsibilities and 37 interfaces. The Component-Function Matrix traces how these components realize the functions from the functional architecture, establishing the foundation for subsequent physical architecture decisions.

## Overview

The knowledge complex framework is fundamentally a **typed simplicial complex** where documents are simplices with typed YAML headers, relationships are typed edges, and triangular structures (like assurance faces) are typed faces. This mathematical foundation enables expressive document types while maintaining coherence through verifiable rules.

The functional architecture established 24 functions organized into 5 functional areas: Document Authoring (F1-F4), Quality Assurance (F5-F9), Knowledge Navigation (F10-F12), Approval & Accountability (F13-F18), and Configuration & Meta (F19-F24).

This logical architecture translates those functions into components organized by responsibility:

1. **Type System (C1-C2)**: Foundation layer defining simplex types, schemas, and coherence rules
2. **Document Management (C3-C5)**: Components for templates, composition, and persistence
3. **Coherence Verification (C6-C8)**: Components ensuring structural and topological compliance
4. **Quality Assessment (C9-C10)**: Components for evaluation and result presentation
5. **Knowledge Graph (C11-C12)**: Components for search and relationship navigation
6. **Workflow & Accountability (C13-C14)**: Components for approval workflows and simplex construction

Each component is specified with responsibilities, interfaces, and collaborations—without reference to implementation technology. The Component-Function Matrix shows how components combine to realize all 24 functions.

## Functional Architecture Reference

[[functional-architecture-knowledge-complex-refactor]]

### Functions Summary

| ID | Name | Area | Description |
|----|------|------|-------------|
| F1 | Template Retrieval | Document Authoring | Provide operators with the correct starting point for document creation |
| F2 | Prior Work Discovery | Document Authoring | Help operators find relevant existing documents to inform their work |
| F3 | Draft Generation | Document Authoring | Create an initial document draft from template and context |
| F4 | Context Parameter Injection | Document Authoring | Resolve remaining parameters in a draft document |
| F5 | Frontmatter Verification | Quality Assurance | Verify that document frontmatter conforms to specification |
| F6 | Section Structure Verification | Quality Assurance | Verify that document body structure conforms to specification |
| F7 | Count Consistency Verification | Quality Assurance | Verify that frontmatter counts match actual document content |
| F8 | Reference Resolution Verification | Quality Assurance | Verify that document references resolve to valid targets |
| F9 | Guidance-Based Evaluation | Quality Assurance | Score document quality against guidance criteria |
| F10 | Full-Text Search | Knowledge Navigation | Find documents containing specific content |
| F11 | Graph Traversal | Knowledge Navigation | Navigate relationships in the knowledge complex |
| F12 | Backlink Discovery | Knowledge Navigation | Find documents that reference a target document |
| F13 | Approval Request Initiation | Approval & Accountability | Formally request approval for a document |
| F14 | Verification Status Presentation | Approval & Accountability | Present verification results in approver-friendly format |
| F15 | Evaluation Score Presentation | Approval & Accountability | Present evaluation scores highlighting areas needing attention |
| F16 | Validation Edge Creation | Approval & Accountability | Create formal record of human validation approval |
| F17 | Runbook Step Tracking | Approval & Accountability | Track progress through runbook execution |
| F18 | Performance Metrics Collection | Approval & Accountability | Collect effectiveness metrics during runbook execution |
| F19 | Specification Authoring | Configuration & Meta | Create specification documents for new document types |
| F20 | Guidance Authoring | Configuration & Meta | Create guidance documents for new document types |
| F21 | Template Authoring | Configuration & Meta | Create template documents for new document types |
| F22 | Coupling Edge Creation | Configuration & Meta | Create coupling edge connecting spec and guidance |
| F23 | Verification Edge Creation | Configuration & Meta | Create verification edge recording structural compliance |
| F24 | Assurance Face Construction | Configuration & Meta | Construct complete assurance face closing the assurance triangle |

## Mathematical Foundation: Typed Simplicial Complex

The knowledge complex implements a **typed simplicial complex** where:

- **0-simplices (vertices)** = documents with typed YAML headers
- **1-simplices (edges)** = typed relationships between vertices
- **2-simplices (faces)** = triangular structures (e.g., assurance triangles)

### Simplex Types and Inheritance

All simplices have YAML frontmatter with type information:

| Field | Purpose | Example |
|-------|---------|---------|
| `type` | Identifies simplex dimension and subtype | `vertex/spec`, `edge/verification`, `face/assurance` |
| `extends` | Structural inheritance from parent type | `doc`, `edge`, `face` |
| `tags` | Complete inheritance chain for type validation | `[vertex, doc, spec]` |
| `id` | Unique identifier with type prefix | `v:spec:logical-architecture`, `e:verification:doc-to-spec` |

**Type Hierarchy:**

```
vertex (0-simplex, abstract)
├── doc → spec, guidance
├── actor → individual → staff
│         → group → team
└── property → role

edge (1-simplex, abstract)
├── verification (doc → spec)
├── validation (doc → guidance)
├── coupling (spec ↔ guidance)
├── inherits (spec → spec for domain specialization)
└── dependency, signs, qualifies, cites

face (2-simplex, abstract)
├── assurance (doc, spec, guidance triangle)
├── signature (doc, guidance, signer triangle)
└── b2 (boundary face with root for bootstrap)
```

### Global Coherence Rules

These rules ensure the complex remains well-formed:

| Rule | Scope | Description |
|------|-------|-------------|
| Edge endpoint types | Every edge | Edge must connect vertices of compatible types (e.g., verification: doc → spec) |
| Face boundary closure | Every face | Face must have exactly 3 edges forming a closed triangle |
| Tag inheritance chain | Every simplex | Tags must include complete inheritance path from type field |
| ID prefix consistency | Every simplex | ID prefix (v:, e:, f:) must match simplex dimension |

### Local Rules

Local rules are constraints evaluated using **topologically adjacent simplices only**. This enables compositional verification: check locally, guarantee globally.

| Rule Type | Scope | Example |
|-----------|-------|---------|
| Edge endpoint rules | 1-neighborhood of edge | "verification edges must connect doc to spec" |
| Face boundary rules | 3 edges of face boundary | "assurance face must have verification + validation + coupling edges" |
| Face adjacency rules | Faces sharing an edge | "every assurance face must be adjacent to a b2 face sharing the coupling edge" |
| Star rules | All simplices incident to a vertex | "every spec vertex must have at least one coupling edge" |

**Why Local Rules Matter:**

- **Compositional verification**: Check locally, guarantee globally
- **Incremental validation**: Adding a simplex only requires checking its neighborhood
- **Domain-specific constraints**: Face types can require adjacent face types
- **Workflow guarantees**: Properties verifiable at simplex creation time propagate to complex-wide properties

### Dependency Faces (Requirements Traceability)

When a document Y is produced by applying a process F that has document X as input, this forms a **dependency face** (triangle):

```
        X (input document)
       / \
      /   \
  input    output
    /       \
   F -------- Y
      applies
```

**Three Face Types for Process Dependencies:**

| Face Type | Pattern | Semantics |
|-----------|---------|-----------|
| Prerequisite | (input, skill, process) | Validates input conditions for process |
| Completion | (input-state, process, output-state) | Represents state transition through process |
| Production | (output-state, process, product) | Represents outputs produced by process |

**Edge Types for Dependency Triangles:**

| Edge Type | Source → Target | Semantics |
|-----------|-----------------|-----------|
| `requires-input` | process → input-type | Process needs this input |
| `produces-output` | process → output-type | Process produces this output |
| `applies` | input → process | Input document feeds process |
| `derives` | process → output | Output derives from process |

**Multistage Runbooks as Charts:**

A process F may have multiple inputs and outputs, creating multiple faces. Chained processes form complete workflows where the output of one process becomes the input to the next:

```
Input₁ → Process₁ → Intermediate → Process₂ → Output
   ↘ face₁ ↙         ↘ face₂ ↙        ↘ face₃ ↙
```

This pattern enables **runbooks as verifiable charts** where each step's I/O dependencies are formally encoded.

## Logical Architecture

### Component Table

| ID | Name | Area | Responsibility | Interfaces |
|----|------|------|----------------|------------|
| C1 | Type Ontology | Type System | Define and manage simplex type hierarchy, inheritance rules, and local rules | I1, I2, I3 |
| C2 | Schema Registry | Type System | Store schemas for each type defining required YAML fields and inheritance chains | I4, I5, I6 |
| C3 | Template Registry | Document Management | Store and retrieve document templates by type, linked to schemas | I7, I8 |
| C4 | Document Composer | Document Management | Assemble documents from templates and parameters ensuring type compliance | I9, I10, I11 |
| C5 | Simplex Store | Document Management | Persist and retrieve typed simplices with coherence enforcement | I12, I13, I14, I35 |
| C6 | Schema Verifier | Coherence Verification | Verify YAML frontmatter against type schemas | I15, I16, I17 |
| C7 | Structure Analyzer | Coherence Verification | Verify markdown body structure against spec-defined sections | I18, I19 |
| C8 | Boundary Verifier | Coherence Verification | Verify simplicial complex rules and local rules | I20, I21, I22 |
| C9 | Evaluation Engine | Quality Assessment | Score documents against guidance criteria | I23, I24 |
| C10 | Result Presenter | Quality Assessment | Format verification and evaluation results for display | I25 |
| C11 | Search Index | Knowledge Graph | Support full-text and filtered search across typed simplices | I26, I27 |
| C12 | Graph Navigator | Knowledge Graph | Traverse typed relationships and discover backlinks | I28, I29 |
| C13 | Workflow Coordinator | Workflow & Accountability | Manage approval requests and runbook execution with typed I/O dependencies | I30, I31, I36 |
| C14 | Simplex Constructor | Workflow & Accountability | Create typed edges and faces ensuring coherence with simplicial complex rules | I32, I33, I34, I37 |

### Component Definitions

#### C1: Type Ontology

**Responsibility:** Define and manage the simplex type hierarchy including vertex types, edge types, face types, inheritance rules, type constraints, and local rules that constrain topologically adjacent simplices.

**Interfaces:**
- I1 (C1→C2): Provides type definitions to Schema Registry
- I2 (C1→C6): Provides type rules for schema verification
- I3 (C1→C8): Provides boundary rules and local rules for coherence checking

**Collaborations:** Foundational component that all type-aware components depend on. Defines what types exist, how they inherit, what constraints apply, and what local adjacency rules must be satisfied.

**Key Responsibilities:**
- Simplex dimension definitions (vertex=0, edge=1, face=2)
- Type inheritance via `extends` field
- Tag chain requirements for each type
- Edge source/target type constraints
- Face boundary edge requirements
- Local rules for topological adjacency

#### C2: Schema Registry

**Responsibility:** Store schemas for each document type defining required YAML fields, allowed values, field types, and inheritance chains.

**Interfaces:**
- I4 (C2→C3): Provides schemas for template creation
- I5 (C2→C6): Provides schemas for verification
- I6 (C2→C14): Provides schemas for simplex construction

**Collaborations:** Receives type definitions from Type Ontology (C1). Provides schemas to Template Registry (C3), Schema Verifier (C6), and Simplex Constructor (C14).

**Schema Contents:**
- Required frontmatter fields per type
- Field types (string, integer, array, datetime)
- Default values and constraints
- Inheritance chain requirements for tags
- Edge source/target type constraints

#### C3: Template Registry

**Responsibility:** Store and retrieve document templates by type, linked to their schemas.

**Interfaces:**
- I7 (C3→C4): Provides templates for document composition
- I8 (C3→C5): Reads/writes templates to Simplex Store

**Collaborations:** Uses schemas from Schema Registry (C2) to validate templates. Provides templates to Document Composer (C4). Stores templates in Simplex Store (C5).

**Template Contents:**
- YAML frontmatter skeleton with placeholders
- Required body sections per spec
- Links to governing spec and guidance
- Placeholder syntax for parameter injection

#### C4: Document Composer

**Responsibility:** Assemble documents from templates and parameters ensuring type compliance.

**Interfaces:**
- I9 (C4→C3): Requests templates by type
- I10 (C4→C5): Writes composed documents
- I11 (C4→C11): Queries for prior work references

**Collaborations:** Receives templates from Template Registry (C3). Queries Search Index (C11) for prior work. Writes composed documents to Simplex Store (C5) with type validation.

**Composition Process:**
1. Retrieve template for requested type
2. Inject context parameters into placeholders
3. Validate resulting frontmatter against schema
4. Store as typed simplex

#### C5: Simplex Store

**Responsibility:** Persist and retrieve typed simplices (vertices, edges, faces) with coherence enforcement and neighborhood query support for local rule verification.

**Interfaces:**
- I12 (C5→C1): Validates simplex types on write
- I13 (C5→C11): Notifies of changes for indexing
- I14 (C5→C12): Provides simplex data for graph operations
- I35 (C5→C8): Provides neighborhood queries for local rule verification

**Collaborations:** Validates all writes against Type Ontology (C1) rules. Notifies Search Index (C11) of changes. Provides data to Graph Navigator (C12). Supports Boundary Verifier (C8) with topological neighborhood queries.

**Coherence Enforcement:**
- Vertex: valid type, complete tag chain
- Edge: valid type, source/target exist and have compatible types
- Face: valid type, boundary edges exist and form closed triangle

**Neighborhood Query Support:**
- Edge neighbors: Get all edges incident to a vertex
- Face neighbors: Get all faces sharing an edge
- Star query: Get all simplices incident to a vertex
- Coboundary query: Get all faces containing a given edge

#### C6: Schema Verifier

**Responsibility:** Verify YAML frontmatter against type schemas including field presence, types, and inheritance chain in tags.

**Interfaces:**
- I15 (C6→C2): Retrieves schema for document type
- I16 (C6→C5): Reads documents for verification
- I17 (C6→C10): Reports verification results

**Collaborations:** Gets schemas from Schema Registry (C2). Reads documents from Simplex Store (C5). Reports results to Result Presenter (C10).

**Verification Checks:**
- All required fields present
- Field values match expected types
- Tags include complete inheritance chain
- Type-specific constraints satisfied

#### C7: Structure Analyzer

**Responsibility:** Verify markdown body structure against spec-defined required sections.

**Interfaces:**
- I18 (C7→C5): Reads documents and specs
- I19 (C7→C10): Reports analysis results

**Collaborations:** Reads documents and their governing specs from Simplex Store (C5). Reports results to Result Presenter (C10).

**Analysis Checks:**
- Required sections present
- Section ordering (if spec requires)
- Subsection nesting validity
- Count fields match actual content

#### C8: Boundary Verifier

**Responsibility:** Verify simplicial complex rules including boundary constraints and local rules that constrain topologically adjacent simplices.

**Interfaces:**
- I20 (C8→C1): Retrieves boundary rules and local rules from Type Ontology
- I21 (C8→C5): Reads simplices for boundary checking and neighborhood queries
- I22 (C8→C10): Reports boundary and local rule verification results

**Collaborations:** Gets boundary rules and local rules from Type Ontology (C1). Reads simplices and their topological neighborhoods from Simplex Store (C5). Reports results to Result Presenter (C10).

**Boundary Checks (Global):**
- Edge source vertex exists and has compatible type
- Edge target vertex exists and has compatible type
- Face has exactly 3 boundary edges
- Face boundary edges form closed triangle
- Reference links resolve to valid targets

**Local Rule Checks:**
- Edge endpoint rules: Verify edge connects vertex types allowed by its type
- Face boundary rules: Verify face's boundary edges match required edge types
- Face adjacency rules: Verify required adjacent faces exist sharing specified edge types
- Star rules: Verify all simplices incident to a vertex satisfy star constraints

#### C9: Evaluation Engine

**Responsibility:** Score documents against guidance criteria using qualitative assessment.

**Interfaces:**
- I23 (C9→C5): Reads documents and guidance
- I24 (C9→C10): Reports evaluation scores

**Collaborations:** Reads documents and their governing guidance from Simplex Store (C5). Reports scores to Result Presenter (C10).

**Evaluation Process:**
- Extract criteria from guidance document
- Assess document against each criterion
- Assign scores (Excellent/Good/Needs Improvement)
- Generate improvement suggestions

#### C10: Result Presenter

**Responsibility:** Format verification and evaluation results for approver review.

**Interfaces:**
- I25 (C10→C13): Provides formatted results for approval workflow

**Collaborations:** Receives results from Schema Verifier (C6), Structure Analyzer (C7), Boundary Verifier (C8), and Evaluation Engine (C9). Provides formatted output to Workflow Coordinator (C13).

**Presentation Formats:**
- Verification summary (pass/fail with details)
- Evaluation summary (scores by criterion)
- Gap highlighting for items needing attention
- Links to detailed results

#### C11: Search Index

**Responsibility:** Support full-text and filtered search across typed simplices.

**Interfaces:**
- I26 (C11→C4): Returns search results for prior work discovery
- I27 (C11→C12): Coordinates with graph for relationship-aware search

**Collaborations:** Receives simplex updates from Simplex Store (C5). Provides search results to Document Composer (C4). Coordinates with Graph Navigator (C12) for relationship-aware queries.

**Search Capabilities:**
- Full-text content search
- Filter by simplex type (vertex, edge, face)
- Filter by document type (spec, guidance, etc.)
- Scope constraints (project, date range)

#### C12: Graph Navigator

**Responsibility:** Traverse typed relationships and discover backlinks respecting simplex structure.

**Interfaces:**
- I28 (C12→C5): Reads simplices for relationship data
- I29 (C12→C8): Provides target existence checking for boundary verification

**Collaborations:** Reads simplices from Simplex Store (C5). Provides graph queries to Boundary Verifier (C8) for reference checking.

**Navigation Capabilities:**
- Traverse edges by type (verification, validation, coupling)
- Discover backlinks (what references this simplex?)
- Path finding between simplices
- Neighborhood exploration with depth limit

#### C13: Workflow Coordinator

**Responsibility:** Manage approval requests and runbook execution with typed I/O dependencies between workflow steps, using dependency faces to encode step relationships.

**Interfaces:**
- I30 (C13→C14): Triggers simplex creation on approval (including dependency faces)
- I31 (C13→C10): Requests formatted results for review
- I36 (C13→C5): Queries dependency faces to determine step prerequisites

**Collaborations:** Receives formatted results from Result Presenter (C10). Triggers Simplex Constructor (C14) when approvals are granted. Queries Simplex Store (C5) for dependency face topology.

**Workflow Capabilities:**
- Approval request initiation and tracking
- Runbook step sequencing with I/O dependencies
- Step status tracking (pending, in progress, completed)
- Performance metrics collection per step

**Runbooks as Charts:**
A runbook is a chart where vertices are documents (inputs, outputs, process specifications), edges are typed relationships (requires-input, produces-output, applies, derives), and faces are dependency triangles (input × process × output).

#### C14: Simplex Constructor

**Responsibility:** Create typed edges and faces including dependency faces for requirements traceability, ensuring coherence with simplicial complex rules and local rules.

**Interfaces:**
- I32 (C14→C2): Retrieves schemas for edge/face types
- I33 (C14→C5): Writes constructed simplices
- I34 (C14→C6): Triggers verification of created simplices
- I37 (C14→C8): Triggers local rule verification for constructed faces

**Collaborations:** Gets schemas from Schema Registry (C2). Writes simplices to Simplex Store (C5). Triggers Schema Verifier (C6) and Boundary Verifier (C8) to verify created simplices.

**Edge Construction Capabilities:**
- Verification edge: doc → spec with automated verifier results
- Validation edge: doc → guidance with human approver and assessment
- Coupling edge: spec ↔ guidance with alignment documentation
- Dependency edges: requires-input, produces-output, applies, derives

**Face Construction Capabilities:**
- Assurance face: triangle of (doc, spec, guidance) with boundary edges
- Prerequisite face: (input, skill/condition, process)
- Completion face: (input-state, process, output-state)
- Production face: (output-state, process, product)

### Interface Specifications

| Interface | From | To | Data Exchanged | Protocol |
|-----------|------|-----|----------------|----------|
| I1 | C1 | C2 | Type definitions, inheritance rules | Request-Response |
| I2 | C1 | C6 | Type rules for schema verification | Request-Response |
| I3 | C1 | C8 | Boundary rules and local rules for coherence | Request-Response |
| I4 | C2 | C3 | Schemas for template creation | Request-Response |
| I5 | C2 | C6 | Schemas for verification | Request-Response |
| I6 | C2 | C14 | Schemas for simplex construction | Request-Response |
| I7 | C3 | C4 | Templates for composition | Request-Response |
| I8 | C3 | C5 | Template storage operations | Read-Write |
| I9 | C4 | C3 | Template requests by type | Request-Response |
| I10 | C4 | C5 | Composed document write | Write |
| I11 | C4 | C11 | Prior work query | Request-Response |
| I12 | C5 | C1 | Type validation on write | Request-Response |
| I13 | C5 | C11 | Change notifications for indexing | Event |
| I14 | C5 | C12 | Simplex data for graph operations | Request-Response |
| I15 | C6 | C2 | Schema retrieval by type | Request-Response |
| I16 | C6 | C5 | Document read for verification | Request-Response |
| I17 | C6 | C10 | Verification results | Event |
| I18 | C7 | C5 | Document and spec read | Request-Response |
| I19 | C7 | C10 | Structure analysis results | Event |
| I20 | C8 | C1 | Boundary and local rules retrieval | Request-Response |
| I21 | C8 | C5 | Simplex read and neighborhood queries | Request-Response |
| I22 | C8 | C10 | Boundary verification results | Event |
| I23 | C9 | C5 | Document and guidance read | Request-Response |
| I24 | C9 | C10 | Evaluation scores | Event |
| I25 | C10 | C13 | Formatted results for workflow | Request-Response |
| I26 | C11 | C4 | Search results for prior work | Request-Response |
| I27 | C11 | C12 | Graph-aware search coordination | Request-Response |
| I28 | C12 | C5 | Simplex relationship data | Request-Response |
| I29 | C12 | C8 | Target existence checking | Request-Response |
| I30 | C13 | C14 | Simplex creation trigger | Command |
| I31 | C13 | C10 | Result request for review | Request-Response |
| I32 | C14 | C2 | Schema retrieval for edge/face types | Request-Response |
| I33 | C14 | C5 | Constructed simplex write | Write |
| I34 | C14 | C6 | Verification trigger for created simplex | Command |
| I35 | C5 | C8 | Neighborhood queries for local rules | Request-Response |
| I36 | C13 | C5 | Dependency face queries for prerequisites | Request-Response |
| I37 | C14 | C8 | Local rule verification for faces | Command |

## Component-Function Matrix

### Matrix View

|      | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 | F12 | F13 | F14 | F15 | F16 | F17 | F18 | F19 | F20 | F21 | F22 | F23 | F24 |
|------|----|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| C1   | S  | S  | S  | S  | S  | S  | S  | S  | S  | S  | S   | S   | S   | S   | S   | S   | S   | S   | S   | S   | S   | S   | S   | S   |
| C2   |    |    |    |    |    |    |    |    |    |    |     |     |     |     |     |     |     |     | X   | X   |     |     |     |     |
| C3   | X  |    |    |    |    |    |    |    |    |    |     |     |     |     |     |     |     |     |     |     | X   |     |     |     |
| C4   |    |    | X  | X  |    |    |    |    |    |    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| C5   | S  | S  | S  | S  | S  | S  | S  | S  | S  | S  | S   | S   | S   | S   | S   | S   | S   | S   | S   | S   | S   | S   | S   | S   |
| C6   |    |    |    |    | X  |    |    |    |    |    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| C7   |    |    |    |    |    | X  | X  |    |    |    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| C8   |    |    |    |    |    |    |    | X  |    |    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| C9   |    |    |    |    |    |    |    |    | X  |    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| C10  |    |    |    |    |    |    |    |    |    |    |     |     |     | X   | X   |     |     |     |     |     |     |     |     |     |
| C11  |    | X  |    |    |    |    |    |    |    | X  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| C12  |    |    |    |    |    |    |    |    |    |    | X   | X   |     |     |     |     |     |     |     |     |     |     |     |     |
| C13  |    |    |    |    |    |    |    |    |    |    |     |     | X   |     |     |     | X   | X   |     |     |     |     |     |     |
| C14  |    |    |    |    |    |    |    |    |    |    |     |     |     |     |     | X   |     |     |     |     |     | X   | X   | X   |

**Legend:** X = Primary Realizer, S = Supporting (foundation/storage)

### Relationship Details

| Component | Function | Realization Type | Rationale |
|-----------|----------|------------------|-----------|
| C1 | All | Supporting | Type Ontology provides foundational type system for all operations |
| C2 | F19 | Primary | Schema Registry defines schemas that Specification Authoring produces |
| C2 | F20 | Primary | Schema Registry defines schemas that Guidance Authoring produces |
| C3 | F1 | Primary | Template Registry provides template retrieval capability |
| C3 | F21 | Primary | Template Registry stores templates that Template Authoring produces |
| C4 | F3 | Primary | Document Composer generates drafts from templates |
| C4 | F4 | Primary | Document Composer injects context parameters |
| C5 | All | Supporting | Simplex Store provides persistence for all document operations |
| C6 | F5 | Primary | Schema Verifier checks frontmatter against schemas |
| C7 | F6 | Primary | Structure Analyzer checks body sections |
| C7 | F7 | Primary | Structure Analyzer validates counts against content |
| C8 | F8 | Primary | Boundary Verifier checks reference resolution |
| C9 | F9 | Primary | Evaluation Engine scores against guidance |
| C10 | F14 | Primary | Result Presenter formats verification status |
| C10 | F15 | Primary | Result Presenter formats evaluation scores |
| C11 | F2 | Primary | Search Index enables prior work discovery |
| C11 | F10 | Primary | Search Index provides full-text search |
| C12 | F11 | Primary | Graph Navigator traverses relationships |
| C12 | F12 | Primary | Graph Navigator discovers backlinks |
| C13 | F13 | Primary | Workflow Coordinator initiates approval requests |
| C13 | F17 | Primary | Workflow Coordinator tracks runbook steps |
| C13 | F18 | Primary | Workflow Coordinator collects performance metrics |
| C14 | F16 | Primary | Simplex Constructor creates validation edges |
| C14 | F22 | Primary | Simplex Constructor creates coupling edges |
| C14 | F23 | Primary | Simplex Constructor creates verification edges |
| C14 | F24 | Primary | Simplex Constructor creates assurance faces |

### Key Allocations

1. **Type System Foundation**: C1 (Type Ontology) + C2 (Schema Registry) provide the mathematical foundation. All components depend on type definitions for coherence. This is the core innovation enabling expressive yet coherent document management through local rules and schema inheritance.

2. **Four-Layer Coherence Verification**: C6 (Schema Verifier) + C7 (Structure Analyzer) + C8 (Boundary Verifier) → C10 (Result Presenter) realizes F5-F8, F14:
   - Schema layer: YAML frontmatter against type schemas
   - Structure layer: Markdown body against spec sections
   - Boundary layer: Simplicial complex rules (edges connect valid vertices, faces have valid boundaries)
   - Local rule layer: Adjacent simplex constraints (face adjacency, star rules)

3. **Document Authoring with Type Compliance**: C3 (Template Registry) → C4 (Document Composer) → C5 (Simplex Store) realizes F1, F3, F4, F21. Templates are linked to schemas; composition validates type compliance; storage enforces coherence.

4. **Knowledge Navigation on Typed Graph**: C11 (Search Index) + C12 (Graph Navigator) realize F2, F10-F12. Search respects simplex types; navigation follows typed edges. Neighborhood queries support local rule verification.

5. **Workflow with Typed I/O Dependencies**: C13 (Workflow Coordinator) realizes F13, F17, F18. Runbook steps have typed inputs/outputs that compose; type checking ensures compatible I/O. Local rules enable workflow-level guarantees because properties verified at simplex creation propagate to complex-wide properties.

6. **Simplex Construction with Local Rule Enforcement**: C14 (Simplex Constructor) realizes F16, F22-F24. Creates edges and faces ensuring simplicial complex rules AND local rules are satisfied before committing to the complex.

## Integration Testing Strategy

### Test Approach by Interface

| Interface | Test Type | Test Method | Success Indicator |
|-----------|-----------|-------------|-------------------|
| I1 (C1→C2) | Contract | Request type definitions for all known types | All types return valid definitions with inheritance rules |
| I2 (C1→C6) | Contract | Request verification rules for each type | Rules enable correct pass/fail determination |
| I3 (C1→C8) | Contract | Request local rules for edge and face types | Local rules correctly constrain adjacency |
| I4 (C2→C3) | Contract | Request schemas for template types | Schemas match template field requirements |
| I5 (C2→C6) | Integration | Verify document against schema | Schema verification matches expected results |
| I6 (C2→C14) | Contract | Request schemas for edge/face construction | Schemas enable correct simplex creation |
| I7 (C3→C4) | Integration | Compose document from template | Document structure matches template |
| I8 (C3→C5) | Integration | Store and retrieve templates | Templates persist with full fidelity |
| I9 (C4→C3) | Contract | Request templates by document type | All registered types return valid templates |
| I10 (C4→C5) | Integration | Write composed documents | Documents pass coherence enforcement |
| I11 (C4→C11) | Integration | Query prior work during composition | Relevant documents returned for reuse |
| I12 (C5→C1) | Integration | Write simplices with type validation | Invalid types rejected, valid accepted |
| I13 (C5→C11) | Event | Index updates on document changes | Search reflects changes within latency bound |
| I14 (C5→C12) | Integration | Graph queries on stored simplices | Correct relationships returned |
| I15 (C6→C2) | Contract | Retrieve schemas for verification | Schemas available for all document types |
| I16 (C6→C5) | Integration | Read documents for verification | All document fields accessible |
| I17 (C6→C10) | Event | Deliver verification results | Results formatted correctly for presentation |
| I18 (C7→C5) | Integration | Read documents and specs | Section structure parseable |
| I19 (C7→C10) | Event | Deliver analysis results | Results include section-by-section status |
| I20 (C8→C1) | Contract | Retrieve boundary and local rules | Rules for all edge/face types available |
| I21 (C8→C5) | Integration | Query neighborhoods for local rules | Correct adjacent simplices returned |
| I22 (C8→C10) | Event | Deliver boundary verification results | Results include rule-by-rule status |
| I23 (C9→C5) | Integration | Read documents and guidance | Criteria extractable from guidance |
| I24 (C9→C10) | Event | Deliver evaluation scores | Scores include per-criterion ratings |
| I25 (C10→C13) | Integration | Provide results for workflow | Results enable approval decisions |
| I26 (C11→C4) | Integration | Return prior work results | Results ranked by relevance |
| I27 (C11→C12) | Integration | Coordinate relationship-aware search | Graph context improves search relevance |
| I28 (C12→C5) | Integration | Query relationship data | All edges and paths returned correctly |
| I29 (C12→C8) | Integration | Check target existence | Broken references detected |
| I30 (C13→C14) | Command | Trigger simplex creation | Edges and faces created correctly |
| I31 (C13→C10) | Integration | Request formatted results | Results available for review |
| I32 (C14→C2) | Contract | Retrieve edge/face schemas | Schemas enable correct construction |
| I33 (C14→C5) | Integration | Write constructed simplices | Simplices pass all coherence checks |
| I34 (C14→C6) | Command | Trigger verification | Created simplices verified immediately |
| I35 (C5→C8) | Integration | Query neighborhoods | Star, coboundary, adjacency queries work |
| I36 (C13→C5) | Integration | Query dependency faces | Prerequisite faces correctly identified |
| I37 (C14→C8) | Command | Trigger local rule verification | Local rules checked before commit |

### Coherence Test Suite

| Test Category | Test Description | Success Criteria |
|---------------|------------------|------------------|
| Type Inheritance | Create simplices with valid/invalid tag chains | Valid chains accepted, invalid rejected |
| Edge Endpoint | Create edges with compatible/incompatible vertex types | Compatible accepted, incompatible rejected |
| Face Boundary | Create faces with valid/invalid edge triangles | Closed triangles accepted, open rejected |
| Local Rules | Create faces violating adjacency rules | Violations detected before commit |
| Euler Characteristic | Count V - E + F across charts | χ matches expected topology |
| Assurance Invariant | Verify "Assurances ≥ Documents" | Every doc vertex has assurance face |

## Traceability to Functional Architecture

### From Functions to Components

| Function | Primary Component | Supporting Components |
|----------|-------------------|----------------------|
| F1 Template Retrieval | C3 Template Registry | C5 Simplex Store |
| F2 Prior Work Discovery | C11 Search Index | C5, C12 |
| F3 Draft Generation | C4 Document Composer | C3, C5 |
| F4 Context Parameter Injection | C4 Document Composer | C5 |
| F5 Frontmatter Verification | C6 Schema Verifier | C2, C5, C10 |
| F6 Section Structure Verification | C7 Structure Analyzer | C5, C10 |
| F7 Count Consistency Verification | C7 Structure Analyzer | C5, C10 |
| F8 Reference Resolution Verification | C8 Boundary Verifier | C1, C5, C10, C12 |
| F9 Guidance-Based Evaluation | C9 Evaluation Engine | C5, C10 |
| F10 Full-Text Search | C11 Search Index | C5 |
| F11 Graph Traversal | C12 Graph Navigator | C5 |
| F12 Backlink Discovery | C12 Graph Navigator | C5 |
| F13 Approval Request Initiation | C13 Workflow Coordinator | C10 |
| F14 Verification Status Presentation | C10 Result Presenter | C6, C7, C8 |
| F15 Evaluation Score Presentation | C10 Result Presenter | C9 |
| F16 Validation Edge Creation | C14 Simplex Constructor | C2, C5, C6, C8 |
| F17 Runbook Step Tracking | C13 Workflow Coordinator | C5 |
| F18 Performance Metrics Collection | C13 Workflow Coordinator | C5 |
| F19 Specification Authoring | C2 Schema Registry | C5 |
| F20 Guidance Authoring | C2 Schema Registry | C5 |
| F21 Template Authoring | C3 Template Registry | C2, C5 |
| F22 Coupling Edge Creation | C14 Simplex Constructor | C2, C5, C6, C8 |
| F23 Verification Edge Creation | C14 Simplex Constructor | C2, C5, C6, C8 |
| F24 Assurance Face Construction | C14 Simplex Constructor | C2, C5, C6, C8 |

### Coverage Analysis

- **Complete coverage**: All 24 functions are realized by at least one component
- **Foundational support**: C1 (Type Ontology) and C5 (Simplex Store) support all functions
- **Focused components**: Each component has 1-4 primary functions (single responsibility)
- **Clear dependencies**: Supporting components provide infrastructure; primary components realize behavior

## Constraints and Assumptions

### Constraints

- **C1**: Components must be technology-agnostic (no implementation dependencies)
- **C2**: Type Ontology (C1) must define all simplex types before other components use them
- **C3**: Schema Verifier (C6) checks are deterministic and automated
- **C4**: Validation edges (F16) require human judgment—cannot be fully automated
- **C5**: Simplex Store (C5) must enforce coherence atomically on write
- **C6**: Local rules must be checkable using only topologically adjacent simplices
- **C7**: Boundary Verifier (C8) must have access to neighborhood queries

### Assumptions

- **A1**: Type definitions are stable (change infrequently after initial design)
- **A2**: All simplices have YAML frontmatter with type, extends, and tags fields
- **A3**: Templates are derived from specs and include all required fields
- **A4**: User identity is authenticated before approval functions
- **A5**: Runbooks define their step I/O types explicitly
- **A6**: The simplicial complex is connected (no isolated components)

---

**Note:** This logical architecture is the third of four extended architecture documents. It establishes system components that flow into [[physical-architecture-knowledge-complex-refactor]] (technologies that realize components) and summarizes the complete architecture chain.
