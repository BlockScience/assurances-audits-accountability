# RBAC Docware Reference

This document is a comprehensive reference for the RBAC (Role-Based Access Control) types implemented in the AAA foundation layer. It captures the complete frontmatter schemas, type relationships, and authorization model so that these types can be reconstructed or reimplemented in an `rbac-docware` package.

## Overview

The RBAC system extends the core AAA simplicial complex (vertices, edges, faces) with six new types that together implement NIST RBAC within the document-as-infrastructure paradigm:

| Layer | Type | AAA Element | Purpose |
|-------|------|-------------|---------|
| Vertex | `vertex/role` | property vertex | Defines a named role with associated authorities |
| Vertex | `vertex/signer` | actor vertex | Identifies a human who can sign validations |
| Edge | `edge/has-role` | directed edge | Assigns a signer to a role (User Assignment) |
| Edge | `edge/conveys` | directed edge | Grants a role authority over a guidance (Permission Assignment) |
| Edge | `edge/qualifies` | directed edge | Derives that a signer is qualified for a guidance (computed from has-role + conveys) |
| Edge | `edge/signs` | directed edge | Records that a signer has signed a validation |
| Face | `face/authorization` | oriented face | Proves WHY a signer is qualified (RBAC derivation proof) |
| Face | `face/signature` | oriented face | Proves a signer signed a specific validation with accountability |

---

## Vertex Types

### `vertex/role`

A role vertex represents a named authority that can be assigned to signers and that conveys permissions over specific guidances.

#### Frontmatter Schema

```yaml
type: vertex/role            # REQUIRED. Literal value.
extends: property            # REQUIRED. Roles are property vertices.
id: "v:role:{role_name}"     # REQUIRED. Unique identifier. Pattern: v:role:<name>.
name: String                 # REQUIRED. Human-readable role name.
description: String          # REQUIRED. What authority this role grants.
tags:                        # REQUIRED. Must include: vertex, property, role.
  - vertex
  - property
  - role
  - "{role_name}"            # Role-specific tag.
  - genesis                  # Present on foundation bootstrap roles.
version: String              # REQUIRED. Semver string.
created: DateTime            # REQUIRED. ISO 8601.
modified: DateTime           # REQUIRED. ISO 8601.
dependencies: []             # REQUIRED. List of dependencies (empty for bootstrap).
```

#### Body Structure

```
# {Role Name} Role

## Purpose
What this role is for and what authority it grants.

## Genesis Context          (present on foundation roles)
Bootstrap context for this role.

## Authority Granted
Bullet list of what this role conveys authority to do.

## Qualification Requirements
How this role is assigned.
```

#### Foundation Instance

- **`v:role:admin`** -- Administrator role. Bootstrap authority for the foundation. Conveys authority to sign foundational documents, establish qualifications, and manage the knowledge complex.

---

### `vertex/signer`

A signer vertex identifies a human actor who can hold roles and sign validations.

#### Frontmatter Schema

```yaml
type: vertex/signer          # REQUIRED. Literal value.
extends: actor               # REQUIRED. Signers are actor vertices.
id: "v:signer:{signer_name}" # REQUIRED. Unique identifier. Pattern: v:signer:<name>.
name: String                 # REQUIRED. Human-readable name.
description: String          # REQUIRED. Description of the signer.
github_username: String      # REQUIRED. GitHub username. Placeholder "ADMIN_USERNAME" for bootstrap.
tags:                        # REQUIRED. Must include: vertex, actor, signer.
  - vertex
  - actor
  - signer
  - "{signer_name}"          # Signer-specific tag.
  - genesis                  # Present on foundation bootstrap signers.
version: String              # REQUIRED. Semver string.
created: DateTime            # REQUIRED. ISO 8601.
modified: DateTime           # REQUIRED. ISO 8601.
dependencies: []             # REQUIRED. List of dependencies (empty for bootstrap).
```

#### Body Structure

```
# {Signer Name}

## Purpose
What this signer represents.

## Genesis Context          (present on foundation signers)
Bootstrap context.

## Capabilities
Numbered list of what this signer can do.

## Note                     (optional)
Implementation notes (e.g. placeholder replacement during aaa init).
```

#### Foundation Instance

- **`v:signer:admin`** -- Bootstrap Administrator Signer. Placeholder for the first human admin. The `github_username` field (`ADMIN_USERNAME`) is replaced during `aaa init` with the actual GitHub username.

---

## Edge Types

### `edge/has-role` (NIST User Assignment)

Assigns a signer to a role. This is the NIST RBAC User Assignment (UA) relationship.

#### Frontmatter Schema

```yaml
type: edge/has-role          # REQUIRED. Literal value.
extends: edge                # REQUIRED.
id: "e:has-role:{signer}:{role}"  # REQUIRED. Pattern: e:has-role:<signer_name>:<role_name>.
name: String                 # REQUIRED. Human-readable name.
description: String          # REQUIRED.
source: "v:signer:{name}"   # REQUIRED. The signer vertex ID.
target: "v:role:{name}"     # REQUIRED. The role vertex ID.
source_type: vertex/signer   # REQUIRED. Literal value.
target_type: vertex/role     # REQUIRED. Literal value.
orientation: directed        # REQUIRED. Literal value.
granted_by: String           # REQUIRED. Who/what granted this role. "genesis" for bootstrap.
granted_date: DateTime       # REQUIRED. When the role was granted. ISO 8601.
tags:                        # REQUIRED. Must include: edge, has-role, rbac.
  - edge
  - has-role
  - rbac
  - foundation               # Present on foundation edges.
version: String              # REQUIRED. Semver string.
created: DateTime            # REQUIRED. ISO 8601.
modified: DateTime           # REQUIRED. ISO 8601.
```

#### Semantics

- **Direction:** signer --> role
- **Meaning:** "This signer holds this role"
- **NIST mapping:** User Assignment (UA)

#### Foundation Instance

- **`e:has-role:admin:admin`** -- Admin signer holds the admin role. `granted_by: genesis`.

---

### `edge/conveys` (NIST Permission Assignment)

Declares that a role conveys authority to validate against a specific guidance. This is the NIST RBAC Permission Assignment (PA) relationship.

#### Frontmatter Schema

```yaml
type: edge/conveys           # REQUIRED. Literal value.
extends: edge                # REQUIRED.
id: "e:conveys:{role}:{guidance}"  # REQUIRED. Pattern: e:conveys:<role_name>:<guidance_id>.
name: String                 # REQUIRED. Human-readable name.
description: String          # REQUIRED.
source: "v:role:{name}"     # REQUIRED. The role vertex ID.
target: "v:guidance:{name}" # REQUIRED. The guidance vertex ID.
source_type: vertex/role     # REQUIRED. Literal value.
target_type: vertex/guidance # REQUIRED. Literal value.
orientation: directed        # REQUIRED. Literal value.
tags:                        # REQUIRED. Must include: edge, conveys, rbac.
  - edge
  - conveys
  - rbac
  - foundation               # Present on foundation edges.
version: String              # REQUIRED. Semver string.
created: DateTime            # REQUIRED. ISO 8601.
modified: DateTime           # REQUIRED. ISO 8601.
```

#### Semantics

- **Direction:** role --> guidance
- **Meaning:** "This role conveys authority to validate documents against this guidance"
- **NIST mapping:** Permission Assignment (PA)

#### Foundation Instances

| ID | Role | Guidance |
|----|------|----------|
| `e:conveys:admin:guidance-guidance` | `v:role:admin` | `v:guidance:guidance` |
| `e:conveys:admin:guidance-ontology` | `v:role:admin` | `v:guidance:ontology` |
| `e:conveys:admin:guidance-spec` | `v:role:admin` | `v:guidance:spec` |

---

### `edge/qualifies` (Derived Permission)

Records that a signer is qualified to validate against a specific guidance. This is the derived result of the RBAC chain: if a signer has a role (has-role) and that role conveys authority for a guidance (conveys), then the signer qualifies for that guidance.

#### Frontmatter Schema

```yaml
type: edge/qualifies         # REQUIRED. Literal value.
extends: edge                # REQUIRED.
id: "e:qualifies:{signer}:{guidance}"  # REQUIRED. Pattern: e:qualifies:<signer>:<guidance_id>.
name: String                 # REQUIRED. Human-readable name.
description: String          # REQUIRED.
source: "v:signer:{name}"   # REQUIRED. The signer vertex ID.
target: "v:guidance:{name}" # REQUIRED. The guidance vertex ID.
source_type: vertex/signer   # REQUIRED. Literal value.
target_type: vertex/guidance # REQUIRED. Literal value.
orientation: directed        # REQUIRED. Literal value.
credential_type: role        # REQUIRED. How the qualification was derived. Currently always "role".
granted_by: "v:role:{name}" # REQUIRED. The role that conveyed this qualification.
granted_date: DateTime       # REQUIRED. ISO 8601.
tags:                        # REQUIRED. Must include: edge, qualifies, rbac.
  - edge
  - qualifies
  - rbac
  - foundation               # Present on foundation edges.
version: String              # REQUIRED. Semver string.
created: DateTime            # REQUIRED. ISO 8601.
modified: DateTime           # REQUIRED. ISO 8601.
```

#### Semantics

- **Direction:** signer --> guidance
- **Meaning:** "This signer is qualified to validate documents against this guidance"
- **Derivation:** Computed from `has-role` + `conveys`. The `granted_by` field traces back to the role.
- **Shared edge:** This edge participates in BOTH the authorization face (proving why) and the signature face (proving who signed).

#### Foundation Instances

| ID | Signer | Guidance | Granted By |
|----|--------|----------|------------|
| `e:qualifies:admin:guidance-guidance` | `v:signer:admin` | `v:guidance:guidance` | `v:role:admin` |
| `e:qualifies:admin:guidance-ontology` | `v:signer:admin` | `v:guidance:ontology` | `v:role:admin` |
| `e:qualifies:admin:guidance-spec` | `v:signer:admin` | `v:guidance:spec` | `v:role:admin` |

---

### `edge/signs` (Signature Attestation)

Records that a signer has signed (attested to) a specific validation. This is the accountability record binding a human to a validation judgment.

#### Frontmatter Schema

```yaml
type: edge/signs             # REQUIRED. Literal value.
extends: edge                # REQUIRED.
id: "e:signs:{signer}:{doc}" # REQUIRED. Pattern: e:signs:<signer>:<doc_id>.
name: String                 # REQUIRED. Human-readable name.
description: String          # REQUIRED.
source: "v:signer:{name}"   # REQUIRED. The signer vertex ID.
target: "v:{type}:{name}"   # REQUIRED. The document vertex being signed.
source_type: vertex/signer   # REQUIRED. Literal value.
target_type: "vertex/{type}" # REQUIRED. The target document's vertex type (e.g. vertex/guidance, vertex/ontology, vertex/spec).
orientation: directed        # REQUIRED. Literal value.
signing_date: DateTime       # REQUIRED. When the signing occurred. ISO 8601.
commit_hash: String          # REQUIRED. Git commit hash at time of signing. "foundation" for bootstrap.
tags:                        # REQUIRED. Must include: edge, signs.
  - edge
  - signs
  - foundation               # Present on foundation edges.
version: String              # REQUIRED. Semver string.
created: DateTime            # REQUIRED. ISO 8601.
modified: DateTime           # REQUIRED. ISO 8601.
```

#### Semantics

- **Direction:** signer --> document
- **Meaning:** "This signer has signed/attested to this document's validation"
- **Note:** The target is the document being validated, NOT the guidance used for validation. The guidance relationship is captured via the signature face.

#### Foundation Instances

| ID | Signer | Document | Target Type |
|----|--------|----------|-------------|
| `e:signs:admin:guidance-ontology` | `v:signer:admin` | `v:guidance:ontology` | vertex/guidance |
| `e:signs:admin:ontology-base` | `v:signer:admin` | `v:ontology:base` | vertex/ontology |
| `e:signs:admin:spec-ontology` | `v:signer:admin` | `v:spec:ontology` | vertex/spec |

---

## Face Types

### `face/authorization` (RBAC Proof)

An authorization face is an oriented 2-simplex that proves WHY a signer is qualified for a specific guidance. It encodes the complete NIST RBAC derivation chain: signer has role, role conveys authority, therefore signer is qualified.

#### Frontmatter Schema

```yaml
type: face/authorization     # REQUIRED. Literal value.
extends: face                # REQUIRED.
id: "f:authorization:{signer}:{guidance}"  # REQUIRED. Pattern: f:authorization:<signer>:<guidance_id>.
name: String                 # REQUIRED. Human-readable name.
description: String          # REQUIRED.
vertices:                    # REQUIRED. Exactly 3 vertices forming the triangle.
  - "v:signer:{name}"       #   The actor (signer).
  - "v:role:{name}"          #   The role.
  - "v:guidance:{name}"      #   The permission (guidance).
edges:                       # REQUIRED. Exactly 3 edges forming the boundary.
  - "e:has-role:{s}:{r}"     #   User Assignment edge.
  - "e:conveys:{r}:{g}"      #   Permission Assignment edge.
  - "e:qualifies:{s}:{g}"    #   Derived permission edge (SHARED with signature face).
has_role_edge: String        # REQUIRED. ID of the has-role edge.
conveys_edge: String         # REQUIRED. ID of the conveys edge.
qualifies_edge: String       # REQUIRED. ID of the qualifies edge.
signer: String               # REQUIRED. ID of the signer vertex.
role: String                 # REQUIRED. ID of the role vertex.
guidance: String             # REQUIRED. ID of the guidance vertex.
orientation: oriented        # REQUIRED. Literal value. Faces are oriented (not merely directed).
tags:                        # REQUIRED. Must include: face, authorization, rbac.
  - face
  - authorization
  - rbac
  - foundation               # Present on foundation faces.
version: String              # REQUIRED. Semver string.
created: DateTime            # REQUIRED. ISO 8601.
modified: DateTime           # REQUIRED. ISO 8601.
```

#### Topological Structure

```
        v:role:{r}
       /          \
  has-role      conveys
     /              \
v:signer:{s} ------- v:guidance:{g}
            qualifies
```

The authorization face is the filled triangle bounded by these three edges. The `qualifies` edge is the hypotenuse -- it is the derived conclusion of the RBAC proof, and it is **shared** with the corresponding signature face.

#### Foundation Instances

| ID | Signer | Role | Guidance |
|----|--------|------|----------|
| `f:authorization:admin:guidance-guidance` | `v:signer:admin` | `v:role:admin` | `v:guidance:guidance` |
| `f:authorization:admin:guidance-ontology` | `v:signer:admin` | `v:role:admin` | `v:guidance:ontology` |
| `f:authorization:admin:guidance-spec` | `v:signer:admin` | `v:role:admin` | `v:guidance:spec` |

---

### `face/signature` (Accountability Record)

A signature face is an oriented 2-simplex that records a signer's attestation of a specific validation. It binds together three facts: (1) a document was validated against a guidance, (2) the signer was qualified for that guidance, and (3) the signer signed that validation.

#### Frontmatter Schema

```yaml
type: face/signature         # REQUIRED. Literal value.
extends: face                # REQUIRED.
id: "f:signature:{doc}"      # REQUIRED. Pattern: f:signature:<doc_id>.
name: String                 # REQUIRED. Human-readable name.
description: String          # REQUIRED.
vertices:                    # REQUIRED. Exactly 3 vertices forming the triangle.
  - "v:{type}:{doc}"         #   The document being validated.
  - "v:guidance:{name}"      #   The quality criteria (guidance).
  - "v:signer:{name}"        #   The qualified validator.
doc: String                  # REQUIRED. ID of the document vertex being validated.
guidance: String             # REQUIRED. ID of the guidance vertex used for validation.
signer: String               # REQUIRED. ID of the signer vertex.
edges:                       # REQUIRED. Exactly 3 edges forming the boundary.
  - "e:validation:{d}:{g}"   #   Validation edge (SHARED with assurance face).
  - "e:qualifies:{s}:{g}"    #   Qualification edge (SHARED with authorization face).
  - "e:signs:{s}:{d}"        #   Signing edge (unique to this face).
validation_edge: String      # REQUIRED. ID of the validation edge.
qualifies_edge: String       # REQUIRED. ID of the qualifies edge.
signs_edge: String           # REQUIRED. ID of the signs edge.
signing_date: DateTime       # REQUIRED. When the signing occurred. ISO 8601.
commit_hash: String          # REQUIRED. Git commit hash. "foundation" for bootstrap.
assurance_face: String       # REQUIRED. ID of the assurance face this signature supports.
orientation: oriented        # REQUIRED. Literal value.
tags:                        # REQUIRED. Must include: face, signature.
  - face
  - signature
  - foundation               # Present on foundation faces.
version: String              # REQUIRED. Semver string.
created: DateTime            # REQUIRED. ISO 8601.
modified: DateTime           # REQUIRED. ISO 8601.
```

#### Topological Structure

```
      v:guidance:{g}
       /          \
  validation    qualifies
     /              \
v:{type}:{d} -------- v:signer:{s}
              signs
```

The signature face is the filled triangle bounded by these three edges. Two of its edges are **shared**:
- The `validation` edge is shared with the corresponding `face/assurance`
- The `qualifies` edge is shared with the corresponding `face/authorization`

Only the `signs` edge is unique to the signature face.

#### Foundation Instances

| ID | Document | Guidance | Signer | Assurance Face |
|----|----------|----------|--------|----------------|
| `f:signature:guidance-ontology` | `v:guidance:ontology` | `v:guidance:guidance` | `v:signer:admin` | `f:assurance:guidance-ontology` |
| `f:signature:ontology-base` | `v:ontology:base` | `v:guidance:ontology` | `v:signer:admin` | `f:assurance:ontology-base` |
| `f:signature:spec-ontology` | `v:spec:ontology` | `v:guidance:spec` | `v:signer:admin` | `f:assurance:spec-ontology` |

---

## The RBAC Authorization Model

### NIST RBAC Mapping

The RBAC types implement a document-native version of NIST RBAC Core:

| NIST Concept | AAA Element | Type | Relationship |
|--------------|-------------|------|--------------|
| User | Vertex | `vertex/signer` | A human actor |
| Role | Vertex | `vertex/role` | A named authority |
| Permission | Vertex | `vertex/guidance` (core AAA type) | Authority over a specific guidance |
| User Assignment (UA) | Edge | `edge/has-role` | signer --> role |
| Permission Assignment (PA) | Edge | `edge/conveys` | role --> guidance |
| Derived Permission | Edge | `edge/qualifies` | signer --> guidance (computed) |

### Authorization Chain

The complete authorization chain from signer to signed document flows through four layers:

```
1. ROLE ASSIGNMENT (has-role)
   v:signer:admin  --[has-role]-->  v:role:admin

2. PERMISSION ASSIGNMENT (conveys)
   v:role:admin  --[conveys]-->  v:guidance:{g}

3. DERIVED QUALIFICATION (qualifies)
   v:signer:admin  --[qualifies]-->  v:guidance:{g}
   (This edge is the derived conclusion of steps 1+2)

4. SIGNATURE (signs)
   v:signer:admin  --[signs]-->  v:{type}:{doc}
   (This edge records the actual attestation)
```

Steps 1-3 are bundled into an **authorization face**. Steps 3-4 plus the validation edge form a **signature face**. The `qualifies` edge is shared between them.

### Face Adjacency and Shared Edges

The RBAC faces integrate with core AAA assurance faces through shared edges:

```
                    AUTHORIZATION FACE              SIGNATURE FACE              ASSURANCE FACE
                    (f:authorization:...)           (f:signature:...)           (f:assurance:...)

                    v:role                          v:guidance                  v:guidance
                   / \                             / \                         / \
              has-role  conveys              validation  qualifies       validation  verification
                 /       \                     /           \                /         \
           v:signer --- v:guidance      v:document --- v:signer      v:document --- v:spec
                  qualifies                     signs                     verified-by
```

Shared edges create the topological gluing:
- **`qualifies` edge** is shared between authorization face and signature face
- **`validation` edge** is shared between signature face and assurance face

This means the three face types form a connected surface where:
- Authorization proves WHY someone is qualified
- Signature records WHO signed WHAT
- Assurance records the verification and validation result

### ID Conventions

All RBAC elements follow strict ID patterns:

| Type | Pattern | Example |
|------|---------|---------|
| Role vertex | `v:role:{role_name}` | `v:role:admin` |
| Signer vertex | `v:signer:{signer_name}` | `v:signer:admin` |
| Has-role edge | `e:has-role:{signer}:{role}` | `e:has-role:admin:admin` |
| Conveys edge | `e:conveys:{role}:{guidance_id}` | `e:conveys:admin:guidance-ontology` |
| Qualifies edge | `e:qualifies:{signer}:{guidance_id}` | `e:qualifies:admin:guidance-spec` |
| Signs edge | `e:signs:{signer}:{doc_id}` | `e:signs:admin:ontology-base` |
| Authorization face | `f:authorization:{signer}:{guidance_id}` | `f:authorization:admin:guidance-ontology` |
| Signature face | `f:signature:{doc_id}` | `f:signature:ontology-base` |

### Filename Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Role vertex | `role-{name}.md` | `role-admin.md` |
| Signer vertex | `signer-{name}.md` | `signer-admin.md` |
| Has-role edge | `has-role-{signer}-{role}.md` | `has-role-admin-admin.md` |
| Conveys edge | `conveys-{role}-{guidance_id}.md` | `conveys-admin-guidance-ontology.md` |
| Qualifies edge | `qualifies-{signer}-{guidance_id}.md` | `qualifies-admin-guidance-spec.md` |
| Signs edge | `signs-{signer}-{doc_id}.md` | `signs-admin-ontology-base.md` |
| Authorization face | `authorization-{signer}-{guidance_id}.md` | `authorization-admin-guidance-ontology.md` |
| Signature face | `signature-{doc_id}.md` | `signature-ontology-base.md` |

---

## Complete Foundation Example

The following traces the full chain for admin signing `v:guidance:ontology` validated against `v:guidance:guidance`.

### Step 1: Vertices exist

- `v:signer:admin` (signer vertex)
- `v:role:admin` (role vertex)
- `v:guidance:guidance` (core AAA guidance vertex -- not an RBAC type)
- `v:guidance:ontology` (core AAA guidance vertex -- the document to be validated)

### Step 2: Role assignment

- `e:has-role:admin:admin` assigns `v:signer:admin` to `v:role:admin`

### Step 3: Permission assignment

- `e:conveys:admin:guidance-guidance` grants `v:role:admin` authority over `v:guidance:guidance`

### Step 4: Derived qualification

- `e:qualifies:admin:guidance-guidance` records that `v:signer:admin` is qualified for `v:guidance:guidance`

### Step 5: Authorization face

- `f:authorization:admin:guidance-guidance` bundles the triangle:
  - `e:has-role:admin:admin` (UA)
  - `e:conveys:admin:guidance-guidance` (PA)
  - `e:qualifies:admin:guidance-guidance` (derived, shared)

### Step 6: Signing

- `e:signs:admin:guidance-ontology` records admin's attestation of `v:guidance:ontology`

### Step 7: Signature face

- `f:signature:guidance-ontology` bundles the triangle:
  - `e:validation:guidance-ontology:guidance-guidance` (shared with assurance face)
  - `e:qualifies:admin:guidance-guidance` (shared with authorization face)
  - `e:signs:admin:guidance-ontology` (unique to this face)
  - References `f:assurance:guidance-ontology` via `assurance_face` field

### Result

Three faces glued along shared edges form a connected accountability surface:

```
Authorization Face          Signature Face            Assurance Face
(proves WHY qualified)      (proves WHO signed)       (proves WHAT is assured)
     |                           |                          |
     +--- qualifies edge --------+                          |
                                 +--- validation edge ------+
```

---

## Extension Points for rbac-docware

### Type Registration

An rbac-docware package must register the following types with the AAA type system:

- `vertex/role` (extends: property)
- `vertex/signer` (extends: actor)
- `edge/has-role` (extends: edge)
- `edge/conveys` (extends: edge)
- `edge/qualifies` (extends: edge)
- `edge/signs` (extends: edge)
- `face/authorization` (extends: face)
- `face/signature` (extends: face)

### Validation Rules

The package should enforce these constraints:

1. **has-role edges** must have `source_type: vertex/signer` and `target_type: vertex/role`
2. **conveys edges** must have `source_type: vertex/role` and `target_type: vertex/guidance`
3. **qualifies edges** must have `source_type: vertex/signer` and `target_type: vertex/guidance`
4. **signs edges** must have `source_type: vertex/signer`; target can be any document vertex type
5. **authorization faces** must contain exactly one has-role, one conveys, and one qualifies edge
6. **signature faces** must contain exactly one validation, one qualifies, and one signs edge
7. **qualifies edge consistency**: for every qualifies edge `signer -> guidance`, there must exist a has-role edge `signer -> role` and a conveys edge `role -> guidance` for some role
8. **signature face must reference a valid assurance face** via `assurance_face`

### Genesis / Bootstrap

The foundation layer uses `genesis` as a special `granted_by` value for has-role edges, indicating role assignments created during system initialization rather than through the normal RBAC chain. The `aaa init` command replaces placeholder values (e.g., `ADMIN_USERNAME` in signer vertices) with actual user data.

### Non-RBAC Types Referenced

The RBAC types reference but do not define these core AAA types:

- `vertex/guidance` -- quality criteria documents (targets of conveys and qualifies edges)
- `vertex/ontology` -- ontology documents (can be targets of signs edges)
- `vertex/spec` -- specification documents (can be targets of signs edges)
- `edge/validation` -- validation edges from assurance faces (shared with signature faces)
- `face/assurance` -- assurance faces (referenced by signature faces via `assurance_face`)
