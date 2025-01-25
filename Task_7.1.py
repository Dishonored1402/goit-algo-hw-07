class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def find_max(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.key

bst = BinarySearchTree()
elements = [20, 10, 30, 5, 15, 25, 35]

for el in elements:
    bst.insert(el)

max_value = bst.find_max()
print(f"Найбільше значення в дереві: {max_value}")
