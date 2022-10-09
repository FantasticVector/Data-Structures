class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
  
# Inorder traversal of a binary tree
def Preorder(root, traversal):
    if(root):
        traversal += (str(root.data) + '-')
        traversal = Preorder(root.left, traversal)
        traversal = Preorder(root.right,traversal)
    return traversal

# Inorder traversal of a binary tree
def Inorder(root, traversal):
    if(root):
        traversal = Inorder(root.left, traversal)
        traversal += (str(root.data) + '-')
        traversal = Inorder(root.right,traversal)
    return traversal
# Postorder traversal of a binary tree
def Postorder(root, traversal):
    if(root):
        traversal = Postorder(root.left, traversal)
        traversal = Postorder(root.right,traversal)
        traversal += (str(root.data) + '-')
    return traversal
                
# Driver code
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print(Inorder(root, ''))
    print(Preorder(root, ''))