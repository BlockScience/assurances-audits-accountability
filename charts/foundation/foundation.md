---
type: chart/chart
extends: doc
id: c:foundation
name: Foundation Chart - Complete Genesis Complex
description: The foundation chart containing all genesis elements including ontology layer with full RBAC

constructed_by: genesis
construction_method: foundation
construction_date: 2026-01-13T00:00:00Z

purpose: Verify that the bundled foundation elements form a valid simplicial complex with full RBAC
scope: Complete foundation with boundary complex + ontology layer + RBAC

elements:
  vertices:
    # Boundary complex (5)
    - b0:root
    - v:spec:spec
    - v:spec:guidance
    - v:guidance:spec
    - v:guidance:guidance
    # Ontology layer (3)
    - v:spec:ontology
    - v:guidance:ontology
    - v:ontology:base
    # RBAC (2)
    - v:signer:admin
    - v:role:admin
  edges:
    # Coupling edges (3)
    - e:coupling:spec
    - e:coupling:guidance
    - e:coupling:ontology
    # Boundary edges (b1) (4)
    - b1:self-verification
    - b1:self-validation
    - b1:couples-GS-root
    - b1:couples-SG-root
    # Genesis verification/validation edges (6)
    - e:verification:spec-guidance:spec-spec
    - e:validation:spec-guidance:guidance-spec
    - e:verification:guidance-spec:spec-guidance
    - e:validation:guidance-spec:guidance-guidance
    - e:validation:spec-spec:guidance-spec
    - e:verification:guidance-guidance:spec-guidance
    # Ontology verification/validation edges (6)
    - e:verification:spec-ontology:spec-spec
    - e:validation:spec-ontology:guidance-spec
    - e:verification:guidance-ontology:spec-guidance
    - e:validation:guidance-ontology:guidance-guidance
    - e:verification:ontology-base:spec-ontology
    - e:validation:ontology-base:guidance-ontology
    # RBAC edges (10)
    - e:has-role:admin:admin
    - e:conveys:admin:guidance-spec
    - e:conveys:admin:guidance-guidance
    - e:conveys:admin:guidance-ontology
    - e:qualifies:admin:guidance-spec
    - e:qualifies:admin:guidance-guidance
    - e:qualifies:admin:guidance-ontology
    - e:signs:admin:spec-ontology
    - e:signs:admin:guidance-ontology
    - e:signs:admin:ontology-base
  faces:
    # Boundary faces (b2) (4)
    - b2:spec-spec
    - b2:guidance-guidance
    - b2:spec-guidance
    - b2:guidance-spec
    # Ontology assurance faces (3)
    - f:assurance:spec-ontology
    - f:assurance:guidance-ontology
    - f:assurance:ontology-base
    # Ontology signature faces (3)
    - f:signature:spec-ontology
    - f:signature:guidance-ontology
    - f:signature:ontology-base
    # Authorization faces (3)
    - f:authorization:admin:guidance-spec
    - f:authorization:admin:guidance-guidance
    - f:authorization:admin:guidance-ontology

tags:
  - chart
  - foundation
  - genesis
  - ontology
  - rbac
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Foundation Chart - Complete Genesis Complex

This chart contains the complete foundation complex - the genesis elements plus ontology layer with full RBAC that bootstrap a new knowledge complex.

## Purpose

Verify that the bundled foundation elements form a valid simplicial complex that passes all topological and ontological rules.

## Structure

### Vertices (10)

**Boundary Complex (5):**
- **b0:root** - Boundary anchor vertex
- **v:spec:spec** (SS) - Specification for specifications
- **v:spec:guidance** (SG) - Specification for guidance
- **v:guidance:spec** (GS) - Guidance for specifications
- **v:guidance:guidance** (GG) - Guidance for guidance

**Ontology Layer (3):**
- **v:spec:ontology** - Specification for ontology documents
- **v:guidance:ontology** - Guidance for ontology documents
- **v:ontology:base** - Base ontology for knowledge complexes

**RBAC (2):**
- **v:signer:admin** - Bootstrap administrator signer
- **v:role:admin** - Administrator role

### Edges (29)

**Coupling (3):**
- e:coupling:spec (SS ↔ GS)
- e:coupling:guidance (SG ↔ GG)
- e:coupling:ontology (spec:ontology ↔ guidance:ontology)

**Boundary b1 (4):**
- b1:self-verification (SS → root)
- b1:self-validation (GG → root)
- b1:couples-GS-root (root → GS)
- b1:couples-SG-root (root → SG)

**Genesis verification/validation (6):**
- e:verification:spec-guidance:spec-spec (SG → SS)
- e:validation:spec-guidance:guidance-spec (SG → GS)
- e:verification:guidance-spec:spec-guidance (GS → SG)
- e:validation:guidance-spec:guidance-guidance (GS → GG)
- e:validation:spec-spec:guidance-spec (SS → GS)
- e:verification:guidance-guidance:spec-guidance (GG → SG)

**Ontology verification/validation (6):**
- e:verification:spec-ontology:spec-spec (spec:ontology → SS)
- e:validation:spec-ontology:guidance-spec (spec:ontology → GS)
- e:verification:guidance-ontology:spec-guidance (guidance:ontology → SG)
- e:validation:guidance-ontology:guidance-guidance (guidance:ontology → GG)
- e:verification:ontology-base:spec-ontology (ontology:base → spec:ontology)
- e:validation:ontology-base:guidance-ontology (ontology:base → guidance:ontology)

**RBAC (10):**
- e:has-role:admin:admin (admin signer → admin role)
- e:conveys:admin:guidance-spec (admin role → GS)
- e:conveys:admin:guidance-guidance (admin role → GG)
- e:conveys:admin:guidance-ontology (admin role → guidance:ontology)
- e:qualifies:admin:guidance-spec (admin → GS)
- e:qualifies:admin:guidance-guidance (admin → GG)
- e:qualifies:admin:guidance-ontology (admin → guidance:ontology)
- e:signs:admin:spec-ontology (admin → spec:ontology)
- e:signs:admin:guidance-ontology (admin → guidance:ontology)
- e:signs:admin:ontology-base (admin → ontology:base)

### Faces (13)

**Boundary b2 (4)** - genesis exempt from signatures:
- b2:spec-spec - SS assured via root
- b2:guidance-guidance - GG assured via root
- b2:spec-guidance - SG assured (standard triangle)
- b2:guidance-spec - GS assured (standard triangle)

**Ontology Assurance (3):**
- f:assurance:spec-ontology
- f:assurance:guidance-ontology
- f:assurance:ontology-base

**Ontology Signature (3):**
- f:signature:spec-ontology
- f:signature:guidance-ontology
- f:signature:ontology-base

**Authorization (3):**
- f:authorization:admin:guidance-spec
- f:authorization:admin:guidance-guidance
- f:authorization:admin:guidance-ontology

## Topology

- V = 10 vertices
- E = 29 edges
- F = 13 faces
- χ = V - E + F = 10 - 29 + 13 = -6

## Verification

```bash
aaa check rules charts/foundation/foundation.md
```

## Notes

1. The b2 boundary faces are exempt from signature requirements (genesis bootstrap)
2. The ontology layer has full RBAC: assurance → signature → authorization
3. The admin signer is a placeholder replaced during `aaa init` with actual username
4. Authorization faces prove WHY admin is qualified via the role chain
