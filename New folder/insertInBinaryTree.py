# Insertion in a Binary Tree in level order
class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.key = key


def inorder(temp):

    if not temp:
        return

    inorder(temp.left)
    print(temp.key, end=' ')
    inorder(temp.right)


def insert(temp, key):

    if not temp:
        root = Node(key)
        return
    q = []
    q.append(temp)
    while(len(q)):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)


root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

print('Inorder Traversel before: ', end=' ')
inorder(root)

key = 12
insert(root, key)

print()
print('Inorder traversal after insertion: ', end=' ')
inorder(root)