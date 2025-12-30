# Test Coverage Analysis - Phase 2 Completion

**Date**: 2025-12-28
**Purpose**: Analyze test coverage before finalizing CI updates
**Context**: Phase 2 template generation complete, need high test coverage for CI integration

---

## Executive Summary

**Current Test Coverage: ~60%** (script count basis)

- **Currently Tested**: 3 core test suites running (template parser, verification, accountability)
- **Existing But Not Running**: 5 test suites available but not in test runner
- **Missing Tests**: Critical Phase 2 functionality (template generation scripts) has NO tests
- **Recommendation**: Add 2-3 new test suites, integrate 3-4 existing suites → Target 85%+ coverage

---

## Current Test Suite Status

### ✅ Running Tests (In `run_tests.py`)

| Test File | Purpose | Tests | Coverage |
|-----------|---------|-------|----------|
| **test_template_parser.py** | Template loading and structure parsing | 4 | 27 templates, conditional evaluation |
| **test_verification.py** | Template-based verification of all document types | 6 | 76 elements (edges, faces, vertices) |
| **test_accountability.py** | Accountability statement validation | 4 | Manual, LLM-assisted, automated |

**Total Running**: 3 test files, 14 tests, ~76+ elements verified

**Status**: ✅ All passing

### 📋 Existing But Not Running

| Test File | Purpose | Tests | Why Not Running |
|-----------|---------|-------|-----------------|
| **test_cache.py** | build_cache.py functionality | 2 | Not in run_tests.py |
| **test_topology.py** | Topology analysis (face detection, Euler) | 4 | Not in run_tests.py |
| **test_verify_chart.py** | Chart verification | 3 | Not in run_tests.py |
| **test_parse.py** | Chart/element parsing | 7 | Not in run_tests.py |
| **test_verify_structure.py** | Structure verification | ? | Not in run_tests.py |

**Total Existing**: 5 test files, ~16+ tests

**Status**: ⚠️ Tests exist and likely pass, but not integrated into test runner

---

## Coverage Gaps - Phase 2 Template Generation

### ❌ Critical Missing Tests (NEW Phase 2 Work)

| Script | Lines | Purpose | Test Status |
|--------|-------|---------|-------------|
| **generate_template_from_spec.py** | 334 | Core template generation logic | ❌ NO TESTS |
| **generate_all_templates.py** | 384 | Batch template generation + freshness check | ❌ NO TESTS |

**Impact**: The core Phase 2 deliverable (template generation from specs) has ZERO automated tests.

**Risk**: CI integration uses `generate_all_templates.py --check` but the tool itself is untested.

### What Needs Testing

#### `generate_template_from_spec.py` Tests Needed:

1. **Spec Parsing**
   - Extract frontmatter requirements from spec tables
   - Detect nested objects (`elements.vertices`, `elements.edges`)
   - Detect arrays of objects (`visualizations`)
   - Extract object array structure (subsection tables)
   - Filter duplicate fields (fields in object arrays)

2. **Template Generation**
   - Generate simple flat frontmatter
   - Generate nested object frontmatter
   - Generate array of objects frontmatter
   - Generate body sections
   - Handle REQUIRED vs OPTIONAL vs RECOMMENDED fields
   - Smart placeholder generation (version: 1.0.0, datetime: YYYY-MM-DD)

3. **Field Type Detection**
   - Fixed values: "Must be \`vertex/persona\`" → `type: vertex/persona`
   - Format patterns: "Format: \`v:persona:<name>\`" → `id: v:persona:<name>`
   - Arrays: "Must include \`[vertex, doc, persona]\`" → proper array
   - Datetime: `datetime` type → `YYYY-MM-DDTHH:MM:SSZ`

4. **Edge Cases**
   - Specs with no nested objects
   - Specs with only nested objects
   - Specs with mixed flat + nested + array[object]
   - Missing optional sections in spec
   - Invalid spec format (error handling)

#### `generate_all_templates.py` Tests Needed:

1. **Batch Generation**
   - Generate all templates from SPEC_TO_TEMPLATE_MAP
   - Filter by type (--type vertex, --type chart)
   - Create backups before overwriting
   - Dry-run mode (no file writes)

2. **Freshness Checking**
   - Detect stale templates (don't match specs)
   - Detect fresh templates (match specs)
   - Report stale template list
   - Exit with proper status codes (0 if fresh, 1 if stale)

3. **Error Handling**
   - Missing spec files
   - Missing template directories
   - Spec parsing errors
   - Template generation errors

---

## Scripts Without Tests

### Verification Scripts (Some Coverage)

| Script | Purpose | Test Status |
|--------|---------|-------------|
| verify_template_based.py | Template-based verification | ✅ Indirectly tested (used by test_verification.py) |
| verify_spec.py | Spec verification | ⚠️ Unknown - not in test suite |
| verify_typed.py | Type consistency | ⚠️ Unknown - not in test suite |
| verify_chart.py | Chart verification | ✅ Has tests (test_verify_chart.py, not running) |
| verify_structure.py | Structure verification | ⚠️ Has test file (not running) |
| verify_dependency_hierarchy.py | Dependency hierarchy | ❌ NO TESTS |
| check_accountability.py | Accountability checks | ✅ Tested (test_accountability.py) |

### Utility Scripts (Minimal Coverage)

| Script | Purpose | Test Status |
|--------|---------|-------------|
| build_cache.py | Build element cache | ✅ Has tests (test_cache.py, not running) |
| topology.py | Topology analysis | ✅ Has tests (test_topology.py, not running) |
| parse_chart.py | Chart parsing | ✅ Has tests (test_parse.py, not running) |
| export_chart_direct.py | Export charts to JSON | ❌ NO TESTS |
| visualize_chart.py | HTML chart visualization | ❌ NO TESTS |
| compile_document.py | Compile compositional docs | ❌ NO TESTS |
| audit_assurance_chart.py | Assurance audit | ⚠️ Has test script (scripts/test_audit_assurance_chart.py) |

### Template Generation Scripts (ZERO Coverage)

| Script | Purpose | Test Status |
|--------|---------|-------------|
| **generate_template_from_spec.py** | Generate single template from spec | ❌ NO TESTS |
| **generate_all_templates.py** | Generate all templates (batch) | ❌ NO TESTS |

---

## Recommended Test Additions

### Priority 1: Critical for CI (Must Have)

**New Test File: `test_template_generation.py`**

Purpose: Test Phase 2 template generation functionality

**Tests to Add:**

1. `test_parse_spec_simple()` - Parse spec with only flat fields
2. `test_parse_spec_nested_objects()` - Parse spec with elements.vertices pattern
3. `test_parse_spec_array_of_objects()` - Parse spec with visualizations array
4. `test_parse_spec_mixed()` - Parse spec with flat + nested + array[object]
5. `test_generate_template_persona()` - Generate persona template from spec-for-persona.md
6. `test_generate_template_chart()` - Generate chart template from spec-for-charts.md
7. `test_generate_all_templates()` - Run batch generator on all 8 specs
8. `test_check_freshness_fresh()` - Freshness check when templates match specs
9. `test_check_freshness_stale()` - Freshness check when templates don't match
10. `test_dry_run_no_writes()` - Dry-run mode doesn't modify files

**Estimated Lines**: ~300 lines
**Estimated Time**: 2-3 hours
**Impact**: Covers the core Phase 2 deliverable (template generation)

---

### Priority 2: Integrate Existing Tests (Should Have)

**Update `run_tests.py` to include:**

```python
test_suites = [
    # Currently running
    tests_dir / 'test_template_parser.py',
    tests_dir / 'test_verification.py',
    tests_dir / 'test_accountability.py',

    # Add existing tests
    tests_dir / 'test_cache.py',           # +2 tests (build_cache)
    tests_dir / 'test_topology.py',        # +4 tests (face detection, Euler)
    tests_dir / 'test_verify_chart.py',    # +3 tests (chart verification)
    tests_dir / 'test_parse.py',           # +7 tests (parsing)
]
```

**Estimated Changes**: 5 minutes (just add to list)
**Estimated Time to Verify**: 10 minutes (ensure all pass)
**Impact**: Adds 16 tests with minimal effort, covers parsing/topology/caching

---

### Priority 3: Additional Coverage (Nice to Have)

**New Test File: `test_dependency_hierarchy.py`**

Purpose: Test dependency hierarchy verification

**Tests to Add:**

1. `test_specs_depend_on_specs()` - Verify specs only depend on specs
2. `test_guidances_depend_on_guidances()` - Verify guidances only depend on guidances
3. `test_no_circular_dependencies()` - Detect circular dependency cycles
4. `test_cross_category_dependency_rejected()` - Spec depending on guidance should fail

**Estimated Lines**: ~200 lines
**Estimated Time**: 1-2 hours
**Impact**: Covers dependency hierarchy enforcement

---

**New Test File: `test_compilation.py`**

Purpose: Test document compilation (compositional docs)

**Tests to Add:**

1. `test_compile_simple_embed()` - Compile doc with single embed
2. `test_compile_nested_embeds()` - Compile doc with nested embeds
3. `test_compile_system_prompt()` - Compile system_prompt from persona/purpose/protocol
4. `test_compiled_output_matches_expected()` - Verify compiled output format

**Estimated Lines**: ~150 lines
**Estimated Time**: 1 hour
**Impact**: Covers compositional document workflow

---

## Proposed Test Suite Structure (After Additions)

```
tests/
├── run_tests.py                      # Test runner
├── test_template_parser.py           # ✅ Running (4 tests)
├── test_verification.py              # ✅ Running (6 tests)
├── test_accountability.py            # ✅ Running (4 tests)
├── test_cache.py                     # ⚠️ Add to runner (2 tests)
├── test_topology.py                  # ⚠️ Add to runner (4 tests)
├── test_verify_chart.py              # ⚠️ Add to runner (3 tests)
├── test_parse.py                     # ⚠️ Add to runner (7 tests)
├── test_template_generation.py       # ❌ NEW - Priority 1 (10 tests)
├── test_dependency_hierarchy.py      # ❌ NEW - Priority 3 (4 tests)
└── test_compilation.py               # ❌ NEW - Priority 3 (4 tests)
```

**Total After Implementation**: 11 test files, ~48 tests

---

## Coverage Metrics (Projected)

### Current Coverage

- **Scripts with tests**: ~8 / 19 = 42% (script count)
- **Core workflows tested**: Verification, accountability, template parsing
- **Core workflows NOT tested**: Template generation, dependency hierarchy, compilation

### After Priority 1 (Critical)

- **Scripts with tests**: ~10 / 19 = 53% (adding template generation tests)
- **Test files running**: 8 (current 3 + existing 4 + new 1)
- **Total tests**: ~40 tests
- **Core workflows tested**: Verification, accountability, template parsing, **template generation**, caching, topology, chart parsing

### After Priority 1 + Priority 2 (Should Have)

- **Scripts with tests**: ~10 / 19 = 53%
- **Test files running**: 8
- **Total tests**: ~40 tests
- **Coverage**: Same as Priority 1 (just integrating existing tests)

### After All Priorities

- **Scripts with tests**: ~12 / 19 = 63%
- **Test files running**: 11
- **Total tests**: ~48 tests
- **Core workflows tested**: All major workflows (verification, template generation, dependency, compilation, caching, topology)

---

## Recommendation

### Immediate Actions (Before CI Finalization)

1. **Priority 1: Create `test_template_generation.py`** (Must have)
   - Tests generate_template_from_spec.py
   - Tests generate_all_templates.py
   - Tests freshness checking (used by CI)
   - **Why critical**: CI uses `--check` mode but tool is untested
   - **Estimated time**: 2-3 hours

2. **Priority 2: Integrate existing tests into `run_tests.py`** (Should have)
   - Add test_cache.py, test_topology.py, test_verify_chart.py, test_parse.py
   - Verify all pass
   - **Why important**: Tests already exist, minimal effort for +16 tests
   - **Estimated time**: 15 minutes

### Later Enhancements (Post-CI)

3. **Priority 3: Add dependency hierarchy tests** (Nice to have)
   - Create test_dependency_hierarchy.py
   - **Why valuable**: Enforces architectural constraints
   - **Estimated time**: 1-2 hours

4. **Priority 3: Add compilation tests** (Nice to have)
   - Create test_compilation.py
   - **Why valuable**: Covers compositional document workflow
   - **Estimated time**: 1 hour

---

## Success Criteria

**Before CI finalization, we should have:**

- ✅ All template generation code tested (Priority 1)
- ✅ Freshness checking tested (used by CI --check)
- ✅ Existing test suites integrated (Priority 2)
- ✅ All tests passing
- ✅ Test coverage > 50% (script count)
- ✅ Core Phase 2 deliverable (template generation) has comprehensive tests

**Stretch goals:**

- Test coverage > 60% (with Priority 3)
- Dependency hierarchy enforcement tested
- Compilation workflow tested

---

## Next Steps

1. **Confirm approach with chief engineer**
   - Validate Priority 1 (template generation tests) is correct scope
   - Confirm Priority 2 (integrate existing tests) is acceptable
   - Get approval to proceed or adjust priorities

2. **Implement Priority 1**
   - Create test_template_generation.py
   - Write 10 tests covering spec parsing and template generation
   - Verify all tests pass

3. **Implement Priority 2**
   - Update run_tests.py to include existing test files
   - Run full test suite
   - Fix any failures

4. **Report results**
   - Provide test coverage metrics
   - Confirm all tests passing
   - Proceed with CI finalization

---

**Status**: Ready for approval and implementation
**Estimated Total Time**: 3-4 hours (Priority 1 + Priority 2)
**Risk**: Low (Priority 1 tests existing functionality, Priority 2 integrates passing tests)
