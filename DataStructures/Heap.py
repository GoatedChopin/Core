from heapq import heappush, heappop, heappushpop, heapify
from collections import deque


class Heap:
    """
    Please don't use any of the other heaps in this file, they're embarrassing.
    The tree one is broken and not worth fixing (it's much more efficient to use an array to back the heap anyway).
    """
    def __init__(self):
        self.elements = []
        self.size = 0

    def push(self, val):
        self.size += 1
        self.elements.append(val)
        self.siftUp(self.size-1)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            out_val = self.elements[0]
            self.elements[0] = self.elements[-1]
            self.elements.pop()
            self.siftDown(0)
            return out_val

    def siftDown(self, parent):
        largest = parent
        leftChild = 2 * parent + 1
        rightChild = 2 * parent + 2

        if leftChild < self.size and self.elements[leftChild] > self.elements[largest]:
            largest = leftChild
        if rightChild < self.size and self.elements[rightChild] > self.elements[largest]:
            largest = rightChild

        if largest != parent:
            self.swap(largest, parent)
            self.siftDown(largest)

    def siftUp(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        print("Parent is {}".format(parent))
        if self.elements[parent] < self.elements[index]:
            self.swap(parent, index)
            self.siftUp(parent)

    def swap(self, index_a, index_b):
        self.elements[index_a], self.elements[index_b] = self.elements[index_b], self.elements[index_a]


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


class MaxTreeHeap:
    """
    Full implementation of a heap using a binary tree,
    all children must be less than or equal to their parents.
    """
    def __init__(self, val=None, parent=None):
        raise NotImplementedError("This class is not fit for use, use Heap.Heap() instead.")
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

    def getMax(self):
        return self.head.val

    def push(self, val):
        node = self.first_empty_node()
        node.val = val
        node.siftUp()

    def pop(self):
        return_val = self.val
        self.val = -float("inf")
        node = self.siftDown()
        del node
        return return_val

    def siftDown(self):
        out = self
        if self.left is not None and self.left.val > self.val:
            largest = self.left
        elif self.right is not None and self.right.val > self.val:
            largest = self.right
        else:
            largest = self

        if largest != self:
            # print("Swapping {} with {}".format(largest.val, self.val))
            self.swap(largest)
            out = largest.siftDown()
        return out

    def siftUp(self):
        if self.parent is not None and self.parent.val < self.val:
            self.swap(self.parent)
            self.parent.siftUp()

    def swap(self, other):
        self.val, other.val = other.val, self.val

    def bfs(self, val):
        if self.val == val:
            return self
        queue = deque()
        if self.left is not None:
            queue.appendleft(self.left)
        if self.right is not None:
            queue.appendleft(self.right)
        while len(queue) > 0:
            current = queue.pop()
            if current.val == val:
                return current
            if current.left is not None:
                queue.appendleft(current.left)
            if current.right is not None:
                queue.appendleft(current.right)
        return None

    def first_empty_node(self):
        """
        O(n) time complexity to find empty spot, very bad for a heap,
        which is supposed to have O(log(n)) time complexity for push / pop
        """
        if self.val is None:
            return self
        queue = deque()
        if self.left is not None:
            queue.appendleft(self.left)
        else:
            self.left = MaxTreeHeap()
            return self.left
        if self.right is not None:
            queue.appendleft(self.right)
        else:
            self.right = MaxTreeHeap()
            return self.right

        while len(queue) > 0:
            current = queue.pop()
            if current.left is None:
                current.left = MaxTreeHeap()
                current.left.parent = current
                return current.left
            else:
                queue.appendleft(current.left)

            if current.right is None:
                current.right = MaxTreeHeap()
                current.right.parent = current
                return current.right
            else:
                queue.appendleft(current.right)


if __name__ == "__main__":
    import random as r
    heap = Heap()
    for i in range(1000):
        heap.push(r.randint(0, 1000))
    current = 1001
    for i in range(1000):
        next_val = heap.pop()
        print(next_val)
        assert current >= next_val
        current = next_val