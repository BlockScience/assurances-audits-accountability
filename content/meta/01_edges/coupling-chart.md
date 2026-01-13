---
type: edge/coupling
extends: edge
id: e:coupling:chart
name: Coupling - Spec-for-Charts and Guidance-for-Charts
source: v:spec:chart
target: v:guidance:chart
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-12-27T20:00:00Z
modified: 2025-12-27T20:00:00Z
---

# Coupling - Spec-for-Charts and Guidance-for-Charts

**This coupling connects the specification that defines all chart documents with the guidance that defines chart quality criteria.**

## Purpose

This coupling enables charts to be treated as full doc types with complete assurance capabilities. Together, these documents enable:

- **Verification:** Checking that a chart document has required fields, sections, and forms a valid simplicial complex (against [spec-for-charts](../00_vertices/spec-for-charts.md))
- **Validation:** Assessing whether a chart document is purposeful, coherent, well-scoped, and interpretable (against [guidance-for-charts](../00_vertices/guidance-for-charts.md))

## Governed Document Type

Both documents govern all chart documents in the knowledge complex, including:
- test-tetrahedron (test chart with deliberate hole)
- Future boundary complex charts
- All analytical and visualization charts

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are charts
- Verification edge: chart → spec-for-charts
- Validation edge: chart → guidance-for-charts
- Coupling edge: spec-for-charts ↔ guidance-for-charts (this edge)

Example: The test-tetrahedron chart can form an assurance face with this coupling as its base.

## Semantic Alignment

The structural requirements in spec-for-charts align with the quality criteria in guidance-for-charts:

| Spec-for-Charts Requires | Guidance-for-Charts Assesses |
|---------------------------|------------------------------|
| Purpose and scope fields | Purpose clarity |
| Construction metadata | Construction documentation quality |
| Element arrays (vertices, edges, faces) | Element coverage and coherence |
| Element tables with counts | Scope coherence |
| Chart properties section | Topological awareness |
| Verification section | Verifiability |
| Forms valid simplicial complex | Validity and completeness |
| Optional interpretation section | Interpretability |

Together, they provide comprehensive coverage of what makes a chart both **valid** (structurally sound simplicial complex) and **excellent** (purposeful and insightful).

## Extension of Doc Framework

This coupling demonstrates that the doc/spec/guidance framework extends beyond metadata documents to analytical artifacts like charts. By making charts extend doc, they gain:
- Full assurance capability (coupling, verification, validation, assurance faces)
- Programmatic structural verification
- Quality assessment framework
- Version control and accountability

## Trust Model

- **Verification** (deterministic): Chart has required structure and forms valid simplicial complex
- **Validation** (qualitative): Chart serves its purpose well and provides insights
- **Coupling** (alignment): Structure requirements support quality assessment
- **Assurance** (attestation): Human reviews triangle and attests chart is trustworthy

---

**Note:** This coupling was created to extend the assurance framework from boundary complex metadata to charts, enabling "charts as docs" and unlocking programmatic chart validation.
