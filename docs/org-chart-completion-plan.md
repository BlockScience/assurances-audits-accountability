# Organization Chart Completion Plan

**Created:** 2025-12-29 (late night session)
**Status:** AWAITING REVIEW
**Next Session Goal:** Complete organization charts and reconcile with module content

---

## Executive Summary

Three organization charts have been created but require refinement:
1. **raci-coordination-chart** - Valid but has 5 topological holes (membership faces)
2. **resource-management-chart** - Valid with no holes but no faces modeled
3. **composed-org-chart** - Valid but inherits holes from coordination chart

All charts pass `verify_chart.py` verification. The spec and guidance documents exist.

---

## Current Status

### Verification Results (All Pass)

| Chart | Vertices | Edges | Faces | χ | Holes |
|-------|----------|-------|-------|---|-------|
| raci-coordination-chart | 14 | 28 | 8 | -6 | 5 |
| resource-management-chart | 9 | 9 | 0 | 0 | 0 |
| composed-org-chart | 21 | 37 | 8 | -8 | 5 |

### Files Created

**Specification & Guidance:**
- `00_vertices/spec-for-organization.md` (~150 lines)
- `00_vertices/guidance-for-organization.md` (~150 lines)

**Team/Staff/Role Vertices (14 files):**
- 2 teams: `team-platform.md`, `team-product.md`
- 5 staff: `staff-alice.md`, `staff-bob.md`, `staff-charlie.md`, `staff-dana.md`, `staff-evan.md`
- 4 roles: `role-tech-lead.md`, `role-sre.md`, `role-senior-developer.md`, `role-developer.md`
- 3 responsibilities: `responsibility-deploy.md`, `responsibility-monitor.md`, `responsibility-build.md`

**Function/Resource Vertices (7 files):**
- 3 functions: `function-build.md`, `function-test.md`, `function-deploy.md`
- 4 resources: `resource-source-code.md`, `resource-built-artifact.md`, `resource-tested-code.md`, `resource-running-service.md`

**Edges (28+ files for coordination, 9 for management):**
- Member edges (5): staff → team
- Holds-role edges (5): staff → role
- Includes edges (4): team → role
- Assigned edges (6): role → responsibility (with raci_type)
- Direct RACI edges (8): accountable/responsible (staff → responsibility)
- Operates edges (3): team → function
- Produces edges (3): function → resource
- Consumes edges (3): function → resource

**Assignment Faces (8 files):**
- `assignment-alice-tech-lead-deploy.md` (A)
- `assignment-bob-sre-deploy.md` (R)
- `assignment-charlie-sre-deploy.md` (R)
- `assignment-alice-tech-lead-monitor.md` (A)
- `assignment-bob-sre-monitor.md` (R)
- `assignment-charlie-sre-monitor.md` (R)
- `assignment-dana-senior-developer-build.md` (A)
- `assignment-evan-developer-build.md` (R)

**Charts (3 directories):**
- `charts/raci-coordination-chart/` - md, json, html
- `charts/resource-management-chart/` - md, json, html
- `charts/composed-org-chart/` - md, json, html

---

## Known Issues Requiring Review

### 1. Topological Holes in Coordination Chart

The topology script detects 5 "missing faces" - triangles where 3 edges exist but no face is modeled:

```
1. Missing: [tech-lead, alice, platform]  -- staff-role-team triangle
2. Missing: [sre, bob, platform]          -- staff-role-team triangle
3. Missing: [sre, charlie, platform]      -- staff-role-team triangle
4. Missing: [senior-developer, dana, product]
5. Missing: [developer, evan, product]
```

**Question for Review:** Should we create "membership" faces to fill these holes? These would represent the constraint "Alice holds tech-lead role in Platform team" as a triangular face.

**Options:**
- A) Create 5 membership faces (e.g., `f:membership:alice:tech-lead:platform`)
- B) Leave as intentional holes (assignment faces are the primary constraint)
- C) Remove includes edges (team→role) so triangles don't form

### 2. Resource Management Chart Has No Faces

The management chart models resource flows but doesn't capture constraints as faces.

**Potential faces:**
- Transformation faces: (function, input-resource, output-resource)
- E.g., `f:transform:build:source-code:built-artifact`

**Question for Review:** Should we add transformation faces to the management chart?

### 3. Edge Naming Consistency

Current edge IDs vary in format:
- `e:holds-role:alice:tech-lead` (subject:predicate:object pattern)
- `e:member:platform:alice` (container:type:member pattern)
- `e:accountable:alice:deploy` (type:subject:object pattern)

**Question for Review:** Standardize edge naming convention?

### 4. JSON/HTML Exports May Be Stale

The JSON and HTML exports were generated before the RACI edges were added. Need to re-export after any changes.

---

## Completion Workflow

### Phase 1: Your Review (Chief Engineer)

1. **Read this plan** - understand current state
2. **Review the charts** - open in Obsidian or read markdown:
   - `charts/raci-coordination-chart/raci-coordination-chart.md`
   - `charts/resource-management-chart/resource-management-chart.md`
   - `charts/composed-org-chart/composed-org-chart.md`
3. **Review spec and guidance** - verify they match your intent:
   - `00_vertices/spec-for-organization.md`
   - `00_vertices/guidance-for-organization.md`
4. **Provide feedback** on:
   - Topological holes: fill them or leave intentional?
   - Face coverage: add transformation faces to management?
   - Naming conventions: standardize or accept variation?
   - Content accuracy: do the charts reflect real organizational patterns?

### Phase 2: Analysis and Design

After your feedback, I will:

1. **Analyze feedback** - understand required changes
2. **Update spec/guidance** if needed
3. **Create any missing elements** (membership faces, transformation faces, etc.)
4. **Fix inconsistencies** in naming or structure

### Phase 3: Execution

1. **Update chart files** with corrected/additional elements
2. **Rebuild cache** - `python scripts/build_cache.py`
3. **Verify all charts** - `python scripts/verify_chart.py <chart>`
4. **Run topology analysis** - `python scripts/topology.py <chart>`
5. **Re-export JSON/HTML** - `python scripts/export_chart_direct.py` + `python scripts/visualize_chart.py`

### Phase 4: Module Content Reconciliation

The module content (920, 932, 906 lines respectively) needs to integrate with these charts:

**Module 08 (Team Coordination):**
- Reference the raci-coordination-chart as primary example
- Add exercises using the chart's RACI structure
- Link to assignment faces as constraint examples

**Module 09 (Resource Management):**
- Reference the resource-management-chart as primary example
- Add exercises using produces/consumes edges
- Explain flow modeling with concrete examples

**Module 10 (Organizational Topology):**
- Reference the composed-org-chart as capstone example
- Demonstrate chart composition (coordination + management)
- Use topology analysis (χ = -8) as learning exercise
- Show Hodge decomposition on organizational flows

**Action Items:**
- [ ] Add cross-references from modules to chart files
- [ ] Add worked examples using real chart elements
- [ ] Add self-assessment questions based on charts
- [ ] Ensure modules explain concepts demonstrated by charts

### Phase 5: Final Verification

1. **Run full build_cache.py** - verify all elements
2. **Verify module charts** (learning-journey-08, 09, 10) still pass
3. **Run topology on all organization charts**
4. **Update visualization exports**
5. **Commit all changes**

---

## Verification Commands

```bash
# Rebuild cache and verify
python scripts/build_cache.py

# Verify individual charts
python scripts/verify_chart.py charts/raci-coordination-chart/raci-coordination-chart.md --root .
python scripts/verify_chart.py charts/resource-management-chart/resource-management-chart.md --root .
python scripts/verify_chart.py charts/composed-org-chart/composed-org-chart.md --root .

# Topology analysis
python scripts/topology.py charts/raci-coordination-chart/raci-coordination-chart.md --root .
python scripts/topology.py charts/resource-management-chart/resource-management-chart.md --root .
python scripts/topology.py charts/composed-org-chart/composed-org-chart.md --root .

# Re-export charts
python scripts/export_chart_direct.py charts/raci-coordination-chart/raci-coordination-chart.md charts/raci-coordination-chart/raci-coordination-chart.json
python scripts/visualize_chart.py charts/raci-coordination-chart/raci-coordination-chart.json
```

---

## Decision Points Awaiting Your Input

| # | Question | Options | Default |
|---|----------|---------|---------|
| 1 | Fill membership holes? | A) Add faces, B) Leave holes, C) Remove includes edges | B |
| 2 | Add transformation faces to management chart? | Yes/No | No |
| 3 | Standardize edge naming? | Yes (specify pattern) / No | No |
| 4 | Depth of module integration | Light (references) / Deep (exercises + examples) | Deep |

---

## Files to Review

**High Priority (charts):**
- `charts/raci-coordination-chart/raci-coordination-chart.md`
- `charts/resource-management-chart/resource-management-chart.md`
- `charts/composed-org-chart/composed-org-chart.md`

**Medium Priority (spec/guidance):**
- `00_vertices/spec-for-organization.md`
- `00_vertices/guidance-for-organization.md`

**Context (modules):**
- `docs/learning/module-08.md`
- `docs/learning/module-09.md`
- `docs/learning/module-10.md`

---

## Next Steps

When you return in the morning:

1. Read this plan
2. Review the charts (start with raci-coordination-chart)
3. Provide feedback on the decision points
4. I will execute the completion workflow based on your guidance

---

*Plan generated by Claude (assistant) at end of 2025-12-29 session*
