class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertion(self, data):
        current = self.head
        node = Node(data)

        if self.head:
            node = Node(data)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = None
        else:
            self.head = self.tail = node

    def deleteValue(self, value):
        current = self.head
        while current.data != value:
            prev = current
            current = current.next
        if self.head.data == value:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail.data == value:
            self.tail = prev
            self.tail.next = None
        else:
            prev.next = current.next
            prev.next.prev = prev

    def display(self):
        current = self.head
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
a.deleteValue(89769)

a.display()