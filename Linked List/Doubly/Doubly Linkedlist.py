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
        node = Node(data)

        if self.head is None:
            self.head = self.tail = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current
            node = self.tail

    def insertionAt(self, data, index):
        index = index - 1
        count = 0
        node = Node(data)
        current = self.head
        while count != index:
            count = count + 1
            prev = current
            current = current.next
        if current == self.head:
            current.prev = node
            node.next = current
            self.head = node
        else:
            next = current.next
            current.next = node
            node.prev = current
            next.prev = node
            node.next = next

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
a.insertionAt(10, 3)
a.display()
