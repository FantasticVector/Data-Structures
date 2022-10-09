class Node:
    def __init__(self):
        self.data = None
        self.next = None
    
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self, next):
        self.next = next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next is not None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def circularListLength(self):
        current = self.head
        count = 0
        if current is None: return 0
        currentNode = currentNode.getNext()