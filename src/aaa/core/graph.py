"""
Typed graph construction and queries for ontology verification.

This module builds a typed directed graph from the knowledge complex cache,
enabling ontology-level rule verification through graph queries.

IMPORTANT DISTINCTION:
- Topology: Structural rules of simplicial complexes (faces have edges, edges
  have vertices, charts are valid simplicial complexes). See topology.py.
- Ontology: Type system layered on topology. Types have local rules that add
  constraints (cannot weaken topological rules). This module supports ontology
  verification through typed graph queries.
"""

from typing import Dict, Any, List, Set, Tuple, Optional
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class TypedVertex:
    """A vertex with type information."""
    id: str
    type: str
    data: Dict[str, Any]


@dataclass
class TypedEdge:
    """An edge with type and direction information."""
    id: str
    type: str
    source: str
    target: str
    orientation: str  # 'directed' or 'undirected'
    data: Dict[str, Any]


@dataclass
class TypedFace:
    """A face with type information."""
    id: str
    type: str
    vertices: List[str]
    edges: List[str]
    orientation: str  # 'oriented' or 'unoriented'
    data: Dict[str, Any]


class ComplexGraph:
    """
    A typed graph representation of a knowledge complex.

    Supports ontology-level queries like:
    - Finding edges of a specific type from/to a vertex
    - Checking degree constraints
    - Finding paths through specific edge types
    - Checking face adjacency (shared edges)
    """

    def __init__(self):
        self.vertices: Dict[str, TypedVertex] = {}
        self.edges: Dict[str, TypedEdge] = {}
        self.faces: Dict[str, TypedFace] = {}

        # Adjacency indices for efficient queries
        self._edges_from: Dict[str, List[str]] = defaultdict(list)  # vertex_id -> [edge_ids]
        self._edges_to: Dict[str, List[str]] = defaultdict(list)    # vertex_id -> [edge_ids]
        self._edges_by_type: Dict[str, List[str]] = defaultdict(list)  # edge_type -> [edge_ids]
        self._faces_by_vertex: Dict[str, List[str]] = defaultdict(list)  # vertex_id -> [face_ids]
        self._faces_by_edge: Dict[str, List[str]] = defaultdict(list)    # edge_id -> [face_ids]
        self._faces_by_type: Dict[str, List[str]] = defaultdict(list)    # face_type -> [face_ids]

    @classmethod
    def from_cache(cls, cache: Dict[str, Any]) -> 'ComplexGraph':
        """
        Build a ComplexGraph from a complex.json cache.

        Args:
            cache: Parsed complex.json data

        Returns:
            ComplexGraph populated with vertices, edges, and faces
        """
        graph = cls()
        elements = cache.get('elements', {})

        # Load vertices
        for vid, vdata in elements.get('vertices', {}).items():
            vertex = TypedVertex(
                id=vid,
                type=vdata.get('type', ''),
                data=vdata
            )
            graph.vertices[vid] = vertex

        # Load edges and build adjacency indices
        for eid, edata in elements.get('edges', {}).items():
            edge = TypedEdge(
                id=eid,
                type=edata.get('type', ''),
                source=edata.get('source', ''),
                target=edata.get('target', ''),
                orientation=edata.get('orientation', 'directed'),
                data=edata
            )
            graph.edges[eid] = edge
            graph._edges_from[edge.source].append(eid)
            graph._edges_to[edge.target].append(eid)

            # For undirected edges, add reverse direction too
            if edge.orientation == 'undirected':
                graph._edges_from[edge.target].append(eid)
                graph._edges_to[edge.source].append(eid)

            # Index by edge type (extract base type from 'edge/type')
            edge_type = edge.type.replace('edge/', '') if edge.type.startswith('edge/') else edge.type
            graph._edges_by_type[edge_type].append(eid)

        # Load faces and build face indices
        for fid, fdata in elements.get('faces', {}).items():
            face = TypedFace(
                id=fid,
                type=fdata.get('type', ''),
                vertices=fdata.get('vertices', []),
                edges=fdata.get('edges', []),
                orientation=fdata.get('orientation', 'oriented'),
                data=fdata
            )
            graph.faces[fid] = face

            # Index faces by vertex
            for vid in face.vertices:
                graph._faces_by_vertex[vid].append(fid)

            # Index faces by edge
            for eid in face.edges:
                graph._faces_by_edge[eid].append(fid)

            # Index by face type (extract base type from 'face/type')
            face_type = face.type.replace('face/', '') if face.type.startswith('face/') else face.type
            graph._faces_by_type[face_type].append(fid)

        return graph

    # ========== Vertex Queries ==========

    def get_vertex(self, vertex_id: str) -> Optional[TypedVertex]:
        """Get a vertex by ID."""
        return self.vertices.get(vertex_id)

    def get_vertex_type(self, vertex_id: str) -> Optional[str]:
        """Get the type of a vertex."""
        vertex = self.vertices.get(vertex_id)
        return vertex.type if vertex else None

    def get_vertices_by_type(self, vertex_type: str) -> List[str]:
        """Get all vertex IDs of a given type (supports prefix matching)."""
        return [
            vid for vid, v in self.vertices.items()
            if v.type == vertex_type or v.type.startswith(f"{vertex_type}/")
        ]

    # ========== Edge Queries ==========

    def get_edge(self, edge_id: str) -> Optional[TypedEdge]:
        """Get an edge by ID."""
        return self.edges.get(edge_id)

    def get_edges_from(self, vertex_id: str, edge_type: Optional[str] = None) -> List[str]:
        """
        Get edge IDs originating from a vertex.

        Args:
            vertex_id: Source vertex ID
            edge_type: Optional filter by edge type (e.g., 'verification', 'coupling')

        Returns:
            List of edge IDs
        """
        edges = self._edges_from.get(vertex_id, [])
        if edge_type:
            return [eid for eid in edges if self._edge_matches_type(eid, edge_type)]
        return edges

    def get_edges_to(self, vertex_id: str, edge_type: Optional[str] = None) -> List[str]:
        """
        Get edge IDs targeting a vertex.

        Args:
            vertex_id: Target vertex ID
            edge_type: Optional filter by edge type

        Returns:
            List of edge IDs
        """
        edges = self._edges_to.get(vertex_id, [])
        if edge_type:
            return [eid for eid in edges if self._edge_matches_type(eid, edge_type)]
        return edges

    def get_edges_incident(self, vertex_id: str, edge_type: Optional[str] = None) -> List[str]:
        """
        Get all edge IDs incident to a vertex (in or out).

        Args:
            vertex_id: Vertex ID
            edge_type: Optional filter by edge type

        Returns:
            List of edge IDs (deduplicated for undirected edges)
        """
        edges = set(self.get_edges_from(vertex_id, edge_type))
        edges.update(self.get_edges_to(vertex_id, edge_type))
        return list(edges)

    def get_edges_by_type(self, edge_type: str) -> List[str]:
        """Get all edge IDs of a given type."""
        return self._edges_by_type.get(edge_type, [])

    def _edge_matches_type(self, edge_id: str, edge_type: str) -> bool:
        """Check if an edge matches the given type."""
        edge = self.edges.get(edge_id)
        if not edge:
            return False
        # Match either full type or base type
        return edge.type == edge_type or edge.type == f"edge/{edge_type}"

    # ========== Face Queries ==========

    def get_face(self, face_id: str) -> Optional[TypedFace]:
        """Get a face by ID."""
        return self.faces.get(face_id)

    def get_faces_containing_vertex(self, vertex_id: str, face_type: Optional[str] = None) -> List[str]:
        """
        Get face IDs containing a vertex.

        Args:
            vertex_id: Vertex ID
            face_type: Optional filter by face type

        Returns:
            List of face IDs
        """
        faces = self._faces_by_vertex.get(vertex_id, [])
        if face_type:
            return [fid for fid in faces if self._face_matches_type(fid, face_type)]
        return faces

    def get_faces_containing_edge(self, edge_id: str, face_type: Optional[str] = None) -> List[str]:
        """
        Get face IDs containing an edge in their boundary.

        Args:
            edge_id: Edge ID
            face_type: Optional filter by face type

        Returns:
            List of face IDs
        """
        faces = self._faces_by_edge.get(edge_id, [])
        if face_type:
            return [fid for fid in faces if self._face_matches_type(fid, face_type)]
        return faces

    def get_faces_by_type(self, face_type: str) -> List[str]:
        """Get all face IDs of a given type."""
        return self._faces_by_type.get(face_type, [])

    def _face_matches_type(self, face_id: str, face_type: str) -> bool:
        """Check if a face matches the given type."""
        face = self.faces.get(face_id)
        if not face:
            return False
        return face.type == face_type or face.type == f"face/{face_type}"

    # ========== Degree Queries ==========

    def out_degree(self, vertex_id: str, edge_type: Optional[str] = None) -> int:
        """Count outgoing edges from a vertex."""
        return len(self.get_edges_from(vertex_id, edge_type))

    def in_degree(self, vertex_id: str, edge_type: Optional[str] = None) -> int:
        """Count incoming edges to a vertex."""
        return len(self.get_edges_to(vertex_id, edge_type))

    def degree(self, vertex_id: str, edge_type: Optional[str] = None) -> int:
        """Count all edges incident to a vertex (in + out, undirected counted once)."""
        return len(self.get_edges_incident(vertex_id, edge_type))

    # ========== Adjacency Queries ==========

    def faces_share_edge(self, face_id1: str, face_id2: str) -> List[str]:
        """
        Find edges shared by two faces.

        Args:
            face_id1: First face ID
            face_id2: Second face ID

        Returns:
            List of shared edge IDs
        """
        face1 = self.faces.get(face_id1)
        face2 = self.faces.get(face_id2)

        if not face1 or not face2:
            return []

        return list(set(face1.edges) & set(face2.edges))

    def get_adjacent_faces(self, face_id: str, edge_type: Optional[str] = None) -> List[Tuple[str, str]]:
        """
        Find faces adjacent to a face (sharing an edge).

        Args:
            face_id: Face ID
            edge_type: Optional - only consider adjacency through edges of this type

        Returns:
            List of (adjacent_face_id, shared_edge_id) tuples
        """
        face = self.faces.get(face_id)
        if not face:
            return []

        adjacent = []
        for eid in face.edges:
            if edge_type and not self._edge_matches_type(eid, edge_type):
                continue

            for adj_fid in self._faces_by_edge.get(eid, []):
                if adj_fid != face_id:
                    adjacent.append((adj_fid, eid))

        return adjacent

    # ========== Path Queries ==========

    def find_path(
        self,
        source_id: str,
        target_id: str,
        edge_type: Optional[str] = None,
        max_depth: int = 10
    ) -> Optional[List[str]]:
        """
        Find a path from source to target vertex through edges.

        Args:
            source_id: Starting vertex ID
            target_id: Ending vertex ID
            edge_type: Optional - only traverse edges of this type
            max_depth: Maximum path length

        Returns:
            List of edge IDs forming the path, or None if no path exists
        """
        if source_id == target_id:
            return []

        # BFS
        visited = {source_id}
        queue = [(source_id, [])]  # (current_vertex, path_so_far)

        while queue:
            current, path = queue.pop(0)

            if len(path) >= max_depth:
                continue

            for eid in self.get_edges_from(current, edge_type):
                edge = self.edges[eid]
                next_vertex = edge.target

                if next_vertex == target_id:
                    return path + [eid]

                if next_vertex not in visited:
                    visited.add(next_vertex)
                    queue.append((next_vertex, path + [eid]))

        return None

    def edge_exists(self, source_id: str, target_id: str, edge_type: Optional[str] = None) -> bool:
        """
        Check if an edge exists between two vertices.

        Args:
            source_id: Source vertex ID
            target_id: Target vertex ID
            edge_type: Optional - require specific edge type

        Returns:
            True if such an edge exists
        """
        for eid in self.get_edges_from(source_id, edge_type):
            edge = self.edges[eid]
            if edge.target == target_id:
                return True
        return False

    # ========== DAG Verification ==========

    def check_dag(self, edge_type: Optional[str] = None) -> Tuple[bool, Optional[List[str]]]:
        """
        Check if edges of a given type form a directed acyclic graph.

        Args:
            edge_type: Edge type to check (None = all edges)

        Returns:
            Tuple of (is_dag, cycle_vertices)
            - is_dag: True if no cycles
            - cycle_vertices: List of vertices in a cycle if found, None if DAG
        """
        # Get relevant edges
        if edge_type:
            edge_ids = self.get_edges_by_type(edge_type)
        else:
            edge_ids = list(self.edges.keys())

        # Build subgraph adjacency
        adj: Dict[str, List[str]] = defaultdict(list)
        vertices_in_subgraph: Set[str] = set()

        for eid in edge_ids:
            edge = self.edges[eid]
            adj[edge.source].append(edge.target)
            vertices_in_subgraph.add(edge.source)
            vertices_in_subgraph.add(edge.target)

        # Topological sort with cycle detection
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {v: WHITE for v in vertices_in_subgraph}
        cycle: List[str] = []

        def dfs(v: str) -> bool:
            """Returns True if cycle found."""
            color[v] = GRAY
            for neighbor in adj[v]:
                if color[neighbor] == GRAY:
                    # Found cycle
                    cycle.append(neighbor)
                    cycle.append(v)
                    return True
                if color[neighbor] == WHITE:
                    if dfs(neighbor):
                        if len(cycle) < 20:  # Limit cycle length for reporting
                            cycle.append(v)
                        return True
            color[v] = BLACK
            return False

        for v in vertices_in_subgraph:
            if color[v] == WHITE:
                if dfs(v):
                    return False, list(reversed(cycle))

        return True, None

    # ========== Star Queries (vertex neighborhood) ==========

    def get_star(self, vertex_id: str) -> Dict[str, Any]:
        """
        Get the star of a vertex - all edges and faces incident to it.

        Args:
            vertex_id: Vertex ID

        Returns:
            Dictionary with:
                - vertex: The vertex data
                - edges_out: Outgoing edge IDs
                - edges_in: Incoming edge IDs
                - faces: Face IDs containing this vertex
        """
        return {
            'vertex': self.vertices.get(vertex_id),
            'edges_out': self.get_edges_from(vertex_id),
            'edges_in': self.get_edges_to(vertex_id),
            'faces': self.get_faces_containing_vertex(vertex_id)
        }

    # ========== Statistics ==========

    def statistics(self) -> Dict[str, Any]:
        """Get graph statistics."""
        return {
            'vertices': len(self.vertices),
            'edges': len(self.edges),
            'faces': len(self.faces),
            'vertex_types': len(set(v.type for v in self.vertices.values())),
            'edge_types': len(self._edges_by_type),
            'face_types': len(self._faces_by_type),
        }


def build_complex_graph(cache: Dict[str, Any]) -> ComplexGraph:
    """
    Build a ComplexGraph from cache data.

    Convenience function wrapping ComplexGraph.from_cache().

    Args:
        cache: Parsed complex.json data

    Returns:
        ComplexGraph instance
    """
    return ComplexGraph.from_cache(cache)
