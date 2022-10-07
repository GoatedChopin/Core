import random as r
import numpy as np
from Algorithms.Search import dijkstra


class CartesianGraph:
    class Node:
        def __init__(self, val=None, coordinate=(0, 0), neighbors=[]):
            self.val = val
            self.coordinate = np.array(coordinate)
            self.neighbors = neighbors
            self.total_distance = float('inf')

        def distance(self, other):
            return np.linalg.norm(self.coordinate - other.coordinate)

        def __str__(self):
            return str(self.coordinate)

        def __eq__(self, other):
            if type(other) == CartesianGraph.Node:
                return other.val == self.val
            else:
                return other == self.val

        def __lt__(self, other):
            if type(other) == CartesianGraph.Node:
                return self.total_distance < other.total_distance
            return self.total_distance < other

        def __gt__(self, other):
            return not self.__lt__(other)

        def __hash__(self):
            return hash(self.val) + hash(tuple(self.coordinate))

    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.start = None
        self.end = None

    def add_node(self, node):
        self.nodes.append(node)

    def connect_nodes(self, node1, node2):
        one, two = False, False
        for node in self.nodes:
            if node == node1:
                node.neighbors.append(node2)
                one = True
            if node == node2:
                node.neighbors.append(node1)
                two = True
            if one and two:
                return

    def shortest_path(self, start_node, end_node):
        return dijkstra(start_node, end_node)


if __name__ == "__main__":
    nodes = [CartesianGraph.Node(val=i, coordinate=(r.randint(i, 100), r.randint(i, 100))) for i in range(10)]
    graph = CartesianGraph(nodes=nodes)
    for node in graph.nodes:
        for i in range(3):
            while (other := r.choice(graph.nodes)) == node:
                other = r.choice(graph.nodes)
            graph.connect_nodes(node, other)
    for i in range(5):
        start, end = r.choice(graph.nodes), r.choice(graph.nodes)
        print("Traveling from {} to {}".format(start, end))
        path = graph.shortest_path(start, end)
        if type(path) != CartesianGraph.Node:
            node = path.head
            while node:
                print(node.val, sep=" -> ")
                node = node.right
        elif not path:
            print("No path between nodes")
