---
type: edge/coupling
extends: edge
id: e:coupling:purpose
name: Coupling - Spec-for-Purpose and Guidance-for-Purpose
source: v:spec:purpose
target: v:guidance:purpose
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

# Coupling - Spec-for-Purpose and Guidance-for-Purpose

**This coupling connects the specification for purpose documents with the guidance for purpose documents.**

## Purpose

This coupling enables complete assurance for purpose documents by connecting structural requirements with quality criteria:

- **Verification:** Checking that a purpose document has required sections and structure (against [spec-for-purpose](../00_vertices/spec-for-purpose.md))
- **Validation:** Assessing whether a purpose document has measurable objectives, specific success criteria, realistic constraints, and clear outputs (against [guidance-for-purpose](../00_vertices/guidance-for-purpose.md))

## Governed Document Type

Both documents govern **purpose documents** - specifications of AI objectives, success criteria, constraints, and expected outputs in the PPP (Persona-Purpose-Protocol) framework.

Purpose documents define WHAT the AI does.

## Role in PPP Framework

Purpose is one of three components in the PPP framework:
- **Persona:** WHO the AI is
- **Purpose:** WHAT the AI does (this coupling's domain)
- **Protocol:** HOW the AI works

System prompts compose all three into complete AI model configurations.

**Critical:** Purpose should be designed FIRST in the PPP framework, as it drives both persona (what expertise is needed) and protocol (how to achieve objectives).

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are purpose documents
- Verification edge: purpose → spec-for-purpose
- Validation edge: purpose → guidance-for-purpose
- Coupling edge: spec-for-purpose ↔ guidance-for-purpose (this edge)

## Semantic Alignment

The structural requirements in spec-for-purpose align with the quality criteria in guidance-for-purpose:

| Spec-for-Purpose Requires | Guidance-for-Purpose Assesses |
|----------------------------|-------------------------------|
| Core Objectives (3-5) | Objective Measurability |
| Success Criteria (≥3) | Criteria Specificity |
| Constraints and Boundaries (≥3) | Constraint Realism |
| Expected Outputs | Output Clarity |
| All sections present | Internal Coherence |

Together, they ensure purpose documents are both **structurally valid** and **high quality**.

## Usage Context

Purpose documents should be created:
- FIRST in the PPP design sequence (before persona and protocol)
- When defining what problem the AI solves and what success looks like
- As part of complete system prompt using PPP framework

**Design Order:** Purpose → Persona → Protocol

---

**Version:** 1.0.0
**Created:** 2025-12-27
