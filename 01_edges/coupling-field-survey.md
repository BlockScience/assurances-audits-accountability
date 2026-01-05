---
type: edge/coupling
extends: edge
id: e:coupling:field-survey
name: Coupling - Spec-for-Field-Survey and Guidance-for-Field-Survey
source: v:spec:field-survey
target: v:guidance:field-survey
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-01-04T23:00:00Z
modified: 2025-01-04T23:00:00Z
---

# Coupling - Spec-for-Field-Survey and Guidance-for-Field-Survey

**This coupling connects the specification for field survey documents with the guidance for field survey quality.**

## Purpose

This coupling links the structural requirements for field survey documents with their quality criteria, enabling complete assurance of context-mapping documentation. Together, these documents enable:

- **Verification:** Checking that a field survey has required sections, actor/resource counts, and relationship mappings (against [[spec-for-field-survey]])
- **Validation:** Assessing whether a field survey effectively maps stakeholders, resources, and relationships within scope (against [[guidance-for-field-survey]])

## Governed Document Type

Both documents govern all field survey documents in the knowledge complex. Field surveys establish context before architecture work by mapping:
- Actors (stakeholders accountable for or affected by the system)
- Resources (technologies, data, infrastructure, services, capital)
- Relationships (bipartite graph of actor-resource connections)
- Scope boundaries (explicit in/out of scope definitions)

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are field survey documents (`type: vertex/doc` with `field-survey` tag)
- Verification edge: field-survey → spec-for-field-survey
- Validation edge: field-survey → guidance-for-field-survey
- Coupling edge: spec-for-field-survey ↔ guidance-for-field-survey (this edge)

## Assurance Triangle Structure

```
               field-survey-doc
                     /\
                    /  \
       verification/    \validation
                  /      \
                 /        \
    spec-for-field-survey ↔ guidance-for-field-survey
              (this coupling edge)
```

## Connection to Foundation

This coupling builds on the foundational boundary complex:

- [[spec-for-field-survey]] verified against [[spec-for-spec]]
- [[spec-for-field-survey]] validated against [[guidance-for-spec]]
- [[guidance-for-field-survey]] verified against [[spec-for-guidance]]
- [[guidance-for-field-survey]] validated against [[guidance-for-guidance]]

## Bipartite Graph Structure

Field survey documents represent systems as bipartite graphs:

| Partition | Contains | Table Format |
|-----------|----------|--------------|
| Actors | Stakeholders (organizations, roles, user classes, external parties) | ID, Name, Type, Description, Accountability |
| Resources | System elements (technology, data, infrastructure, service, capital) | ID, Name, Type, Description, Status |
| Edges | Relationships (produces, consumes, maintains, depends on, governs) | Actor ID, Resource ID, Relationship Type, Description |

## Position in Documentation Workflow

Field surveys are prerequisites for architecture documents:

```
Field Survey → Architecture → Lifecycle → Program Plan → Program Memo
(what exists)   (what we build) (how we build) (execution)   (executive summary)
```

## Document References

| Role | Document | ID |
|------|----------|-----|
| Source | [[spec-for-field-survey]] | v:spec:field-survey |
| Target | [[guidance-for-field-survey]] | v:guidance:field-survey |

---

**Note:** This coupling enables field survey documents to be assured within the typed simplicial complex framework, supporting context-mapping before architecture work begins.
