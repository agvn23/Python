class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root_value):
        self.root = BSTNode(root_value)

    def insert(self, value):
        """Insert a new value into the BST."""
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = BSTNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else: # value >= current_node.value goes to the right
            if current_node.right is None:
                current_node.right = BSTNode(value)
            else:
                self._insert_recursive(current_node.right, value)
                
    def search(self, value):
        """
        Search for 'value' starting from the root.
        Return True if found, False otherwise.
        """
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False


bst = BinarySearchTree(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(9)
bst.insert(20)
bst.insert(12)
bst.insert(18)

print(bst.search(5)) # Expected: True
print(bst.search(50)) # Expected: False