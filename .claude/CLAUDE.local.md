# Local Notes for Claude - DO NOT MODIFY FOUNDATION

## CRITICAL WARNING

The foundation directory (`src/aaa/foundation/`) contains carefully tested genesis
documents. At commit `92ef8f4` ("RBAC all ontology rules pass"), all ontology rules
passed. This was achieved through extensive testing and visual inspection.

### DO NOT:
- Add new files to src/aaa/foundation/ without explicit user approval
- Copy files from the main repo (00_vertices/, 01_edges/, 02_faces/) into foundation
- Modify the foundation_edge_files or foundation_face_files lists in init.py
- Create charts in foundation

### The foundation is MINIMAL by design:
- 8 vertices (root + 3 spec + 3 guidance + ontology-base)
- 11 edges (3 coupling + 4 b1 boundary + 4 genesis verification/validation)
- 4 faces (4 b2 boundary faces)

### RBAC elements (qualifies, signs, signature faces) are NOT foundation:
- They are created dynamically by `aaa init` based on the user's GitHub username
- The main repo has user-specific RBAC (mzargham), NOT generic foundation RBAC
- DO NOT copy these to foundation

### If asked to bundle a chart:
- Ask user to clarify which existing chart from the main repo
- Do NOT create new genesis charts
- The boundary-complex chart in the main repo is the tested reference

### Known working commit: 92ef8f4
- Message: "RBAC all ontology rules pass"
- All ontology rules passed at this commit
- Foundation state at this commit is the canonical reference

## Foundation File Inventory (canonical at 92ef8f4)

### 00_vertices/ (8 files)
```
b0-root.md
guidance-for-guidance.md
guidance-for-ontology.md
guidance-for-spec.md
ontology-base.md
spec-for-guidance.md
spec-for-ontology.md
spec-for-spec.md
```

### 01_edges/ (11 files)
```
b1-couples-GS-root.md
b1-couples-SG-root.md
b1-self-validation.md
b1-self-verification.md
coupling-guidance.md
coupling-ontology.md
coupling-spec.md
validation-guidance-spec-guidance-guidance.md
validation-spec-guidance-guidance-spec.md
verification-guidance-spec-spec-guidance.md
verification-spec-guidance-spec-spec.md
```

### 02_faces/ (4 files)
```
b2-guidance-guidance.md
b2-guidance-spec.md
b2-spec-guidance.md
b2-spec-spec.md
```

### NO charts/ directory in foundation

## Why This Matters

On 2026-01-12, Claude made a mess by:
1. Creating new edge files that didn't belong (validation-spec-spec-guidance-spec.md, verification-guidance-guidance-spec-guidance.md)
2. Copying RBAC elements from main repo to foundation (6 edges + 4 faces)
3. Creating a genesis-complex chart in foundation
4. Updating init.py to reference all these non-existent foundation files

This required surgical cleanup to restore the working state. The user explicitly said:
"stop stop stop. you are making a huge mess and are likely to force me to revert into an awkward state stop fucking with the foundational elements. we already tested that out and it worked it was very hard to get working and i do NOT WANT TO DO THAT AGAIN"

Learn from this mistake. The foundation is SACRED. Do not touch it without explicit approval.