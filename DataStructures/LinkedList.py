class ListNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def pushLeft(self, val):
        if not self.head:
            self.size = 1
            self.head = ListNode(val=val)
            self.tail = self.head
            return
        node = ListNode(val=val, right=self.head)
        self.head.left = node
        self.head = node
        self.size += 1

    def pushRight(self, val):
        if not self.tail:
            self.size = 1
            self.head = ListNode(val=val)
            self.tail = self.head
            return
        node = ListNode(val=val, left=self.tail)
        self.tail.right = node
        self.tail = node
        self.size += 1

    def peekLeft(self):
        if self.size > 0:
            return self.head.val

    def peekRight(self):
        if self.size > 0:
            return self.tail.val

    def popLeft(self):
        if self.size > 0:
            val = self.head.val
            self.head = self.head.right
            self.size -= 1
            if not self.size:
                # print("Removing tail as well")
                self.tail = None
            return val

    def popRight(self):
        if self.size > 0:
            val = self.tail.val
            self.tail = self.tail.left
            self.size -= 1
            if not self.size:
                # print("Removing head as well")
                self.head = None
            return val

    def inList(self, val):
        node = self.head
        while node:
            if node.val == val:
                return True
            node = node.right
        return False

    def __str__(self):
        out = ""
        node = self.head
        while node:
            out = out + " <-> {}".format(node.val)
            node = node.right
        out = out + " <->"
        return out


if __name__ == "__main__":
    l = LinkedList()
    l.pushLeft(1)
    assert l.peekRight() == 1
    assert not l.inList(5)
    l.pushLeft(5)
    assert l.inList(5)
    assert l.peekRight() == 1
    assert l.peekLeft() == 5
    l.pushRight(3)
    assert l.peekRight() == 3
    assert l.popRight() == 3
    assert l.popLeft() == 5
    assert l.popLeft() == 1
    assert not l.popLeft()
    assert not l.popRight()
    assert not l.peekLeft()
    assert not l.peekRight()
