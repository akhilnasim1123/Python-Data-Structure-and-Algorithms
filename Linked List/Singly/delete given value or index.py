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
    def deleteValue(self,value):
        current = self.head
        if self.head.data == value:
            self.head = current.next
        else:
            while current.data != value:
                prev = current
                current = current.next
            prev.next = current.next
    def deleteIndex(self,index):
        index -= 1
        current = self.head
        count = 0
        while count != index-1:
            current= current.next
            count += 1
        current.next = current.next.next




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
# a.deleteValue(235123)
a.deleteIndex(2)
a.display()