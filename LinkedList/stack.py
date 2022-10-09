# Implementing Stack using Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

class Stack:
    def __init__(self):
        self.head = Node('head')
        self.size = 0
    
    def __str__(self):
        curr= self.head.next
        out = ''
        while curr:
            out+=str(curr.data)+'->'
            curr = curr.next
        return out[:-2]
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def peek(self):
        if self.isEmpty():
            raise Exception('Peeking from an empty stack')
        return self.head.next.value
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            raise Exception('Poping from an empty stack')
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.data
    
if __name__ == '__main__':
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f'Stack: {stack}')

    for i in range(1, 6):
        remove = stack.pop()
        print(f'Pop: {remove}')
    
    print(f'Stack: {stack}')
    