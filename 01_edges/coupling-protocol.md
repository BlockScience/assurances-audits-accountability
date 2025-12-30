---
type: edge/coupling
extends: edge
id: e:coupling:protocol
name: Coupling - Spec-for-Protocol and Guidance-for-Protocol
source: v:spec:protocol
target: v:guidance:protocol
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-12-27T23:30:00Z
modified: 2025-12-27T23:30:00Z
---

# Coupling - Spec-for-Protocol and Guidance-for-Protocol

**This coupling connects the specification for protocol documents with the guidance for protocol documents.**

## Purpose

This coupling enables complete assurance for protocol documents by connecting structural requirements with quality criteria:

- **Verification:** Checking that a protocol document has required sections and structure (against [spec-for-protocol](../00_vertices/spec-for-protocol.md))
- **Validation:** Assessing whether a protocol document has clear workflow, comprehensive guidelines, robust error handling, and appropriate quality standards (against [guidance-for-protocol](../00_vertices/guidance-for-protocol.md))

## Governed Document Type

Both documents govern **protocol documents** - specifications of AI operational workflow, behavioral guidelines, error handling, and quality standards in the PPP (Persona-Purpose-Protocol) framework.

Protocol documents define HOW the AI works.

## Role in PPP Framework

Protocol is one of three components in the PPP framework:
- **Persona:** WHO the AI is
- **Purpose:** WHAT the AI does
- **Protocol:** HOW the AI works (this coupling's domain)

System prompts compose all three into complete AI model configurations.

**Critical:** Protocol should be designed LAST in the PPP framework, as it operationalizes purpose objectives through persona approach.

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are protocol documents
- Verification edge: protocol → spec-for-protocol
- Validation edge: protocol → guidance-for-protocol
- Coupling edge: spec-for-protocol ↔ guidance-for-protocol (this edge)

## Semantic Alignment

The structural requirements in spec-for-protocol align with the quality criteria in guidance-for-protocol:

| Spec-for-Protocol Requires | Guidance-for-Protocol Assesses |
|----------------------------|-------------------------------|
| Operational Workflow | Workflow Clarity |
| Behavioral Guidelines (≥3) | Guideline Comprehensiveness |
| Error Handling | Error Handling Robustness |
| Quality Standards | Quality Standard Appropriateness |
| All sections present | Internal Coherence |

Together, they ensure protocol documents are both **structurally valid** and **high quality**.

## Usage Context

Protocol documents should be created:
- LAST in the PPP design sequence (after purpose and persona)
- To operationalize purpose objectives through persona approach
- As part of complete system prompt using PPP framework

**Design Order:** Purpose → Persona → Protocol

---

**Version:** 1.0.0
**Created:** 2025-12-27
