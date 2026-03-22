# AAA Docware

**A typed simplicial complex framework for document verification, validation, and assurance.**

AAA (Assurances, Audits & Accountability) enables test-driven document development where collections of documents are assembled according to the rules of typed simplicial complexes — treating them as "greater than the sum of their parts."

## Key Ideas

- **Documents are vertices** (0-simplices) in a typed complex
- **Verification, validation, and coupling are edges** (1-simplices) connecting documents
- **Assurance triangles are faces** (2-simplices) representing complete quality attestation
- **Human accountability** is structurally required for validation judgments

## Quick Start

```bash
pip install aaa-docware

aaa init my-project
cd my-project
aaa build
aaa audit charts/foundation
```

## The Assurance Triangle

Every assured document requires three edges forming a closed triangle:

1. **Verification edge** — document passes structural checks against spec
2. **Coupling edge** — spec is linked to corresponding guidance
3. **Validation edge** — document assessed against guidance (requires human approver)

This structure ensures that no document can be "assured" without both automated verification and human judgment.

## Learn More

- [Installation](getting-started/installation.md) — install and set up
- [Quick Start](getting-started/quickstart.md) — create your first knowledge complex
- [CLI Reference](cli-reference.md) — all `aaa` commands
- [Contributing](https://github.com/BlockScience/assurances-audits-accountability/blob/main/CONTRIBUTING.md) — development guide
