class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def reversed(self):
        prev = None
        while self.head:
            next = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = next
        self.head = prev
    def insertion(self,data):
        node = Node(data)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
    def sizeOf(self):
        current = self.head
        count = 0
        while current:
            current = current.next
            count +=1
        return count

    def binaryToDecimal(self):
        current  = self.head
        d = 0
        s = self.sizeOf()-1
        while current:
            d+=current.data*(2**s)
            s-=1
            current = current.next
        return d
    def binary(self):
        current = self.head
        d = 0
        s = self.sizeOf()-1
        while current:
            d+=current.data*(2**s)
            s-=1
            current = current.next
        print(d)
    def reverse(self):
        prev = None
        while self.head:
            next = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = next
        self.head = prev
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
print(a.binaryToDecimal())
a.binary()
a.reversed()
a.display()