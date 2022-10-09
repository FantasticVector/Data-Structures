class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
def Inorder(root, traversal=''):
    if(root):
        traversal += (str(root.data) + '-')
        traversal = Inorder(root.left, traversal)
        traversal = Inorder(root.right,traversal)
    return traversal


def deleteNode(root, key):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return root
    
    key_node = None
    temp = None
    last = None
    q = []
    q.append(root)
    while(q):
        temp = q[0]
        q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            last = temp
            q.append(temp.left)
        if temp.right:
            last = temp
            q.append(temp.right)
        
    if key_node is not None:
        key_node.data = temp.data
        if last.right == temp:
            last.right = None
        else:
            last.left = None
        temp = None
    return root

#       1
#     /   \
#    2     3
#   / \   / \
#  4  5  6   7
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(Inorder(root))
deleteNode(root, 2)
print(Inorder(root))