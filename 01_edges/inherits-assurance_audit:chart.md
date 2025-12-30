---
type: edge/inherits
extends: edge
id: e:inherits:assurance_audit:chart
name: Inherits - Assurance Audit extends Chart
description: Spec-for-assurance-audits inherits structure from spec-for-charts (domain specialization)
source: v:spec:assurance_audit
target: v:spec:chart
source_type: vertex/spec
target_type: vertex/spec
orientation: directed
inheritance_type: domain_specialization
inherited_fields:
  - elements (vertices, edges, faces)
  - topology (euler_characteristic, dimension)
  - constructed_by
  - construction_method
  - purpose
  - scope
added_fields:
  - audit_targets
  - audit_date
  - auditor
  - audit_status
  - audit_coverage
  - assurance_requirements
version: 1.0.0
created: 2025-12-27T17:00:00Z
modified: 2025-12-27T17:00:00Z
tags:
  - edge
  - inherits
  - domain-specialization
---

# Inherits - Assurance Audit extends Chart

This inheritance edge tracks that spec-for-assurance-audits extends spec-for-charts through domain specialization. Assurance audits ARE charts with additional requirements.

## Inheritance Relationship

**Child:** `v:spec:assurance_audit` (Specification for Assurance Audit Documents)
**Parent:** `v:spec:chart` (Specification for Chart Documents)
**Relationship:** assurance_audit extends chart (domain specialization)

**Direction:** SAA inherits FROM SC (SC is parent, SAA is child)

**Assurance Note:** This inheritance edge tracks domain specialization and is **separate from the assurance DAG**. For assurance purposes, SAA verifies against v:spec:spec (because SAA is fundamentally a spec document), not against v:spec:chart.

## Inherited Structure

### Fields Inherited from Spec-for-Charts

Assurance audit specs inherit all chart fields:

- **elements**: Lists of vertices, edges, faces comprising the chart
- **topology**: Euler characteristic (χ = V - E + F), dimension
- **constructed_by**: Who constructed the chart
- **construction_method**: How it was constructed (manual, assisted, automated)
- **purpose**: Why this chart exists
- **scope**: What the chart covers

### Fields Added by Spec-for-Assurance-Audits

Assurance audit specs add audit-specific fields:

- **audit_targets**: Which vertices must be assured for PASS status
- **audit_date**: When the audit was performed
- **auditor**: Who performed the audit
- **audit_status**: PASS/FAIL/PARTIAL
- **audit_coverage**: Percentage of targets assured
- **assurance_requirements**: Detailed requirements (all_vertices_assured, minimum_assurance_level, etc.)

## Semantic Justification

### Why This Inheritance Makes Sense

**Domain Perspective:** Assurance audits ARE charts. They use the same graph structure (vertices, edges, faces), same topology concepts (Euler characteristic), and same construction metadata.

**Specialization:** The audit-specific fields (audit_targets, audit_status, etc.) extend the base chart concept without contradicting it. Every assurance_audit is a valid chart with extra semantics.

**Use Case:** When tools need to process assurance audits, they can use all chart-processing logic plus audit-specific validation logic.

### Relationship to Assurance

**THIS IS NOT AN ASSURANCE EDGE.**

The assurance relationships are:
- SAA **verifies** against SS (structural compliance as a spec)
- SAA **validates** against GAA (quality assessment)
- SAA **couples** with GAA (cross-domain alignment)

The inheritance edge explains why SAA has certain fields (inherited from SC), but doesn't affect whether SAA is properly assured.

## Notes

This inheritance forms part of a hierarchy:
```
v:spec:spec (SS - root spec type)
  ↑ inherits
v:spec:chart (SC - charts)
  ↑ inherits
v:spec:assurance_audit (SAA - audit charts)
```

Each level adds domain-specific requirements while maintaining compatibility with parent types.

---

**Version:** 1.0.0
**Type:** Inherits Edge
**Last Modified:** 2025-12-27
