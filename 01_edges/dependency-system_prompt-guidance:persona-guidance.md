---
type: edge/dependency
extends: edge
id: e:dependency:system_prompt-guidance:persona-guidance
name: Dependency - Guidance for System Prompts uses Guidance for Personas
description: System prompt guidances reference persona quality criteria in compositional assessment
source: v:guidance:system_prompt
target: v:guidance:persona
source_type: vertex/guidance
target_type: vertex/guidance
orientation: directed
dependency_type: typed_subsection
subsection_field: persona
required: true
version: 1.0.0
created: 2025-12-27T23:00:00Z
modified: 2025-12-27T23:00:00Z
tags:
  - edge
  - dependency
  - typed-subsection
---

# Dependency - Guidance for System Prompts uses Guidance for Personas

This dependency edge tracks that system_prompt guidances reference persona guidances for quality assessment of the persona subsection within system prompts.

## Dependency Relationship

**Dependent:** `v:guidance:system_prompt` (Guidance for System Prompt Documents)
**Dependency:** `v:guidance:persona` (Guidance for Persona Documents)
**Relationship:** system_prompt guidance uses persona guidance (compositional quality criteria)

**Direction:** System prompt guidance depends on persona guidance (system_prompt-guidance → persona-guidance)

**Usage:** When assessing system prompt quality, the persona subsection must be evaluated using persona guidance quality criteria.

**Assurance Note:** This dependency tracks compositional quality assessment and is **separate from the assurance DAG**. For assurance purposes, both system_prompt guidance and persona guidance validate against v:guidance:guidance.

## Dependency Usage

### Quality Assessment Usage

System prompt guidances check persona subsection quality using persona guidance criteria:
- Does persona satisfy [[guidance-for-persona]] quality criteria?
- Are expertise areas appropriate (persona guidance criterion)?
- Is role specific and credible (persona guidance criterion)?
- Are boundaries honest (persona guidance criterion)?

### Requirements

- **Required:** Yes - persona subsections must meet persona quality standards
- **Cardinality:** One persona guidance dependency
- **Conformance:** Persona subsections assessed using v:guidance:persona criteria
- **Parallel to spec dependency:** Mirrors `e:dependency:system_prompt:persona`

## Compositional Justification

### Why Compositional Quality Assessment

System prompt quality depends on component quality. To assess whether a system prompt's persona subsection is excellent, we apply persona guidance criteria.

**Pattern:** When compositional documents (system_prompt) have typed subsections (persona), quality assessment for those subsections uses the subsection type's guidance (persona guidance).

### Relationship to Assurance

**Separate Validation Paths:**

```
Compositional dependency:
  v:guidance:system_prompt --depends-on--> v:guidance:persona

Assurance for system_prompt guidance:
  v:guidance:system_prompt --validates--> v:guidance:guidance

Assurance for persona guidance:
  v:guidance:persona --validates--> v:guidance:guidance
```

---

**Version:** 1.0.0
**Type:** Dependency Edge
**Last Modified:** 2025-12-27
