# Use Case: Assurance Audit

This use case demonstrates a complete assurance audit trail for chart type specifications, showing how verification, validation, and assurance work together to ensure quality documentation.

## Overview

**Chart:** [chart-types-audit](../../../charts/chart-types-audit/)

**Purpose:** Demonstrate the complete assurance process for specifications using the verification → validation → assurance triangle pattern.

**What's Being Assured:**
- Specification for Charts (`spec-for-charts`)
- Specification for Assurance Audits (`spec-for-assurance-audits`)

## The Assurance Triangle Pattern

The core pattern for quality assurance in knowledge complexes:

```
         Spec (S)
        /    |    \
       /     |     \
  Verify  Validate  \
     /       |       \
    /        |        \
Guidance(G)--+--Root(B0)
             |
          Assure
```

Each document goes through three steps:
1. **Verification** (S → S): Automated structural checks against spec template
2. **Validation** (S → G): Human expert review against guidance
3. **Assurance** (Triangle S-G-B0): Attestation that both verification and validation passed

## Key Concepts

### Verification Edges

Automated tool-based checks that verify a document structurally conforms to its specification template.

**Example:** `verification-chart:spec.md`
- **Source:** `spec-for-charts` (the document being verified)
- **Target:** `spec-for-spec` (the specification it must conform to)
- **Tool:** `verify_template_based.py`
- **Result:** PASS (all required fields present, correct structure)

### Validation Edges

Human expert review that validates a document meets quality standards described in guidance.

**Example:** `validation-chart:guidance.md`
- **Source:** `spec-for-charts` (the document being validated)
- **Target:** `guidance-for-charts` (the quality standards)
- **Reviewer:** Human expert
- **Result:** APPROVED (clear, complete, actionable)

### Assurance Faces

Triangular faces that attest a document has passed both verification AND validation, creating a complete audit trail.

**Example:** `assurance-chart.md`
- **Vertices:** `spec-for-charts`, `guidance-for-charts`, `root`
- **Edges:** verification edge, validation edge, coupling edge
- **Meaning:** `spec-for-charts` is fully assured (verified + validated)

## Documentation

- **[Audit Trail Walkthrough](audit-trail.md)** - Complete step-by-step guide
- **[Triangle Pattern Explained](triangle-pattern.md)** - Deep dive into verification → validation → assurance
- **[Tooling Guide](tooling.md)** - How to use audit scripts

## Example Files

### Chart
- [charts/chart-types-audit/chart-types-audit.md](../../../charts/chart-types-audit/chart-types-audit.md) - Main chart document
- [charts/chart-types-audit/chart-types-audit-audit-trail.md](../../../charts/chart-types-audit/chart-types-audit-audit-trail.md) - Detailed audit trail
- [charts/chart-types-audit/chart-types-audit.html](../../../charts/chart-types-audit/chart-types-audit.html) - Interactive visualization

### Vertices (Documents Being Assured)
- [00_vertices/spec-for-charts.md](../../../00_vertices/spec-for-charts.md)
- [00_vertices/spec-for-assurance-audits.md](../../../00_vertices/spec-for-assurance-audits.md)
- [00_vertices/guidance-for-charts.md](../../../00_vertices/guidance-for-charts.md)
- [00_vertices/guidance-for-assurance-audits.md](../../../00_vertices/guidance-for-assurance-audits.md)

### Edges (Verification & Validation)
- [01_edges/verification-chart:spec.md](../../../01_edges/verification-chart:spec.md) - Verification edge
- [01_edges/validation-chart:guidance.md](../../../01_edges/validation-chart:guidance.md) - Validation edge

### Faces (Assurance)
- [02_faces/assurance-chart.md](../../../02_faces/assurance-chart.md) - Assurance face

## Running the Audit

### Verify All Documents
```bash
# Build cache and verify all documents
python scripts/build_cache.py

# Verify specific document against template
python scripts/verify_template_based.py 00_vertices/spec-for-charts.md --templates templates
```

### Run Assurance Audit
```bash
# Audit the chart-types-audit chart
python scripts/audit_assurance_chart.py charts/chart-types-audit/chart-types-audit.md
```

**Expected Output:**
```
Assurance Audit for Chart: chart-types-audit
==============================================

Vertices to Assure: 9
Assured Vertices: 9 (100%)

All vertices are assured!
Audit: PASS ✓
```

### Check Accountability
```bash
# Check accountability statements in edges
python scripts/check_accountability.py 01_edges/verification-chart:spec.md
python scripts/check_accountability.py 01_edges/validation-chart:guidance.md
```

## Topology

The chart-types-audit has these topological properties:

```
V = 9 vertices (specs + guidances + root)
E = 12 edges (verifications + validations + coupling + boundary)
F = 4 faces (assurance triangles)
χ = 1 (Euler characteristic)
```

This indicates a well-formed assurance complex with complete audit trails.

## Learning Path

For a hands-on learning experience, see:
- [Learning Module 02: Verification](../../learning/02-verification.md) - Verification, validation, assurance concepts
- [Learning Module 05: Use Cases](../../learning/05-use-cases.md) - Assurance audit walkthrough

## Related Concepts

- [Validation & Accountability](../../concepts/validation-accountability.md) - Governance theory
- [Charts vs Documents](../../concepts/charts-vs-documents.md) - Understanding charts

---

**Note:** This use case demonstrates the complete assurance infrastructure. Every spec and guidance document in the repository follows this pattern, creating a comprehensive audit trail for all documentation.
