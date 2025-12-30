# Document Development Tracker

**Purpose:** Track the development and assurance status of all documents required for the INCOSE IS 2026 paper submission.

**Last Updated:** 2025-12-30

---

## Document Types (Spec + Guidance Pairs)

These define the "types" of documents we can create. Each type requires a spec, guidance, and coupling edge, with assurance faces for both.

### Architecture Documents

| Element | File | Status |
|---------|------|:------:|
| Spec | `00_vertices/spec-for-architecture.md` | ✅ |
| Guidance | `00_vertices/guidance-for-architecture.md` | ✅ |
| Coupling | `01_edges/coupling-architecture.md` | ✅ |
| Spec Verification | `01_edges/verification-architecture-spec:spec-spec.md` | ✅ |
| Spec Validation | `01_edges/validation-architecture-spec:guidance-spec.md` | ✅ |
| Spec Assurance | `02_faces/assurance-architecture-spec.md` | ✅ |
| Guidance Verification | `01_edges/verification-architecture-guidance:spec-guidance.md` | ✅ |
| Guidance Validation | `01_edges/validation-architecture-guidance:guidance-guidance.md` | ✅ |
| Guidance Assurance | `02_faces/assurance-architecture-guidance.md` | ✅ |

**Type Status:** ✅ COMPLETE

---

### Lifecycle Documents

| Element | File | Status |
|---------|------|:------:|
| Spec | `00_vertices/spec-for-lifecycle.md` | ✅ |
| Guidance | `00_vertices/guidance-for-lifecycle.md` | ✅ |
| Coupling | `01_edges/coupling-lifecycle.md` | ✅ |
| Spec Verification | `01_edges/verification-lifecycle-spec:spec-spec.md` | ❌ |
| Spec Validation | `01_edges/validation-lifecycle-spec:guidance-spec.md` | ❌ |
| Spec Assurance | `02_faces/assurance-lifecycle-spec.md` | ❌ |
| Guidance Verification | `01_edges/verification-lifecycle-guidance:spec-guidance.md` | ❌ |
| Guidance Validation | `01_edges/validation-lifecycle-guidance:guidance-guidance.md` | ❌ |
| Guidance Assurance | `02_faces/assurance-lifecycle-guidance.md` | ❌ |

**Type Status:** ⚠️ NEEDS ASSURANCE INFRASTRUCTURE

---

### Literature Review Documents

| Element | File | Status |
|---------|------|:------:|
| Spec | `00_vertices/spec-for-incose-literature-review.md` | ✅ |
| Guidance | `00_vertices/guidance-for-incose-literature-review.md` | ✅ |
| Coupling | `01_edges/coupling-incose-literature-review.md` | ✅ |
| Spec Verification | `01_edges/verification-literature-review-spec:spec-spec.md` | ❌ |
| Spec Validation | `01_edges/validation-literature-review-spec:guidance-spec.md` | ❌ |
| Spec Assurance | `02_faces/assurance-literature-review-spec.md` | ❌ |
| Guidance Verification | `01_edges/verification-literature-review-guidance:spec-guidance.md` | ❌ |
| Guidance Validation | `01_edges/validation-literature-review-guidance:guidance-guidance.md` | ❌ |
| Guidance Assurance | `02_faces/assurance-literature-review-guidance.md` | ❌ |

**Type Status:** ⚠️ NEEDS ASSURANCE INFRASTRUCTURE

---

### Novel Contributions Documents

| Element | File | Status |
|---------|------|:------:|
| Spec | `00_vertices/spec-for-novel-contributions.md` | ✅ |
| Guidance | `00_vertices/guidance-for-novel-contributions.md` | ✅ |
| Coupling | `01_edges/coupling-novel-contributions.md` | ✅ |
| Spec Verification | `01_edges/verification-novel-contributions-spec:spec-spec.md` | ✅ |
| Spec Validation | `01_edges/validation-novel-contributions-spec:guidance-spec.md` | ⏳ |
| Spec Assurance | `02_faces/assurance-novel-contributions-spec.md` | ⏳ |
| Guidance Verification | `01_edges/verification-novel-contributions-guidance:spec-guidance.md` | ✅ |
| Guidance Validation | `01_edges/validation-novel-contributions-guidance:guidance-guidance.md` | ⏳ |
| Guidance Assurance | `02_faces/assurance-novel-contributions-guidance.md` | ⏳ |

**Type Status:** ⏳ AWAITING HUMAN APPROVAL

---

### INCOSE Paper Documents (Target Type)

| Element | File | Status |
|---------|------|:------:|
| Spec | `00_vertices/spec-for-incose-paper.md` | ✅ |
| Guidance | `00_vertices/guidance-for-incose-paper.md` | ✅ |
| Coupling | `01_edges/coupling-incose-paper.md` | ✅ |
| Spec Verification | `01_edges/verification-incose-paper-spec:spec-spec.md` | ✅ |
| Spec Validation | `01_edges/validation-incose-paper-spec:guidance-spec.md` | ✅ |
| Spec Assurance | `02_faces/assurance-incose-paper-spec.md` | ✅ |
| Guidance Verification | `01_edges/verification-incose-paper-guidance:spec-guidance.md` | ✅ |
| Guidance Validation | `01_edges/validation-incose-paper-guidance:guidance-guidance.md` | ✅ |
| Guidance Assurance | `02_faces/assurance-incose-paper-guidance.md` | ✅ |

**Type Status:** ✅ COMPLETE

---

## Content Documents (Instances)

These are the actual content documents that will be used to compose the final INCOSE paper.

### Architecture Document Instance

| Element | File | Status |
|---------|------|:------:|
| Content | `00_vertices/doc-architecture-incose-paper.md` | ✅ |
| Verification | `01_edges/verification-architecture-incose:spec-architecture.md` | ✅ |
| Validation | `01_edges/validation-architecture-incose:guidance-architecture.md` | ✅ |
| Assurance | `02_faces/assurance-architecture-incose.md` | ✅ |
| Copied to .claude | `.claude/doc-architecture-incose-paper.md` | ✅ |

**Instance Status:** ✅ ASSURED & STAGED

---

### Lifecycle Document Instance

| Element | File | Status |
|---------|------|:------:|
| Content | `00_vertices/doc-lifecycle-incose-paper.md` | ✅ |
| Verification | `01_edges/verification-lifecycle-incose:spec-lifecycle.md` | ❌ |
| Validation | `01_edges/validation-lifecycle-incose:guidance-lifecycle.md` | ❌ |
| Assurance | `02_faces/assurance-lifecycle-incose.md` | ❌ |
| Copied to .claude | `.claude/doc-lifecycle-incose-paper.md` | ❌ |

**Instance Status:** ⚠️ NEEDS ASSURANCE

---

### Literature Review Document Instance

| Element | File | Status |
|---------|------|:------:|
| Content | `00_vertices/doc-literature-review-incose-paper.md` | ✅ |
| Verification | `01_edges/verification-literature-review-incose:spec-literature-review.md` | ❌ |
| Validation | `01_edges/validation-literature-review-incose:guidance-literature-review.md` | ❌ |
| Assurance | `02_faces/assurance-literature-review-incose.md` | ❌ |
| Copied to .claude | `.claude/doc-literature-review-incose-paper.md` | ❌ |

**Instance Status:** ⚠️ NEEDS ASSURANCE

---

### Novel Contributions Document Instance

| Element | File | Status |
|---------|------|:------:|
| Content | `00_vertices/doc-novel-contributions-incose-paper.md` | ❌ |
| Verification | `01_edges/verification-novel-contributions-incose:spec-novel-contributions.md` | ❌ |
| Validation | `01_edges/validation-novel-contributions-incose:guidance-novel-contributions.md` | ❌ |
| Assurance | `02_faces/assurance-novel-contributions-incose.md` | ❌ |
| Copied to .claude | `.claude/doc-novel-contributions-incose-paper.md` | ❌ |

**Instance Status:** ❌ NOT STARTED (type awaiting approval)

---

### INCOSE Paper Document Instance (Final Output)

| Element | File | Status |
|---------|------|:------:|
| Content | `00_vertices/doc-incose-paper-2026.md` | ✅ (draft) |
| Verification | `01_edges/verification-incose-paper-content:spec-incose-paper.md` | ❌ |
| Validation | `01_edges/validation-incose-paper-content:guidance-incose-paper.md` | ❌ |
| Assurance | `02_faces/assurance-incose-paper-content.md` | ✅ (old) |
| Copied to .claude | `.claude/doc-incose-paper-2026.md` | ❌ |

**Instance Status:** ⚠️ DRAFT EXISTS - WILL BE REWRITTEN FROM ASSURED INPUTS

---

## Summary Dashboard

### Document Types

| Type | Spec | Guidance | Coupling | Spec Assured | Guidance Assured | Overall |
|------|:----:|:--------:|:--------:|:------------:|:----------------:|:-------:|
| Architecture | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Lifecycle | ✅ | ✅ | ✅ | ❌ | ❌ | ⚠️ |
| Literature Review | ✅ | ✅ | ✅ | ❌ | ❌ | ⚠️ |
| Novel Contributions | ✅ | ✅ | ✅ | ⏳ | ⏳ | ⏳ |
| INCOSE Paper | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### Content Documents

| Document | Exists | Verified | Validated | Assured | In .claude |
|----------|:------:|:--------:|:---------:|:-------:|:----------:|
| Architecture | ✅ | ✅ | ✅ | ✅ | ✅ |
| Lifecycle | ✅ | ❌ | ❌ | ❌ | ❌ |
| Literature Review | ✅ | ❌ | ❌ | ❌ | ❌ |
| Novel Contributions | ❌ | ❌ | ❌ | ❌ | ❌ |
| INCOSE Paper (final) | ✅ | ❌ | ❌ | ❌ | ❌ |

### Legend

- ✅ = Complete/Approved
- ⏳ = Awaiting human approval
- ⚠️ = Partially complete / needs work
- ❌ = Not yet created

---

## Execution Plan

### Phase 1: Complete Document Type Assurance

- [ ] **Lifecycle Type:** Create verification/validation edges and assurance faces for spec and guidance
- [ ] **Literature Review Type:** Create verification/validation edges and assurance faces for spec and guidance
- [ ] **Novel Contributions Type:** Obtain human approval for pending validations and assurance faces

### Phase 2: Create and Assure Content Documents

- [ ] **Lifecycle Instance:** Create verification/validation edges and assurance face
- [ ] **Literature Review Instance:** Create verification/validation edges and assurance face
- [ ] **Novel Contributions Instance:** Create content document from `.claude/NOVEL-CONTRIBUTIONS.md`, then assure

### Phase 3: Stage Assured Documents

- [ ] Copy `doc-lifecycle-incose-paper.md` to `.claude/`
- [ ] Copy `doc-literature-review-incose-paper.md` to `.claude/`
- [ ] Copy `doc-novel-contributions-incose-paper.md` to `.claude/`

### Phase 4: Compose Final Paper

- [ ] Rewrite `doc-incose-paper-2026.md` using assured content documents as inputs
- [ ] Verify against `spec-for-incose-paper`
- [ ] Validate against `guidance-for-incose-paper`
- [ ] Close assurance face
- [ ] Copy to `.claude/` as canonical reference

### Phase 5: Post-Processing

- [ ] Create submission version (strip YAML, anonymize)
- [ ] Convert to PDF
- [ ] Final review and submission

---

## Human Approvals Required

The following items are awaiting mzargham's review and sign-off:

1. `01_edges/validation-novel-contributions-spec:guidance-spec.md`
2. `01_edges/validation-novel-contributions-guidance:guidance-guidance.md`
3. `02_faces/assurance-novel-contributions-spec.md`
4. `02_faces/assurance-novel-contributions-guidance.md`

---

## Notes

- **Architecture:** Fully assured and staged in `.claude/` - ready to use
- **INCOSE Paper Type:** Fully assured - ready to verify/validate final paper
- **Lifecycle & Literature Review:** Content exists but types need assurance infrastructure before instances can be assured
- **Novel Contributions:** Type infrastructure complete but awaiting approval; content document not yet created

---

*This tracker should be updated as work progresses.*