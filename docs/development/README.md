# Development Documentation

This directory contains technical documentation for developers working on the knowledge complex infrastructure, test suite, and template generation system.

## Available Documentation

### [Test Coverage](test-coverage.md)
Complete documentation of the test suite architecture and 100% critical functionality coverage. Includes:
- Test suite organization (10 test suites, 76+ tests)
- Coverage analysis for all critical components
- Test execution and CI/CD integration
- How to add new tests

### [Template Generation Design](template-generation-design.md)
Technical design of the template generation system. Covers:
- Template generation architecture (SpecParser, TemplateGenerator)
- How templates are generated from specs
- Template freshness checking
- Bugs fixed during development
- Examples of complex type handling

### [Repository Cleanup Plan](REPOSITORY-CLEANUP-PLAN.md)
Strategic plan for organizing the repository to serve dual purposes (template + learning resource). Details:
- Repository purpose and success criteria
- Asset inventory and problems identified
- Phased cleanup strategy
- Documentation reorganization approach

### [Archive](archive/)
Historical development documentation preserved for reference:
- Template generation phase documentation
- Test coverage analysis and results
- Specs vs templates analysis
- Test suite fixes

## Development Workflows

### Running Tests
```bash
# Run all tests
python tests/run_tests.py

# Run specific test suite
python tests/test_parse.py
python tests/test_verify_chart.py
python tests/test_topology.py

# Run with pytest
python -m pytest tests/ -v
```

### Verifying Documents
```bash
# Verify single document against template
python scripts/verify_template_based.py <file> --templates templates

# Build cache and verify all documents
python scripts/build_cache.py

# Check template freshness
python scripts/generate_all_templates.py --check
```

### Template Generation
```bash
# Generate all templates from specs
python scripts/generate_all_templates.py

# Generate specific template
python scripts/generate_template.py <spec-file>
```

## Contributing

When contributing to the knowledge complex infrastructure:

1. **Test First**: Write tests before implementing features
2. **Verify Templates**: Ensure all documents pass `verify_template_based.py`
3. **Update Docs**: Keep documentation current with changes
4. **Run Full Suite**: Verify all 10 test suites pass before committing

See [test-coverage.md](test-coverage.md) for detailed testing guidelines.

## Related Documentation

- **Scripts Reference**: [scripts/README.md](../../scripts/README.md) - Script usage and workflows (to be created)
- **Learning Path**: [docs/learning/](../learning/) - Understanding the system you're developing
- **Concepts**: [docs/concepts/](../concepts/) - Theoretical foundation

---

**For New Contributors**: Start by reading [template-generation-design.md](template-generation-design.md) and [test-coverage.md](test-coverage.md) to understand the core infrastructure.
