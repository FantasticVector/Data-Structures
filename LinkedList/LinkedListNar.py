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
        return self.next != None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def listLength(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count+=1
        return count
    
    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.setData(data)
        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length += 1
    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(newNode)
        self.length += 1
    def insertAtPos(self, pos, data):
        if pos > self.length or pos < 0: return None
        else: 
            if pos == 0: self.insertAtBeginning
            else:
                if pos == self.length: 
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    newNode.setData(data)
                    current = self.head
                    count = 0
                    while count < pos-1:
                        count+=1
                        current = current.getNext()
                    newNode.setNext(current.getNext())
                    current.setNext(newNode)
                    self.length+=1
    def deleteFromBeginning(self):
        if self.length == 0: return 'The List is Empty'
        else:
            self.head = self.head.getNext()
            self.length -= 1
    def deleteFromEnd(self):
        if self.length == 0: return 'The List is Empty'
        else:
            current = self.head
            prev = self.head
            while current.getNext() is not None:
                prev = current
                current = current.getNext()
            prev.setNext(None)
            self.length -= 1
    def deleteNode(self, node):
        if self.length == 0: raise ValueError('List is Empty')
        else:
            current = self.head
            prev = None
            found = False
            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError('Node not in Linked List')
                else:
                    prev = current
                    current = current.getNext()
            if prev is None:
                self.head = current.getNext()
            else:
                prev.setNext(current.getNext())
            self.length -= 1
    def deleteValue(self, value):
        current = self.head
        prev = self.head
        while current.next is not None or current.value is not value:
            if current.value == value:
                prev.next = current.next
                self.length -= 1
                return
            else:
                prev = current
                current = current.next
            print('The value provided is not present')
    
    def deleteAtPosition(self, pos):
        count = 0
        current = self.head
        prev = self.head
        if pos > self.length or pos < 0:
            print('The position does not exist. Please enter valid position')
        else:
            while current.next != None or count < pos:
                count += 1
                if count == pos:
                    prev.next = current.next
                    self.length -= 1
                    return 
                else:
                    prev = current
                    current = current.next
    def clear(self):
        self.head = None
