# Audit Trail for c:chart-types-audit

**Status:** PASS
**Coverage:** 100.0% (3/3 vertices)

## Vertex Assurance Results

### ✅ b0:root

**Root Anchored:** Yes
**Issues:**
- Root vertex - provides assurance, not assured itself

### ✅ c:assurance_audit:boundary-complex

**Assurance Faces:** f:assurance:boundary-complex-assurance-audit
**Root Anchored:** Yes
**Boundary Faces in Trace:** b2:guidance-guidance, b2:spec-spec
**Trace Length:** 7 faces
**Trace:** b2:guidance-guidance → b2:spec-spec → f:assurance:assurance_audit → f:assurance:assurance_audit-guidance → f:assurance:boundary-complex-assurance-audit → f:assurance:guidance-spec → f:assurance:spec-guidance

### ✅ v:guidance:assurance_audit

**Assurance Faces:** f:assurance:assurance_audit-guidance
**Root Anchored:** Yes
**Boundary Faces in Trace:** b2:guidance-guidance, b2:spec-spec
**Trace Length:** 5 faces
**Trace:** b2:guidance-guidance → b2:spec-spec → f:assurance:assurance_audit-guidance → f:assurance:guidance-spec → f:assurance:spec-guidance

### ✅ v:guidance:chart

**Assurance Faces:** f:assurance:chart-guidance
**Root Anchored:** Yes
**Boundary Faces in Trace:** b2:guidance-guidance, b2:spec-spec
**Trace Length:** 5 faces
**Trace:** b2:guidance-guidance → b2:spec-spec → f:assurance:chart-guidance → f:assurance:guidance-spec → f:assurance:spec-guidance

### ✅ v:guidance:guidance

**Assurance Faces:** b2:guidance-guidance
**Root Anchored:** Yes
**Boundary Faces in Trace:** b2:guidance-guidance, b2:spec-spec
**Trace Length:** 4 faces
**Trace:** b2:guidance-guidance → b2:spec-spec → f:assurance:guidance-spec → f:assurance:spec-guidance

### ✅ v:guidance:spec

**Assurance Faces:** f:assurance:guidance-spec
**Root Anchored:** Yes
**Boundary Faces in Trace:** b2:guidance-guidance, b2:spec-spec
**Trace Length:** 4 faces
**Trace:** b2:guidance-guidance → b2:spec-spec → f:assurance:guidance-spec → f:assurance:spec-guidance

### ✅ v:spec:assurance_audit

**Assurance Faces:** f:assurance:assurance_audit
**Root Anchored:** Yes
**Boundary Faces in Trace:** b2:guidance-guidance, b2:spec-spec
**Trace Length:** 6 faces
**Trace:** b2:guidance-guidance → b2:spec-spec → f:assurance:assurance_audit → f:assurance:assurance_audit-guidance → f:assurance:guidance-spec → f:assurance:spec-guidance

### ✅ v:spec:chart

**Assurance Faces:** f:assurance:chart
**Root Anchored:** Yes
**Boundary Faces in Trace:** b2:guidance-guidance, b2:spec-spec
**Trace Length:** 5 faces
**Trace:** b2:guidance-guidance → b2:spec-spec → f:assurance:chart → f:assurance:guidance-spec → f:assurance:spec-guidance

### ✅ v:spec:guidance

**Assurance Faces:** f:assurance:spec-guidance
**Root Anchored:** Yes
**Boundary Faces in Trace:** b2:guidance-guidance, b2:spec-spec
**Trace Length:** 4 faces
**Trace:** b2:guidance-guidance → b2:spec-spec → f:assurance:guidance-spec → f:assurance:spec-guidance

### ✅ v:spec:spec

**Assurance Faces:** b2:spec-spec
**Root Anchored:** Yes
**Boundary Faces in Trace:** b2:guidance-guidance, b2:spec-spec
**Trace Length:** 4 faces
**Trace:** b2:guidance-guidance → b2:spec-spec → f:assurance:guidance-spec → f:assurance:spec-guidance
