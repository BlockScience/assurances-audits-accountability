---
type: edge/coupling
extends: edge
id: e:coupling:conceptual-architecture
name: Coupling - Spec-for-Conceptual-Architecture and Guidance-for-Conceptual-Architecture
source: v:spec:conceptual-architecture
target: v:guidance:conceptual-architecture
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-01-11T00:00:00Z
modified: 2025-01-11T00:00:00Z
---

# Coupling - Spec-for-Conceptual-Architecture and Guidance-for-Conceptual-Architecture

**This coupling connects the specification that defines conceptual architecture document structure with the guidance that defines conceptual architecture document quality criteria.**

## Purpose

This coupling enables the complete assurance of conceptual architecture documents. Together, these documents enable:

- **Verification:** Checking that a conceptual architecture document has required fields, sections, stakeholder-criterion matrix, and proper counts (against [spec-for-conceptual-architecture](../00_vertices/spec-for-conceptual-architecture.md))
- **Validation:** Assessing whether a conceptual architecture document has complete stakeholder coverage, quality criteria, accurate matrix relationships, and clear operational context (against [guidance-for-conceptual-architecture](../00_vertices/guidance-for-conceptual-architecture.md))

## Governed Document Type

Both documents govern all conceptual architecture documents in the knowledge complex, including:
- System conceptual architectures establishing stakeholder needs
- Project ConOps documentation with acceptance criteria
- First-layer extended architecture documents in the architecture chain

## Role in Architecture Chain

Conceptual architecture is the first of four extended architecture documents:

```
field-survey (prerequisite)
    │
    ▼
conceptual-architecture (governed by this coupling)
    │
    ▼
functional-architecture (future)
    │
    ▼
logical-architecture (future)
    │
    ▼
physical-architecture (future)
    │
    ▼
architecture (summary - synthesizes all four)
```

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are conceptual architecture documents (`vertex/doc` with `conceptual-architecture` tag)
- Verification edge: conceptual-architecture-doc → spec-for-conceptual-architecture
- Validation edge: conceptual-architecture-doc → guidance-for-conceptual-architecture
- Coupling edge: spec-for-conceptual-architecture ↔ guidance-for-conceptual-architecture (this edge)

## Semantic Alignment

The structural requirements in spec-for-conceptual-architecture align with the quality criteria in guidance-for-conceptual-architecture:

| Spec Requires | Guidance Assesses |
|---------------|-------------------|
| Field survey reference present | Traceability to field survey |
| Stakeholder count matches subsections | Stakeholder Completeness |
| Criterion count matches table rows | Criterion Quality |
| Matrix covers all stakeholders | Matrix Accuracy |
| Operational Context section | ConOps Clarity |
| Acceptance Testing Strategy section | Testing Strategy |

Together, they provide comprehensive coverage of what makes a conceptual architecture document both **valid** (structurally) and **excellent** (qualitatively).

## Stakeholder-Criterion Matrix Support

This coupling specifically supports the stakeholder-criterion matrix innovation:

| Spec Ensures | Guidance Assesses |
|--------------|-------------------|
| Matrix View table present | Relationships are meaningful |
| Relationship Details table present | Rationale is justified |
| Key Dependencies section | Critical dependencies identified |
| Every stakeholder has >= 1 relationship | Appropriate sparsity (not fully connected) |
| Relationship types documented | Types used appropriately |

## Bipartite Graph Properties

The stakeholder-criterion matrix forms a bipartite graph similar to the actor-resource graph in field surveys:

- **Partition 1:** Stakeholders (subset of actors from field survey)
- **Partition 2:** Acceptance Criteria (defined in this document)
- **Edges:** Relationships with types and rationale

The spec ensures structural validity of this graph; the guidance assesses its semantic quality.

## Relationship to Boundary Complex

This coupling extends the boundary complex pattern to conceptual architecture documents:

```
        [spec-for-conceptual-architecture] ↔ [guidance-for-conceptual-architecture]
                        ↑                                   ↑
                 (verified by)                       (validated by)
                        ↑                                   ↑
                  [spec-for-spec]                  [guidance-for-guidance]
```

The spec-for-conceptual-architecture is itself a specification (verified against spec-for-spec, validated against guidance-for-spec). The guidance-for-conceptual-architecture is itself a guidance document (verified against spec-for-guidance, validated against guidance-for-guidance).

## Bootstrap Significance

This coupling establishes conceptual architecture documents as a first-class document type in the knowledge complex, enabling:
1. Formal verification of conceptual architecture documentation
2. Qualitative validation of stakeholder-criterion quality
3. Complete assurance triangles for conceptual architecture artifacts
4. Foundation for the extended architecture document chain
