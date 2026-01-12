---
type: vertex/doc
extends: doc
id: v:doc:architecture-knowledge-complex-refactor
name: Architecture - Knowledge Complex Framework Refactor
description: Capstone architecture document synthesizing the extended architecture chain for the Knowledge Complex Framework
tags:
  - vertex
  - doc
  - architecture
version: 1.2.0
created: 2026-01-11T00:00:00Z
modified: 2026-01-12T00:00:00Z
system_name: Knowledge Complex Framework
scope: Internal-first deployment enabling systematic documentation with verification, validation, and assurance for BlockScience client work
field_survey_ref: v:doc:field-survey-knowledge-complex-refactor
conceptual_architecture_ref: v:doc:conceptual-architecture-knowledge-complex-refactor
functional_architecture_ref: v:doc:functional-architecture-knowledge-complex-refactor
logical_architecture_ref: v:doc:logical-architecture-knowledge-complex-refactor
physical_architecture_ref: v:doc:physical-architecture-knowledge-complex-refactor
stakeholders:
  - A3 Operators
  - A4 Approvers
  - A5 Workflow Builders
  - A6 Infrastructure Builders
---

# Architecture - Knowledge Complex Framework Refactor

This architecture document synthesizes the complete extended architecture chain for the Knowledge Complex Framework—from stakeholder needs through physical implementation. The framework enables systematic documentation, verification, validation, and assurance of work products for BlockScience's internal use and eventual external productization.

## Overview

The Knowledge Complex Framework transforms how organizations manage knowledge-intensive work products. Built on the mathematical foundation of **typed simplicial complexes**, the framework provides:

- **Typed Documents** (vertices) with YAML frontmatter defining structure and semantics
- **Typed Relationships** (edges) for verification, validation, coupling, and accountability
- **Typed Triangles** (faces) for assurance, signatures, and authorization
- **Charts** (subcomplexes) for modular organization and contextual interpretation

The key innovation is the **base ontology** ([[ontology-base]]) which defines the foundational type system:
- 10 vertex types across 5 categories (documents, actors, organizational, modules)
- 13 edge types across 6 categories (assurance, signature, RBAC, module I/O, document relationships)
- 9 face types across 4 categories (assurance, RBAC, module I/O)
- 12 local rules enabling compositional verification
- 3 chart types (audit, module, runbook) for bounded sub-complexes

This architecture uses **Extended Mode**—each layer is documented in a separate extended architecture document, with this summary synthesizing key decisions and traceability.

### Architecture Chain

| Layer | Document | Key Content |
|-------|----------|-------------|
| Field Survey | [[field-survey-knowledge-complex-refactor]] | 6 stakeholders (A1-A6), 15 resources (R1-R15), 28 relationships |
| Conceptual | [[conceptual-architecture-knowledge-complex-refactor]] | 4 stakeholders (A3-A6), 12 acceptance criteria (AC1-AC12), 3 constraints |
| Functional | [[functional-architecture-knowledge-complex-refactor]] | 31 functions (F1-F31) in 6 functional areas |
| Logical | [[logical-architecture-knowledge-complex-refactor]] | 14 components (C1-C14), 40 interfaces, references [[ontology-base]] |
| Physical | [[physical-architecture-knowledge-complex-refactor]] | 12 elements (E1-E12), deployment architecture |

## V-Model Summary

| Layer | Left Side (Idealized) | Design Status | Right Side (Realized) | Implementation Status |
|-------|----------------------|---------------|----------------------|----------------------|
| **Conceptual** | ConOps: 4 stakeholders, 12 acceptance criteria defining success | Assured | Acceptance Testing: Operator/Approver workflow validation, effectiveness metrics | Partial |
| **Functional** | Functional Architecture: 31 functions in 6 areas | Assured | System Testing: Function-by-function test criteria | Partial |
| **Logical** | Logical Architecture: 14 components, 40 interfaces, [[ontology-base]] | Assured | Integration Testing: 40 interface tests, coherence suite | In Progress |
| **Physical** | Physical Architecture: 12 elements (OFM, Git, Python, Obsidian, Claude Code) | Assured | Unit Testing: Element-by-element test criteria | Partial |

**Status Legend:**

| Column | Values | Meaning |
|--------|--------|---------|
| Design Status | Draft, Review, Assured | Maturity of design documentation |
| Implementation Status | Not Started, In Progress, Partial, Complete | Progress on realization and testing |

**Current State:** All design documents are assured. Implementation is partial—core verification scripts exist and pass, but full test suites for all 40 interfaces and acceptance testing workflows are in progress.

## Conceptual Layer

**Reference:** [[conceptual-architecture-knowledge-complex-refactor]]

### Problem Statement (ConOps)

BlockScience produces complex deliverables for clients—research reports, system designs, technical specifications, audit findings. Current pain points:

- **Documentation chaos**: Scattered locations, inconsistent formats, quality by individual expertise
- **Knowledge capture**: Institutional knowledge not systematized or searchable
- **Client deliverable quality**: Need to produce demonstrably assured work products

**Desired state**: Documents in version-controlled repositories with consistent structure, measurable quality criteria, systematic verification, clear accountability, and demonstrable work quality through assurance charts.

### Stakeholder Needs Summary

| Stakeholder                    | Key Needs                                                                                                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A3 Operators**               | Find templates quickly, create conforming documents without needing to understand framework, get immediate verification feedback, work with familiar tools (IDE, markdown, git) |
| **A4 Approvers**               | Know documents are verification-ready, understand attestation scope, review efficiently, trust verification infrastructure, see both compliance and effectiveness evidence      |
| **A5 Workflow Builders**       | Configure types without mathematical expertise, create runbooks, access reusable components, test workflows, define effectiveness metrics                                       |
| **A6 Infrastructure Builders** | Maintain clean abstractions; develop, use and enforce ontologies; develop testable tooling, support multiple deployment contexts                                                |

### Acceptance Criteria Summary

| ID | Criterion | Target | Stakeholder Impact |
|----|-----------|--------|-------------------|
| AC1 | Document creation time | <30 min for standard types | A3, A5 |
| AC2 | Verification feedback speed | <3 seconds | A3, A5, A6 |
| AC3 | Verification accuracy | <5% false negatives/positives | A3, A4, A5, A6 |
| AC4 | Search effectiveness | <5 min to find usable reference | A3, A6 |
| AC5 | Approval efficiency | <15 min for standard documents | A4 |
| AC6 | Approval confidence | >90% report confident | A4 |
| AC7 | Effectiveness visibility | 100% runbooks include metrics | A4, A5 |
| AC8 | Workflow builder productivity | <2 hr for new runbook with types | A5, A6 |
| AC9 | Self-demonstration | 100% framework docs assured | A6 |
| AC10 | Evaluation usefulness | >90% find scores useful | A3, A4, A5, A6 |
| AC11 | Client demonstration | ≥3 production-quality examples | A5, A6 |
| AC12 | Runbook execution support | 100% show step/context/I/O | A3, A4, A5, A6 |

### Constraints

| ID | Constraint |
|----|------------|
| C1 | Documents must remain human-readable markdown with YAML frontmatter |
| C2 | Git must remain the source of truth for version control |
| C3 | Human approval required for all validation and assurance (no automated trust) |

## Functional Layer

**Reference:** [[functional-architecture-knowledge-complex-refactor]]

### Functional Architecture

The framework provides 31 functions organized into 6 functional areas:

| Area | Functions | Purpose |
|------|-----------|---------|
| **Document Authoring** | F1-F4 | Template retrieval, prior work discovery, draft generation, parameter injection |
| **Quality Assurance** | F5-F9 | Frontmatter verification, section structure verification, count verification, reference verification, guidance evaluation |
| **Knowledge Navigation** | F10-F12 | Full-text search, graph traversal, backlink discovery |
| **Approval & Accountability** | F13-F18 | Approval requests, status presentation, validation edge creation, runbook tracking, metrics collection |
| **Configuration & Meta** | F19-F24 | Spec authoring, guidance authoring, template authoring, coupling/verification/assurance construction |
| **Runbook Management** | F25-F31 | Runbook retrieval, module authoring, runbook assembly, I/O validation, execution instantiation, step context, completion |

### Function-Criterion Matrix (Key Traces)

| Criterion | Primary Functions | Rationale |
|-----------|-------------------|-----------|
| AC1 (Creation time) | F1, F3 | Template retrieval + draft generation enable fast document creation |
| AC2, AC3 (Verification) | F5, F6, F7, F8 | Four-layer verification: frontmatter, sections, counts, references |
| AC4 (Search) | F2, F10, F11, F12 | Discovery + search + graph navigation |
| AC5, AC6, AC10 (Approval) | F14, F15, F16 | Status presentation + evaluation scores + validation edges |
| AC7 (Effectiveness) | F17, F18, F27, F31 | Runbook tracking + metrics collection + assembly + completion |
| AC8 (Workflow builder) | F19, F20, F21, F22, F26, F27, F28 | Type configuration + module authoring + runbook assembly + I/O validation |
| AC9 (Self-demonstration) | F8, F22, F23, F24 | Coupling + verification edge + assurance face construction |
| AC12 (Runbook execution) | F25, F29, F30, F31 | Runbook retrieval + execution instantiation + step context + completion |

### System Testing Criteria

All 31 functions have specific test methods with measurable success indicators. Key system-level tests include:
- End-to-end workflow completion (draft → verify → validate → assure)
- Verification accuracy against known-good and known-bad document suites
- Evaluation correlation with expert ratings (>80% agreement)
- Runbook step tracking accuracy (100% correct)

## Logical Layer

**Reference:** [[logical-architecture-knowledge-complex-refactor]]

### The Base Ontology Innovation

The logical architecture is founded on [[ontology-base]]—a typed simplicial complex where:

**Simplex Structure:**
- **0-simplices (vertices)** = documents with typed YAML headers
- **1-simplices (edges)** = typed relationships between vertices
- **2-simplices (faces)** = triangular structures (assurance, signature, authorization)

**Type Hierarchy:**
```
vertex (abstract base)
├── doc (content artifacts)
│   ├── spec (structural requirements)
│   ├── guidance (quality criteria)
│   ├── ontology (type definitions)
│   └── module (typed I/O transformation)
├── actor (entities that can act)
│   └── signer (verified identity for signing)
├── role (organizational position)
└── authority (atomic permission)
```

**Local Rules (Compositional Verification):**

Local rules are constraints evaluated using only topologically adjacent simplices, enabling:
- Check locally → guarantee globally
- Incremental validation on simplex addition
- Domain-specific constraints through face adjacency requirements

Key local rules include:
- **Module Qualification Cascade**: `qualifies(signer, module)` requires `qualifies(signer, g)` for all output guidances
- **Signature-Assurance Adjacency**: Signature faces must share validation edge with assurance faces
- **Assurance-B2 Anchor**: All assurance faces must trace to bootstrap (b2) anchor
- **Runbook DAG Requirement**: `precedes` edges form directed acyclic graph
- **Runbook I/O Chaining**: Output type of module N = input type of module N+1

### Logical Architecture

14 components organized into 6 areas:

| Area | Components | Responsibility |
|------|------------|----------------|
| **Type System** | C1 Type Ontology, C2 Schema Registry | Define simplex types, schemas, local rules |
| **Document Management** | C3 Template Registry, C4 Document Composer, C5 Simplex Store | Templates, composition, persistence with coherence enforcement |
| **Coherence Verification** | C6 Schema Verifier, C7 Structure Analyzer, C8 Boundary Verifier | YAML, markdown, and simplicial complex verification |
| **Quality Assessment** | C9 Evaluation Engine, C10 Result Presenter | Guidance scoring, result formatting |
| **Knowledge Graph** | C11 Search Index, C12 Graph Navigator | Full-text search, relationship traversal |
| **Workflow & Accountability** | C13 Workflow Coordinator, C14 Simplex Constructor | Approval workflow, edge/face creation |

### Component-Function Matrix (Key Allocations)

| Component | Primary Functions | Rationale |
|-----------|-------------------|-----------|
| C1 Type Ontology | All (supporting) | Foundation for all typed operations |
| C6 Schema Verifier | F5 | Frontmatter verification |
| C7 Structure Analyzer | F6, F7 | Section and count verification |
| C8 Boundary Verifier | F8 | Reference resolution + local rules |
| C14 Simplex Constructor | F16, F22-F24 | All edge and face creation |

### Integration Testing Criteria

40 interface tests ensure correct component collaboration. Key coherence tests:
- Type inheritance chain validation
- Edge endpoint type compliance
- Face boundary closure
- Local rule satisfaction (all 12 rules)
- Euler characteristic verification

## Physical Layer

**Reference:** [[physical-architecture-knowledge-complex-refactor]]

### Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Data standard | Obsidian Flavored Markdown (OFM) | Wikilinks for navigation, YAML for structure, human-readable |
| Structural truth | YAML frontmatter | Boundaries computed from YAML fields, not wikilinks |
| Toolchain | Python-only with uv | Single language, fast environment management |
| Human interface | Obsidian + Claude Code | Dual interface for navigation and AI-assisted authoring |
| Accountability | GPG signatures on commits | Cryptographic verification of approvers |
| CI enforcement | GitHub Actions | Prevents invalid documents from reaching main branch |

### Physical Elements Summary

| ID | Element | Technology | Purpose |
|----|---------|------------|---------|
| E1 | Ontology Files | OFM + YAML | Load-bearing type definitions |
| E2 | Document Files | OFM + YAML | All simplices as markdown with frontmatter |
| E3 | Template Files | OFM + placeholders | Document scaffolding |
| E4 | Git Repository | Git 2.40+ with GPG | Version control and cryptographic accountability |
| E5 | Python Package | Python 3.12+, uv | Core library implementing all logic |
| E6 | YAML Parser | PyYAML 6.0+ | Frontmatter parsing |
| E7 | Graph Library | NetworkX 3.2+ | In-memory graph for traversal and verification |
| E8 | Chart Visualization | matplotlib + plotly | Visual validation of charts |
| E9 | Obsidian | Obsidian 1.5+ | Human navigation, search, review |
| E10 | Claude Code | Claude Code | LLM-assisted authoring |
| E11 | GPG Signatures | GnuPG 2.x | Commit and edge signing |
| E12 | GitHub Actions | GitHub Actions | CI enforcement of ontology rules |

### Element-Component Matrix (Key Implementations)

| Element | Components | Implementation Notes |
|---------|------------|---------------------|
| E1, E2, E3, E4 | C3, C5 | File-based storage—documents ARE the stores |
| E5 | C4, C6-C10, C13-C14 | Python implements all programmatic logic |
| E6 | C6, C14 | YAML parser extracts structural truth |
| E7 | C8, C12 | NetworkX for boundary verification and graph traversal |
| E9, E10 | C11, C12, C4, C13 | Dual interface for human and AI access |
| E11, E12 | C13, C6-C8 | Cryptographic accountability + CI enforcement |

### Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        User Workstation                              │
├─────────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐              ┌──────────────┐                     │
│  │   Obsidian   │              │  Claude Code │                     │
│  │    (E9)      │              │    (E10)     │                     │
│  └──────┬───────┘              └──────┬───────┘                     │
│         └─────────────┬───────────────┘                              │
│                       ▼                                              │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                  Python Package (E5)                          │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────────────────────────┐     │   │
│  │  │  YAML   │ │ NetworkX│ │  Visualization               │     │   │
│  │  │ Parser  │ │  Graph  │ │  (matplotlib, plotly)        │     │   │
│  │  │  (E6)   │ │  (E7)   │ │        (E8)                 │     │   │
│  │  └─────────┘ └─────────┘ └─────────────────────────────┘     │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                       │                                              │
│                       ▼                                              │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │              Git Repository (E4) + GPG (E11)                  │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐             │   │
│  │  │  Ontology   │ │  Template   │ │  Document   │             │   │
│  │  │  Files (E1) │ │  Files (E3) │ │  Files (E2) │             │   │
│  │  └─────────────┘ └─────────────┘ └─────────────┘             │   │
│  │  ┌───────────────────────────────────────────────────────┐   │   │
│  │  │  00_vertices/  │  01_edges/  │  02_faces/  │  charts/  │   │   │
│  │  └───────────────────────────────────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────────────┘   │
└───────────────────────┼─────────────────────────────────────────────┘
                        │ git push
                        ▼
┌─────────────────────────────────────────────────────────────────────┐
│                          GitHub (Remote)                             │
├─────────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                  GitHub Actions (E12)                         │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐             │   │
│  │  │   verify-   │ │   verify-   │ │   verify-   │             │   │
│  │  │  documents  │ │    types    │ │  boundaries │             │   │
│  │  └─────────────┘ └─────────────┘ └─────────────┘             │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

### Deferred Elements

The following are deferred for future scaling:
- Full-text search engine (when >10k docs)
- CLI framework (Click) for polished non-IDE experience
- Document/Relational database for complex queries
- LLM abstraction layer for multi-provider support

## Traceability Matrix

### End-to-End Traceability

| Stakeholder Need | Acceptance Criterion | Primary Functions | Components | Elements |
|------------------|---------------------|-------------------|------------|----------|
| Operators find templates (A3) | AC1 | F1, F3 | C3, C4 | E3, E5 |
| Operators get verification feedback (A3) | AC2, AC3 | F5, F6, F7, F8 | C6, C7, C8 | E5, E6 |
| Operators search prior work (A3) | AC4 | F2, F10, F11 | C11, C12 | E7, E9 |
| Approvers review efficiently (A4) | AC5 | F14, F15 | C10 | E5, E8 |
| Approvers sign with confidence (A4) | AC6 | F16 | C14 | E5, E11 |
| Approvers see effectiveness (A4) | AC7, AC10 | F9, F17, F18 | C9, C13 | E5, E10 |
| Workflow builders create types (A5) | AC8 | F19, F20, F21, F22 | C2, C3 | E1, E3, E5 |
| Framework self-demonstrates (A6) | AC9 | F23, F24 | C14 | E5 |
| Client demonstration (A5, A6) | AC11 | F3, F24 | C4, C14 | E2, E5 |

### Constraints Trace

| Constraint | Enforcement Layer | Mechanism |
|------------|-------------------|-----------|
| C1 (Human-readable markdown) | Physical | OFM documents (E2), YAML frontmatter (E6) |
| C2 (Git as truth) | Physical | Git repository (E4), GitHub Actions (E12) |
| C3 (Human approval required) | Logical + Physical | C13 Workflow Coordinator + GPG signatures (E11) |

## Risks and Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Learning curve deters adoption | High | Medium | Simple document types first; hands-on training; pair with experienced users |
| Verification too slow | Medium | Low | Profile and optimize; cache results; incremental verification |
| Operators bypass verification | High | Medium | Automatic non-blocking verification; prominent results; tie to approval workflow |
| Approvers rubber-stamp | High | Medium | Explicit attestation; track patterns; review effectiveness metrics |
| Runbooks lack effectiveness metrics | Medium | High | Templates with metric placeholders; review before deployment |
| Local rules too complex to verify | Medium | Low | Neighborhood queries in C5; star/coboundary primitives; incremental checking |
| Ontology changes break existing docs | High | Low | Ontology files (E1) protected; change control; version-locked deployments |

## Key Design Decisions

### 1. OFM as Data Standard

**Decision**: Use Obsidian Flavored Markdown with YAML frontmatter as the universal data format.

**Rationale**:
- Human-readable (constraint C1)
- Wikilinks enable Obsidian navigation
- YAML provides structural truth for programmatic access
- Documents remain valid even if wikilinks removed

### 2. YAML Frontmatter as Structural Truth

**Decision**: Compute simplicial complex boundaries from YAML fields (`source`, `target`, `boundary_edges`, `boundary_vertices`), not from wikilink presence.

**Rationale**:
- Non-Obsidian tools can compute graph structure from YAML alone
- Separates navigation concerns (wikilinks) from structural concerns (YAML)
- Enables reliable programmatic verification

### 3. Typed Simplicial Complex Foundation

**Decision**: Base all document relationships on [[ontology-base]] typed simplicial complex.

**Rationale**:
- Local rules enable compositional verification (check locally, guarantee globally)
- Face types (assurance, signature, authorization) encode accountability
- Chart types (audit, module, runbook) enable modular organization
- Mathematical foundation ensures coherence

### 4. Python-Only Toolchain with uv

**Decision**: Implement all tooling in Python 3.12+ with uv for environment management.

**Rationale**:
- Single language simplifies maintenance
- Team expertise in Python
- uv provides fast, reliable environment management
- Defers TypeScript/VS Code extension complexity

### 5. Dual Interface (Obsidian + Claude Code)

**Decision**: Obsidian for human navigation/review; Claude Code for AI-assisted authoring.

**Rationale**:
- Obsidian excels at graph navigation and search
- Claude Code excels at template filling and verification interpretation
- Both operate on same git repository
- No lock-in to either tool

### 6. Cryptographic Accountability (GPG)

**Decision**: Use GPG signatures on git commits for accountability.

**Rationale**:
- Verifiable attribution for validation edges
- Tamper-evident commit history
- Standard tooling (git + gpg)
- Supports constraint C3 (human approval)

### 7. CI Enforcement (GitHub Actions)

**Decision**: Use GitHub Actions to enforce ontology rules at repository level.

**Rationale**:
- Prevents invalid documents from reaching main branch
- Catches issues even if local checks bypassed
- Maintains coherence across contributors
- Enables branch protection integration

---

**Note:** This architecture document is the capstone of the extended architecture chain. It synthesizes decisions from [[field-survey-knowledge-complex-refactor]] through [[physical-architecture-knowledge-complex-refactor]], with the [[ontology-base]] typed simplicial complex as the foundational innovation enabling systematic, verifiable knowledge management.