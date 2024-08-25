class Node:
    """Represents a single node in the binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """Represents the binary tree itself."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserts a new value into the binary tree."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Recursive helper function for inserting values."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def traverse_inorder(self):
        """Traverses the binary tree in-order and prints the values."""
        self._traverse_inorder_recursive(self.root)

    def _traverse_inorder_recursive(self, node):
        """Recursive helper function for in-order traversal."""
        if node is not None:
            self._traverse_inorder_recursive(node.left)
            print(node.value)
            self._traverse_inorder_recursive(node.right)

    def traverse_preorder(self):
        """Traverses the binary tree pre-order and prints the values."""
        self._traverse_preorder_recursive(self.root)

    def _traverse_preorder_recursive(self, node):
        """Recursive helper function for pre-order traversal."""
        if node is not None:
            print(node.value)
            self._traverse_preorder_recursive(node.left)
            self._traverse_preorder_recursive(node.right)

    def traverse_postorder(self):
        """Traverses the binary tree post-order and prints the values."""
        self._traverse_postorder_recursive(self.root)

    def _traverse_postorder_recursive(self, node):
        """Recursive helper function for post-order traversal."""
        if node is not None:
            self._traverse_postorder_recursive(node.left)
            self._traverse_postorder_recursive(node.right)
            print(node.value)
