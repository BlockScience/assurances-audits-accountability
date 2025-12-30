# The Assurance Triangle Pattern

This document provides a deep dive into the verification → validation → assurance triangle pattern, the core governance mechanism for knowledge complexes.

## The Pattern

Every assured document forms a triangle connecting three vertices:

```
         Document (D)
        /            \
       /              \
  Verification    Validation
     /                  \
    /                    \
Guidance (G)----Coupling----Root (B0)
```

**Three Vertices:**
1. **Document (D):** The artifact being assured (spec, guidance, chart, etc.)
2. **Guidance (G):** The quality standards the document should meet
3. **Root (B0):** The boundary anchor providing trust foundation

**Three Edges:**
1. **Verification (D → Template):** Automated structural check
2. **Validation (D → G):** Human expert review
3. **Coupling (G ↔ B0):** Links guidance to trust root

**One Face:**
The assurance face (triangle) that attests both verification and validation passed.

## Why This Pattern?

### Separation of Concerns

**Verification** checks **structure** (automated):
- Are all required fields present?
- Is the YAML frontmatter valid?
- Do references resolve correctly?
- Does it conform to the template?

**Validation** checks **quality** (human):
- Is the content clear and understandable?
- Are the requirements actionable?
- Are examples helpful?
- Does it serve its purpose?

**Assurance** combines both:
- Structure is correct (verified)
- Quality is acceptable (validated)
- Therefore, the document is assured

### Accountability

Each edge has different accountability:

**Verification Edge:**
- Created by: Automated tool
- Reviewed by: Human (ensures tool ran correctly)
- Authority: Tool correctness + human oversight
- Can be regenerated: Yes (deterministic)

**Validation Edge:**
- Created by: Human expert
- Reviewed by: Same human (they sign off)
- Authority: Expert's domain knowledge
- Can be regenerated: No (requires expert judgment)

**Assurance Face:**
- Created by: Automated or human
- Reviewed by: Human (final sign-off)
- Authority: Combination of verification + validation
- Can be regenerated: Only if both edges exist

### Traceability

The triangle pattern creates a complete audit trail:

1. **Document exists:** We have the artifact
2. **Verification edge exists:** We know structure was checked
3. **Validation edge exists:** We know quality was reviewed
4. **Assurance face exists:** We know both checks passed
5. **Traces to root:** We know the trust chain is intact

If any element is missing, the audit fails.

## Pattern Variants

### Standard Assurance (Spec → Spec Template)

**Example:** Assuring `spec-for-charts`

```
   spec-for-charts
      /         \
     /           \
  verify      validate
   /               \
  /                 \
spec-for-spec   guidance-for-charts
    |                 |
    +-------root-------+
```

- **Document:** `spec-for-charts`
- **Template:** `spec-for-spec` (verification target)
- **Guidance:** `guidance-for-charts` (validation target)
- **Result:** `spec-for-charts` is assured

### Self-Referential Assurance (Foundational Docs)

**Example:** Assuring `spec-for-spec` (the root specification)

```
   spec-for-spec
      /       \
     /         \
  verify    validate
   /             \
  /               \
root      guidance-for-spec
 |               |
 +-------root----+
```

- **Document:** `spec-for-spec`
- **Template:** `root` (boundary anchor, axiomatic)
- **Guidance:** `guidance-for-spec`
- **Result:** `spec-for-spec` is assured (self-bootstrapping)

**Special Case:** The foundational specifications (spec-for-spec, guidance-for-guidance) verify against the root boundary because they define their own templates. This creates a self-bootstrapping foundation.

### Extended Assurance (Inheriting Specs)

**Example:** Assuring `spec-for-assurance-audits`

```
   spec-for-assurance-audits
      /                    \
     /                      \
  verify                 validate
   /                          \
  /                            \
spec-for-charts    guidance-for-assurance-audits
    |                          |
    |                          |
    +-----------root-----------+
```

- **Document:** `spec-for-assurance-audits`
- **Template:** `spec-for-charts` (inherits from chart spec)
- **Guidance:** `guidance-for-assurance-audits`
- **Result:** `spec-for-assurance-audits` is assured

**Note:** Verification can target a parent spec when a document extends another spec type.

## Topological Properties

The assurance triangle has specific topological properties:

### Closure Property

For a triangle to exist, all its boundary edges must exist:
- Verification edge must exist
- Validation edge must exist
- Coupling edge must exist

If any edge is missing, the triangle cannot be created (incomplete assurance).

### Euler Characteristic Contribution

Each assurance triangle contributes to the chart's Euler characteristic:
- V: +3 vertices (document, guidance, root)
- E: +3 edges (verification, validation, coupling)
- F: +1 face (assurance triangle)
- Contribution to χ: +3 - 3 + 1 = +1

Multiple assurance triangles create a simplicial complex with richer topology.

### Orientation

Assurance faces are **oriented** (not unoriented):
- The triangle has a specific direction (counterclockwise by convention)
- Verification and validation edges are **directed** (have source → target)
- Coupling edges are **undirected** (bidirectional relationship)

This orientation encodes the dependency structure.

## Practical Workflow

### Creating an Assurance Triangle

**Step 1:** Create the document (vertex)
```bash
# Create spec-for-foo.md
vim 00_vertices/spec-for-foo.md
```

**Step 2:** Run verification (create edge)
```bash
# Verify structure
python scripts/verify_template_based.py 00_vertices/spec-for-foo.md --templates templates

# Document result in verification edge
vim 01_edges/verification-foo:spec.md
```

**Step 3:** Perform validation (create edge)
```bash
# Human reviews against guidance-for-spec
# Reviewer creates validation edge documenting their review
vim 01_edges/validation-foo:spec.md
```

**Step 4:** Create assurance face (complete triangle)
```bash
# Create assurance face referencing both edges
vim 02_faces/assurance-foo.md
```

**Step 5:** Audit the result
```bash
# Add to chart and audit
python scripts/audit_assurance_chart.py charts/my-chart/my-chart.md
```

### Updating an Assured Document

When a document changes, the assurance must be refreshed:

1. **Modify document:** Make changes to the spec/guidance/etc.
2. **Re-verify:** Run verification tool again, update verification edge
3. **Re-validate:** Human re-reviews, updates validation edge (or confirms still valid)
4. **Update assurance:** Update assurance face timestamps and attestation
5. **Re-audit:** Confirm audit still passes

**Key Principle:** Assurance is temporal - it attests quality at a specific time. Changes invalidate assurance until re-checked.

## Common Patterns

### Batch Assurance

For multiple related documents, create assurance triangles in sequence:

```bash
for doc in spec-for-*.md; do
    # Verify
    python scripts/verify_template_based.py "00_vertices/$doc" --templates templates

    # Create edges (verification + validation)
    # (requires human intervention for validation)

    # Create assurance face
    # (can be automated if both edges exist)
done
```

### Progressive Assurance

Build assurance incrementally:
1. Start with foundational docs (spec-for-spec, guidance-for-guidance)
2. Assure templates next (spec-for-charts, etc.)
3. Assure domain docs using assured templates
4. Assure complex docs that depend on multiple assured docs

This creates a dependency tree of assured documents.

### Assurance Audit Trail

The complete audit trail shows the assurance history:

```
spec-for-foo.md
├─ v1.0.0 (2025-12-27)
│  ├─ Verification: PASS (2025-12-27 14:00)
│  ├─ Validation: APPROVED by Chief Engineer (2025-12-27 15:00)
│  └─ Assurance: ASSURED (2025-12-27 15:30)
├─ v1.1.0 (2025-12-28)
│  ├─ Verification: PASS (2025-12-28 10:00)
│  ├─ Validation: APPROVED by Chief Engineer (2025-12-28 11:00)
│  └─ Assurance: ASSURED (2025-12-28 11:30)
```

This is tracked through:
- Document version and modified timestamp
- Edge creation/modified timestamps
- Assurance face modified timestamp

## Anti-Patterns

### ❌ Verification Without Validation

**Problem:** A document passes automated checks but is never human-reviewed.

**Result:** The document may be structurally correct but unclear, incomplete, or wrong.

**Solution:** Require both verification AND validation for assurance.

### ❌ Validation Without Verification

**Problem:** A human reviews a document but it was never structurally verified.

**Result:** The document may have quality content but invalid structure.

**Solution:** Require both verification AND validation for assurance.

### ❌ Assurance Without Edges

**Problem:** Creating an assurance face without creating verification and validation edges.

**Result:** The assurance is unsupported - we don't know what checks were performed.

**Solution:** Always create edges before creating the assurance face.

### ❌ Stale Assurance

**Problem:** A document is modified but the assurance face is not updated.

**Result:** The assurance attests to an old version, not the current state.

**Solution:** Check timestamps - if document modified > assurance modified, assurance is stale.

## Advanced Topics

### Conditional Assurance

Some documents may require additional checks beyond verification and validation:
- Security review (for authentication specs)
- Performance testing (for algorithm specs)
- Legal review (for privacy specs)

These create **extended triangles** with additional edges.

### Partial Assurance

In some cases, partial assurance may be acceptable:
- Verification passed, validation pending
- Validation approved, verification being re-run

The assurance audit will flag these as incomplete but may allow them temporarily.

### Assurance Inheritance

When a document extends another, its assurance may partially inherit:
- If parent is assured, child may need less validation
- But child still requires its own verification (different structure)

This creates assurance hierarchies.

## Summary

The assurance triangle pattern provides:
- **Automated checking** (verification) for correctness
- **Human oversight** (validation) for quality
- **Combined attestation** (assurance) for confidence
- **Complete traceability** (audit trail) for accountability

Every assured document in the knowledge complex follows this pattern, creating a comprehensive quality assurance system.

## Related Documentation

- [Audit Trail Walkthrough](audit-trail.md) - Step-by-step example
- [Tooling Guide](tooling.md) - How to use audit scripts
- [Validation & Accountability](../../concepts/validation-accountability.md) - Governance theory

---

**Design Principle:** The triangle pattern separates mechanical correctness (verification) from semantic quality (validation), combining both for complete assurance. This reflects the reality that neither automated tools nor human review alone is sufficient for confidence.
