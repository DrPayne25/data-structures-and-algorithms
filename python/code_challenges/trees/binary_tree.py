from code_challenges.trees.node import Node

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        # order for pre_order root > left > right
        values = []
        if self.root is None:
            raise Exception("Sorry this Tree is currently empty")

        def walk(root):
            if root:
                values.append(root.value)
                walk(root.left)
                walk(root.right)
        walk(self.root)
        return values

    def in_order(self):
        # order for in_order left > root > right
        values = []

        if self.root == None:
            raise Exception("Sorry this Tree is currently empty")

        def walk(node):
            if node:
                walk(node.left)
                values.append(node.value)
                walk(node.right)
        walk(self.root)
        return values

    def post_order(self):
        # order for post_order left > right > root
        values = []

        if self.root == None:
            raise Exception("Sorry this Tree is currently empty")

        def walk(node):
            if node:
                walk(node.left)
                walk(node.right)
                values.append(node.value)
        walk(self.root)
        return values

class BinarySearchTree(BinaryTree):

    def add(self, value):
        def walk(root):
            if value < root.value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    walk(root.left)
            else:
                if root.right is None:
                    root.right = Node(value)
                else:
                    walk(root.right)
        walk(self.root)

    def contains(self, value):
        def walk(root):
            if root is None:
                return False
            elif root.value == value:
                return True
            elif value < root.value:
                return walk(root.left)
            else:
                return walk(root.right)
        return walk(self.root)
