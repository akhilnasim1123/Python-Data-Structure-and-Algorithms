class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.top = None

    def push(self,data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
    def pop(self):
        if self.top:
            self.top = self.top.next
        else:
            print('Stack UnderFlow')

    def display(self):
        current = self.top
        while current:
            print(current.data,end=' ')
            current = current.next



a = Linkedlist()
a.push(123)
a.push(5634)
a.push(1231123)
a.push(234123)
a.push(67856)
a.push(67312)
a.push(9876)
a.push(788944)
a.push(43683)
a.push(35828)
a.push(1)
a.display()
print()
a.pop()
a.display()
