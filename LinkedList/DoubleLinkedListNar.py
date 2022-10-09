class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self, next):
        self.next = next
    def getNext(self, next):
        return self.next
    def hasNext(self):
        return self.next is not None
    def setPrev(self, prev):
        self.prev = prev
    def getPrev(self):
        return self.prev
    def hasPrev(self):
        return self.prev is not None
    def __str__(self):
        return 'Node[Data=%s]'%(self.data,)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode
    
    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            current.next = newNode
            newNode.setPrev(current)
    def insertAtGivenPos(self, data, index):
        newNode = Node()
        newNode.setData(data)
        if self.head is None or index == 0:
            self.insertAtBeginning(data)
        elif index > 0:
            temp = self.getNode(index)
            if temp == None or temp.getNext() is None:
                self.insertAtEnd(data)
            else:
                newNode.setNext(temp.getNext())
                newNode.setPrev(temp)
                temp.getNext().setPrev(newNode)
                temp.setNext(newNode)
    
    def getNode(self, index):
        current = self.head
        if current is None: return 'List is Empty'
        i = 0
        while i<index and current.getNext() is not None:
            current = current.getNext()
            if current is None:
                break
            i+=1
        return current
    
    def deleteWithData(self, data):
        temp = self.head
        while temp is not None:
            if temp.getData() == data:
                if temp.getNext() is not None:
                    temp.getNext().setNext(temp.getNext())
                    temp.getNext().setPrev(temp.getPrev())
                else:
                    self.head = temp.getNext()
                    temp.getNext().setPrev(None)
            temp = temp.getNext()
