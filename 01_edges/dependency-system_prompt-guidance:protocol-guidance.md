---
type: edge/dependency
extends: edge
id: e:dependency:system_prompt-guidance:protocol-guidance
name: Dependency - Guidance for System Prompts uses Guidance for Protocols
description: System prompt guidances reference protocol quality criteria in compositional assessment
source: v:guidance:system_prompt
target: v:guidance:protocol
source_type: vertex/guidance
target_type: vertex/guidance
orientation: directed
dependency_type: typed_subsection
subsection_field: protocol
required: true
version: 1.0.0
created: 2025-12-27T23:00:00Z
modified: 2025-12-27T23:00:00Z
tags:
  - edge
  - dependency
  - typed-subsection
---

# Dependency - Guidance for System Prompts uses Guidance for Protocols

This dependency edge tracks that system_prompt guidances reference protocol guidances for quality assessment of the protocol subsection within system prompts.

## Dependency Relationship

**Dependent:** `v:guidance:system_prompt` (Guidance for System Prompt Documents)
**Dependency:** `v:guidance:protocol` (Guidance for Protocol Documents)
**Relationship:** system_prompt guidance uses protocol guidance (compositional quality criteria)

**Direction:** System prompt guidance depends on protocol guidance (system_prompt-guidance → protocol-guidance)

**Usage:** When assessing system prompt quality, the protocol subsection must be evaluated using protocol guidance quality criteria.

**Assurance Note:** This dependency tracks compositional quality assessment and is **separate from the assurance DAG**. For assurance purposes, both system_prompt guidance and protocol guidance validate against v:guidance:guidance.

## Dependency Usage

### Quality Assessment Usage

System prompt guidances check protocol subsection quality using protocol guidance criteria:
- Does protocol satisfy [[guidance-for-protocol]] quality criteria?
- Is workflow clear and sequential (protocol guidance criterion)?
- Are behavioral guidelines comprehensive (protocol guidance criterion)?
- Is error handling well-defined (protocol guidance criterion)?

### Requirements

- **Required:** Yes - protocol subsections must meet protocol quality standards
- **Cardinality:** One protocol guidance dependency
- **Conformance:** Protocol subsections assessed using v:guidance:protocol criteria
- **Parallel to spec dependency:** Mirrors `e:dependency:system_prompt:protocol`

## Compositional Justification

### Why Compositional Quality Assessment

System prompt quality depends on component quality. To assess whether a system prompt's protocol subsection is excellent, we apply protocol guidance criteria.

**Pattern:** When compositional documents (system_prompt) have typed subsections (protocol), quality assessment for those subsections uses the subsection type's guidance (protocol guidance).

### Relationship to Assurance

**Separate Validation Paths:**

```
Compositional dependency:
  v:guidance:system_prompt --depends-on--> v:guidance:protocol

Assurance for system_prompt guidance:
  v:guidance:system_prompt --validates--> v:guidance:guidance

Assurance for protocol guidance:
  v:guidance:protocol --validates--> v:guidance:guidance
```

---

**Version:** 1.0.0
**Type:** Dependency Edge
**Last Modified:** 2025-12-27
