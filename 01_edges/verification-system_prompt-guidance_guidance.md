---
type: edge/verification
extends: edge
id: e:verification:system_prompt-guidance:guidance
name: Verification - Guidance-for-System-Prompt against Spec-for-Guidance
source: v:guidance:system_prompt
target: v:spec:guidance
source_type: vertex/guidance
target_type: vertex/spec
orientation: directed
tags:
  - edge
  - verification
version: 1.0.0
created: 2025-12-27T23:45:00Z
modified: 2025-12-27T23:45:00Z
---

# Verification - Guidance-for-System-Prompt against Spec-for-Guidance

**This verification edge confirms that the guidance for system prompt documents is itself a valid guidance document.**

## Verification Output

```text
Verifying: 00_vertices/guidance-for-system-prompt.md
======================================================================
======================================================================
Result: ✓ PASS
Checks: 7/7 passed
```

## Verification Status

- **Status:** PASS
- **Date:** 2025-12-27
- **Checks:** 7/7 passed
- **Errors:** 0
- **Tool:** verify_template_based.py

## What This Verifies

The guidance-for-system-prompt document satisfies all structural requirements defined in spec-for-guidance:

- ✓ Has required frontmatter fields (type, extends, id, name, version, created, modified, dependencies, tags)
- ✓ Follows correct type hierarchy (vertex/guidance extends doc)
- ✓ Has complete tag inheritance chain [vertex, doc, guidance]
- ✓ Has Purpose section
- ✓ Has Quality Criteria section (8 criteria for compositional guidance)
- ✓ Has Workflow Guidance section (with integration validation checklist)
- ✓ Includes Obsidian compatibility criterion
- ✓ Includes reference/referent clarity criterion
- ✓ Declares dependencies field (compositional guidance pattern)

## Role in Assurance

This verification edge is one side of the assurance triangle for guidance-for-system-prompt:

```
    v:guidance:system_prompt (the guidance being assured)
       /              \
      /                \
 verification      validation
    /                    \
   /                      \
v:spec:guidance ←→ v:guidance:guidance
      (coupling)
```

The assurance face confirms that guidance-for-system-prompt is both:
- **Structurally valid** (this verification)
- **High quality** (validation against guidance-for-guidance)

## PPP Framework Context

This verification ensures the system_prompt guidance itself follows guidance best practices, which enables:
- Confidence in the quality criteria defined for system prompt documents
- Clear assessment methodology for system prompt authors
- Consistent quality evaluation across system prompt documents
- Proper integration checking of compositional components

System prompts demonstrate the **compositional guidance pattern** with quality criteria for component integration.

---

**Verified:** 2025-12-27
