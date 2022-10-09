class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def __str__(self):
        curr = self.front
        value = ''
        while curr:
            value+=str(curr.data)+'->'
            curr = curr.next
        return value[:-2]
    
    def isEmpty(self):
        return self.front == None
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear == None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.isEmpty():
            return 
        self.front = self.front.next
        if self.front == None:
            self.rear = None

if __name__ == '__main__':
    q = Queue()
    for i in range(1, 10):
        q.enqueue(i)
    print(f'Queue: {q}')
    for i in range(1, 5):
        q.dequeue()
    print(f'Queue: {q}')