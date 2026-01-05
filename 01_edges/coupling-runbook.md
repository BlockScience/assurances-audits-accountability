---
type: edge/coupling
extends: edge
id: e:coupling:runbook
name: Coupling - Spec-for-Runbook and Guidance-for-Runbook
source: v:spec:runbook
target: v:guidance:runbook
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-01-04T16:00:00Z
modified: 2025-01-04T16:00:00Z
---

# Coupling - Spec-for-Runbook and Guidance-for-Runbook

**This coupling connects the specification for runbook documents with the guidance for runbook quality.**

## Purpose

This coupling links the structural requirements for runbook documents with their quality criteria, enabling complete assurance of human-activity guides. Together, these documents enable:

- **Verification:** Checking that a runbook has required sections, steps, and checkpoints (against [[spec-for-runbook]])
- **Validation:** Assessing whether a runbook effectively guides practitioners through workflows (against [[guidance-for-runbook]])

## Governed Document Type

Both documents govern all runbook documents in the knowledge complex. Runbooks serve as human-activity guides that walk practitioners through multi-step workflows:

- runbook-program-development (creating architecture, lifecycle, program plan, program memo)
- runbook-system-prompt-development (creating purpose, persona, protocol, system prompt)
- runbook-document-type-creation (creating spec, guidance, coupling, assurance)
- Any future runbooks for practitioner workflows

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are runbook documents (`type: vertex/doc` with `runbook` tag)
- Verification edge: runbook → spec-for-runbook
- Validation edge: runbook → guidance-for-runbook
- Coupling edge: spec-for-runbook ↔ guidance-for-runbook (this edge)

## Assurance Triangle Structure

```
                runbook-doc
                     /\
                    /  \
       verification/    \validation
                  /      \
                 /        \
    spec-for-runbook ↔ guidance-for-runbook
              (this coupling edge)
```

## Distinction from Lifecycle Documents

| Aspect | Lifecycle | Runbook |
|--------|-----------|---------|
| **Purpose** | How an engineering object gets built | How a human walks through a workflow |
| **Focus** | V&V gates for one artifact | Coordination across multiple artifacts |
| **Output** | One assured object | Multiple related artifacts |
| **Audience** | Engineering process definition | Practitioner guidance |

## Connection to Foundation

This coupling builds on the foundational boundary complex:

- [[spec-for-runbook]] verified against [[spec-for-spec]]
- [[spec-for-runbook]] validated against [[guidance-for-spec]]
- [[guidance-for-runbook]] verified against [[spec-for-guidance]]
- [[guidance-for-runbook]] validated against [[guidance-for-guidance]]

## Document References

| Role | Document | ID |
|------|----------|-----|
| Source | [[spec-for-runbook]] | v:spec:runbook |
| Target | [[guidance-for-runbook]] | v:guidance:runbook |

---

**Note:** This coupling enables runbook documents to be assured within the typed simplicial complex framework, supporting human-activity guidance for complex workflows.
