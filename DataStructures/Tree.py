class BinarySearchTree:
    class BinaryNode:
        def __init__(self, val=None):
            self.val = val
            self.left = None
            self.right = None

        def add_child(self, node):
            if node.val < self.val:
                self.left = node
            else:
                self.right = node

        def has_children(self):
            return self.left is not None or self.right is not None

        def get_all_children_values(self):
            children = []
            if self.left is not None:
                children.append(self.left.val)
                children.extend(self.left.get_all_children_values())
            if self.right is not None:
                children.append(self.right.val)
                children.extend(self.right.get_all_children_values())
            return children

        def height(self):
            l = r = 0
            if self.left is not None:
                l = self.left.height()
            if self.right is not None:
                r = self.right.height()
            return 1 + max(l, r)

        def __lt__(self, other):
            return self.val < other.val

        def __gt__(self, other):
            return self.val > other.val

        def __str__(self):  # "{}/\n\t{}\\{}".format(self.left, self.val, self.right)
            return self.display()

        # Big thanks to J.V. at https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
        # for this pprint implementation
        def display(self, show=False):
            out = ""
            lines, *_ = self._display_aux()
            for line in lines:
                if show:
                    print(line)
                out = out + line + "\n"
            return out

        def _display_aux(self):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if self.right is None and self.left is None:
                line = '%s' % self.val
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if self.right is None:
                lines, n, p, x = self.left._display_aux()
                s = '%s' % self.val
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if self.left is None:
                lines, n, p, x = self.right._display_aux()
                s = '%s' % self.val
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = self.left._display_aux()
            right, m, q, y = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

    def __init__(self, rootval=None):
        self.root = self.BinaryNode(val=rootval)

    def insert(self, val):
        node = self.BinaryNode(val=val)
        if self.root.val is None:
            self.root = node
        current = self.root
        while current is not None:
            if node < current:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            elif node > current:
                if current.right is None:
                    current.right = node
                    break
                current = current.right
            else:
                raise ValueError("Duplicate values are not accepted in binary search trees.")

    def get_node_count(self):
        pass

    def get(self, val):
        """returns the node containing 'val' if val is in the Tree, returns None otherwise"""
        current = self.root
        while current is not None:
            if current.val == val:
                return current
            elif current.val < val:
                current = current.right
            else:
                current = current.left
        return None  # Not strictly necessary to return None, just more readable code

    def height(self):
        return self.root.height()

    def min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.val

    def max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.val

    def remove(self, val):  # FIX ME, BROKEN
        raise Exception("Not implemented error")
        """
        Implemented using get and get_successor,
        shifts all rightmost child nodes up one level
        to fill any resultant gaps
        """
        parent = self.get(val)
        if parent is not None:
            current = parent
            while current.right is not None:
                current.val = current.right.val
                current = current.right
            children = current.get_all_children_values()
            self.get(current.val).right = None
            for c in children:
                self.insert(c)

    def get_parent(self, val):
        """
        Returns the node directly above val in the tree,
        if both val and a parent for val
        exist in the tree
        """
        current = self.root
        while current is not None:
            l = r = None
            if current.left is not None:
                l = current.left.val
            if current.right is not None:
                r = current.right.val
            if val in (l, r):
                return current
            elif current.val < val:
                current = current.right
            else:
                current = current.left
        return None

    def get_successor(self, val):
        """
        Out of the nodes in Tree with values greater than 'val',
        returns the node with value closest to 'val'.
        If no such node exists, returns None.
        """
        node = self.get(val)
        if node.right is not None:
            current = node.right
            while current.left is not None:
                current = current.left
            return current
        elif (parent := self.get_parent(val)) is not None:
            while parent is not None:
                parent = self.get_parent(parent.val)
                if parent.val > val:
                    return parent
        return None

    def __str__(self):
        return str(self.root)


if __name__ == "__main__":
    bst = BinarySearchTree(6)
    bst.insert(4)
    bst.insert(8)
    bst.insert(7)
    bst.insert(9)
    bst.insert(5)
    bst.insert(3)
    breakpoint()