# Node
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

# Binary Tree
class BinaryTree:
    def __init__(self, key):
        self.root = Node(key)

    def print_tree(self, root=None):
        
        if root:
            self.print_tree(root.left)
            self.print_tree(root.right)

if __name__ == '__main__':
    # Creating Below Binary Tree
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4  5  6   7
    tree = BinaryTree(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    tree.print_tree()