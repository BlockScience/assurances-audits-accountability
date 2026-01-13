---
type: edge/coupling
extends: edge
id: e:coupling:persona
name: Coupling - Spec-for-Persona and Guidance-for-Persona
source: v:spec:persona
target: v:guidance:persona
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

# Coupling - Spec-for-Persona and Guidance-for-Persona

**This coupling connects the specification for persona documents with the guidance for persona documents.**

## Purpose

This coupling enables complete assurance for persona documents by connecting structural requirements with quality criteria:

- **Verification:** Checking that a persona document has required sections and structure (against [spec-for-persona](../00_vertices/spec-for-persona.md))
- **Validation:** Assessing whether a persona document has appropriate expertise, clear approach, honest boundaries, and internal coherence (against [guidance-for-persona](../00_vertices/guidance-for-persona.md))

## Governed Document Type

Both documents govern **persona documents** - specifications of AI identity, expertise, approach, tone, and boundaries in the PPP (Persona-Purpose-Protocol) framework.

Persona documents define WHO the AI is.

## Role in PPP Framework

Persona is one of three components in the PPP framework:
- **Persona:** WHO the AI is (this coupling's domain)
- **Purpose:** WHAT the AI does
- **Protocol:** HOW the AI works

System prompts compose all three into complete AI model configurations.

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are persona documents
- Verification edge: persona → spec-for-persona
- Validation edge: persona → guidance-for-persona
- Coupling edge: spec-for-persona ↔ guidance-for-persona (this edge)

## Semantic Alignment

The structural requirements in spec-for-persona align with the quality criteria in guidance-for-persona:

| Spec-for-Persona Requires | Guidance-for-Persona Assesses |
|----------------------------|-------------------------------|
| Role and Identity section | Role Specificity |
| Domain Expertise (2-4 items) | Expertise Appropriateness |
| Approach and Methodology | Approach Clarity |
| Communication Tone | Tone Appropriateness |
| Boundaries and Limitations (≥3) | Boundary Honesty |
| All sections present | Internal Coherence |

Together, they ensure persona documents are both **structurally valid** and **high quality**.

## Usage Context

Persona documents should be created:
- AFTER purpose is defined (persona expertise must enable purpose objectives)
- BEFORE protocol is designed (protocol reflects persona approach)
- As part of complete system prompt using PPP framework

**Design Order:** Purpose → Persona → Protocol

---

**Version:** 1.0.0
**Created:** 2025-12-27
