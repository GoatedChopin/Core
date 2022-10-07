from heapq import heappush, heappop, heappushpop, heapify


class Heap:
    """
    Lazy implementation of a heap using heapq, will replace with the full binary tree logic soon(ish).
    """
    def __init__(self, elements=[], minheap=True):
        self.elements = elements
        if self.elements:
            heapify(self.elements)
        self.augment = 1 if minheap else -1

    def push(self, val):
        heappush(self.elements, val*self.augment)

    def pop(self):
        if self.elements:
            return heappop(self.elements)*self.augment

    def pushpop(self, val):
        return heappushpop(self.elements, val*self.augment)*self.augment
