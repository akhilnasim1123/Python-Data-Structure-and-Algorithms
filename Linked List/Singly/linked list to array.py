class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


from array import *

array = array('i', [])


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

    def LinkedlistToArray(self, array):
        current = self.head
        while current:
            array.append(current.data)
            current = current.next


a = Linkedlist()
a.insertion(123)
a.insertion(345)
a.insertion(156324)
a.insertion(1234)
a.insertion(235123)
a.insertion(89769)
a.LinkedlistToArray(array)
for i in range(len(array) - 1):
    print(array[i], end=' ')
