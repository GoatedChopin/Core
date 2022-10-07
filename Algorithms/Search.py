from DataStructures.Heap import Heap
from DataStructures.LinkedList import LinkedList

def dijkstra_length(start_node, end_node):
    if start_node == end_node:
        return 0
    visited = set()
    start_node.total_distance = 0
    current_node = start_node
    heap = Heap()
    total_distance = 0
    for node in current_node.neighbors:
        node.total_distance = min(node.total_distance, current_node.distance(node) + total_distance)
        heap.push((node.total_distance, node))
    while heap:
        previous_distance, current_node = heap.pop()
        if current_node == end_node:
            return current_node.total_distance
        total_distance = current_node.total_distance
        visited.add(current_node)
        for node in current_node.neighbors:
            node.total_distance = min(node.total_distance, current_node.distance(node) + total_distance)
            if node not in visited:
                visited.add(node)
                heap.push((node.total_distance, node))
    return None


def dijkstra(start_node, end_node):
    if start_node == end_node:
        return start_node
    visited = set()
    start_node.total_distance = 0
    current_node = start_node
    heap = Heap()
    total_distance = 0
    for node in current_node.neighbors:
        node.total_distance = min(node.total_distance, current_node.distance(node) + total_distance)
        heap.push((node.total_distance, node))
    while heap:
        previous_distance, current_node = heap.pop()
        if current_node == end_node:
            path = LinkedList()
            while current_node != start_node:
                path.pushLeft(current_node)
                current_node = min(current_node.neighbors)
            path.pushLeft(current_node)
            return path
        total_distance = current_node.total_distance
        visited.add(current_node)
        for node in current_node.neighbors:
            if node not in visited:
                node.total_distance = min(node.total_distance, current_node.distance(node) + total_distance)
                heap.push((node.total_distance, node))
    return None
