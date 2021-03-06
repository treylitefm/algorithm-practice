#silently fails when add/remove is unsuccessful; not very pythonic, i know #shame
class Graph(object): #this implementation is geared towards representing matrices as graphically
    vertices_to_edges = None
    vertex_values = None

    def __init__(self):
        self.vertices_to_edges = {}
        self.vertex_values = {}

    def add_vertex(self, vertex, value=None): #passed in as tuple of the form (y,x)
        self.vertices_to_edges[vertex] = []
        self.vertex_values[vertex] = value

    def remove_vertex(self, vertex):
        return self.vertices_to_edges.pop(vertex)

    def add_edge(self, vertex, edge): #adjacency list relationships are symmetric; a is adjacent to b iff b is adjacent to a; therefore we must add an edge to the entry for both vertices
        if vertex in self.vertices_to_edges and edge in self.vertices_to_edges:
            self.vertices_to_edges[vertex].append(edge)
            self.vertices_to_edges[edge].append(vertex)

    def remove_edge(self, vertex, edge):
        if vertex in self.vertices_to_edges and edge in self.vertices_to_edges:
            self.vertices_to_edges[vertex].remove(edge)
            self.vertices_to_edges[edge].remove(vertex)

    def neighbors(self, vertex):
        return self.vertices_to_edges[vertex]

    def adjacent(self, vertex_1, vertex_2):
        if vertex_1 in self.vertices_to_edges and vertex_2 in self.vertices_to_edges:
            return vertex_2 in self.vertices_to_edges[vertex_1]

    def get_vertex_value(self, vertex):
        return self.vertex_values[vertex]

    def set_vertex_value(self, vertex, value):
        if vertex in self.vertex_values:
            self.vertex_values[vertex] = value

    def __depth_first_traversal(self):
        pass
