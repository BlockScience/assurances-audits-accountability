---
type: vertex/spec
extends: doc
id: v:spec:signature
name: Specification for Signature Face Documents
description: Defines what makes a valid signature face - accountability triangle coupling doc, guidance, and signer with shared validation edge
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-30T00:00:00Z
modified: 2025-12-30T00:00:00Z
dependencies:
  - v:spec:signer
  - v:spec:qualifies
  - v:spec:signs
---

# Specification for Signature Face Documents

**This specification defines the structure and requirements for signature face documents in the knowledge complex.**

## Purpose

Signature faces represent **accountability triangles** that complement assurance faces. While assurance faces couple (doc, spec, guidance) with verification and validation edges, signature faces couple (doc, guidance, signer) with validation, signs, and qualifies edges. The key property is that signature and assurance faces **share the validation edge as a common boundary**, making the signer's accountability explicit in the simplicial complex.

## Semantic Meaning

A signature face with vertices (doc D, guidance G, signer S) means:
- "S signed the validation of D against G"
- "S was qualified to validate against G at signing time"
- "The signing event is cryptographically recorded"

## Relationship to Assurance

Signature faces complement assurance faces through a **shared boundary**:

```
                    doc
                   / | \
                  /  |  \
                 /   |   \
         verification | validation (SHARED)
               /     |     \
              /      |      \
           spec    signs   guidance
              \      |      /
               \     |     /
          coupling   |  qualifies
                 \   |   /
                  \  |  /
                   signer

Assurance Face: (doc, spec, guidance) - verification, validation, coupling
Signature Face: (doc, guidance, signer) - validation, signs, qualifies
Common Boundary: validation edge
```

## Required Frontmatter Fields

All signature face documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `face/signature` |
| `extends` | string | REQUIRED | Must be `face` |
| `id` | string | REQUIRED | Unique identifier (format: `f:signature:<doc>:<signer>`) |
| `name` | string | REQUIRED | Human-readable face name |
| `tags` | array[string] | REQUIRED | Must include `[face, signature]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Vertex References

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `vertices` | array[string] | REQUIRED | Exactly 3 vertex IDs: [doc, guidance, signer] |
| `doc` | string | REQUIRED | Document vertex ID |
| `guidance` | string | REQUIRED | Guidance vertex ID |
| `signer` | string | REQUIRED | Signer vertex ID |

### Edge References (Boundary)

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `boundary` | array[string] | REQUIRED | Exactly 3 edge IDs: [validation, signs, qualifies] |
| `validation_edge` | string | REQUIRED | Validation edge ID (shared with assurance) |
| `signs_edge` | string | REQUIRED | Signs edge ID |
| `qualifies_edge` | string | REQUIRED | Qualifies edge ID |

### Signing Event Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `signing_date` | datetime | REQUIRED | When signature was created |
| `commit_hash` | string | REQUIRED | Git commit recording the signature |

### Related Assurance

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `assurance_face` | string | OPTIONAL | ID of corresponding assurance face (shares validation edge) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

## Required Body Sections

### 1. Face Description

**Format:**
```markdown
## Face Description

**Type:** Signature Triangle
**Signing Date:** [timestamp]
**Commit:** [hash]

This signature face records [signer]'s attestation to [doc] based on validation against [guidance].
```

### 2. Vertices

**Format:**
```markdown
## Vertices

1. **[Document Name]** (`<doc-id>`)
   - The document being signed
   - Type: [document type]
   - Role: Target of signature

2. **[Guidance Name]** (`<guidance-id>`)
   - Quality criteria for validation
   - Type: vertex/guidance
   - Role: Validation target

3. **[Signer Name]** (`<signer-id>`)
   - The signing authority
   - Type: vertex/signer
   - GitHub: [username]
   - Role: Accountable party
```

### 3. Edges (Boundary)

**Format:**
```markdown
## Edges (Boundary)

1. **[Validation Edge]** (`<validation-edge-id>`)
   - Source: [doc] → Target: [guidance]
   - Type: edge/validation
   - Status: [Pass/Fail]
   - **SHARED** with assurance face: [assurance-face-id]

2. **[Signs Edge]** (`<signs-edge-id>`)
   - Source: [signer] → Target: [doc]
   - Type: edge/signs
   - Signing Date: [timestamp]
   - Commit: [hash]

3. **[Qualifies Edge]** (`<qualifies-edge-id>`)
   - Source: [signer] → Target: [guidance]
   - Type: edge/qualifies
   - Credential Type: [type]
   - Valid At: [confirmation]
```

### 4. Triangle Coherence

**Format:**
```markdown
## Triangle Coherence

**Topological Properties:**
- **Closed Boundary:** All three edges form a cycle
- **Complete:** All vertices connected by edges
- **Oriented:** Validation and qualifies directed to guidance; signs directed to doc

**Signature Completeness:**
- ✓/✗ Validation assessment exists and passed
- ✓/✗ Signer qualification verified at signing time
- ✓/✗ Signing event recorded with commit hash
- ✓/✗ Shared boundary with assurance face (if applicable)
```

### 5. Accountability Statement

**Format:**
```markdown
## Accountability Statement

This signature records that [signer name] ([github_username]) attested to [document name] on [date].

The signer's qualification was verified through [qualifies-edge-id], which establishes [credential_type] authority to validate against [guidance name].

This signature is recorded in commit [hash] and can be verified through GitHub's commit signature verification.

**Signed:** [signer name]
**GitHub:** [username]
**Date:** [signing_date]
```

## Optional Body Sections

### Related Assurance

```markdown
## Related Assurance

**Assurance Face:** [Link to assurance face]
**Shared Edge:** [validation edge id]

This signature face complements the assurance face by making the signer explicit.
```

### Signature Context

```markdown
## Signature Context

[Additional context about why this signature was made, what it represents in the workflow]
```

## Type Constraints

1. **Type Field:** MUST be exactly `face/signature`
2. **Extends Field:** MUST be exactly `face`
3. **ID Format:** MUST match pattern `f:signature:[doc-name]:[signer-username]`
4. **Vertex Count:** MUST have exactly 3 vertices
5. **Edge Count:** MUST have exactly 3 edges in boundary
6. **Vertex Types:** Must include one doc, one guidance, one signer
7. **Edge Types:** Must include one validation, one signs, one qualifies
8. **Tag Inheritance:** Tags MUST include: `[face, signature]`

## Topological Requirements

### Triangle Formation

The three edges must form a valid triangle:
- validation: doc → guidance
- signs: signer → doc
- qualifies: signer → guidance

### Boundary Cycle

Following the boundary edges must traverse all three vertices exactly once and return to start.

### Shared Boundary Property

If an assurance face exists for the same doc, the validation edge MUST be shared (same edge ID referenced by both faces).

## Verification vs. Validation

- **Verification** (against this spec): Check vertex/edge counts, types match, boundary forms triangle, shared edge properly referenced
- **Validation** (against guidance-for-signature): Assess coherence, appropriateness of signer, clarity of accountability

## Schema Summary

```yaml
# Required frontmatter
type: face/signature
extends: face
id: f:signature:<doc>:<signer>
name: <string>
vertices:
  - <doc-vertex-id>
  - <guidance-vertex-id>
  - <signer-vertex-id>
doc: <doc-vertex-id>
guidance: <guidance-vertex-id>
signer: <signer-vertex-id>
boundary:
  - <validation-edge-id>
  - <signs-edge-id>
  - <qualifies-edge-id>
validation_edge: <validation-edge-id>
signs_edge: <signs-edge-id>
qualifies_edge: <qualifies-edge-id>
signing_date: <ISO8601>
commit_hash: <git-commit-hash>
tags: [face, signature]
version: <semver>
created: <ISO8601>
modified: <ISO8601>

# Optional frontmatter
assurance_face: <assurance-face-id>
description: <string>

# Required body sections (markdown)
## Face Description
## Vertices (3 items)
## Edges (Boundary) (3 items, noting shared validation)
## Triangle Coherence
## Accountability Statement

# Optional body sections
## Related Assurance
## Signature Context
```

## Compliance

A document claiming `type: face/signature` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. Exactly 3 vertices: one doc, one guidance, one signer
3. Exactly 3 boundary edges: validation, signs, qualifies
4. Edges form a valid triangle (boundary cycle)
5. signing_date and commit_hash are present
6. All REQUIRED body sections are present
7. Accountability statement includes signer identity and date
8. Type constraints are satisfied
9. If assurance_face referenced, validation_edge must match

---

**Note:** Signature faces complement assurance faces by making human accountability explicit in the simplicial complex. The shared validation edge creates a common boundary, ensuring that the structural assurance (verification + coupling) and accountability assurance (signs + qualifies) are topologically connected.
