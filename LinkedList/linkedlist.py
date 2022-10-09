class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    
    def detect_loop(self):
        hashmap = set()
        current = self.head
        while current:
            if (current in hashmap):
                return True
            hashmap.add(current)
            current = current.next
        return False
            

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

if __name__ == '__main__': 
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    ll.head.next = second
    second.next = third
    third.next = fourth

    ll.display()
    # # Print linked list items
    # while linked_list.head != None:
    #     print(linked_list.head.item, end=" ")
    #     linked_list.head = linked_list.head.next