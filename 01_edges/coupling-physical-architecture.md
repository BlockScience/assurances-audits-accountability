---
type: edge/coupling
extends: edge
id: e:coupling:physical-architecture
name: Coupling - Spec-for-Physical-Architecture and Guidance-for-Physical-Architecture
source: v:spec:physical-architecture
target: v:guidance:physical-architecture
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

# Coupling - Spec-for-Physical-Architecture and Guidance-for-Physical-Architecture

**This coupling connects the specification that defines physical architecture document structure with the guidance that defines physical architecture document quality criteria.**

## Purpose

This coupling enables the complete assurance of physical architecture documents. Together, these documents enable:

- **Verification:** Checking that a physical architecture document has required fields, sections, element-component matrix, and proper counts (against [spec-for-physical-architecture](../00_vertices/spec-for-physical-architecture.md))
- **Validation:** Assessing whether a physical architecture document has complete component coverage, specific technology choices with versions, clear rationale, and well-defined deployment configurations (against [guidance-for-physical-architecture](../00_vertices/guidance-for-physical-architecture.md))

## Governed Document Type

Both documents govern all physical architecture documents in the knowledge complex, including:
- System physical architectures defining technology choices
- Project implementation specifications with deployment configurations
- Fourth-layer extended architecture documents completing the architecture chain

## Role in Architecture Chain

Physical architecture is the fourth and final extended architecture document:

```
field-survey (prerequisite to conceptual)
    │
    ▼
conceptual-architecture
    │
    ▼
functional-architecture
    │
    ▼
logical-architecture (prerequisite)
    │
    ▼
physical-architecture (governed by this coupling)
    │
    ▼
architecture (summary - synthesizes all four)
```

Physical architecture completes the extended architecture chain, providing the final layer before the summary architecture document.

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are physical architecture documents (`vertex/doc` with `physical-architecture` tag)
- Verification edge: physical-architecture-doc → spec-for-physical-architecture
- Validation edge: physical-architecture-doc → guidance-for-physical-architecture
- Coupling edge: spec-for-physical-architecture ↔ guidance-for-physical-architecture (this edge)

## Semantic Alignment

The structural requirements in spec-for-physical-architecture align with the quality criteria in guidance-for-physical-architecture:

| Spec Requires | Guidance Assesses |
|---------------|-------------------|
| Logical architecture reference present | Traceability to logical architecture |
| Element count matches definitions | Component Coverage |
| Technology/Tool column in Element Table | Technology Specificity |
| Rationale in Element Definitions | Rationale Clarity |
| Deployment View section | Deployment Clarity |
| Unit Testing Strategy section | Testing Strategy |

Together, they provide comprehensive coverage of what makes a physical architecture document both **valid** (structurally) and **excellent** (qualitatively).

## Element-Component Matrix Support

This coupling specifically supports the element-component matrix innovation:

| Spec Ensures | Guidance Assesses |
|--------------|-------------------|
| Matrix View table present | Elements implement components meaningfully |
| Relationship Details table present | Implementation types justified |
| Key Implementations section | Critical technology decisions identified |
| Every element has >= 1 relationship | Appropriate component coverage |
| Implementation types documented | Types used appropriately |

## Technology Specificity: Key Quality

The physical architecture layer has special significance for technology specificity:

| Aspect | Importance |
|--------|------------|
| Concreteness | Physical architecture must name actual technologies |
| Versions | Version information enables reproducible builds |
| Rationale | Explains why specific technologies were chosen |
| Alternatives | Documents what was considered and rejected |

Both spec and guidance emphasize technology specificity as a REQUIRED quality—physical architecture documents that use vague technology references fail their purpose.

## Bipartite Graph Properties

The element-component matrix forms a bipartite graph:

- **Partition 1:** Elements (defined in this document)
- **Partition 2:** Components (from logical architecture)
- **Edges:** Implementation relationships with types and rationale

The spec ensures structural validity of this graph; the guidance assesses its semantic quality.

## V-Model Alignment

Physical architecture corresponds to the V-Model's implementation level:

| V-Model Aspect | Physical Architecture Coverage |
|----------------|--------------------------------|
| Left Side (Design) | Physical Architecture section |
| Right Side (Testing) | Unit Testing Strategy section |
| Evaluation Level | Unit Testing |

## Full Architecture Chain Traceability

Physical architecture completes the full traceability chain:

```
Stakeholder Needs (Conceptual)
    ↓ addressed by
Acceptance Criteria (Conceptual)
    ↓ achieved by
Functions (Functional)
    ↓ realized by
Components (Logical)
    ↓ implemented by
Elements (Physical) ← THIS LAYER
```

A complete architecture chain enables tracing any implementation element back to the stakeholder need it ultimately serves.

## Relationship to Boundary Complex

This coupling extends the boundary complex pattern to physical architecture documents:

```
        [spec-for-physical-architecture] ↔ [guidance-for-physical-architecture]
                        ↑                                   ↑
                 (verified by)                       (validated by)
                        ↑                                   ↑
                  [spec-for-spec]                  [guidance-for-guidance]
```

## Bootstrap Significance

This coupling establishes physical architecture documents as a first-class document type in the knowledge complex, enabling:
1. Formal verification of physical architecture documentation
2. Qualitative validation of element-component quality
3. Complete assurance triangles for physical architecture artifacts
4. Completion of the extended architecture document chain
5. Full traceability from stakeholder needs to implementation technologies
