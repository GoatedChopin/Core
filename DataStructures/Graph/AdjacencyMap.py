from collections import deque


class AdjacencyMap:
    def __init__(self, directed=False):
        self.map = {}
        self.directed = directed
    
    def addNode(self, node):
        if node not in self.map:
            self.map[node] = []
    
    def connect(self, start, end):
        self.map[start].append(end)
        if not self.directed:
            self.map[end].append(start)

    def existsPath(self, start, end):
        queue = deque()
        visited = set()
        current = start
        for neighbor in self.map[current]:
            queue.appendleft(neighbor)
            visited.add(neighbor)
        while len(queue) > 0:
            current = queue.pop()
            if current == end:
                return True
            for neighbor in self.map[current]:
                if neighbor not in visited:
                    queue.appendleft(neighbor)
                    visited.add(neighbor)
        return False

    def shortestPathLength(self, start, end):
        if start == end:
            return 0

        queue = deque()
        visited = set()
        current = start

        for neighbor in self.map[current]:
            queue.appendleft((1, neighbor))
            visited.add(neighbor)

        while len(queue) > 0:
            current_length, current = queue.pop()
            if current == end:
                return current_length
            for neighbor in self.map[current]:
                if neighbor not in visited:
                    queue.appendleft((current_length + 1, neighbor))
                    visited.add(neighbor)
        return -1


if __name__ == "__main__":
    am = AdjacencyMap()
    am.addNode("a")
    am.addNode("b")
    am.addNode("c")
    assert am.shortestPathLength("a", "b") == -1
    am.connect("a", "b")
    assert am.shortestPathLength("a", "b") == 1
    am.connect("b", "c")
    assert am.shortestPathLength("a", "c") == 2
