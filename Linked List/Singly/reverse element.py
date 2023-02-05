class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertion(self,data):
        node = Node(data)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
    def reverse(self):
        current = self.head
        prev = None
        while self.head:
            next = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = next
        self.head = prev

    def whereIsMid(self):
        current = mid = self.head
        while current:
            current = current.next.next
            mid = mid.next
        print(mid.data)

    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next


a = Linkedlist()
a.insertion(123)
a.insertion(345)
a.insertion(156324)
a.insertion(1234)
a.insertion(235123)
a.insertion(89769)
a.reverse()
a.display()
print()
a.whereIsMid()
