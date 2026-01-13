---
type: edge/coupling
extends: edge
id: e:coupling:ontology
name: Coupling - Ontology Spec and Guidance
source: v:spec:ontology
target: v:guidance:ontology
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2026-01-11T00:00:00Z
modified: 2026-01-11T00:00:00Z
---

# Coupling - Ontology Spec and Guidance

This coupling connects the specification for ontology documents with the guidance for evaluating ontology quality.

## Purpose

Together, these documents enable complete assurance of ontology documents:

- **Verification** (against [[spec-for-ontology]]): Checking that an ontology has required sections, correct type definition formats, and consistent frontmatter
- **Validation** (against [[guidance-for-ontology]]): Assessing whether an ontology is complete, coherent, extensible, well-documented, and verifiable

## Governed Document Type

Both documents govern ontology documents (`type: vertex/ontology`) which define the type system for a knowledge complex. Ontologies specify:

- Vertex types (0-simplices)
- Edge types (1-simplices)
- Face types (2-simplices)
- Local rules (constraints on adjacent simplices)

## Structural-Quality Alignment

| Structural Requirement (Spec) | Quality Criterion (Guidance) |
|-------------------------------|------------------------------|
| Vertex type definitions present | Type Completeness |
| Local rule definitions present | Coherence Rules |
| Extension mechanism documented | Extension Clarity |
| Type hierarchy (extends, tags) | Type Hierarchy Consistency |
| Purpose and field documentation | Documentation Quality |
| Local rule format | Local Rule Verifiability |

## Role in Assurance

This coupling forms the base of assurance triangles for all ontology documents:

```
         ontology-doc
           /      \
          /        \
  verification   validation
        /            \
       /              \
v:spec:ontology ---- v:guidance:ontology
           e:coupling:ontology
```

When an ontology document:
1. Passes verification against spec-for-ontology
2. Receives validation approval against guidance-for-ontology
3. Has this coupling edge connecting its spec and guidance

...an assurance face can be constructed, attesting to both structural correctness and quality.

## Significance

Ontologies are foundational infrastructure. This coupling ensures that:

1. **Structural soundness**: Ontologies have required components (types, rules, extension points)
2. **Quality assurance**: Ontologies are evaluated for completeness, coherence, and usability
3. **Foundation integrity**: The types defined in ontologies can be trusted by all dependent documents

Every other spec, guidance, and document in a knowledge complex depends on the ontology's correctness. This coupling is therefore critical infrastructure.
