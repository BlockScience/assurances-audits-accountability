---
type: edge/coupling
extends: edge
id: e:coupling:assurance_audit
name: Coupling - Assurance Audit Spec and Guidance Cross-Domain Alignment
description: Ensures spec-for-assurance-audits and guidance-for-assurance-audits are mutually consistent
source: v:spec:assurance_audit
target: v:guidance:assurance_audit
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-12-27T20:50:00Z
modified: 2025-12-27T20:50:00Z
---

# Coupling - Assurance Audit Spec and Guidance Cross-Domain Alignment

This coupling edge establishes that spec-for-assurance-audits and guidance-for-assurance-audits are mutually consistent and aligned in their treatment of assurance audit documents.

## Coupling Relationship

**Source:** `v:spec:assurance_audit` (Specification for Assurance Audit Documents)
**Target:** `v:guidance:assurance_audit` (Guidance for Assurance Audit Documents)
**Relationship:** spec-for-assurance-audits COUPLES_WITH guidance-for-assurance-audits (cross-domain consistency)

## Cross-Domain Alignment

### Structural-Quality Consistency ✅

The spec and guidance align on what constitutes a valid assurance audit:

- ✅ Spec defines required structural elements (inherits from chart + audit-specific)
- ✅ Guidance defines quality criteria for audits
- ✅ No contradictions between spec and guidance
- ✅ Quality criteria map to structural requirements

### Coverage Alignment ✅

Both documents cover the same domain:

- ✅ Audit targets (spec: required field, guidance: scope selection)
- ✅ Assurance requirements (spec: all_vertices_assured, guidance: coverage strategies)
- ✅ Audit trails (spec: required section, guidance: documentation standards)
- ✅ Root anchoring (spec: hard requirement, guidance: verification methodology)

### Terminology Consistency ✅

Shared terminology ensures coherence:

- ✅ Both use same audit terms (targets, coverage, trace, anchoring)
- ✅ Definitions align across documents
- ✅ Status values consistent (PASS/FAIL/PARTIAL)
- ✅ Cross-references work correctly

## Coherence Assessment

**Coupling Strength:** Strong

**Rationale:** The spec and guidance are tightly aligned on assurance audit requirements. The spec defines what makes an audit structurally valid (all targets assured, traces to root), while the guidance defines what makes it excellent (appropriate scope, systematic coverage, clear documentation). Together they provide complete coverage of audit quality.

## Examples of Alignment

### Example 1: Audit Targets

**Spec says:** `audit_targets` field specifies which vertices must be assured
**Guidance says:** Choose audit targets that form coherent scope, avoid cherry-picking, document rationale

**Alignment:** ✅ Spec provides mechanism, guidance provides methodology

### Example 2: Root Anchoring

**Spec says:** All assurance must trace to boundary complex (hard requirement #2)
**Guidance says:** Verify trace networks reach b2 faces, document boundary faces in trace, confirm root connection

**Alignment:** ✅ Spec enforces requirement, guidance explains how to verify

### Example 3: Coverage Metrics

**Spec says:** `audit_coverage` field shows percentage of targets assured
**Guidance says:** 100% coverage required for PASS, partial coverage requires gap analysis and remediation plan

**Alignment:** ✅ Spec quantifies coverage, guidance interprets meaning

## Notes

This coupling is essential for the assurance triangle that assures assurance_audit documents. The spec-guidance alignment ensures that audit quality is both structurally enforced and meaningfully assessed.

---

**Version:** 1.0.0
**Status:** Coupled
**Strength:** Strong
**Last Modified:** 2025-12-27
