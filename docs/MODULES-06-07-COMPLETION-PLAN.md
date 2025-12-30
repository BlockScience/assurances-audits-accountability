# Modules 06-07 Completion Plan

**Created:** 2025-12-29T00:45:00Z
**Author:** Claude Assistant
**Status:** READY FOR REVIEW

---

## Executive Summary

Modules 06 and 07 charts are **structurally complete and verified**. All vertices/edges exist in the complex, topology validates (χ = 1 for each), and charts pass verification. However, no module has TEACHING-GUIDE content yet. This plan outlines the path from current state to full module completion.

---

## Current Status

### Infrastructure Status

| Component | Status | Notes |
|-----------|--------|-------|
| Cache (complex.json) | ✓ Valid | 95 vertices, 187 edges, 76 faces, 19 charts |
| Assurance faces (8) | ✓ Fixed | All coupling edges corrected |
| Doc-kit registry | ✓ Valid | Connected component, V=16, E=40, F=10 |
| Full learning journey | ⚠️ 4 holes | See topology analysis below |

### Module 06: Document Composition

| Item | Status |
|------|--------|
| Chart file | ✓ Complete (302 lines) |
| JSON export | ✓ Generated |
| HTML visualization | ✓ Generated |
| Topology | ✓ V=6, E=9, F=4, χ=1 |
| All 6 vertices exist | ✓ Verified |
| All 9 edges exist | ✓ Verified |
| TEACHING-GUIDE | ✗ Not created |

**Module 06 Structure:**
- Entry: assurance-learner (5 skills)
- Prerequisites: assurance-audits + composing-typed-simplicial-complexes (dual)
- Develops: document-composition
- Exit: document-architect (6 skills)

### Module 07: Reference & Reuse

| Item | Status |
|------|--------|
| Chart file | ✓ Complete (304 lines) |
| JSON export | ✓ Generated |
| HTML visualization | ✓ Generated |
| Topology | ✓ V=5, E=7, F=3, χ=1 |
| All 5 vertices exist | ✓ Verified |
| All 7 edges exist | ✓ Verified |
| TEACHING-GUIDE | ✗ Not created |

**Module 07 Structure:**
- Entry: assurance-learner (4 skills)
- Prerequisites: assurance-audits (single)
- Develops: reference-reuse
- Exit: document-architect (5 skills)

### All Modules Overview

| Module | Topic | V | E | F | χ | TEACHING-GUIDE |
|--------|-------|---|---|---|---|----------------|
| 01 | Simplicial Complex Fundamentals | 5 | 7 | 3 | 1 | ✗ |
| 02 | Typed Simplicial Complexes | 5 | 7 | 3 | 1 | ✗ |
| 03 | Composing Typed Complexes | 6 | 9 | 4 | 1 | ✗ |
| 04 | Verification & Validation | 5 | 7 | 3 | 1 | ✗ |
| 05 | Assurance & Audits | 5 | 7 | 3 | 1 | ✗ |
| 06 | Document Composition | 6 | 9 | 4 | 1 | ✗ |
| 07 | Reference & Reuse | 5 | 7 | 3 | 1 | ✗ |
| 08 | Team Coordination | 5 | 7 | 3 | 1 | ✗ |
| 09 | Resource Management | 5 | 7 | 3 | 1 | ✗ |
| 10 | Organizational Topology (Capstone) | 8 | 13 | 6 | 1 | ✗ |

### Known Issues

**Full Learning Journey (4 Topological Holes):**
1. Missing face: [fundamentals, foundational-learner, intermediate-learner]
2. Missing face: [typed-module, fundamentals, intermediate-learner]
3. Missing face: [team-coordination, coordination-architect, management-architect]
4. Missing face: [resource-module, team-coordination, management-architect]

These holes suggest missing constraint faces in the composed syllabus.

---

## Phase 1: Your Rigorous Review

### 1.1 Review Module 06 Chart

Open and review `charts/learning-journey-module-06/learning-journey-module-06.md`:

**Questions to Consider:**
- [ ] Is the dual prerequisite pattern (assurance + composition) correct?
- [ ] Does the skill "document-composition" accurately represent the learning outcome?
- [ ] Is assurance-learner → document-architect the right state transition?
- [ ] Does the 20/20/30/20/10 pedagogical breakdown make sense?
- [ ] Is "convergence point" the right term for where M06 and M07 merge?

### 1.2 Review Module 07 Chart

Open and review `charts/learning-journey-module-07/learning-journey-module-07.md`:

**Questions to Consider:**
- [ ] Is single prerequisite (assurance-audits only) correct for doc-kits?
- [ ] Does "reference-reuse" accurately capture the doc-kit pattern skill?
- [ ] Should Module 07 also require composition skill (Module 03)?
- [ ] Is the 20/20/30/20/10 pedagogical breakdown appropriate?
- [ ] Does the "minimum path" (skip M06, take M07) make sense?

### 1.3 Review Convergence Design

Both modules exit to document-architect. Consider:

- [ ] Should they be truly parallel (either/or) or sequential?
- [ ] Is 5-7 skills for document-architect the right range?
- [ ] Should there be an explicit "both paths" student state?

### 1.4 Verify Recent Fixes

The 8 assurance faces were fixed (coupling edge corrections). Verify:

```bash
python scripts/build_cache.py
# Should parse without errors

# Check face consistency
python3 << 'EOF'
import json
with open('complex.json', 'r') as f:
    data = json.load(f)
faces = data['elements']['faces']
for fid in ['f:assurance:persona:spec', 'f:assurance:purpose:spec',
            'f:assurance:protocol:spec', 'f:assurance:system_prompt:spec',
            'f:assurance:persona-guidance:guidance', 'f:assurance:purpose-guidance:guidance',
            'f:assurance:protocol-guidance:guidance', 'f:assurance:system_prompt-guidance:guidance']:
    if fid in faces:
        print(f"✓ {fid}")
    else:
        print(f"✗ {fid} MISSING")
EOF
```

---

## Phase 2: Analysis & Feedback

### 2.1 Capture Your Feedback

After review, document decisions in this section:

**Module 06 Decisions:**
- Dual prerequisite pattern: [ KEEP / MODIFY ]
- Skill name: [ KEEP "document-composition" / RENAME TO ___ ]
- State transition: [ KEEP / MODIFY ]
- Pedagogical breakdown: [ KEEP / ADJUST ]

**Module 07 Decisions:**
- Single prerequisite pattern: [ KEEP / ADD composition requirement ]
- Skill name: [ KEEP "reference-reuse" / RENAME TO ___ ]
- Minimum path concept: [ KEEP / REMOVE ]
- Pedagogical breakdown: [ KEEP / ADJUST ]

**Convergence Decisions:**
- Parallel structure: [ KEEP / MAKE SEQUENTIAL ]
- Skill range (5-7): [ KEEP / ADJUST ]
- Need explicit "both" state: [ NO / YES ]

**Topological Holes:**
- Investigate 4 holes in full journey: [ YES / DEFER ]
- Priority: [ HIGH / MEDIUM / LOW ]

### 2.2 Identify Missing Content

What additional content is needed beyond TEACHING-GUIDEs?

- [ ] Use-case examples for Module 06 (PPP composition)
- [ ] Use-case examples for Module 07 (doc-kit registry)
- [ ] RACI coordination content (for Module 08)
- [ ] docs/ directory reorganization

---

## Phase 3: Execution

### 3.1 Apply Chart Modifications (if any)

Based on Phase 2 decisions, modify:
- [ ] `charts/learning-journey-module-06/learning-journey-module-06.md`
- [ ] `charts/learning-journey-module-07/learning-journey-module-07.md`
- [ ] Related vertex/edge files if renamed

### 3.2 Create TEACHING-GUIDEs

For each module, create TEACHING-GUIDE.md with:
- Learning objectives
- Prerequisites explanation
- Hands-on exercises
- Assessment criteria
- Common pitfalls

**Priority Order:**
1. Module 06 (convergence path 1)
2. Module 07 (convergence path 2)
3. Modules 01-05 (foundations)
4. Modules 08-10 (organizational)

### 3.3 Regenerate Artifacts

After any changes:
```bash
# Rebuild cache
python scripts/build_cache.py

# Verify changed charts
python scripts/verify_chart.py charts/learning-journey-module-06/learning-journey-module-06.md --root .
python scripts/verify_chart.py charts/learning-journey-module-07/learning-journey-module-07.md --root .

# Re-export JSON
python scripts/export_chart_direct.py charts/learning-journey-module-06/learning-journey-module-06.md charts/learning-journey-module-06/learning-journey-module-06.json --root .
python scripts/export_chart_direct.py charts/learning-journey-module-07/learning-journey-module-07.md charts/learning-journey-module-07/learning-journey-module-07.json --root .

# Regenerate visualizations
python scripts/visualize_syllabus.py charts/learning-journey-module-06/learning-journey-module-06.json
python scripts/visualize_syllabus.py charts/learning-journey-module-07/learning-journey-module-07.json
```

### 3.4 Fix Topological Holes (if prioritized)

Investigate and create missing faces:
1. Analyze what constraint each hole represents
2. Create face documents in `02_faces/`
3. Update `charts/learning-journey-full/` chart
4. Verify χ improves (χ = -3 → χ = 1?)

---

## Phase 4: Reconciliation

### 4.1 Verify Full Learning Journey

```bash
python scripts/verify_chart.py charts/learning-journey-full/learning-journey-full.md --root .
python scripts/topology.py charts/learning-journey-full/learning-journey-full.md --root .
```

Target: No holes (χ = 1), all modules composable.

### 4.2 Verify Module Composition

Test that modules compose correctly:
```bash
# Compose M05 → M06
python scripts/compose_charts.py \
  charts/learning-journey-module-05/learning-journey-module-05.md \
  charts/learning-journey-module-06/learning-journey-module-06.md \
  --output charts/test-composition.json --root .

# Compose M05 → M07
python scripts/compose_charts.py \
  charts/learning-journey-module-05/learning-journey-module-05.md \
  charts/learning-journey-module-07/learning-journey-module-07.md \
  --output charts/test-composition.json --root .
```

### 4.3 Update Documentation

After all changes:
- [ ] Update `docs/learning/README.md` if syllabus changed
- [ ] Update main `README.md` if module descriptions changed
- [ ] Ensure all wikilinks resolve in Obsidian

### 4.4 Final Commit

```bash
git add -A
git commit -m "Complete Modules 06-07 with TEACHING-GUIDEs

- Module 06: Document Composition (dual prerequisites)
- Module 07: Reference & Reuse via Doc-Kits
- Fixed topological holes in full journey (if applicable)
- All charts verified and visualizations regenerated

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Quick Reference Commands

```bash
# Build and verify
python scripts/build_cache.py
python scripts/verify_chart.py charts/learning-journey-module-06/learning-journey-module-06.md --root .
python scripts/verify_chart.py charts/learning-journey-module-07/learning-journey-module-07.md --root .

# Topology check
python scripts/topology.py charts/learning-journey-module-06/learning-journey-module-06.md --root .
python scripts/topology.py charts/learning-journey-module-07/learning-journey-module-07.md --root .
python scripts/topology.py charts/learning-journey-full/learning-journey-full.md --root .

# Export and visualize
python scripts/export_chart_direct.py charts/learning-journey-module-06/learning-journey-module-06.md charts/learning-journey-module-06/learning-journey-module-06.json --root .
python scripts/visualize_syllabus.py charts/learning-journey-module-06/learning-journey-module-06.json

python scripts/export_chart_direct.py charts/learning-journey-module-07/learning-journey-module-07.md charts/learning-journey-module-07/learning-journey-module-07.json --root .
python scripts/visualize_syllabus.py charts/learning-journey-module-07/learning-journey-module-07.json
```

---

## Files Changed This Session

| File | Change |
|------|--------|
| `02_faces/assurance-persona:spec.md` | Fixed coupling edge → `e:coupling:spec` |
| `02_faces/assurance-purpose:spec.md` | Fixed coupling edge → `e:coupling:spec` |
| `02_faces/assurance-protocol:spec.md` | Fixed coupling edge → `e:coupling:spec` |
| `02_faces/assurance-system_prompt:spec.md` | Fixed coupling edge → `e:coupling:spec` |
| `02_faces/assurance-persona-guidance:guidance.md` | Fixed coupling edge → `e:coupling:guidance` |
| `02_faces/assurance-purpose-guidance:guidance.md` | Fixed coupling edge → `e:coupling:guidance` |
| `02_faces/assurance-protocol-guidance:guidance.md` | Fixed coupling edge → `e:coupling:guidance` |
| `02_faces/assurance-system_prompt-guidance:guidance.md` | Fixed coupling edge → `e:coupling:guidance` |

---

**Next Steps When You Resume:**

1. Read this plan
2. Complete Phase 1 (review charts in Obsidian or VS Code)
3. Fill in Phase 2 decisions
4. Ask Claude to execute Phase 3 based on your decisions
5. Reconcile in Phase 4

Good night!
