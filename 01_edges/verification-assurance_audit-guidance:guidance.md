---
type: edge/verification
extends: edge
id: e:verification:assurance_audit-guidance:guidance
name: Verification - Guidance-for-Assurance-Audits verifies against Spec-for-Guidance
description: Structural verification that guidance-for-assurance-audits is a valid guidance document
source: v:guidance:assurance_audit
target: v:spec:guidance
source_type: vertex/guidance
target_type: vertex/spec
orientation: directed
verification_method: automated
verifier: verify_guidance.py
assurance_method: automated
assurer: guidance-verification-system
tags:
  - edge
  - verification
  - assurance
version: 1.0.0
created: 2025-12-27T17:00:00Z
modified: 2025-12-27T17:00:00Z
---

# Verification - Guidance-for-Assurance-Audits verifies against Spec-for-Guidance

This verification edge confirms that guidance-for-assurance-audits is a structurally valid guidance document according to spec-for-guidance requirements.

## Verification Relationship

**Source:** `v:guidance:assurance_audit` (Guidance for Assurance Audit Documents)
**Target:** `v:spec:guidance` (Specification for Guidance Documents)
**Relationship:** GAA verifies against SG (GAA is-a guidance document)

**Assurance Note:** This is part of the assurance DAG. GAA verifies against SG because GAA is fundamentally a guidance document, even though it *inherits* from guidance-for-charts in the domain hierarchy (tracked by a separate inherits edge).

## Verification Output

```
Verifying: 00_vertices/guidance-for-assurance-audits.md
Type: vertex/guidance

✓ Document type is vertex/guidance
✓ Has 'id' field
✓ Has 'name' field
✓ Has 'description' field
✓ Has 'extends' field set to 'vertex'
✓ Has 'type' field set to 'vertex/guidance'
✓ Has 'version' field
✓ Has 'created' timestamp
✓ Has 'modified' timestamp
✓ Has 'tags' list
✓ Has required section: Purpose
✓ Has required section: Document Overview
✓ Has required section: Quality Criteria (with ≥3 criteria)
✓ Has required section: Section-by-Section Guidance
✓ Proper markdown heading structure
✓ No broken internal references

Verification: PASS (15/15 checks passed)
```

## Verification Semantics

**What this proves:** GAA meets all structural requirements for being a guidance document

**What this does NOT prove:**
- That GAA properly extends guidance-for-charts (that's tracked by inheritance edge)
- That GAA is high quality (that's validation against GG)

## Significance

This verification is part of GAA's assurance triangle:
- **Verification (this edge):** GAA → SG (structural compliance as a guidance)
- **Validation:** GAA → GG (quality assessment)
- **Coupling:** SAA ↔ GAA (cross-domain alignment)

Together these three edges provide complete assurance for GAA.

## Accountability Statement

This verification was performed by automated tool `verify_guidance.py`. The tool checks structural compliance against spec-for-guidance requirements. Results are deterministic and reproducible.

**Verifier:** guidance-verification-system
**Method:** Automated structural checking
**Date:** 2025-12-27

---

**Version:** 1.0.0
**Status:** PASS
**Last Modified:** 2025-12-27
