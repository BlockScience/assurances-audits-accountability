# Knowledge Complex Test Suite

Comprehensive regression tests to ensure the knowledge complex remains valid as it evolves.

## Running Tests

### Run all tests

```bash
python tests/run_tests.py
```

### Run individual test suites

```bash
# Template parser tests
python tests/test_template_parser.py

# Verification tests
python tests/test_verification.py

# Accountability tests
python tests/test_accountability.py
```

## Test Suites

### test_template_parser.py

Tests the template parsing functionality that extracts requirements from templates.

**Tests:**
- Template loading (15 templates)
- Validation edge template parsing (frontmatter, body, tags, conditional requirements)
- Assurance face template parsing (frontmatter extraction from template yaml)
- Conditional requirement evaluation

**Coverage:**
- Template discovery and loading
- Frontmatter requirement extraction from tables
- Frontmatter requirement extraction from template yaml
- Body section requirement extraction
- Tag requirement extraction
- Conditional logic (REQUIRED if/when/for)

### test_verification.py

Tests template-based verification of all boundary complex elements.

**Tests:**
- All validation edges (4 edges, 19-23 checks each)
- All verification edges (4 edges, 18 checks each)
- All coupling edges (2 edges, 17 checks each)
- All assurance faces (4 faces, 8 checks each)
- All foundational vertices (4 vertices, 7 checks each)
- Conditional requirements (llm-assisted and automated methods)

**Coverage:**
- Template-based verification engine
- Frontmatter field validation
- Expected value checking
- Conditional requirement evaluation
- Body section presence
- Tag requirements
- Type checking with datetime handling

### test_accountability.py

Tests the accountability enforcement system for validation and assurance.

**Tests:**
- Manual validation accountability (validator field)
- LLM-assisted validation accountability (human_approver field)
- Automated validation accountability (human_approver field)
- Username matching strategies (exact, contains, substring)

**Coverage:**
- Accountability field extraction
- Committer/approver matching
- Rejection of unauthorized commits
- Multiple username formats

## CI/CD Integration

### GitHub Actions Workflows

**test.yml** - Runs on every PR and push to main/dev
- Executes full test suite
- Comments on PR if tests fail
- Must pass before merge (configure as required status check)

**validate-accountability.yml** - Validates accountability on commits
- Checks validation edges are committed by accountable party
- Enforces human_approver for llm-assisted/automated
- Must pass before merge (configure as required status check)

### Branch Protection Setup

To enforce tests in PRs:

1. Go to: `https://github.com/OWNER/REPO/settings/branches`
2. Add branch protection rule for `main`:
   - ☑ Require status checks to pass before merging
   - ☑ Require branches to be up to date before merging
   - Select: `test` (from test.yml workflow)
   - Select: `check-accountability` (from validate-accountability.yml)
3. Save

## Adding New Tests

### For new element types

1. Add template to `templates/`
2. Verification tests automatically cover new type
3. Add specific test if type has unique behavior

### For new features

1. Add test to appropriate suite:
   - Template parsing → `test_template_parser.py`
   - Verification → `test_verification.py`
   - Accountability → `test_accountability.py`
2. Run `python tests/run_tests.py` to verify
3. Commit with passing tests

## Test Philosophy

**Regression prevention**: Tests lock in current behavior so changes don't break existing functionality.

**Template-driven**: Tests verify against templates, not hardcoded expectations. When templates change, verification behavior changes automatically.

**Comprehensive coverage**: All boundary complex elements tested. New elements tested automatically through template-based approach.

**Fast feedback**: Tests run in < 5 seconds locally, enabling rapid iteration.

**CI enforcement**: Tests must pass before merge, preventing broken states from entering main/dev branches.

## Debugging Test Failures

### Template parser failures

Check:
- Template file exists in `templates/`
- Frontmatter table format matches expected pattern
- Template yaml has correct structure
- Inline comments use REQUIRED keyword correctly

### Verification failures

Check:
- Element has correct `type` field
- All required frontmatter fields present
- Required body sections present (exact header match)
- Tags include full inheritance chain
- Conditional requirements met (e.g., llm_model when llm-assisted)

### Accountability failures

Check:
- Frontmatter has `validator` (manual) or `human_approver` (llm-assisted/automated)
- Username matches Git committer or GitHub actor
- Validation method is one of: manual, llm-assisted, automated
- For llm-assisted: both `llm_model` and `human_approver` present

## Test Statistics

As of initial implementation:
- **3 test suites** covering all major systems
- **14 individual tests** with comprehensive assertions
- **~100 individual assertions** across all tests
- **< 5 seconds** total execution time
- **100% pass rate** on boundary complex

The test suite covers:
- 15 template types
- 4 validation edges (all methods: manual, llm-assisted, automated)
- 4 verification edges
- 2 coupling edges
- 4 assurance faces (all methods: manual, llm-assisted, automated)
- 4 foundational vertices
- Conditional requirement logic
- Accountability enforcement
