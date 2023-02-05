class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertion(self, data):
        node = Node(data)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
    def deleteFirst(self):
        current = self.head
        self.head = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next


a = Linkedlist()
a.insertion(123)
a.insertion(345)
a.insertion(156324)
a.insertion(1234)
a.insertion(235123)
a.insertion(89769)
a.deleteFirst()
a.display()
