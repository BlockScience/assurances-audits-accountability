# Specs vs Templates: Verification Architecture Analysis

**Date**: 2025-12-28
**Question**: Do we verify documents against specs or templates? What's the reference/referent distinction?

## Current State Analysis

### What We Have

**Two Verification Approaches:**

1. **`verify_template_based.py`** - Template-driven verification
   - Uses templates in `templates/` directory as authority
   - Parses template structure to extract requirements
   - Verifies documents match template structure
   - **Currently used**: Verification edges cite this tool

2. **`verify_spec.py`** - Spec-based verification (HARDCODED)
   - Has hardcoded logic for spec documents
   - Uses spec-for-spec as conceptual authority
   - Does NOT actually parse spec-for-spec dynamically
   - **Status**: Appears unused in verification edges

### What Verification Edges Actually Do

Looking at [01_edges/verification-persona:spec.md](../01_edges/verification-persona:spec.md):

```yaml
## Verification Status
- **Status:** PASS
- **Date:** 2025-12-27
- **Checks:** 7/7 passed
- **Tool:** verify_template_based.py
```

**Verification edges verify against TEMPLATES, not specs.**

---

## The Reference/Referent Distinction

### Current Architecture (As Implemented)

```
spec-for-persona.md ──────────────────┐
  (prescriptive text)                 │
  "A persona MUST have..."            │ (human reads and creates)
                                      ▼
                            templates/00_vertices/persona.md
                              (structured reference)
                              "name: <Persona Name>"
                                      │
                                      │ (verify_template_based.py parses)
                                      ▼
                            TemplateRequirement objects
                              (executable checks)
                                      │
                                      │ (tool applies to)
                                      ▼
                            00_vertices/persona-claude.md
                              (document instance)
```

**The Template IS the Referent** (structured authority that tools can parse)
**The Spec IS the Reference** (human-readable explanation of requirements)

### The Problem You've Identified

For **edges and faces**, we have:

```
templates/01_edges/verification.md
  (structured reference - what tools parse)

??? NO SPEC ???
  (missing human-readable explanation)
```

For **vertices**, we have both:

```
00_vertices/spec-for-persona.md        templates/00_vertices/persona.md
  (human-readable reference)  +  (machine-parseable referent)
```

---

## Your Insight: "Specs for Payloads, Not Containers"

You said:
> "we write specs for the documents which are the payloads of the higher order objects for the objects themselves"

Let me unpack this:

### Payload vs Container

**Payload documents** (what goes in the vertices):
- Personas, purposes, protocols (PPP content)
- System prompts (compositional content)
- Specs, guidance (meta content)

**Container documents** (the topology itself):
- Verification edges (structure: source, target, verification output)
- Assurance faces (structure: 3 vertices, 3 edges, triangle coherence)
- Charts (structure: element arrays, metadata)

### Current Approach

**For payloads** - We have both spec AND template:
- `spec-for-persona.md` explains requirements (reference)
- `templates/00_vertices/persona.md` implements requirements (referent)
- Tool verifies against template (uses referent)

**For containers** - We have only template:
- `templates/01_edges/verification.md` defines structure (referent)
- ❌ No `spec-for-verification.md` (missing reference)
- Tool verifies against template (uses referent)

### Your Question

Should we create `spec-for-verification.md`, `spec-for-assurance.md` etc?

---

## Analysis: Two Possible Architectures

### Architecture A: Specs for Everything (Including Containers)

**Create specs for edges/faces:**
- `spec-for-verification-edge.md` - explains what verification edges are
- `spec-for-assurance-face.md` - explains assurance triangles
- `spec-for-chart.md` - ✅ Already exists!

**Advantage:**
- Complete reference documentation for all document types
- Clear human-readable explanation of every construct
- Consistent: everything has a spec

**Disadvantage:**
- Circular dependency: spec-for-verification would need verification edges
- Self-reference paradox: who verifies the verifiers?
- Complexity: adds 7+ new specs for meta-constructs

**Chart is the exception**: `spec-for-charts.md` exists because charts are:
- User-facing artifacts (not just meta-constructs)
- Complex enough to need explanation
- Don't create circular dependencies (charts document relationships, don't define them)

### Architecture B: Specs for Payloads Only (Current + Clarification)

**Specs exist for:**
- ✅ Payload document types (persona, purpose, protocol, system_prompt)
- ✅ Meta-document types (spec, guidance)
- ✅ Charts (user-facing artifacts)

**Templates ARE the spec for:**
- ❌ Edges (verification, validation, coupling, dependency, inherits)
- ❌ Faces (assurance, doc-kit)

**Advantage:**
- Avoids circular dependencies
- Simpler: 6 fewer specs to maintain
- Clear distinction: payloads get specs, topology gets templates
- Pragmatic: templates are detailed enough for meta-constructs

**Disadvantage:**
- Inconsistent: some types have specs, others don't
- Templates must be VERY clear and well-documented
- Risk: templates might not explain "why" sufficiently

---

## Recommendation: Hybrid Architecture (B+)

**Architecture B+ = Architecture B + Enhanced Template Documentation**

### Principle

**Specs for payloads, enhanced templates for containers:**

1. **Payload Documents** → Full spec + template
   - Persona, Purpose, Protocol, System_Prompt
   - Spec, Guidance
   - Why: These are what users create, need full explanation

2. **Charts** → Full spec + template
   - Why: User-facing artifacts, complex, don't create circular deps

3. **Edges & Faces** → Enhanced template only
   - Why: Meta-constructs, templates can serve dual role

### What "Enhanced Template" Means

Templates for edges/faces should include:

1. **Type Hierarchy Section** (already present)
   ```markdown
   ## Type Hierarchy
   edge (abstract)
   └── verification (concrete)
   ```

2. **Purpose Section** (add if missing)
   ```markdown
   ## Purpose
   Verification edges represent the relationship "this document
   satisfies this spec structurally". They are generated by
   verification tools as evidence of compliance.
   ```

3. **Semantic Constraints Section** (add if missing)
   ```markdown
   ## Semantic Constraints
   - Source must be a document (vertex/doc or subtype)
   - Target must be a spec (vertex/spec)
   - Orientation must be directed (child → spec)
   - Body must contain verification tool output
   ```

4. **Role in Assurance Pattern** (already present for verification)

5. **Example Instance** (already present)

### Implementation

For each edge/face template WITHOUT a spec:

```markdown
---
# Frontmatter remains same
---

# <Type> Template

<!-- AUTO-GENERATED SECTION -->
**Note:** This template serves as BOTH the template AND the specification
for <type> documents. It is the authoritative reference for structural
requirements. For meta-constructs like edges and faces, the template IS
the spec to avoid circular dependencies.
<!-- END AUTO-GENERATED SECTION -->

[Rest of template content...]

## Purpose
[Why this document type exists]

## Semantic Constraints
[What makes this type valid beyond structure]

## Role in Knowledge Complex
[How this type fits into the larger system]

[... rest of existing content ...]
```

---

## Reference vs Referent Clarity

### For Payload Documents (Persona, Purpose, etc.)

**Reference** (human reads):
- `00_vertices/spec-for-persona.md`
- Natural language explanation
- "A persona MUST define role and identity..."

**Referent** (tool parses):
- `templates/00_vertices/persona.md`
- Structured placeholders
- `role_and_identity: [content]`

**Verification**:
- `verify_template_based.py` parses **referent** (template)
- Checks that instance matches template structure
- Verification edge cites template as authority

### For Container Documents (Verification Edge, Assurance Face)

**Reference = Referent** (template serves both roles):
- `templates/01_edges/verification.md`
- Both human-readable explanation AND structured requirements
- Template is detailed enough to explain purpose and structure

**Verification**:
- `verify_template_based.py` parses **template** (which IS the spec)
- Checks that instance matches template structure
- No separate spec needed

---

## Architectural Decision Record

### Decision

**Adopt Architecture B+ (Hybrid):**
- Specs for payload documents (persona, purpose, protocol, system_prompt, spec, guidance)
- Specs for charts (user-facing, complex)
- Enhanced templates (no separate specs) for edges and faces

### Rationale

1. **Avoids Circular Dependencies**: spec-for-verification would need verification, creating self-reference
2. **Pragmatic**: Templates for meta-constructs are detailed and can serve dual role
3. **Clear Distinction**: Payload types get full specs, topological types get enhanced templates
4. **Maintainability**: 6 fewer specs to keep synchronized
5. **Precedent**: spec-for-charts exists because charts are user-facing, not because all containers need specs

### Consequences

**Positive:**
- No circular dependency issues
- Templates are single source of truth for edges/faces
- Clear separation: content vs structure
- Reduced maintenance burden

**Negative:**
- Inconsistent: some types have specs, others don't
- Templates must be very thorough and clear
- Need to document this architectural choice explicitly

### Mitigation

1. **Document the distinction**: Add section to each edge/face template explaining it serves as both template and spec
2. **Enhance templates**: Ensure edge/face templates include Purpose, Semantic Constraints, Role sections
3. **Update verification docs**: Clarify that templates are authoritative for meta-constructs
4. **Add to README**: Explain the payload vs container distinction

---

## Template Generation Implications

### What This Means for Phase 2

Given Architecture B+:

**CAN auto-generate templates from specs:**
- ✅ Persona, Purpose, Protocol, System_Prompt (7 types including b0)
- ✅ Spec, Guidance (already have specs)
- ⚠️ Charts (once nested object parser is built)

**CANNOT auto-generate (no specs, templates ARE specs):**
- ❌ Verification, Validation, Coupling, Dependency, Inherits edges (5 types)
- ❌ Assurance, Doc-Kit faces (2 types)

**Revised Phase 2 Scope:**
- 9 types with specs (7 vertices + 2 charts)
- Templates for these 9 can be auto-generated
- Templates for 7 meta-constructs remain hand-crafted

### Future: Can We Generate Specs from Templates?

**Interesting reversal**: Could we generate specs from templates for edges/faces?

**Template → Spec Generation:**
```python
# Read template
template = parse_template('templates/01_edges/verification.md')

# Extract requirements
frontmatter_reqs = template.frontmatter_requirements
body_sections = template.body_sections

# Generate spec document
spec = generate_spec_from_template(template)
# Output: spec-for-verification-edge.md
```

**Would this solve the circular dependency?**
- No - generated spec would still need verification
- But: generated spec could be validated (qualitative assessment)
- And: if template changes, spec regenerates automatically

**Recommendation**: Defer to Phase 3 or later. Solve the problem we have (template generation from specs) before reversing it.

---

## Summary

### Current State
- Verification uses `verify_template_based.py` (templates are authority)
- Specs exist for payloads and charts
- Templates exist for everything
- Templates serve dual role (template + spec) for meta-constructs

### Your Insight
- Correctly identified that we have specs for "payloads" (content documents)
- Correctly noted we don't have specs for "containers" (topological meta-constructs)
- Raised important question: should we?

### Answer
- **No** - Templates should serve as both template and spec for meta-constructs
- **Why** - Avoids circular dependencies, pragmatic, reduces maintenance
- **Exception** - Charts have specs because they're user-facing artifacts
- **Mitigation** - Enhance templates to be more thorough, document this choice

### Action Items

1. ✅ Document architecture decision (this doc)
2. ⬜ Add "Template IS Spec" notice to edge/face templates
3. ⬜ Enhance edge/face templates with Purpose, Semantic Constraints sections
4. ⬜ Update README to explain payload vs container distinction
5. ⬜ Revise Phase 2 plan with correct scope (9 types, not 16)

---

**Next Step**: Confirm this architectural understanding with user, then proceed with Phase 2 template generation for the 9 types with specs.
