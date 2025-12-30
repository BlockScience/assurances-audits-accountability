---
type: edge/dependency
extends: edge
id: e:dependency:system_prompt-guidance:purpose-guidance
name: Dependency - Guidance for System Prompts uses Guidance for Purposes
description: System prompt guidances reference purpose quality criteria in compositional assessment
source: v:guidance:system_prompt
target: v:guidance:purpose
source_type: vertex/guidance
target_type: vertex/guidance
orientation: directed
dependency_type: typed_subsection
subsection_field: purpose
required: true
version: 1.0.0
created: 2025-12-27T23:00:00Z
modified: 2025-12-27T23:00:00Z
tags:
  - edge
  - dependency
  - typed-subsection
---

# Dependency - Guidance for System Prompts uses Guidance for Purposes

This dependency edge tracks that system_prompt guidances reference purpose guidances for quality assessment of the purpose subsection within system prompts.

## Dependency Relationship

**Dependent:** `v:guidance:system_prompt` (Guidance for System Prompt Documents)
**Dependency:** `v:guidance:purpose` (Guidance for Purpose Documents)
**Relationship:** system_prompt guidance uses purpose guidance (compositional quality criteria)

**Direction:** System prompt guidance depends on purpose guidance (system_prompt-guidance → purpose-guidance)

**Usage:** When assessing system prompt quality, the purpose subsection must be evaluated using purpose guidance quality criteria.

**Assurance Note:** This dependency tracks compositional quality assessment and is **separate from the assurance DAG**. For assurance purposes, both system_prompt guidance and purpose guidance validate against v:guidance:guidance.

## Dependency Usage

### Quality Assessment Usage

System prompt guidances check purpose subsection quality using purpose guidance criteria:
- Does purpose satisfy [[guidance-for-purpose]] quality criteria?
- Are objectives clear and measurable (purpose guidance criterion)?
- Are success criteria specific (purpose guidance criterion)?
- Are constraints realistic (purpose guidance criterion)?

### Requirements

- **Required:** Yes - purpose subsections must meet purpose quality standards
- **Cardinality:** One purpose guidance dependency
- **Conformance:** Purpose subsections assessed using v:guidance:purpose criteria
- **Parallel to spec dependency:** Mirrors `e:dependency:system_prompt:purpose`

## Compositional Justification

### Why Compositional Quality Assessment

System prompt quality depends on component quality. To assess whether a system prompt's purpose subsection is excellent, we apply purpose guidance criteria.

**Pattern:** When compositional documents (system_prompt) have typed subsections (purpose), quality assessment for those subsections uses the subsection type's guidance (purpose guidance).

### Relationship to Assurance

**Separate Validation Paths:**

```
Compositional dependency:
  v:guidance:system_prompt --depends-on--> v:guidance:purpose

Assurance for system_prompt guidance:
  v:guidance:system_prompt --validates--> v:guidance:guidance

Assurance for purpose guidance:
  v:guidance:purpose --validates--> v:guidance:guidance
```

---

**Version:** 1.0.0
**Type:** Dependency Edge
**Last Modified:** 2025-12-27
