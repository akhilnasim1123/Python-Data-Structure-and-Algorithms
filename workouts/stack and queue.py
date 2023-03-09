class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.max = 10

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

    def push(self, data):
        node = Node(data)
        if self.size() < self.max:
            if self.top:
                node.next = self.top
                self.top = node
            else:
                self.top = node
        else:
            print('stack overflow')

    def pop(self):
        if self.top:
            self.top = self.top.next
        else:
            print('Stack Underflow')

    def show_stack(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next

    def peek(self):
        if self.top:
            print('Top is : ', self.top.data)
        else:
            print('Stack Underflow')

    def is_empty(self):
        if self.top:
            print(False)
        else:
            print(True)

    def is_full(self):
        if self.size() >= self.max:
            print(True)
        else:
            print(False)


class Queue:
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
        if self.front:
            self.front = self.front.next
        else:
            print('queue is empty')
            self.rear = None

    def show_queue(self):
        current = self.front
        while current:
            print(current.data, end=' ')
            current = current.next


stack = Stack()
stack.is_full()
stack.is_empty()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.push(10) 
stack.show_stack()
stack.peek()
stack.is_full()
stack.is_empty()
stack.pop()
stack.show_stack()
stack.is_full()
stack.is_empty()
print('----------------------------------------------------------------------')
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.show_queue()
print()
queue.dequeue()
queue.show_queue()


