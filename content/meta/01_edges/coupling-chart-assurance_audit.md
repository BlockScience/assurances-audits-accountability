---
type: edge/coupling
extends: edge
id: e:coupling:chart-assurance_audit
name: Coupling - Spec-for-Charts and Guidance-for-Assurance-Audits
description: Alignment between chart specification and assurance audit guidance
source: v:spec:chart
target: v:guidance:assurance_audit
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-12-27T23:25:00Z
modified: 2025-12-27T23:25:00Z
---

# Coupling - Spec-for-Charts and Guidance-for-Assurance-Audits

This coupling edge establishes alignment between the specification for chart documents and the guidance for assurance audit documents.

## Coupling Relationship

**Connects:** `v:spec:chart` ↔ `v:guidance:assurance_audit`

**Type:** Cross-domain coupling (spec for one type, guidance for specialized type)

**Orientation:** Undirected (mutual alignment)

## Alignment Points

### 1. Required Sections Alignment ✅

**Spec-for-Charts requires:**
- Chart construction metadata
- Chart purpose
- Elements lists (vertices, edges, faces)
- Element tables
- Chart properties
- Verification section

**Guidance-for-Assurance-Audits recommends:**
- All standard chart sections PLUS
- Assurance Audit Results section
- Vertex Assurance Status table
- Face Validation table
- Coverage Analysis
- Compliance Assessment

**Alignment:** Guidance builds on spec requirements, adding audit-specific sections ✅

### 2. Metadata Fields Alignment ✅

**Spec-for-Charts requires:**
- `constructed_by`, `construction_method`, `construction_date`
- `purpose`, `scope`
- `elements` (vertices, edges, faces)

**Guidance-for-Assurance-Audits expects:**
- All chart metadata PLUS
- `audit_date`, `auditor`, `audit_status`, `audit_coverage`
- `assurance_requirements`

**Alignment:** Guidance-recommended fields extend but don't contradict spec requirements ✅

### 3. Status Definitions Alignment ✅

**Spec-for-Charts:**
- Doesn't define status enums (charts can have various purposes)

**Guidance-for-Assurance-Audits:**
- Defines PASS/FAIL/PARTIAL for audit-specific use
- Tied to coverage percentage
- Clear criteria for each status

**Alignment:** Guidance adds domain-specific status that charts don't need ✅

### 4. Validation Approach Alignment ✅

**Spec-for-Charts:**
- Provides structural validation (required fields, sections)
- General topology validation (valid simplicial complex)

**Guidance-for-Assurance-Audits:**
- Adds assurance-specific validation (vertex coverage, face validity)
- Builds on structural validation
- Adds semantic validation (assurance completeness)

**Alignment:** Guidance extends, not replaces, chart validation ✅

### 5. Extension Pattern Alignment ✅

**Spec-for-Charts:**
- Supports extension via inheritance (`extends: chart`)
- Allows additional fields
- Enables specialized chart types

**Guidance-for-Assurance-Audits:**
- Recommends extending chart for specialized types
- Provides assurance_audit as example
- Documents extension best practices

**Alignment:** Guidance demonstrates the extension pattern defined in spec ✅

## Mutual Support

### Spec Enables Guidance

The spec-for-charts:
- Defines extensible base structure
- Allows additional metadata fields
- Supports specialized validation
- Enables type hierarchy

This **enables** the guidance to recommend specialized audit charts.

### Guidance Respects Spec

The guidance-for-assurance-audits:
- Builds on chart requirements (doesn't violate them)
- Adds requirements only for audit-specific needs
- Maintains chart structure
- Follows extension pattern

This **respects** the constraints defined in spec.

## Coupling Strength

**Status:** ✅ **Strongly Coupled**

**Evidence:**
1. Guidance explicitly references spec requirements
2. Audit metadata extends (not replaces) chart metadata
3. Validation approach is additive
4. Examples follow spec structure
5. Extension pattern matches spec design

## Impact on Assurance

This coupling edge is critical for:

**f:assurance:assurance_audit** face:
- Validates that spec-for-assurance-audits follows spec-for-charts (verification edge)
- Validates that spec-for-assurance-audits aligns with guidance-for-assurance-audits (validation edge)
- **This coupling edge** ensures spec and guidance are aligned

Without this coupling, the assurance triangle would be invalid.

## Related Elements

- **Source:** v:spec:chart - Base chart specification
- **Target:** v:guidance:assurance_audit - Specialized audit guidance
- **Enables:** f:assurance:assurance_audit - Assurance face for audit spec
- **Pattern:** Cross-domain coupling (spec/guidance for different but related types)

---

**Note:** This is a cross-domain coupling edge connecting the specification for one type (chart) with guidance for a specialized type (assurance_audit). This pattern supports type hierarchies where specialized types extend base types while maintaining alignment between specification and guidance domains.
