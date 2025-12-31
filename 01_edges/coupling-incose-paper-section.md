---
type: edge/coupling
extends: edge
id: e:coupling:incose-paper-section
name: Coupling - INCOSE Paper Section Spec and Guidance
source: v:spec:incose-paper-section
target: v:guidance:incose-paper-section
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-12-31T18:00:00Z
modified: 2025-12-31T18:00:00Z
description: Connects specification defining INCOSE paper section structural requirements with guidance defining section quality criteria
---

# Coupling - INCOSE Paper Section Spec and Guidance

This coupling connects the specification that defines structural requirements for INCOSE symposium paper sections with the guidance that defines quality criteria for those sections.

## Purpose

Together, [spec-for-incose-paper-section](../00_vertices/spec-for-incose-paper-section.md) and [guidance-for-incose-paper-section](../00_vertices/guidance-for-incose-paper-section.md) enable complete assurance of paper sections:

- **Verification:** Checking that a section has required structural elements, proper heading hierarchy, appropriate length, and correct formatting (against spec)
- **Validation:** Assessing whether a section is clear, coherent, contributes visibly, is accessible to practitioners, demonstrates rigor, and engages readers (against guidance)

## Governed Document Type

Both documents govern sections within INCOSE symposium research papers, including:

- Abstract
- Introduction
- Background
- Body sections (Framework/Architecture layers, Methods, etc.)
- Self-Demonstration / Case Study
- Conclusions
- Recommendations
- Acknowledgements

## Relationship Between Spec and Guidance

The spec and guidance are complementary but distinct:

| Aspect | Spec Addresses | Guidance Addresses |
|--------|---------------|-------------------|
| **Heading levels** | Maximum 3 levels, no skipping | Appropriate use of hierarchy for narrative flow |
| **Word count** | Target ±20% range | Proportionality to importance, avoiding bloat |
| **Figure references** | Must cite before appearance | Effective use of visuals to support understanding |
| **Citations** | Format and placement rules | Appropriate attribution and connection to prior art |
| **Section structure** | Required subsections and elements | Logical flow and coherence within section |
| **Transitions** | Presence of transitional elements | Quality and smoothness of narrative bridges |

## Role in Paper Assurance

This coupling enables the assurance pattern for paper sections:

```
       paper_section
           /      \
          /        \
  verification   validation
        /            \
       /              \
   spec-for-     guidance-for-
   incose-       incose-
   paper-        paper-
   section       section
      \            /
       \          /
        coupling
```

When a paper section is:
1. **Verified** against the spec (structural compliance)
2. **Validated** against the guidance (quality assessment)
3. The **coupling** ensures both aspects address the same document type

Then an **assurance face** can close, providing confidence that the section is both structurally compliant and fit for purpose.

## Application to INCOSE Paper Development

This coupling supports systematic paper development:

1. **Planning:** Use spec to outline required sections and structural elements
2. **Drafting:** Use guidance quality criteria to assess section fitness while writing
3. **Verification:** Run automated checks against spec requirements
4. **Validation:** Human assessment against guidance criteria (clarity, coherence, etc.)
5. **Assurance:** Complete face closes when both verification and validation pass

## Strictness Alignment

- **Spec strictness:** `strict` - structural requirements are non-negotiable for INCOSE compliance
- **Guidance rubric:** `validation-assessment` - quality criteria support human judgment, not binary pass/fail

This alignment ensures:
- Automated verification catches formatting and structural issues
- Human validation focuses on qualitative aspects machines cannot assess
- Both work together for complete quality assurance

## Self-Demonstration

This coupling itself demonstrates the framework:
- The spec and guidance were created using the PPP framework
- Both passed verification against their respective templates
- This coupling edge follows the coupling template
- The entire set can be assured through the framework it describes

---

**Note:** This coupling is part of the assurance infrastructure for the INCOSE IS 2026 paper on document assurance using typed simplicial complexes. It enables systematic verification and validation of each paper section before integration into the final submission.
