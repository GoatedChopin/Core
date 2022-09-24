from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.l = LinkedList()

    def enqueue(self, val):
        self.l.pushLeft(val)

    def dequeue(self):
        if not self.l.empty():
            return self.l.popRight()
