class Node:
    def __init__(self, data) -> None:
        self.right=None
        self.left=None
        self.data=data

# def height(node):
#     if node is None:
#         return 0
#     return 1 + max(height(node.left), height(node.right))

# def diameter(root):
#     if root is None:
#         return 0
#     lheight = height(root.left)
#     rheight = height(root.right)

#     ldiameter = diameter(root.left)
#     rdiameter = diameter(root.right)

#     return max(lheight + rheight + 1, max(ldiameter, rdiameter))

def height(root, ans):
    if (root == None):
        return 0
    left_height = height(root.left, ans)
    right_height = height(root.right, ans)

    ans[0] = max(ans[0], 1+left_height+right_height)
    return 1 + max(left_height, right_height)

def diameter(root):
    if (root == None):
        return 0
    ans = [-99999999999]
    height_of_tree = height(root, ans)
    return ans[0]
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(diameter(root))