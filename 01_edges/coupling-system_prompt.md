---
type: edge/coupling
extends: edge
id: e:coupling:system_prompt
name: Coupling - Spec-for-System-Prompt and Guidance-for-System-Prompt
source: v:spec:system_prompt
target: v:guidance:system_prompt
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

# Coupling - Spec-for-System-Prompt and Guidance-for-System-Prompt

**This coupling connects the specification for system prompt documents with the guidance for system prompt documents.**

## Purpose

This coupling enables complete assurance for system prompt documents by connecting structural requirements with quality criteria:

- **Verification:** Checking that a system prompt document has required sections, typed subsections, and compositional structure (against [spec-for-system-prompt](../00_vertices/spec-for-system-prompt.md))
- **Validation:** Assessing whether a system prompt document has excellent individual components AND seamless integration (against [guidance-for-system-prompt](../00_vertices/guidance-for-system-prompt.md))

## Governed Document Type

Both documents govern **system prompt documents** - compositional documents that integrate persona, purpose, and protocol into complete AI model configurations using the PPP (Persona-Purpose-Protocol) framework.

System prompts define complete AI model configurations (WHO + WHAT + HOW).

## Role in PPP Framework

System prompt is the **compositional container** in the PPP framework:
- Contains **Persona subsection** (WHO the AI is) - must conform to `v:spec:persona`
- Contains **Purpose subsection** (WHAT the AI does) - must conform to `v:spec:purpose`
- Contains **Protocol subsection** (HOW the AI works) - must conform to `v:spec:protocol`

System prompts demonstrate the **typed subsection pattern** - subsections with defined type constraints, analogous to JSON-LD context.

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are system prompt documents
- Verification edge: system_prompt → spec-for-system-prompt
- Validation edge: system_prompt → guidance-for-system-prompt
- Coupling edge: spec-for-system-prompt ↔ guidance-for-system-prompt (this edge)

## Semantic Alignment

The structural requirements in spec-for-system-prompt align with the quality criteria in guidance-for-system-prompt:

| Spec-for-System-Prompt Requires | Guidance-for-System-Prompt Assesses |
|---------------------------------|-------------------------------------|
| Persona subsection (conforms to persona spec) | Component Verification (persona passes individual checks) |
| Purpose subsection (conforms to purpose spec) | Component Verification (purpose passes individual checks) |
| Protocol subsection (conforms to protocol spec) | Component Verification (protocol passes individual checks) |
| Dependencies field declares subsections | Persona-Purpose Alignment |
| All three subsections present | Purpose-Protocol Alignment |
| - | Persona-Protocol Consistency |
| - | Tone Consistency |
| - | No Contradictions |
| - | Integration Validation |

Together, they ensure system prompt documents are both **structurally valid** (typed subsections conform) and **high quality** (components align and integrate).

## Compositional Pattern

System prompts exemplify compositional documents where:
- Structure is defined by composition (HAS typed subsections)
- NOT by inheritance (IS NOT a persona/purpose/protocol)
- Dependencies are explicit (declared in frontmatter)
- Subsections have type constraints (like schema typing)

This pattern enables modular, reusable components with mechanical verification.

## Usage Context

System prompt documents should be created:
- When defining complete AI model configurations
- By composing pre-designed persona, purpose, and protocol components
- Following PPP design order: Purpose → Persona → Protocol → Integration
- With explicit validation that components align and work together

---

**Version:** 1.0.0
**Created:** 2025-12-27
