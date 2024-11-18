import os
import pydot


class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list
        self.edges = []  # Edge list for Kruskal's algorithm
        self.image_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'img', 'graph.png')

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2, weight):
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append((node2, weight))
        self.graph[node2].append((node1, weight))  # Assuming undirected graph
        self.edges.append((node1, node2, weight))

    def get_graph(self):
        return self.graph

    def kruskal(self):
        """Apply Kruskal's algorithm to find the MST."""
        # Sort edges by weight
        self.edges.sort(key=lambda x: x[2])

        parent = {}
        rank = {}

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        for node in self.graph:
            parent[node] = node
            rank[node] = 0

        mst = []
        for edge in self.edges:
            node1, node2, weight = edge
            if find(node1) != find(node2):
                union(node1, node2)
                mst.append(edge)

        return mst

    def generate_graph_image(self, mst_edges=None):
        """Generate a graphical representation of the graph."""
        if not os.path.exists(os.path.dirname(self.image_path)):
            os.makedirs(os.path.dirname(self.image_path))

        graph = pydot.Dot(graph_type="graph")

        for node in self.graph:
            graph.add_node(pydot.Node(node, style="filled", fillcolor="lightblue"))

        for edge in self.edges:
            node1, node2, weight = edge
            color = "red" if mst_edges and edge in mst_edges else "black"
            graph.add_edge(pydot.Edge(node1, node2, label=str(weight), color=color))

        graph.write_png(self.image_path)
