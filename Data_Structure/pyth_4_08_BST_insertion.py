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
        else:  # value >= current_node.value goes to the right
            if current_node.right is None:
                current_node.right = BSTNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def in_order_traversal(self, node, visit_list):
        """In-order yields ascending order for a BST."""
        if node is None:
            return
        self.in_order_traversal(node.left, visit_list)
        visit_list.append(node.value)
        self.in_order_traversal(node.right, visit_list)

bst = BinarySearchTree(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(9)
bst.insert(20)
bst.insert(12)
bst.insert(18)

values = []
bst.in_order_traversal(bst.root, values)
print("In-order traversal (sorted):", values)
# Expected output: In-order traversal (sorted): [2, 5, 7, 9, 10, 12, 15, 18, 20] 