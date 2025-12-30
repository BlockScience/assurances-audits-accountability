---
type: edge/signs
extends: edge
id: e:signs:mzargham:incose-paper-2026
name: Signs - mzargham attests to INCOSE Paper 2026
description: Attestation event where mzargham signs the INCOSE paper
source: v:signer:mzargham
target: v:doc:incose-paper-2026
source_type: vertex/signer
target_type: vertex/doc
orientation: directed
signing_date: 2025-12-30T23:00:00Z
commit_hash: f66b6747acfe6d10ca7c878cb98ad332338aa06f
qualifies_edge: e:qualifies:mzargham:guidance-incose-paper
tags:
  - edge
  - signs
version: 1.0.0
created: 2025-12-30T23:00:00Z
modified: 2025-12-30T23:00:00Z
---

# Signs - mzargham attests to INCOSE Paper 2026

This signs edge records the attestation event where [[signer-mzargham]] formally attests to [[doc-incose-paper-2026]].

## Signing Event

**Signer:** [[signer-mzargham]]
**Document:** [[doc-incose-paper-2026]]
**Date:** 2025-12-30T23:00:00Z
**Commit:** f66b6747acfe6d10ca7c878cb98ad332338aa06f

This signing event records mzargham's formal attestation to the INCOSE IS 2026 paper submission "Test-Driven Document Development: Simplicial Complexes for Verification, Validation, and Assurance with Human Accountability."

## Qualification at Signing

**Qualifies Edge:** [[qualifies-mzargham:guidance-incose-paper]]
**Credential Type:** expertise
**Valid At:** 2025-12-30 (no expiry)

At the time of signing, mzargham held a valid qualifies edge to guidance-for-incose-paper, establishing the expertise necessary to attest to the paper's quality.

## Attestation Statement

I, Michael Zargham (mzargham), attest to the INCOSE Paper 2026 on 2025-12-30.

This attestation confirms that:
- The paper passes validation against guidance-for-incose-paper
- The quality criteria have been met
- I take responsibility for the paper's fitness-for-purpose

This attestation is recorded in commit f66b6747acfe6d10ca7c878cb98ad332338aa06f and can be verified through GitHub's commit signature verification.

**Signed:** mzargham
**Date:** 2025-12-30T23:00:00Z

## Context

This is the primary signature for the INCOSE paper, establishing human accountability for the base assurance triangle. A separate signs edge exists for the self-demonstration triangle.

---

**Note:** This signs edge, combined with the qualifies edge and validation edge, forms the base signature face for the INCOSE paper.