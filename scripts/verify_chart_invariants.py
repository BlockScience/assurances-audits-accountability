#!/usr/bin/env python3
"""
Verify chart counting invariants for assured-signed complexes.

This script checks two key invariants:
1. Number of assurances == Number of signatures (all assurances are signed)
2. Number of assurances == Number of documents (all documents are assured)

The V-F=1 invariant comes from:
- V = #documents + #signers + #root
- F = #assurances + #signatures
- If #assurances = #documents and #signatures = #assurances, then:
  V - F = (#docs + #signers + 1) - (#assurances + #signatures)
        = (#docs + #signers + 1) - (2 * #docs)
        = #signers + 1 - #docs

For the standard case with 1 root and signers not being documents:
  V - F depends on the ratio of signers to documents.

Usage:
    python scripts/verify_chart_invariants.py <chart.json>
"""

import json
import sys
from pathlib import Path


def load_chart(chart_path: str) -> dict:
    """Load chart JSON file."""
    with open(chart_path) as f:
        return json.load(f)


def analyze_chart(chart: dict) -> dict:
    """Analyze chart for counting invariants."""
    faces = chart.get("elements", {}).get("faces", [])
    vertices = chart.get("elements", {}).get("vertices", [])

    # Count face types - include both standard assurance (f:) and boundary assurance (b2:)
    assurance_faces = [f for f in faces if f.get("type") in ("face/assurance", "face/b2")]
    signature_faces = [f for f in faces if f.get("type") == "face/signature"]

    # Count vertex types
    signer_vertices = [v for v in vertices if v.get("type") == "vertex/signer"]
    root_vertices = [v for v in vertices if v.get("type") == "vertex/b0" or v.get("id", "").startswith("b0:")]
    # Documents are specs, guidances, and docs - anything that needs assurance
    doc_vertices = [v for v in vertices
                    if v.get("type") not in ("vertex/signer", "vertex/b0")
                    and not v.get("id", "").startswith("b0:")]

    # Get the target docs for each assurance
    # For b2 faces, the target is the last vertex (not root)
    # For standard assurance faces, the target is the first vertex
    assurance_targets = set()
    for f in assurance_faces:
        verts = f.get("vertices", [])
        if verts:
            if f.get("type") == "face/b2":
                # b2 faces: root is first, target doc is last
                target = verts[-1] if not verts[-1].startswith("b0:") else verts[-2]
            else:
                target = verts[0]
            assurance_targets.add(target)

    # Get the target docs for each signature (first vertex in the face)
    signature_targets = set()
    for f in signature_faces:
        verts = f.get("vertices", [])
        if verts:
            signature_targets.add(verts[0])

    return {
        "total_vertices": len(vertices),
        "total_faces": len(faces),
        "assurance_faces": len(assurance_faces),
        "signature_faces": len(signature_faces),
        "signer_vertices": len(signer_vertices),
        "root_vertices": len(root_vertices),
        "doc_vertices": len(doc_vertices),
        "assurance_targets": assurance_targets,
        "signature_targets": signature_targets,
        "signer_ids": [v.get("id") for v in signer_vertices],
        "root_ids": [v.get("id") for v in root_vertices],
        "doc_ids": [v.get("id") for v in doc_vertices],
    }


def check_invariants(analysis: dict) -> list:
    """Check counting invariants and return list of issues."""
    issues = []

    # Invariant 1: assurance_faces == signature_faces (all assurances are signed)
    if analysis["assurance_faces"] != analysis["signature_faces"]:
        issues.append({
            "invariant": "#assurances == #signatures",
            "status": "FAIL",
            "expected": analysis["assurance_faces"],
            "actual": analysis["signature_faces"],
            "message": f"Expected {analysis['assurance_faces']} signatures to match {analysis['assurance_faces']} assurances, got {analysis['signature_faces']}"
        })
    else:
        issues.append({
            "invariant": "#assurances == #signatures",
            "status": "PASS",
            "expected": analysis["assurance_faces"],
            "actual": analysis["signature_faces"],
            "message": f"All {analysis['assurance_faces']} assurances have matching signatures"
        })

    # Invariant 2: number of unique assured documents == number of document vertices
    # (every document has at least one assurance)
    num_assured_docs = len(analysis["assurance_targets"])
    if num_assured_docs != analysis["doc_vertices"]:
        issues.append({
            "invariant": "#assured_docs == #documents",
            "status": "FAIL",
            "expected": analysis["doc_vertices"],
            "actual": num_assured_docs,
            "message": f"Expected {analysis['doc_vertices']} documents to be assured, got {num_assured_docs}"
        })
    else:
        issues.append({
            "invariant": "#assured_docs == #documents",
            "status": "PASS",
            "expected": analysis["doc_vertices"],
            "actual": num_assured_docs,
            "message": f"All {analysis['doc_vertices']} documents have assurance faces"
        })

    # Check which assurances are missing signatures
    unsigned_assurances = analysis["assurance_targets"] - analysis["signature_targets"]
    if unsigned_assurances:
        issues.append({
            "invariant": "all assurances signed",
            "status": "FAIL",
            "unsigned": sorted(list(unsigned_assurances)),
            "message": f"Found {len(unsigned_assurances)} documents with assurance but no signature"
        })

    # Check which documents lack assurance
    doc_set = set(analysis["doc_ids"])
    unassured_docs = doc_set - analysis["assurance_targets"]
    if unassured_docs:
        issues.append({
            "invariant": "all documents assured",
            "status": "FAIL",
            "unassured": sorted(list(unassured_docs)),
            "message": f"Found {len(unassured_docs)} documents without assurance"
        })

    return issues


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/verify_chart_invariants.py <chart.json>")
        sys.exit(1)

    chart_path = sys.argv[1]
    if not Path(chart_path).exists():
        print(f"Error: File not found: {chart_path}")
        sys.exit(1)

    chart = load_chart(chart_path)
    analysis = analyze_chart(chart)
    issues = check_invariants(analysis)

    print(f"\n=== Chart Invariant Verification ===")
    print(f"Chart: {chart.get('name', chart_path)}")
    print(f"\n--- Element Counts ---")
    print(f"  Vertices:          {analysis['total_vertices']}")
    print(f"    - Root:          {analysis['root_vertices']} ({analysis['root_ids']})")
    print(f"    - Signers:       {analysis['signer_vertices']} ({analysis['signer_ids']})")
    print(f"    - Documents:     {analysis['doc_vertices']}")
    print(f"  Faces:             {analysis['total_faces']}")
    print(f"    - Assurance:     {analysis['assurance_faces']}")
    print(f"    - Signature:     {analysis['signature_faces']}")

    print(f"\n--- Invariant Checks ---")
    all_pass = True
    for issue in issues:
        status = issue["status"]
        if status == "FAIL":
            all_pass = False
            print(f"  [{status}] {issue['invariant']}")
            print(f"         {issue['message']}")
            if "unsigned" in issue:
                for u in issue["unsigned"]:
                    print(f"           - {u}")
            if "unassured" in issue:
                for u in issue["unassured"]:
                    print(f"           - {u}")
        else:
            print(f"  [{status}] {issue['invariant']}: {issue['message']}")

    print(f"\n--- Summary ---")
    if all_pass:
        print("  All invariants satisfied.")
        sys.exit(0)
    else:
        print("  Some invariants failed. See above for details.")
        sys.exit(1)


if __name__ == "__main__":
    main()
