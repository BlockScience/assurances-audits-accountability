---
type: edge/coupling
extends: edge
id: e:coupling:functional-architecture
name: Coupling - Spec-for-Functional-Architecture and Guidance-for-Functional-Architecture
source: v:spec:functional-architecture
target: v:guidance:functional-architecture
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

# Coupling - Spec-for-Functional-Architecture and Guidance-for-Functional-Architecture

**This coupling connects the specification that defines functional architecture document structure with the guidance that defines functional architecture document quality criteria.**

## Purpose

This coupling enables the complete assurance of functional architecture documents. Together, these documents enable:

- **Verification:** Checking that a functional architecture document has required fields, sections, function-criterion matrix, and proper counts (against [spec-for-functional-architecture](../00_vertices/spec-for-functional-architecture.md))
- **Validation:** Assessing whether a functional architecture document has complete criterion coverage, clear I/O specifications, technology independence, and effective testing strategy (against [guidance-for-functional-architecture](../00_vertices/guidance-for-functional-architecture.md))

## Governed Document Type

Both documents govern all functional architecture documents in the knowledge complex, including:
- System functional architectures defining system behaviors
- Project functional specifications with I/O definitions
- Second-layer extended architecture documents in the architecture chain

## Role in Architecture Chain

Functional architecture is the second of four extended architecture documents:

```
field-survey (prerequisite to conceptual)
    │
    ▼
conceptual-architecture (prerequisite)
    │
    ▼
functional-architecture (governed by this coupling)
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
- Child docs are functional architecture documents (`vertex/doc` with `functional-architecture` tag)
- Verification edge: functional-architecture-doc → spec-for-functional-architecture
- Validation edge: functional-architecture-doc → guidance-for-functional-architecture
- Coupling edge: spec-for-functional-architecture ↔ guidance-for-functional-architecture (this edge)

## Semantic Alignment

The structural requirements in spec-for-functional-architecture align with the quality criteria in guidance-for-functional-architecture:

| Spec Requires | Guidance Assesses |
|---------------|-------------------|
| Conceptual architecture reference present | Traceability to conceptual architecture |
| Function count matches definitions | Function Completeness |
| Function table with I/O columns | I/O Clarity |
| Matrix covers all functions | Criterion Coverage |
| Functions are technology-agnostic | Technology Independence |
| System Testing Strategy section | Testing Strategy |

Together, they provide comprehensive coverage of what makes a functional architecture document both **valid** (structurally) and **excellent** (qualitatively).

## Function-Criterion Matrix Support

This coupling specifically supports the function-criterion matrix innovation:

| Spec Ensures | Guidance Assesses |
|--------------|-------------------|
| Matrix View table present | Functions address criteria meaningfully |
| Relationship Details table present | Contribution types justified |
| Key Traces section | Critical behaviors identified |
| Every function has >= 1 relationship | Appropriate criterion coverage |
| Contribution types documented | Types used appropriately |

## Bipartite Graph Properties

The function-criterion matrix forms a bipartite graph:

- **Partition 1:** Functions (defined in this document)
- **Partition 2:** Acceptance Criteria (from conceptual architecture)
- **Edges:** Contribution relationships with types and rationale

The spec ensures structural validity of this graph; the guidance assesses its semantic quality.

## V-Model Alignment

Functional architecture corresponds to the V-Model's functional requirements level:

| V-Model Aspect | Functional Architecture Coverage |
|----------------|----------------------------------|
| Left Side (Design) | Functional Architecture section |
| Right Side (Testing) | System Testing Strategy section |
| Evaluation Level | System Testing |

## Relationship to Boundary Complex

This coupling extends the boundary complex pattern to functional architecture documents:

```
        [spec-for-functional-architecture] ↔ [guidance-for-functional-architecture]
                        ↑                                   ↑
                 (verified by)                       (validated by)
                        ↑                                   ↑
                  [spec-for-spec]                  [guidance-for-guidance]
```

## Bootstrap Significance

This coupling establishes functional architecture documents as a first-class document type in the knowledge complex, enabling:
1. Formal verification of functional architecture documentation
2. Qualitative validation of function-criterion quality
3. Complete assurance triangles for functional architecture artifacts
4. Continuation of the extended architecture document chain
