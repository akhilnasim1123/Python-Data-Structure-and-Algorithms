class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,data):
        node = Node(data)
        if self.front:
            self.rear.next = node
            self.rear = node
        else:
            self.front = self.rear = node
    def dequeue(self):
        if self.front is None:
            print('queue is empty')
            self.rear = None
        else:
            self.front = self.front.next
    def display(self):
        current = self.front
        while current:
            print(current.data,end=' ')
            current = current.next

a = Linkedlist()
a.enqueue(1223)
a.enqueue(1)
a.enqueue(23)
a.enqueue(22)
a.enqueue(2)
a.enqueue(442)
a.enqueue(6783)
a.enqueue(24)
a.display()
print()
a.dequeue()
a.display()