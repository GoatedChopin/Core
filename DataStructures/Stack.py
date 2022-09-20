class Stack:
    def __init__(self):
        self.l = []

    def push(self, val):
        self.l.append(val)

    def pop(self):
        if self.l:
          return self.l.pop()
        return None

    def peek(self):
        if self.l:
            return self.l[-1]
        return None


if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(5)
    s.push(6)
    assert s.peek() == 6
    assert s.pop() == 6
    assert s.peek() == 5
    s.pop()
    s.pop()
    assert s.pop() is None
    assert s.peek() is None
