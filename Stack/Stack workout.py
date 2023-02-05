class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

    def pop(self):
        if self.top:
            print('deleted value :',self.top.data)
            self.top = self.top.next
        else:
            print('your stack is empty')

    def peek(self):
        if self.top:
            print(self.top.data)
        else:
            print('your stack is empty')

    def is_empty(self):
        if self.top is None:
            print(True)
        else:
            print(False)
    def display(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next

a = Stack()
a.push(12)
a.push(12)
a.push(13)
a.push(14)
a.push(15)
a.push(16)
a.push(17)
a.push(19)
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.display()
print('\n')
a.pop()
print('\n')
a.display()
a.is_empty()
print()
a.pop()

a.peek()