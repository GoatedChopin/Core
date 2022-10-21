from heapq import heappush, heappop, heappushpop, heapify


class LazyHeap:
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


class Heap:
    """
    Full implementation of a heap using a binary tree,
    all children must be less than or equal to their parents.
    """
    class HeapNode:
        def __init__(self, val=None):
            self.val = None
            self.left = None
            self.right = None

    def __init__(self, val=None):
        self.head = self.HeapNode(val=val)

    def getMax(self):
        return self.head.val

    def push(self, val):
        pass

    def pop(self):
        pass

    def heapify(self):
        pass

    def siftDown(self):
        pass

    def siftUp(self):
        pass