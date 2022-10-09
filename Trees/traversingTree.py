class Node:
    def __init__(self, data) -> None:
        self.right = None
        self.left = None
        self.data = data
        
def inorder(root):
    stack = []
    curr = root
    done = 0
    
    while(True):
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        elif(stack):
            curr = stack.pop()
            print(curr.data, end=' ')
            curr = curr.right
        else:
            break
    print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.left.right= Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
inorder(root)
            

