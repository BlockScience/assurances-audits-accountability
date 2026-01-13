# RBAC Domain Pack - Role-Based Access Control

## Overview

The RBAC pack provides infrastructure for human accountability in knowledge complexes. It defines signer and role types, along with the edges and faces needed to establish authorization chains.

## Dependencies

- **foundation**: Base ontology and genesis elements

## Vertex Types

| Type | Description |
|------|-------------|
| signer | Named entity that can sign validations |
| role | Named role that conveys authority |

## Edge Types

| Type | Source → Target | Description |
|------|-----------------|-------------|
| signs | signer → doc | Signer attests to validation |
| qualifies | signer → guidance | Signer is qualified to sign |
| has-role | signer → role | Signer holds a role |
| conveys | role → guidance | Role conveys authority |

## Face Types

| Type | Boundary | Description |
|------|----------|-------------|
| signature | validation + qualifies + signs | Human accountability |
| authorization | has-role + conveys + qualifies | Proves qualification |

## Authorization Chain

```
Signer ──has-role──► Role ──conveys──► Guidance
   │                                      │
   └──────────qualifies──────────────────►│
   │                                      │
   └──────────signs──────────────────────►Doc
```

## Domain Rules

### signer_must_qualify
A signer must have a `qualifies` edge to the relevant guidance before signing validations against it.

### qualification_requires_role
Qualifies edges should be supported by authorization faces proving why the signer is qualified (via role chain).

## Demo Chart

See `charts/demo-authorization-chain.md` for an example multi-step authorization.
