"""
Typed simplicial complex construction and queries for ontology verification.

This module builds a typed simplicial complex from the knowledge complex cache,
enabling ontology-level rule verification through simplex queries.

A simplicial complex consists of:
- Vertices (0-simplices): The basic elements (documents)
- Edges (1-simplices): Relationships between pairs of vertices
- Faces (2-simplices): Triangular relationships between triples of vertices

IMPORTANT DISTINCTION:
- Topology: Structural rules of simplicial complexes (faces have edges, edges
  have vertices, charts are valid simplicial complexes). See topology.py.
- Ontology: Type system layered on topology. Types have local rules that add
  constraints (cannot weaken topological rules). This module supports ontology
  verification through typed simplex queries.
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


class SimplicialComplex:
    """
    A typed simplicial complex representation of a knowledge complex.

    A 2-dimensional simplicial complex with vertices, edges, and faces.
    All elements are typed according to the ontology, enabling type-aware queries.

    Supports ontology-level queries like:
    - Finding edges of a specific type from/to a vertex
    - Checking degree constraints
    - Finding paths through specific edge types
    - Checking face adjacency (shared edges)
    - Getting boundaries and coboundaries
    - Computing closures, stars, and links
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
    def from_cache(cls, cache: Dict[str, Any]) -> 'SimplicialComplex':
        """
        Build a SimplicialComplex from a complex.json cache.

        Args:
            cache: Parsed complex.json data

        Returns:
            SimplicialComplex populated with vertices, edges, and faces
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

    def get_vertices_by_type(self, vertex_type: str, strict: bool = False) -> List[str]:
        """
        Get all vertex IDs of a given type.

        Args:
            vertex_type: Type to match (e.g., 'vertex/doc', 'vertex/spec')
            strict: If False (default), include subtypes (spec inherits from doc).
                    If True, only exact type matches.

        Returns:
            List of vertex IDs matching the type

        Examples:
            get_vertices_by_type('vertex/doc')           # Returns docs, specs, guidances, etc.
            get_vertices_by_type('vertex/doc', strict=True)  # Returns only docs, not specs
        """
        if strict:
            return [vid for vid, v in self.vertices.items() if v.type == vertex_type]
        else:
            return [
                vid for vid, v in self.vertices.items()
                if v.type == vertex_type or v.type.startswith(f"{vertex_type}/")
            ]

    def get_all_vertices(self) -> List[str]:
        """Get all vertex IDs."""
        return list(self.vertices.keys())

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

    def get_edges_by_type(self, edge_type: str, strict: bool = False) -> List[str]:
        """
        Get all edge IDs of a given type.

        Args:
            edge_type: Type to match (e.g., 'verification', 'edge/verification')
            strict: If False (default), include subtypes.
                    If True, only exact type matches.

        Returns:
            List of edge IDs matching the type
        """
        # Normalize type (handle both 'verification' and 'edge/verification')
        base_type = edge_type.replace('edge/', '') if edge_type.startswith('edge/') else edge_type

        if strict:
            return [
                eid for eid, e in self.edges.items()
                if e.type == edge_type or e.type == f"edge/{base_type}"
            ]
        else:
            # Include subtypes
            return [
                eid for eid, e in self.edges.items()
                if (e.type == edge_type or
                    e.type == f"edge/{base_type}" or
                    e.type.startswith(f"edge/{base_type}/"))
            ]

    def get_all_edges(self) -> List[str]:
        """Get all edge IDs."""
        return list(self.edges.keys())

    def _edge_matches_type(self, edge_id: str, edge_type: str, strict: bool = False) -> bool:
        """Check if an edge matches the given type."""
        edge = self.edges.get(edge_id)
        if not edge:
            return False
        base_type = edge_type.replace('edge/', '') if edge_type.startswith('edge/') else edge_type
        if strict:
            return edge.type == edge_type or edge.type == f"edge/{base_type}"
        else:
            return (edge.type == edge_type or
                    edge.type == f"edge/{base_type}" or
                    edge.type.startswith(f"edge/{base_type}/"))

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

    def get_faces_by_type(self, face_type: str, strict: bool = False) -> List[str]:
        """
        Get all face IDs of a given type.

        Args:
            face_type: Type to match (e.g., 'assurance', 'face/assurance')
            strict: If False (default), include subtypes.
                    If True, only exact type matches.

        Returns:
            List of face IDs matching the type
        """
        base_type = face_type.replace('face/', '') if face_type.startswith('face/') else face_type

        if strict:
            return [
                fid for fid, f in self.faces.items()
                if f.type == face_type or f.type == f"face/{base_type}"
            ]
        else:
            return [
                fid for fid, f in self.faces.items()
                if (f.type == face_type or
                    f.type == f"face/{base_type}" or
                    f.type.startswith(f"face/{base_type}/"))
            ]

    def get_all_faces(self) -> List[str]:
        """Get all face IDs."""
        return list(self.faces.keys())

    def _face_matches_type(self, face_id: str, face_type: str, strict: bool = False) -> bool:
        """Check if a face matches the given type."""
        face = self.faces.get(face_id)
        if not face:
            return False
        base_type = face_type.replace('face/', '') if face_type.startswith('face/') else face_type
        if strict:
            return face.type == face_type or face.type == f"face/{base_type}"
        else:
            return (face.type == face_type or
                    face.type == f"face/{base_type}" or
                    face.type.startswith(f"face/{base_type}/"))

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

    # ========== General Element Access ==========

    def get_elements(
        self,
        dimension: Optional[int] = None,
        element_type: Optional[str] = None,
        strict: bool = False
    ) -> Dict[str, List[str]]:
        """
        Get elements filtered by dimension and/or type.

        Args:
            dimension: 0 for vertices, 1 for edges, 2 for faces, None for all
            element_type: Type to filter by (e.g., 'vertex/doc', 'edge/verification')
            strict: If False (default), include subtypes.
                    If True, only exact type matches.

        Returns:
            Dictionary with keys 'vertices', 'edges', 'faces' containing
            lists of matching element IDs.

        Examples:
            get_elements()                           # All elements
            get_elements(dimension=0)                # All vertices
            get_elements(element_type='vertex/doc') # All doc vertices (+ subtypes)
            get_elements(element_type='vertex/doc', strict=True)  # Only doc, not spec
            get_elements(dimension=1, element_type='verification')  # All verification edges
        """
        result = {'vertices': [], 'edges': [], 'faces': []}

        # Vertices (dimension 0)
        if dimension is None or dimension == 0:
            if element_type:
                # Normalize type for vertices
                vtype = element_type if element_type.startswith('vertex/') else f"vertex/{element_type}"
                result['vertices'] = self.get_vertices_by_type(vtype, strict=strict)
            else:
                result['vertices'] = self.get_all_vertices()

        # Edges (dimension 1)
        if dimension is None or dimension == 1:
            if element_type:
                result['edges'] = self.get_edges_by_type(element_type, strict=strict)
            else:
                result['edges'] = self.get_all_edges()

        # Faces (dimension 2)
        if dimension is None or dimension == 2:
            if element_type:
                result['faces'] = self.get_faces_by_type(element_type, strict=strict)
            else:
                result['faces'] = self.get_all_faces()

        return result

    def get_element_data(self, element_id: str) -> Optional[Dict[str, Any]]:
        """
        Get the data for any element by ID.

        Args:
            element_id: Element ID (vertex, edge, or face)

        Returns:
            Element data dictionary, or None if not found
        """
        if element_id in self.vertices:
            return self.vertices[element_id].data
        if element_id in self.edges:
            return self.edges[element_id].data
        if element_id in self.faces:
            return self.faces[element_id].data
        return None

    def get_element_type(self, element_id: str) -> Optional[str]:
        """
        Get the type of any element by ID.

        Args:
            element_id: Element ID (vertex, edge, or face)

        Returns:
            Element type string, or None if not found
        """
        if element_id in self.vertices:
            return self.vertices[element_id].type
        if element_id in self.edges:
            return self.edges[element_id].type
        if element_id in self.faces:
            return self.faces[element_id].type
        return None

    def list_types(self, dimension: Optional[int] = None) -> Dict[str, List[str]]:
        """
        List all types present in the complex.

        Args:
            dimension: 0 for vertex types, 1 for edge types, 2 for face types,
                      None for all

        Returns:
            Dictionary with keys 'vertex_types', 'edge_types', 'face_types'
            containing lists of type strings
        """
        result = {'vertex_types': [], 'edge_types': [], 'face_types': []}

        if dimension is None or dimension == 0:
            result['vertex_types'] = sorted(set(v.type for v in self.vertices.values()))

        if dimension is None or dimension == 1:
            result['edge_types'] = sorted(set(e.type for e in self.edges.values()))

        if dimension is None or dimension == 2:
            result['face_types'] = sorted(set(f.type for f in self.faces.values()))

        return result

    # ========== Boundary Operations (Simplicial Complex) ==========

    def get_boundary(self, element_id: str) -> Optional[List[str]]:
        """
        Get the boundary of an element.

        In a simplicial complex:
        - Boundary of a vertex (0-simplex) is empty []
        - Boundary of an edge (1-simplex) is its two endpoint vertices
        - Boundary of a face (2-simplex) is its three boundary edges

        Args:
            element_id: Element ID (vertex, edge, or face)

        Returns:
            List of boundary element IDs, or None if element not found

        Examples:
            get_boundary('v:doc:test')      # Returns [] (vertices have empty boundary)
            get_boundary('e:verification:a') # Returns ['v:doc:test', 'v:spec:test']
            get_boundary('f:assurance:test') # Returns ['e:verification:a', 'e:validation:a', 'e:coupling:a']
        """
        if element_id in self.vertices:
            # Vertices (0-simplices) have empty boundary
            return []

        if element_id in self.edges:
            # Edges (1-simplices) have vertices as boundary
            edge = self.edges[element_id]
            return [edge.source, edge.target]

        if element_id in self.faces:
            # Faces (2-simplices) have edges as boundary
            face = self.faces[element_id]
            return list(face.edges)

        return None

    def get_edge_boundary(self, edge_id: str) -> Optional[Tuple[str, str]]:
        """
        Get the boundary vertices of an edge.

        Args:
            edge_id: Edge ID

        Returns:
            Tuple of (source_vertex_id, target_vertex_id), or None if not found
        """
        edge = self.edges.get(edge_id)
        if edge:
            return (edge.source, edge.target)
        return None

    def get_face_boundary(self, face_id: str) -> Optional[List[str]]:
        """
        Get the boundary edges of a face.

        Args:
            face_id: Face ID

        Returns:
            List of edge IDs forming the boundary, or None if not found
        """
        face = self.faces.get(face_id)
        if face:
            return list(face.edges)
        return None

    def get_face_vertices(self, face_id: str) -> Optional[List[str]]:
        """
        Get the vertices of a face.

        Args:
            face_id: Face ID

        Returns:
            List of vertex IDs, or None if not found
        """
        face = self.faces.get(face_id)
        if face:
            return list(face.vertices)
        return None

    def get_coboundary(self, element_id: str) -> List[str]:
        """
        Get the coboundary of an element (elements that have this in their boundary).

        In a simplicial complex:
        - Coboundary of a vertex is all edges containing it
        - Coboundary of an edge is all faces containing it in their boundary

        Args:
            element_id: Element ID (vertex or edge)

        Returns:
            List of element IDs that have this element in their boundary

        Examples:
            get_coboundary('v:doc:test')       # Returns edges that have this vertex
            get_coboundary('e:verification:a') # Returns faces that have this edge
        """
        if element_id in self.vertices:
            # Coboundary of vertex = all edges incident to it
            return self.get_edges_incident(element_id)

        if element_id in self.edges:
            # Coboundary of edge = all faces containing it
            return self.get_faces_containing_edge(element_id)

        # Faces have no coboundary in a 2-complex
        if element_id in self.faces:
            return []

        return []

    def get_dimension(self, element_id: str) -> Optional[int]:
        """
        Get the dimension of an element.

        Args:
            element_id: Element ID

        Returns:
            0 for vertex, 1 for edge, 2 for face, None if not found
        """
        if element_id in self.vertices:
            return 0
        if element_id in self.edges:
            return 1
        if element_id in self.faces:
            return 2
        return None

    def is_in_boundary(self, inner_id: str, outer_id: str) -> bool:
        """
        Check if an element is in the boundary of another element.

        Args:
            inner_id: Potential boundary element ID
            outer_id: Element to check boundary of

        Returns:
            True if inner_id is in the boundary of outer_id
        """
        boundary = self.get_boundary(outer_id)
        if boundary is None:
            return False
        return inner_id in boundary

    def closure(self, element_ids: List[str]) -> Dict[str, List[str]]:
        """
        Compute the closure of a set of elements.

        The closure includes all elements plus their boundaries recursively.

        Args:
            element_ids: List of element IDs

        Returns:
            Dictionary with 'vertices', 'edges', 'faces' containing
            all elements in the closure
        """
        result = {'vertices': set(), 'edges': set(), 'faces': set()}

        to_process = list(element_ids)
        processed = set()

        while to_process:
            eid = to_process.pop()
            if eid in processed:
                continue
            processed.add(eid)

            # Add to appropriate set
            if eid in self.vertices:
                result['vertices'].add(eid)
            elif eid in self.edges:
                result['edges'].add(eid)
                # Add boundary (vertices)
                boundary = self.get_boundary(eid)
                if boundary:
                    to_process.extend(boundary)
            elif eid in self.faces:
                result['faces'].add(eid)
                # Add boundary (edges) and their vertices
                boundary = self.get_boundary(eid)
                if boundary:
                    to_process.extend(boundary)

        return {
            'vertices': sorted(result['vertices']),
            'edges': sorted(result['edges']),
            'faces': sorted(result['faces'])
        }

    def star(self, vertex_id: str) -> Dict[str, List[str]]:
        """
        Compute the star of a vertex - all simplices containing it.

        Args:
            vertex_id: Vertex ID

        Returns:
            Dictionary with 'vertices', 'edges', 'faces' containing
            all elements in the star
        """
        result = {'vertices': [vertex_id], 'edges': [], 'faces': []}

        # Edges containing this vertex
        result['edges'] = self.get_edges_incident(vertex_id)

        # Faces containing this vertex
        result['faces'] = self.get_faces_containing_vertex(vertex_id)

        return result

    def link(self, vertex_id: str) -> Dict[str, List[str]]:
        """
        Compute the link of a vertex.

        The link consists of all simplices in closure(star(v)) that don't contain v.

        For a vertex in a 2-complex:
        - Link vertices: opposite vertices in faces containing v
        - Link edges: edges in faces containing v that don't contain v

        Args:
            vertex_id: Vertex ID

        Returns:
            Dictionary with 'vertices', 'edges' containing elements in the link
        """
        result = {'vertices': set(), 'edges': set()}

        # For each face containing the vertex
        for face_id in self.get_faces_containing_vertex(vertex_id):
            face = self.faces[face_id]

            # Add vertices that are not the query vertex
            for vid in face.vertices:
                if vid != vertex_id:
                    result['vertices'].add(vid)

            # Add edges that don't contain the query vertex
            for eid in face.edges:
                edge = self.edges.get(eid)
                if edge and vertex_id not in (edge.source, edge.target):
                    result['edges'].add(eid)

        return {
            'vertices': sorted(result['vertices']),
            'edges': sorted(result['edges'])
        }

    # ========== Statistics ==========

    def statistics(self) -> Dict[str, Any]:
        """Get complex statistics."""
        return {
            'vertices': len(self.vertices),
            'edges': len(self.edges),
            'faces': len(self.faces),
            'vertex_types': len(set(v.type for v in self.vertices.values())),
            'edge_types': len(set(e.type for e in self.edges.values())),
            'face_types': len(set(f.type for f in self.faces.values())),
        }


# Backwards compatibility alias
ComplexGraph = SimplicialComplex


def build_simplicial_complex(cache: Dict[str, Any]) -> SimplicialComplex:
    """
    Build a SimplicialComplex from cache data.

    Convenience function wrapping SimplicialComplex.from_cache().

    Args:
        cache: Parsed complex.json data

    Returns:
        SimplicialComplex instance
    """
    return SimplicialComplex.from_cache(cache)


# Backwards compatibility alias
build_complex_graph = build_simplicial_complex
