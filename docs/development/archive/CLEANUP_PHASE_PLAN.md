# Knowledge Complex Cleanup Phase Plan

**Goal:** Get repository into clean, testable, shareable state
**Status:** In Progress
**Started:** 2025-12-27

---

## Current State Assessment

### Inventory

**Vertices (00_vertices/):** 22 files
- 9 Specs (spec-for-*)
- 8 Guidances (guidance-for-*)
- 5 Other vertices (boundary, test vertices)

**Edges (01_edges/):** 38 files
- Coupling edges (10)
- Verification edges (incomplete)
- Validation edges (incomplete)
- Inherits edges (2)
- Boundary edges (4)
- Test edges (6)

**Faces (02_faces/):** 16 files
- Assurance faces (incomplete)
- Doc-kit faces (1 - draft)
- Boundary faces
- Test faces

**Charts (charts/):** 0 markdown files in root
- Subdirectories exist with charts

### Recent Changes Requiring Integration

1. **PPP Framework Added** (2025-12-27)
   - 4 new specs: persona, purpose, protocol, system_prompt
   - 4 new guidances: persona, purpose, protocol, system_prompt
   - Compositional spec pattern established
   - **Missing:** All coupling/verification/validation edges, assurance faces

2. **Doc-Kit Pattern Added** (2025-12-27)
   - Template created: `templates/02_faces/doc-kit.md`
   - 1 draft instance: `f:doc_kit:persona`
   - **Missing:** Edges for doc-kit, complete assurance triangle

3. **Breaking Changes Made**
   - Obsidian compatibility criteria added to all guidances
   - Reference/referent clarity criteria added
   - May require updating existing validation edges

### Known Issues

1. **Incomplete Assurance Network**
   - Many specs without coupling edges
   - Many specs/guidances without verification/validation edges
   - Many specs/guidances without assurance faces

2. **Test Coverage Gaps**
   - Tests may not cover new PPP framework docs
   - Tests may not cover doc-kit pattern
   - Tests may expect old validation criteria (pre-Obsidian, pre-ref/referent)

3. **Organizational Gaps**
   - No doc-kit-registry chart yet
   - No comprehensive chart of all document types
   - Test edges/faces/charts mixed with production

---

## Phase Plan

### Phase 0: Baseline Testing ⏳

**Goal:** Establish what currently works and what breaks

**Tasks:**

- [ ] Run all existing tests, document failures
  ```bash
  cd tests
  python run_tests.py > ../test-baseline-results.txt 2>&1
  ```
- [ ] Run verification on all vertices
  ```bash
  for f in 00_vertices/*.md; do python scripts/verify_template_based.py "$f"; done > vertex-verification-baseline.txt 2>&1
  ```
- [ ] Run verification on all edges
  ```bash
  for f in 01_edges/*.md; do python scripts/verify_template_based.py "$f"; done > edge-verification-baseline.txt 2>&1
  ```
- [ ] Run verification on all faces
  ```bash
  for f in 02_faces/*.md; do python scripts/verify_template_based.py "$f"; done > face-verification-baseline.txt 2>&1
  ```
- [ ] Document all failures in `BASELINE_ISSUES.md`
- [ ] Categorize failures: breaking changes vs. missing infrastructure

**Success Criteria:** Clear understanding of what needs fixing

**Estimated Time:** 30 minutes

---

### Phase 1: Fix Core Infrastructure ⏳

**Goal:** Ensure all existing documents verify correctly

**Priority 1.1: Fix Template Compliance Issues**

- [ ] Fix any template violations in existing vertices
- [ ] Fix any template violations in existing edges
- [ ] Fix any template violations in existing faces
- [ ] Update templates if reasonable issues found

**Priority 1.2: Update Tests for Breaking Changes**

- [ ] Update validation edge templates to expect Obsidian compatibility criterion
- [ ] Update validation edge templates to expect reference/referent clarity criterion
- [ ] Update test expectations for guidance documents (now 7 criteria instead of 6)
- [ ] Run tests again, verify fixes

**Priority 1.3: Clean Up Test vs Production**

- [ ] Move test edges to `tests/fixtures/edges/` or mark clearly
- [ ] Move test faces to `tests/fixtures/faces/` or mark clearly
- [ ] Move test vertices to `tests/fixtures/vertices/` or mark clearly
- [ ] Update test paths in test files
- [ ] Document which elements are fixtures vs production

**Success Criteria:**
- All existing vertices verify (100%)
- All existing edges verify (100%)
- All existing faces verify (100%)
- Tests pass with updated expectations
- Clear separation of test fixtures from production

**Estimated Time:** 2-3 hours

---

### Phase 2: Complete PPP Framework Assurance ⏳

**Goal:** Fully integrate PPP framework into assurance network

**Priority 2.1: Create Coupling Edges**

- [ ] `e:coupling:persona` (v:spec:persona ↔ v:guidance:persona)
- [ ] `e:coupling:purpose` (v:spec:purpose ↔ v:guidance:purpose)
- [ ] `e:coupling:protocol` (v:spec:protocol ↔ v:guidance:protocol)
- [ ] `e:coupling:system_prompt` (v:spec:system_prompt ↔ v:guidance:system_prompt)
- [ ] Verify all 4 coupling edges

**Priority 2.2: Create Verification Edges (Spec → Spec-for-Spec)**

- [ ] `e:verification:persona:spec`
- [ ] `e:verification:purpose:spec`
- [ ] `e:verification:protocol:spec`
- [ ] `e:verification:system_prompt:spec`
- [ ] Run actual verification, document results in edges
- [ ] Verify all 4 verification edges

**Priority 2.3: Create Validation Edges (Spec → Guidance-for-Spec)**

- [ ] `e:validation:persona:spec`
- [ ] `e:validation:purpose:spec`
- [ ] `e:validation:protocol:spec`
- [ ] `e:validation:system_prompt:spec`
- [ ] Perform quality assessment, document in edges
- [ ] Verify all 4 validation edges

**Priority 2.4: Create Verification Edges (Guidance → Spec-for-Guidance)**

- [ ] `e:verification:persona-guidance:guidance`
- [ ] `e:verification:purpose-guidance:guidance`
- [ ] `e:verification:protocol-guidance:guidance`
- [ ] `e:verification:system_prompt-guidance:guidance`
- [ ] Run actual verification, document results
- [ ] Verify all 4 verification edges

**Priority 2.5: Create Validation Edges (Guidance → Guidance-for-Guidance)**

- [ ] `e:validation:persona-guidance:guidance`
- [ ] `e:validation:purpose-guidance:guidance`
- [ ] `e:validation:protocol-guidance:guidance`
- [ ] `e:validation:system_prompt-guidance:guidance`
- [ ] Perform quality assessment, document in edges
- [ ] Verify all 4 validation edges

**Priority 2.6: Create Assurance Faces**

- [ ] `f:assurance:persona` (spec assurance)
- [ ] `f:assurance:persona-guidance` (guidance assurance)
- [ ] `f:assurance:purpose`
- [ ] `f:assurance:purpose-guidance`
- [ ] `f:assurance:protocol`
- [ ] `f:assurance:protocol-guidance`
- [ ] `f:assurance:system_prompt`
- [ ] `f:assurance:system_prompt-guidance`
- [ ] Verify all 8 assurance faces

**Success Criteria:**
- All PPP specs have complete assurance triangles
- All PPP guidances have complete assurance triangles
- All edges verify successfully
- All faces verify successfully

**Estimated Time:** 4-5 hours

---

### Phase 3: Complete Existing Document Assurance ⏳

**Goal:** Ensure all existing spec-guidance pairs have complete assurance

**Current Pairs Needing Completion:**

- [ ] spec-for-chart ↔ guidance-for-charts (check if complete)
- [ ] spec-for-assurance-audits ↔ guidance-for-assurance-audits (check if complete)
- [ ] Any other spec-guidance pairs identified in Phase 0

**For Each Incomplete Pair:**

- [ ] Create coupling edge if missing
- [ ] Create verification edge (spec → spec-for-spec) if missing
- [ ] Create validation edge (spec → guidance-for-spec) if missing
- [ ] Create verification edge (guidance → spec-for-guidance) if missing
- [ ] Create validation edge (guidance → guidance-for-guidance) if missing
- [ ] Create assurance face for spec
- [ ] Create assurance face for guidance
- [ ] Verify all edges and faces

**Success Criteria:**
- Every spec has a coupled guidance
- Every spec has complete assurance triangle
- Every guidance has complete assurance triangle
- Assurance network is fully connected

**Estimated Time:** 3-4 hours

---

### Phase 4: Doc-Kit Pattern Completion ⏳

**Goal:** Establish doc-kit registry as organizational layer

**Priority 4.1: Complete Persona Doc-Kit**

- [ ] Convert `workshop/input-docs/vv_research/persona/persona_example.yml` to markdown
- [ ] Place as `00_vertices/example-persona.md` or similar
- [ ] Create `e:verification:example-persona:persona`
- [ ] Create `e:validation:example-persona:persona`
- [ ] Update `f:doc_kit:persona` with actual edge IDs
- [ ] Update `f:doc_kit:persona` status to COMPLETE
- [ ] Verify doc-kit face

**Priority 4.2: Create Additional Doc-Kits**

Choose 2-3 more to establish pattern:

- [ ] `f:doc_kit:purpose` (if purpose example exists/can be created)
- [ ] `f:doc_kit:spec` (using spec-for-spec as example)
- [ ] `f:doc_kit:guidance` (using guidance-for-guidance as example)

For each:
- [ ] Identify/create example document
- [ ] Create verification edge (example → spec)
- [ ] Create validation edge (example → guidance)
- [ ] Create doc-kit face
- [ ] Verify doc-kit face

**Priority 4.3: Create Doc-Kit Registry Chart**

- [ ] Create `charts/doc-kit-registry/doc-kit-registry.md`
- [ ] List all doc-kit faces as vertices
- [ ] Document purpose: navigation/discovery for document types
- [ ] Export and visualize
- [ ] Verify chart

**Success Criteria:**
- At least 3-4 complete doc-kits
- Doc-kit registry chart created and verified
- Pattern clearly demonstrated

**Estimated Time:** 3-4 hours

---

### Phase 5: Testing and Validation ⏳

**Goal:** Ensure all automated tests pass

**Priority 5.1: Update Test Expectations**

- [ ] Review all test files in `tests/`
- [ ] Update to expect new document types (persona, purpose, protocol, system_prompt)
- [ ] Update to expect new criteria in validations (Obsidian, ref/referent)
- [ ] Update fixture paths if changed in Phase 1

**Priority 5.2: Run Full Test Suite**

- [ ] Run `python tests/run_tests.py`
- [ ] Document any failures
- [ ] Fix issues
- [ ] Re-run until all pass

**Priority 5.3: Create New Tests if Needed**

- [ ] Test for compositional spec pattern (system_prompt dependencies)
- [ ] Test for doc-kit face pattern
- [ ] Test for complete assurance triangles
- [ ] Test for Obsidian compatibility criterion
- [ ] Test for reference/referent clarity criterion

**Priority 5.4: Manual Verification Pass**

- [ ] Verify ALL vertices: `for f in 00_vertices/*.md; do python scripts/verify_template_based.py "$f" || echo "FAIL: $f"; done`
- [ ] Verify ALL edges: `for f in 01_edges/*.md; do python scripts/verify_template_based.py "$f" || echo "FAIL: $f"; done`
- [ ] Verify ALL faces: `for f in 02_faces/*.md; do python scripts/verify_template_based.py "$f" || echo "FAIL: $f"; done`
- [ ] Verify ALL charts: `find charts -name "*.md" -exec python scripts/verify_chart.py {} \; | grep -i fail`

**Success Criteria:**
- All automated tests pass
- All documents verify successfully
- No verification errors anywhere

**Estimated Time:** 2-3 hours

---

### Phase 5.5: UX Test - Build Organization Chart ⏳

**Goal:** Use newly tested infrastructure to build the originally scoped organization chart demo - test how easy it is to build, analyze, and visualize a simple complex

**Reference:** See `workshop/development-plan.md` Phase 3 for original scope

**Priority 5.5.1: Create Organization Chart Elements**

Based on original plan:

**Vertices - Staff (extends individual extends actor):**
- [ ] `00_vertices/staff-alice.md`
- [ ] `00_vertices/staff-bob.md`
- [ ] `00_vertices/staff-carol.md`

**Vertices - Teams (extends group extends actor):**
- [ ] `00_vertices/team-frontend.md`
- [ ] `00_vertices/team-backend.md`

**Vertices - Roles (extends property):**
- [ ] `00_vertices/role-lead.md`
- [ ] `00_vertices/role-developer.md`
- [ ] `00_vertices/role-reviewer.md`

**Edges - Qualified (individual → role):**
- [ ] `01_edges/qualified-alice-lead.md`
- [ ] `01_edges/qualified-alice-developer.md`
- [ ] `01_edges/qualified-bob-developer.md`
- [ ] `01_edges/qualified-bob-reviewer.md`
- [ ] `01_edges/qualified-carol-developer.md`

**Edges - Member (individual → team):**
- [ ] `01_edges/member-alice-frontend.md`
- [ ] `01_edges/member-bob-backend.md`
- [ ] `01_edges/member-carol-frontend.md`

**Edges - Includes (team → role):**
- [ ] `01_edges/includes-frontend-lead.md`
- [ ] `01_edges/includes-frontend-developer.md`
- [ ] `01_edges/includes-backend-developer.md`
- [ ] `01_edges/includes-backend-reviewer.md`

**Faces - Role Assignments:**
- [ ] `02_faces/role-assignment-alice-frontend-lead.md`
- [ ] `02_faces/role-assignment-alice-frontend-developer.md`
- [ ] `02_faces/role-assignment-carol-frontend-developer.md`
- [ ] **Deliberate hole:** No role-assignment-bob-backend-reviewer (demonstrates topological gap detection)

**Priority 5.5.2: Create Organization Charts**

- [ ] `charts/org-chart-frontend/org-chart-frontend.md` (Frontend team structure)
- [ ] `charts/org-chart-backend/org-chart-backend.md` (Backend team - with hole)
- [ ] `charts/org-chart-program/org-chart-program.md` (Combined organization)

**Priority 5.5.3: Test Workflow**

- [ ] Verify all elements using verify_template_based.py
- [ ] Export charts to JSON using export_chart_direct.py
- [ ] Visualize using visualize_chart.py
- [ ] Confirm topology.py detects the hole at bob-backend-reviewer
- [ ] Test that organization chart constraints can be checked (all requirements filled)

**Priority 5.5.4: Document UX Observations**

Create `workshop/output_logs/ux-test-organization-chart.md`:
- [ ] Document time taken to create all elements
- [ ] Note any friction points in the workflow
- [ ] Identify any missing templates or unclear patterns
- [ ] Record whether tools were intuitive
- [ ] Note any error messages that were unclear
- [ ] Assess whether verification/validation loop is smooth
- [ ] Document what worked well
- [ ] List improvements for future users

**Success Criteria:**
- All organization chart elements created and verified
- Charts export and visualize successfully
- Topological hole correctly detected
- UX observations documented
- Clear understanding of end-user workflow
- Confidence that pattern is reusable

**Estimated Time:** 2-3 hours

---

### Phase 6: Documentation and Polish ⏳

**Goal:** Make repository presentable and usable

**Priority 6.1: Update README**

- [ ] Document compositional spec pattern
- [ ] Document doc-kit pattern
- [ ] Document PPP framework
- [ ] Update examples
- [ ] Update getting started guide
- [ ] Add quick reference for document types

**Priority 6.2: Create Navigation Docs**

- [ ] Create `DOCUMENT_TYPES.md` listing all types with doc-kit links
- [ ] Create `PATTERNS.md` documenting key patterns (assurance triangle, compositional specs, doc-kits)
- [ ] Update `VERIFICATION_TOOLS_CHECKLIST.md` if needed
- [ ] Create `CONTRIBUTING.md` with workflow guidance

**Priority 6.3: Clean Up Session Logs**

- [ ] Review all files in `workshop/output_logs/`
- [ ] Ensure 2025-12-27 logs are complete
- [ ] Add index file: `workshop/output_logs/INDEX.md`
- [ ] Archive old/obsolete logs if any

**Priority 6.4: Audit Metadata**

- [ ] Check all timestamps are reasonable
- [ ] Check all `created` and `modified` dates
- [ ] Check all `version` fields (should be 1.0.0 for stable)
- [ ] Check all `assurer` and `maintainer` fields
- [ ] Ensure consistency

**Priority 6.5: Final Cleanup**

- [ ] Remove any temporary files
- [ ] Remove any `.DS_Store` or OS-specific files
- [ ] Check `.gitignore` is comprehensive
- [ ] Clean up any debug output files
- [ ] Check for any TODOs or FIXMEs in code

**Success Criteria:**
- Documentation is clear and complete
- Repository structure is well-explained
- Contribution process is documented
- No cruft or temporary files

**Estimated Time:** 2-3 hours

---

### Phase 7: Final Validation ⏳

**Goal:** Confirm repository is ready to share

**Checklist:**

- [ ] All tests pass (`python tests/run_tests.py`)
- [ ] All vertices verify (`scripts/verify_all_vertices.sh` or manual loop)
- [ ] All edges verify (`scripts/verify_all_edges.sh` or manual loop)
- [ ] All faces verify (`scripts/verify_all_faces.sh` or manual loop)
- [ ] All charts verify and export successfully
- [ ] README is accurate and helpful
- [ ] CONTRIBUTING guide is clear
- [ ] No broken internal links
- [ ] No TODO placeholders in production files
- [ ] Git status is clean (no uncommitted changes or untracked important files)
- [ ] All session logs are complete

**Final Smoke Tests:**

```bash
# Test that someone could clone and immediately verify
git status
python tests/run_tests.py
python scripts/verify_template_based.py 00_vertices/spec-for-spec.md
python scripts/verify_template_based.py 00_vertices/spec-for-persona.md
python scripts/verify_chart.py charts/boundary-complex/boundary-complex.md
```

**Success Criteria:**
- All checks pass
- Repository ready to share publicly
- Confidence in stability

**Estimated Time:** 1-2 hours

---

## Summary

### Total Estimated Time: 18-26 hours

### Phase Breakdown:
- **Phase 0:** Baseline Testing - 0.5 hours
- **Phase 1:** Fix Core Infrastructure - 2-3 hours
- **Phase 2:** Complete PPP Framework Assurance - 4-5 hours
- **Phase 3:** Complete Existing Document Assurance - 3-4 hours
- **Phase 4:** Doc-Kit Pattern Completion - 3-4 hours
- **Phase 5:** Testing and Validation - 2-3 hours
- **Phase 6:** Documentation and Polish - 2-3 hours
- **Phase 7:** Final Validation - 1-2 hours

### Priority Order:
1. **Critical:** Phase 0, 1, 5 (baseline, fix core, test) - Must do first
2. **High:** Phase 2, 3 (complete assurance network) - Core functionality
3. **Medium:** Phase 4 (doc-kits) - Nice organizational layer
4. **Polish:** Phase 6, 7 (docs, final validation) - Makes it shareable

### Can Be Done in Parallel (if multiple people):
- Phase 2 and Phase 3 (different assurance triangles)
- Phase 4 and Phase 6 (doc-kits and documentation)

### Minimum Viable for Sharing:
Phases 0, 1, 2, 3, 5, 7 (skip Phase 4 doc-kits and Phase 6 polish if time-constrained)

---

## Notes

- This plan assumes working alone
- Parallelization possible with team
- Each phase builds on previous
- Can pause between phases for review
- Document blockers/issues as they arise
- Update this plan as you learn more

---

## Future Work (Post-Cleanup)

### Comprehensive Guide for Creating New Document Types

**Priority:** Documentation / Educational
**Estimated Time:** 4-6 hours
**Dependencies:** Phases 0-7 complete (need stable examples to reference)

**Description:**

Write a comprehensive, step-by-step guide for creating new document types in the knowledge complex framework. This guide should serve as both documentation and tutorial, demonstrating the complete meta-pattern of "creating infrastructure for a new type."

**Required Coverage:**

1. **Create Spec Document** - Define structural requirements for the new type
   - What fields are required
   - What sections must be present
   - How to write clear, testable requirements
   - Examples from existing specs

2. **Create Guidance Document** - Define quality criteria for the new type
   - What quality dimensions to assess
   - How to write actionable quality criteria
   - How to define assessment levels (Excellent/Good/Needs Improvement)
   - Examples from existing guidances

3. **Create Template** - Create template in `templates/` directory for instances
   - Where to place it (00_vertices, 01_edges, 02_faces)
   - How to structure it to match the spec
   - What placeholders to use
   - Testing the template

4. **Create Example Document** - Demonstrate the type with a real instance
   - How to create an example that satisfies both spec and guidance
   - Where to place examples
   - How to use the example in documentation

5. **Create Coupling Edge** - Link spec and guidance
   - Why coupling is needed
   - How to create the coupling edge
   - How to verify it

6. **Create Verification Edge** - Prove structural compliance
   - From example to spec
   - How to run verification
   - How to document verification results in the edge
   - What to do when verification fails

7. **Create Validation Edge** - Prove quality achievement
   - From example to guidance
   - How to perform quality assessment
   - How to document validation results with proper accountability
   - Manual vs llm-assisted vs automated methods

8. **Create Assurance Face** - Complete the assurance triangle
   - What an assurance face represents
   - How to assess triangle coherence
   - How to write accountability statements
   - When to mark status as ASSURED

9. **Create Doc-Kit Face** - Encapsulate the complete pattern
   - What a doc-kit contains (spec, guidance, coupling, template, example, edges, assurance)
   - How to create the doc-kit face
   - How doc-kits support discoverability
   - Reference vs registry patterns

10. **Add to Doc-Kit Registry Chart** - Enable discoverability
    - How to add the doc-kit face to the registry chart
    - How to add all component simplices
    - How charts support navigation and visualization
    - Testing the complete registry

**Deliverables:**

- [ ] `docs/guides/creating-new-document-types.md` - Main guide
- [ ] `docs/guides/examples/` - Directory with example walkthrough (create a trivial type from scratch)
- [ ] Templates for each artifact type in the guide
- [ ] Checklist for "have I completed all steps?"
- [ ] Troubleshooting section for common issues

**Success Criteria:**

- Someone unfamiliar with the framework can follow the guide to create a new document type
- All 10 steps clearly explained with examples
- Demonstrates the complete meta-pattern
- Explains *why* each piece is needed, not just *how*
- Guide validated by creating a new type as demonstration

**Value:**

This guide is critical for framework extensibility. It documents the "knowledge complex development process" and enables contributors to add new types without needing to reverse-engineer patterns from existing code. It makes the framework teachable and maintainable.

## Progress Tracking

Use checkboxes in each phase. Mark `⏳` as `✅` when complete.

**Current Phase:** Phase 0 (Baseline Testing)
**Last Updated:** 2025-12-27
