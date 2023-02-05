class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class Solution:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertion(self,data):
        newNode = Node(data)
        if self.head:
            current  = self.head
            while current.next:
                current = current.next
            current.next = newNode
            self.tail = newNode
        else:
            self.head = self.tail = newNode

    def findDuplicate(self):
        current = self.head
        prev = current
        while current.next != None:
            if current.next.data != current.data:
                current= current.next
            current.next = current.next.next





    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


a = Solution()
a.insertion(1)
a.insertion(1)
a.insertion(2)

a.findDuplicate()
a.display()


