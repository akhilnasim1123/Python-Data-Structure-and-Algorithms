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

    def insertionAfter(self, data, index):
        node = Node(data)
        count = 0
        index = index - 1
        current = self.head
        while count != index - 1:
            count += 1
            current = current.next
        val = current.next
        current.next = node
        node.next = val

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
a.insertionAfter(10, 5)
a.display()
