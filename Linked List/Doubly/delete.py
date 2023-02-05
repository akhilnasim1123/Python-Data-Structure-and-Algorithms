class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertion(self,data):
        node = Node(data)
        if self.head:
            current = self.head
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = None
        else:
            self.head = self.tail = node
    def deleteLast(self):
        self.tail = self.tail.prev
        self.tail.next = None
    def deleteIndex(self,index):
        index -= 1
        count = 0
        current = self.head
        while count != index:
            count +=1
            prev = current
            current = current.next
        if current == self.head:
            self.head = current.next
            self.head.prev= None
        else:
            current.next = current.next.next
            current.next.prev = current
    def display(self):
        current= self.head
        while current:
            print(current.data, end=" ")
            current = current.next
a = Linkedlist()
a.insertion(123)
a.insertion(345)
a.insertion(156324)
a.insertion(1234)
a.insertion(235123)
a.insertion(89769)
a.deleteIndex(2)
a.display()

