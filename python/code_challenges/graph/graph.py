from code_challenges.stack_and_queue.queues import Queue

class Graph:

    def __init__(self):
        # key will be the node, value adj node with a value of the edge
        self.adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, vertex_1, vertex_2, weight=1):
            # Arguments: 2 nodes to be connected by the edge, weight (optional)
            # Returns: nothing
            # Adds a new edge between two nodes in the graph
            # If specified, assign a weight to the edge
            # Both nodes should already be in the Graph
        if vertex_1 and vertex_2 not in self.adjacency_list:
            raise Exception
        edge = Edge(vertex_2,weight)
        self.adjacency_list[vertex_1].append(edge)

    def get_node(self):
            # Arguments: none
            # Returns all nodes in graph as a collection (set, list, or similar)
        return list(self.adjacency_list.keys())

    def get_neighbor(self, vertex):
            # Arguments: node
            # Returns a collection of edges connected to the given node
                # Include the weight of connection in returned collection
        return self.adjacency_list[vertex]

    def size(self):
        return len(self.adjacency_list)
            # Arguments: none
            # Returns the total number of nodes in the graph

    def breadthfirst(self, vertex):
        nodes = list()
        breadth = Queue()
        visited = set()
        breadth.enqueue(vertex)
        visited.add(vertex)
        while breadth:
            front = breadth.dequeue()
            nodes.append(front)
            for child in nodes:
                if child not in visited:
                    visited.add(child)
                    breadth.enqueue(child)
        return nodes




class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex,weight=1):
        self.vertex = vertex
        self.weight = weight
