---
type: edge/coupling
extends: edge
id: e:coupling:architecture
name: Coupling - Spec-for-Architecture and Guidance-for-Architecture
source: v:spec:architecture
target: v:guidance:architecture
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-12-30T12:00:00Z
modified: 2025-12-30T12:00:00Z
---

# Coupling - Spec-for-Architecture and Guidance-for-Architecture

**This coupling connects the specification that defines architecture document structure with the guidance that defines architecture document quality criteria.**

## Purpose

This coupling enables the complete assurance of architecture documents. Together, these documents enable:

- **Verification:** Checking that an architecture document has required fields, sections, and the V-model summary table (against [spec-for-architecture](../00_vertices/spec-for-architecture.md))
- **Validation:** Assessing whether an architecture document is complete, coherent, traceable, and fit-for-purpose (against [guidance-for-architecture](../00_vertices/guidance-for-architecture.md))

## Governed Document Type

Both documents govern all architecture documents in the knowledge complex, including:
- System architecture descriptions
- Project architecture documentation
- Self-demonstrating projects (like the INCOSE paper framework)

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are architecture documents (`vertex/doc` with `architecture` tag)
- Verification edge: architecture-doc → spec-for-architecture
- Validation edge: architecture-doc → guidance-for-architecture
- Coupling edge: spec-for-architecture ↔ guidance-for-architecture (this edge)

## Semantic Alignment

The structural requirements in spec-for-architecture align with the quality criteria in guidance-for-architecture:

| Spec-for-Architecture Requires | Guidance-for-Architecture Assesses |
|-------------------------------|-----------------------------------|
| V-Model Summary table | V-Model Alignment quality |
| Four layer sections | Layer Completeness depth |
| Test criteria per layer | Testability specificity |
| Technology-agnostic logical layer | Technology Independence |
| Stakeholder needs in conceptual | Stakeholder Clarity |
| Minimum element counts | Traceability across layers |

Together, they provide comprehensive coverage of what makes an architecture document both **valid** (structurally) and **excellent** (qualitatively).

## 4-Layer Framework Support

This coupling specifically supports the SE 4-layer architecture framework:

| Layer | Spec Ensures | Guidance Assesses |
|-------|-------------|-------------------|
| **Conceptual** | ConOps section present, acceptance criteria included | Stakeholder clarity, need distinctiveness |
| **Functional** | Function table with I/O, system test criteria | Function coverage, testability |
| **Logical** | Component table with interfaces, integration tests | Technology independence, design cohesion |
| **Physical** | Implementation table, unit test criteria | Implementation specificity, rationale clarity |

## Relationship to Boundary Complex

This coupling extends the boundary complex pattern to architecture documents:

```
                    [spec-for-architecture] ←→ [guidance-for-architecture]
                              ↑                           ↑
                       (verified by)               (validated by)
                              ↑                           ↑
                        [spec-for-spec]          [guidance-for-guidance]
```

The spec-for-architecture is itself a specification (verified against spec-for-spec, validated against guidance-for-spec). The guidance-for-architecture is itself a guidance document (verified against spec-for-guidance, validated against guidance-for-guidance).

## Bootstrap Significance

This coupling establishes architecture documents as a first-class document type in the knowledge complex, enabling:
1. Formal verification of architecture documentation
2. Qualitative validation of architecture quality
3. Complete assurance triangles for architecture artifacts
4. Self-demonstrating architecture documents (architectures that describe themselves)
