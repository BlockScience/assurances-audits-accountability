#!/usr/bin/env python3
"""
Hodge decomposition and edge PageRank analysis for simplicial complexes.

This module provides tools for:
- Computing edge Laplacians
- Personalized PageRank on edges
- Hodge decomposition (gradient, circular, harmonic components)
- Edge influence measures (spread, absolute influence, penetration, relative influence)

Usage:
    python scripts/hodge_analysis.py charts/chart-types-audit/chart-types-audit.json
    python scripts/hodge_analysis.py charts/boundary-complex/boundary-complex.json --top 5
"""

import sys
import json
import numpy as np
import scipy.sparse as sp
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass


@dataclass
class HodgeDecomposition:
    """Results from Hodge decomposition of an edge vector."""
    gradient: np.ndarray  # Gradient flow component
    circular: np.ndarray  # Circular/curl flow component
    harmonic: np.ndarray  # Harmonic flow component

    def as_dict(self) -> Dict[str, np.ndarray]:
        """Return components as dictionary."""
        return {
            'gradient': self.gradient,
            'circular': self.circular,
            'harmonic': self.harmonic
        }


@dataclass
class EdgeInfluence:
    """Influence measures for an edge."""
    edge_id: str
    spread: float  # ||v||₂ / ||v||₁
    absolute_influence: float  # ||v||₁
    penetration: float  # ||v||₂
    relative_influence: float  # Σv (signed sum)


@dataclass
class EdgePageRankResults:
    """Results from edge PageRank analysis."""
    chart_id: str
    edge_to_index: Dict[str, int]
    index_to_edge: Dict[int, str]

    # PageRank vectors (one per edge)
    pagerank_vectors: Dict[str, np.ndarray]

    # Hodge decompositions (one per edge)
    hodge_decompositions: Dict[str, HodgeDecomposition]

    # Influence measures (one per edge)
    influences: Dict[str, EdgeInfluence]

    # Global measures (aggregated across all edges)
    global_gradient_influence: np.ndarray
    global_circular_influence: np.ndarray
    global_harmonic_influence: np.ndarray


class ChartData:
    """Simple container for chart data loaded from JSON."""

    def __init__(self, data: Dict[str, Any]):
        self.id = data.get('chart_id', 'unknown')
        self.name = data.get('name', 'Unknown Chart')

        elements = data.get('elements', {})

        # Extract vertex IDs
        self.vertices = []
        for v in elements.get('vertices', []):
            if isinstance(v, dict):
                self.vertices.append(v.get('id', ''))
            else:
                self.vertices.append(str(v))

        # Extract edge data (need source/target)
        self.edges = {}  # edge_id -> {source, target}
        self.edge_ids = []
        for e in elements.get('edges', []):
            if isinstance(e, dict):
                edge_id = e.get('id', '')
                self.edge_ids.append(edge_id)
                self.edges[edge_id] = {
                    'source': e.get('source', ''),
                    'target': e.get('target', '')
                }
            else:
                self.edge_ids.append(str(e))
                self.edges[str(e)] = {'source': '', 'target': ''}

        # Extract face data (need boundary edges)
        self.faces = {}  # face_id -> [edge_ids]
        self.face_ids = []
        for f in elements.get('faces', []):
            if isinstance(f, dict):
                face_id = f.get('id', '')
                self.face_ids.append(face_id)
                # Faces may have 'edges' or 'boundary' field
                edges = f.get('edges', f.get('boundary', []))
                self.faces[face_id] = edges if edges else []
            else:
                self.face_ids.append(str(f))
                self.faces[str(f)] = []


class HodgeAnalyzer:
    """Analyze simplicial complexes using Hodge decomposition and edge PageRank."""

    def __init__(self, chart: ChartData, verbose: bool = True):
        """
        Initialize Hodge analyzer.

        Args:
            chart: Parsed chart data
            verbose: If True, print solver warnings. If False, suppress them.
        """
        self.chart = chart
        self.verbose = verbose

    def analyze(
        self,
        beta: float = 0.1,
        compute_all_pagerank: bool = True
    ) -> EdgePageRankResults:
        """
        Perform complete Hodge analysis on the chart.

        Args:
            beta: PageRank jumping parameter (default 0.1)
                  Related to jumping probability α by β = 2α/(1-α)
            compute_all_pagerank: If True, compute personalized PageRank for all edges
                                 If False, only compute Laplacian and decompositions

        Returns:
            EdgePageRankResults object
        """
        # Build edge indexing
        edge_to_index, index_to_edge = self._build_edge_index()
        n_edges = len(edge_to_index)

        if n_edges == 0:
            return EdgePageRankResults(
                chart_id=self.chart.id,
                edge_to_index={},
                index_to_edge={},
                pagerank_vectors={},
                hodge_decompositions={},
                influences={},
                global_gradient_influence=np.array([]),
                global_circular_influence=np.array([]),
                global_harmonic_influence=np.array([])
            )

        # Build boundary operators
        d0 = self._build_d0(edge_to_index)  # edges → vertices
        d1 = self._build_d1(edge_to_index)  # faces → edges

        # Build edge Laplacian
        L1 = self._build_edge_laplacian(d0, d1, edge_to_index)

        # Compute PageRank vectors for each edge
        pagerank_vectors = {}
        hodge_decompositions = {}
        influences = {}

        if compute_all_pagerank:
            for edge_id in self.chart.edge_ids:
                if edge_id not in edge_to_index:
                    continue

                edge_idx = edge_to_index[edge_id]

                # Indicator vector for this edge
                indicator = np.zeros(n_edges, dtype=np.float64)
                indicator[edge_idx] = 1.0

                # Compute personalized PageRank
                pr_vector = self._compute_pagerank(L1, indicator, beta)
                pagerank_vectors[edge_id] = pr_vector

                # Hodge decomposition
                decomp = self._hodge_decompose(pr_vector, d0, d1)
                hodge_decompositions[edge_id] = decomp

                # Influence measures
                influences[edge_id] = self._compute_influence(edge_id, pr_vector)

        # Compute global influence measures
        global_gradient = np.zeros(n_edges, dtype=np.float64)
        global_circular = np.zeros(n_edges, dtype=np.float64)
        global_harmonic = np.zeros(n_edges, dtype=np.float64)

        if hodge_decompositions:
            for decomp in hodge_decompositions.values():
                global_gradient += np.abs(decomp.gradient)
                global_circular += np.abs(decomp.circular)
                global_harmonic += np.abs(decomp.harmonic)

        return EdgePageRankResults(
            chart_id=self.chart.id,
            edge_to_index=edge_to_index,
            index_to_edge=index_to_edge,
            pagerank_vectors=pagerank_vectors,
            hodge_decompositions=hodge_decompositions,
            influences=influences,
            global_gradient_influence=global_gradient,
            global_circular_influence=global_circular,
            global_harmonic_influence=global_harmonic
        )

    def _build_edge_index(self) -> Tuple[Dict[str, int], Dict[int, str]]:
        """Build bidirectional edge indexing."""
        edge_to_index = {edge_id: idx for idx, edge_id in enumerate(self.chart.edge_ids)}
        index_to_edge = {idx: edge_id for edge_id, idx in edge_to_index.items()}
        return edge_to_index, index_to_edge

    def _build_d0(self, edge_to_index: Dict[str, int]) -> sp.csr_matrix:
        """
        Build ∂₁: edges → vertices boundary operator.

        For each edge, marks its source and target vertices.
        Matrix is (n_vertices × n_edges).
        """
        # Build vertex index
        vertex_to_index = {v_id: idx for idx, v_id in enumerate(self.chart.vertices)}
        n_vertices = len(vertex_to_index)
        n_edges = len(edge_to_index)

        # Build sparse matrix
        row_indices = []
        col_indices = []
        data = []

        for edge_id, edge_data in self.chart.edges.items():
            if edge_id not in edge_to_index:
                continue

            edge_idx = edge_to_index[edge_id]
            source = edge_data.get('source', '')
            target = edge_data.get('target', '')

            # Source vertex gets -1
            if source in vertex_to_index:
                source_idx = vertex_to_index[source]
                row_indices.append(source_idx)
                col_indices.append(edge_idx)
                data.append(-1.0)

            # Target vertex gets +1
            if target in vertex_to_index:
                target_idx = vertex_to_index[target]
                row_indices.append(target_idx)
                col_indices.append(edge_idx)
                data.append(1.0)

        if not data:
            return sp.csr_matrix((n_vertices, n_edges), dtype=np.float64)

        # Convert to numpy arrays with explicit dtype
        data = np.array(data, dtype=np.float64)
        row_indices = np.array(row_indices, dtype=np.int32)
        col_indices = np.array(col_indices, dtype=np.int32)

        d0 = sp.csr_matrix(
            (data, (row_indices, col_indices)),
            shape=(n_vertices, n_edges),
            dtype=np.float64
        )

        return d0

    def _build_d1(self, edge_to_index: Dict[str, int]) -> sp.csr_matrix:
        """
        Build ∂₂: faces → edges boundary operator.

        For each face, marks its boundary edges.
        Matrix is (n_edges × n_faces).
        """
        n_edges = len(edge_to_index)
        n_faces = len(self.chart.face_ids)

        # Build face index
        face_to_index = {f_id: idx for idx, f_id in enumerate(self.chart.face_ids)}

        # Build sparse matrix
        row_indices = []
        col_indices = []
        data = []

        for face_id, boundary_edges in self.chart.faces.items():
            if face_id not in face_to_index:
                continue

            face_idx = face_to_index[face_id]

            # Mark each boundary edge
            for edge_id in boundary_edges:
                if edge_id in edge_to_index:
                    edge_idx = edge_to_index[edge_id]
                    row_indices.append(edge_idx)
                    col_indices.append(face_idx)
                    data.append(1.0)

        if not data:
            return sp.csr_matrix((n_edges, n_faces), dtype=np.float64)

        # Convert to numpy arrays with explicit dtype
        data = np.array(data, dtype=np.float64)
        row_indices = np.array(row_indices, dtype=np.int32)
        col_indices = np.array(col_indices, dtype=np.int32)

        d1 = sp.csr_matrix(
            (data, (row_indices, col_indices)),
            shape=(n_edges, n_faces),
            dtype=np.float64
        )

        return d1

    def _build_edge_laplacian(
        self,
        d0: sp.csr_matrix,
        d1: sp.csr_matrix,
        edge_to_index: Dict[str, int]
    ) -> sp.csr_matrix:
        """
        Build edge Laplacian: L₁ = ∂₁D₀⁻¹∂₁* + D₁⁻¹∂₂*∂₂

        Where:
        - D₀ is diagonal with vertex degrees
        - D₁ is diagonal with edge degrees (number of incident faces)
        """
        n_edges = len(edge_to_index)
        n_vertices = d0.shape[0]

        # Build D0: diagonal matrix with vertex degrees
        vertex_degrees = np.zeros(n_vertices, dtype=np.float64)
        for i in range(n_vertices):
            vertex_degrees[i] = np.abs(d0[i, :]).sum()
        vertex_degrees[vertex_degrees == 0] = 1.0  # Avoid division by zero
        D0_inv = sp.diags(1.0 / vertex_degrees, dtype=np.float64)

        # Build D1: diagonal matrix with edge degrees (faces per edge)
        edge_degrees = np.zeros(n_edges, dtype=np.float64)
        for i in range(n_edges):
            edge_degrees[i] = np.abs(d1[i, :]).sum()
        edge_degrees[edge_degrees == 0] = 1.0  # Avoid division by zero
        D1_inv = sp.diags(1.0 / edge_degrees, dtype=np.float64)

        # Compute L1 = d0.T @ D0_inv @ d0 + D1_inv @ d1 @ d1.T
        # First term: connection to vertices (down-Laplacian)
        L1_down = d0.T @ D0_inv @ d0

        # Second term: connection to faces (up-Laplacian)
        L1_up = D1_inv @ (d1 @ d1.T)

        L1 = L1_down + L1_up

        # Ensure final matrix is float64
        return L1.astype(np.float64).tocsr()

    def _compute_pagerank(
        self,
        L1: sp.csr_matrix,
        indicator: np.ndarray,
        beta: float
    ) -> np.ndarray:
        """
        Compute personalized PageRank: PR = (βI + L₁)⁻¹ χ

        Args:
            L1: Edge Laplacian
            indicator: Indicator vector for edge of interest
            beta: Jumping parameter

        Returns:
            PageRank vector
        """
        n = L1.shape[0]

        # Ensure everything is float64 and convert to proper format
        L1 = L1.astype(np.float64).tocsr()
        indicator = np.asarray(indicator, dtype=np.float64).ravel()

        # Build system matrix A = βI + L1
        I = sp.eye(n, format='csr', dtype=np.float64)
        A = (beta * I + L1).tocsr()

        # Try iterative solver first for larger systems
        try:
            from scipy.sparse.linalg import cg
            pr, info = cg(A, indicator, atol=1e-10, maxiter=1000)
            if info != 0:
                if self.verbose:
                    print(f"Warning: CG solver convergence issue (info={info}), using dense solver")
                pr = np.linalg.solve(A.toarray(), indicator)
            pr = np.asarray(pr, dtype=np.float64).ravel()
        except Exception as e:
            if self.verbose:
                print(f"Warning: Iterative solver failed ({e}), using dense solver")
            pr = np.linalg.solve(A.toarray(), indicator)

        return np.asarray(pr, dtype=np.float64).ravel()

    def _hodge_decompose(
        self,
        vector: np.ndarray,
        d0: sp.csr_matrix,
        d1: sp.csr_matrix
    ) -> HodgeDecomposition:
        """
        Perform Hodge decomposition: v = g + c + h

        Where:
        - g = proj_{im(∂₁)} v  (gradient flow)
        - c = proj_{im(∂₂*)} v  (circular flow)
        - h = proj_{ker(∂₂) ∩ im(∂₁)^⊥} v  (harmonic flow)

        Args:
            vector: Edge vector to decompose
            d0: ∂₁ boundary operator (edges → vertices)
            d1: ∂₂ boundary operator (faces → edges)

        Returns:
            HodgeDecomposition object
        """
        # Ensure vector is float64
        vector = np.asarray(vector, dtype=np.float64)

        # Gradient component: project onto image of d0.T (= ∂₁)
        gradient = self._project_onto_image(vector, d0.T)

        # Circular component: project onto image of d1 (= ∂₂*)
        circular = self._project_onto_image(vector, d1)

        # Harmonic component: residual
        harmonic = vector - gradient - circular

        return HodgeDecomposition(
            gradient=gradient,
            circular=circular,
            harmonic=harmonic
        )

    def _project_onto_image(
        self,
        vector: np.ndarray,
        operator: sp.csr_matrix,
        regularization: float = 1e-10
    ) -> np.ndarray:
        """
        Project vector onto image of operator.

        proj_{im(A)} v = A @ (A.T @ A)⁻¹ @ A.T @ v

        Args:
            vector: Vector to project
            operator: Operator whose image we project onto
            regularization: Small value added to diagonal for numerical stability

        Returns:
            Projected vector
        """
        # Ensure types
        vector = np.asarray(vector, dtype=np.float64).ravel()
        operator = operator.astype(np.float64).tocsr()

        # Compute A.T @ A (this is symmetric positive semidefinite)
        ATA = (operator.T @ operator).tocsr()

        # Add regularization
        n = ATA.shape[0]
        ATA_reg = ATA + regularization * sp.eye(n, dtype=np.float64)
        ATA_reg = ATA_reg.tocsr()

        # Compute A.T @ v
        ATv = operator.T @ vector
        if hasattr(ATv, 'toarray'):
            ATv = ATv.toarray().ravel()
        ATv = np.asarray(ATv, dtype=np.float64).ravel()

        # Solve (A.T @ A) @ x = A.T @ v using iterative solver
        try:
            from scipy.sparse.linalg import cg
            x, info = cg(ATA_reg, ATv, atol=1e-10, maxiter=1000)
            if info != 0:
                if self.verbose:
                    print(f"Warning: CG projection convergence issue (info={info}), using dense solver")
                x = np.linalg.lstsq(ATA_reg.toarray(), ATv, rcond=None)[0]
            x = np.asarray(x, dtype=np.float64).ravel()
        except Exception as e:
            if self.verbose:
                print(f"Warning: Projection solver failed ({e}), using dense solver")
            x = np.linalg.lstsq(ATA_reg.toarray(), ATv, rcond=None)[0]
            x = np.asarray(x, dtype=np.float64).ravel()

        # Project: A @ x
        projection = operator @ x
        if hasattr(projection, 'toarray'):
            projection = projection.toarray().ravel()

        return np.asarray(projection, dtype=np.float64).ravel()

    def _compute_influence(
        self,
        edge_id: str,
        pagerank_vector: np.ndarray
    ) -> EdgeInfluence:
        """
        Compute influence measures for an edge's PageRank vector.

        Measures:
        - spread: ||v||₂ / ||v||₁ (how spread out is influence)
        - absolute_influence: ||v||₁ (total magnitude of influence)
        - penetration: ||v||₂ (emphasis on influencing many edges)
        - relative_influence: Σv (signed sum, accounts for excitation/inhibition)
        """
        # L1 norm (absolute influence)
        l1_norm = np.linalg.norm(pagerank_vector, ord=1)

        # L2 norm (penetration)
        l2_norm = np.linalg.norm(pagerank_vector, ord=2)

        # Spread
        spread = l2_norm / l1_norm if l1_norm > 0 else 0.0

        # Relative influence (signed sum)
        relative = np.sum(pagerank_vector)

        return EdgeInfluence(
            edge_id=edge_id,
            spread=spread,
            absolute_influence=l1_norm,
            penetration=l2_norm,
            relative_influence=relative
        )

    def get_top_edges_by_measure(
        self,
        results: EdgePageRankResults,
        measure: str = 'penetration',
        component: Optional[str] = None,
        top_k: int = 10
    ) -> List[Tuple[str, float]]:
        """
        Get top K edges by influence measure.

        Args:
            results: EdgePageRankResults from analyze
            measure: One of 'spread', 'absolute_influence', 'penetration', 'relative_influence'
            component: Optional Hodge component: 'gradient', 'circular', 'harmonic', or None for full PR
            top_k: Number of top edges to return

        Returns:
            List of (edge_id, score) tuples sorted by score
        """
        scores = []

        if component is None:
            # Use influence measures directly
            for edge_id, influence in results.influences.items():
                if measure == 'spread':
                    score = influence.spread
                elif measure == 'absolute_influence':
                    score = influence.absolute_influence
                elif measure == 'penetration':
                    score = influence.penetration
                elif measure == 'relative_influence':
                    score = influence.relative_influence
                else:
                    raise ValueError(f"Unknown measure: {measure}")
                scores.append((edge_id, score))
        else:
            # Compute measure on Hodge component
            for edge_id in results.hodge_decompositions.keys():
                decomp = results.hodge_decompositions[edge_id]

                if component == 'gradient':
                    vector = decomp.gradient
                elif component == 'circular':
                    vector = decomp.circular
                elif component == 'harmonic':
                    vector = decomp.harmonic
                else:
                    raise ValueError(f"Unknown component: {component}")

                # Compute requested measure
                if measure == 'absolute_influence':
                    score = np.linalg.norm(vector, ord=1)
                elif measure == 'penetration':
                    score = np.linalg.norm(vector, ord=2)
                elif measure == 'relative_influence':
                    score = np.sum(vector)
                elif measure == 'spread':
                    l1 = np.linalg.norm(vector, ord=1)
                    l2 = np.linalg.norm(vector, ord=2)
                    score = l2 / l1 if l1 > 0 else 0.0
                else:
                    raise ValueError(f"Unknown measure: {measure}")

                scores.append((edge_id, score))

        # Sort by score (descending) and return top K
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]

    def print_influence_report(
        self,
        results: EdgePageRankResults,
        top_k: int = 10
    ) -> None:
        """
        Print formatted report of edge influences.
        """
        separator = "=" * 80
        print(f"\n{separator}")
        print(f"Edge Influence Report: {results.chart_id}")
        print(f"{separator}\n")

        # Summary stats
        n_edges = len(results.edge_to_index)
        print(f"Total edges analyzed: {n_edges}")

        if n_edges == 0:
            print("No edges to analyze.")
            return

        # Compute Hodge component percentages
        if results.hodge_decompositions:
            total_gradient = np.sum(results.global_gradient_influence)
            total_circular = np.sum(results.global_circular_influence)
            total_harmonic = np.sum(results.global_harmonic_influence)
            total = total_gradient + total_circular + total_harmonic

            if total > 0:
                print(f"\nHodge Decomposition (global):")
                print(f"  Gradient:  {100 * total_gradient / total:.1f}%")
                print(f"  Circular:  {100 * total_circular / total:.1f}%")
                print(f"  Harmonic:  {100 * total_harmonic / total:.1f}%")

        # Overall top edges by penetration
        print(f"\nTop {top_k} Edges by Penetration (overall influence):")
        print("-" * 80)
        top_penetration = self.get_top_edges_by_measure(
            results, 'penetration', None, top_k
        )
        for i, (edge_id, score) in enumerate(top_penetration, 1):
            print(f"  {i:2d}. {edge_id:50s} {score:10.6f}")

        # Top edges by gradient component
        print(f"\nTop {top_k} Edges by Gradient Flow (Structural Bridges):")
        print("-" * 80)
        top_gradient = self.get_top_edges_by_measure(
            results, 'penetration', 'gradient', top_k
        )
        for i, (edge_id, score) in enumerate(top_gradient, 1):
            print(f"  {i:2d}. {edge_id:50s} {score:10.6f}")

        # Top edges by circular component
        print(f"\nTop {top_k} Edges by Circular Flow (Confluence Zones):")
        print("-" * 80)
        top_circular = self.get_top_edges_by_measure(
            results, 'penetration', 'circular', top_k
        )
        for i, (edge_id, score) in enumerate(top_circular, 1):
            print(f"  {i:2d}. {edge_id:50s} {score:10.6f}")

        # Top edges by harmonic component
        print(f"\nTop {top_k} Edges by Harmonic Flow (Topological Cycles):")
        print("-" * 80)
        top_harmonic = self.get_top_edges_by_measure(
            results, 'penetration', 'harmonic', top_k
        )
        for i, (edge_id, score) in enumerate(top_harmonic, 1):
            print(f"  {i:2d}. {edge_id:50s} {score:10.6f}")

        print(f"\n{separator}\n")


def load_chart_json(json_path: Path) -> ChartData:
    """Load chart from JSON file."""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return ChartData(data)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Hodge decomposition and edge PageRank analysis for charts'
    )
    parser.add_argument('chart_json', type=str, help='Path to chart JSON file')
    parser.add_argument('--top', type=int, default=10, help='Number of top edges to show')
    parser.add_argument('--beta', type=float, default=0.1, help='PageRank jumping parameter')
    parser.add_argument('--quiet', action='store_true', help='Suppress solver warnings')

    args = parser.parse_args()

    json_path = Path(args.chart_json)
    if not json_path.exists():
        print(f"Error: File not found: {json_path}")
        sys.exit(1)

    # Load chart
    print(f"Loading chart: {json_path}")
    chart = load_chart_json(json_path)
    print(f"  Vertices: {len(chart.vertices)}")
    print(f"  Edges: {len(chart.edge_ids)}")
    print(f"  Faces: {len(chart.face_ids)}")

    # Run analysis
    print(f"\nRunning Hodge analysis (beta={args.beta})...")
    analyzer = HodgeAnalyzer(chart, verbose=not args.quiet)
    results = analyzer.analyze(beta=args.beta)

    # Print report
    analyzer.print_influence_report(results, top_k=args.top)


if __name__ == '__main__':
    main()
