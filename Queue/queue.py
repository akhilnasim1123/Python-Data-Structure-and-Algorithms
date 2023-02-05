class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        if self.front:
            self.rear.next = node
            self.rear = node
        else:
            self.front = self.rear = node

    def dequeue(self):
        if self.front == None:
            print('Queue is empty')
            self.rear = None
        else:
            self.front = self.front.next

    def display(self):
        current = self.front
        while current:
            print(current.data, end=' ')
            current = current.next


a= Linkedlist()
a.enqueue(452)
a.enqueue(234)
a.enqueue(896)
a.enqueue(46)
a.enqueue(284)
a.enqueue(476)
a.enqueue(348)
a.enqueue(24)
a.enqueue(8902)
a.enqueue(5427)
a.enqueue(13234)
a.display()
print()
a.dequeue()
a.display()
