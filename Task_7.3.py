class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def sum_values(self):
        return self._sum_values(self.root)

    def _sum_values(self, node):
        if node is None:
            return 0
        return node.key + self._sum_values(node.left) + self._sum_values(node.right)

bst = BinarySearchTree()
elements = [20, 10, 30, 5, 15, 25, 35]
for el in elements:
    bst.insert(el)

total_sum = bst.sum_values()
print(f"Сума всіх значень у дереві: {total_sum}")
