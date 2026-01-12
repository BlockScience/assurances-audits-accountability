---
type: edge/verification
extends: edge
id: e:verification:incose-self-demonstration-guidance:spec-guidance
name: Verification - guidance-for-incose-self-demonstration against spec-for-guidance
source: v:guidance:incose-self-demonstration
target: v:spec:guidance
source_type: vertex/guidance
target_type: vertex/spec
orientation: directed
tags:
  - edge
  - verification
version: 1.0.0
created: 2025-12-30T23:55:00Z
modified: 2025-12-30T23:55:00Z
---

# Verification - guidance-for-incose-self-demonstration against spec-for-guidance

This verification edge confirms that guidance-for-incose-self-demonstration satisfies the structural requirements defined in spec-for-guidance.

## Verification Output

```
Verifying: 00_vertices/guidance-for-incose-self-demonstration.md
======================================================================
Result: ✓ PASS

Required Frontmatter Fields:
✓ type: vertex/guidance
✓ extends: vertex/guidance (inherits from guidance-for-incose-paper)
✓ id: v:guidance:incose-self-demonstration
✓ name: Guidance for INCOSE Self-Demonstrating Paper
✓ tags: [vertex, doc, guidance]
✓ version: 1.0.0

Required Body Sections:
✓ Purpose Statement - Present
✓ Quality Criteria - Present (7 extended criteria: SD1-SD7)
✓ Assessment Methodology - Present (scoring rubrics)
✓ Coupled Specification Reference - Present

Content Requirements per spec-for-guidance:
✓ Qualitative Language - Uses scoring rubrics and subjective assessment
✓ Quality Focus - Defines quality, not structure
✓ Human Judgment - Criteria require human evaluation
✓ Paired with Spec - References spec-for-incose-self-demonstration

All structural requirements satisfied.
```

## Verification Status

- **Status:** Pass
- **Date:** 2025-12-30T23:55:00Z
- **Tool:** verify_template_based.py + manual inspection

## Verification Notes

The guidance-for-incose-self-demonstration document extends guidance-for-incose-paper and fully conforms to spec-for-guidance requirements:

1. **Type System Compliance** - Correctly typed as `vertex/guidance`
2. **Inheritance** - Properly extends parent guidance with 7 additional criteria
3. **Section Coverage** - All required sections present
4. **Quality Focus** - Appropriately focuses on qualitative assessment
5. **Spec Coupling** - Correctly paired with spec-for-incose-self-demonstration

---

**Note:** This verification is part of the type-level assurance for the self-demonstration document type.