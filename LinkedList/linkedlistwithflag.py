from calendar import c


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.flag = 0

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        return 
    
    # Detecting Loop using Flag
    def hasLoop(self):
        current = self.head
        while current:
            if current.flag == 1: return True
            current.flag = 1
            current = current.next
        return False
    
    # Detecting Loop using Flloyd-Cycle
    def hasLoopFloyd(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False
   # Removing Loop Using Flag 
    def removeLoopUsingFlag(self):
        prev = self.head
        current = self.head
        while current:
            if current.flag == 1:
                prev.next = None
                break
                #prev.next = None
            current.flag = 1
            prev = current
            current = current.next
        return 

    def NthNodeFromEnd(self, k):
        # Total nodes in list
        nodes = 0
        current = self.head
        while current:
            current = current.next
            nodes+=1
        kth_node = self.head
        for _ in range(nodes-k):
            kth_node = kth_node.next
        print(kth_node.data)
    
    def MidNode(self):
        nodes = 0
        current = self.head
        while current:
            current = current.next
            nodes+=1
        mid_node = self.head
        for _ in range(nodes//2):
            mid_node = mid_node.next
        return mid_node.data
    
    def isPalindrome(self):
        data = ''
        current = self.head
        while current:
            data+=str(current.data)
            current = current.next
        if data == data[::-1]:
            return True
        return False
    
    def removeDuplicatesUnsorted(self):
        table = set()
        current = self.head
        table.add(self.head.data)
        while current.next is not None:
            if current.next.data in table:
                current.next = current.next.next
            else:
                table.add(current.next.data)
                current = current.next
    def removeDuplicatesSorted(self):
        current = self.head
        while current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
    
    def reverseLinkedList(self):
        prev = None
        current = self.head
        next = None

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def hasIntersection(self, head1, head2):
        while head2:
            temp = head1
            while temp:
                if temp == head2:
                    return True
                temp = temp.next
            head2 = head2.next
        return False

    def getIntersectionNode(self,head1, head2):
        ptr1 = head1
        ptr2 = head2
        while ptr1!=ptr2:
            ptr1 = head2 if ptr1 is None else ptr1.next
            ptr2 = head1 if ptr2 is None else ptr2.next
        return ptr2.data
    
    def deleteNodeWithoutHead(self, curr_node):
        curr_node.data = curr_node.next.data
        curr_node.next = curr_node.next.next
        return curr_node
    
    def rotateLinkedList(self, k):
        # Time Complexity = k*N
        # current = self.head
        # for i in range(k):
        #     while current.next is not None:
        #         prev = current
        #         current = current.next
        #     prev.next = None
        #     current.next = self.head
        #     self.head = current
        if k == 0: return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = self.head
        current = self.head

        for i in range(k-1):
            current = current.next
        self.head = current.next
        current.next = None
        return self.head
            
        

        
if __name__ == '__main__':
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)

    #ll.display()
    ll.rotateLinkedList(4)
    ll.display()