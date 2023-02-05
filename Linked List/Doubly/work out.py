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
        if self.head:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = self.tail = node

    def insertFirst(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
            node.prev = None
            self.head = node
        else:
            self.head = self.tail = node

    def insertLast(self, data):
        node = Node(data)
        if self.head:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = self.tail = node

    def insertBetween(self, index, data):
        node = Node(data)
        index -= 1
        count = 0
        prev = None
        current = self.head
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            while count != index:
                prev = current
                current = current.next
                count += 1
            prev.next = node
            node.prev = prev
            node.next = current

    def insertAfterThisValue(self, After, data):
        count = 0
        node = Node(data)
        prev = None
        current = self.head
        if self.head.data == After:
            node.next = self.head.next
            node.prev = self.head
        else:
            while current and current.data != After:
                prev = current
                current = current.next
            node.next = current.next
            current.next = node
            node.prev = current

    def insertBefore(self, before, data):
        node = Node(data)
        current = self.head
        prev = None
        if self.head.data == before:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            while current.data != before:
                prev = current
                current = current.next
            node.prev = prev
            prev.next = node
            node.next = current
            current.prev = node

    def deleteLast(self):
        if self.head:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            print('empty linkedlist aahn pottaaaa')

    def deleteFirst(self):
        if self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            print('empty linkedlist aahn pottaaaa')

    def deleteBefore(self, before):
        current = self.head
        prev = None
        if self.head.data == before:
            print('There is no Before The Element, this is Head')

        elif self.head.next.data == before:
            self.head = self.head.next
            self.head.prev = None
        else:
            while current.data != before:
                prev = current
                current = current.next
            element = prev.prev
            element.next = current
            current.prev = prev.prev

    def midElement(self):
        front = self.head
        back = self.tail
        while front:
            front = front.next
            if front == back:
                print('the Mid element is :', front.data)
            back = back.prev

    def whereIsMid(self):
        double = self.head
        single = self.head
        while double:
            double = double.next.next
            single = single.next
        print('Other way of find Mid element: ', single.data)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

    def displayReverse(self):
        last = self.tail
        while last:
            print(last.data, end=' ')
            last = last.prev


a = Linkedlist()
a.insertion(123)
a.insertion(345)
a.insertion(156324)
a.insertion(1234)
a.insertion(235123)
a.insertion(89769)
a.insertion(3424)
a.insertion(4352)
# a.display()
# print()
# a.insertFirst(10)
# a.display()
# print()
# a.insertLast(11)
# a.display()
# print()
# a.displayReverse()
# print()
# a.insertAfterThisValue(1234, 22)
# a.display()
# print()
# a.insertBetween(3, 33)
# a.display()
# print()
# a.insertBefore(123, 44)
# a.display()
# print()
# a.deleteLast()
# a.display()
# print()
# a.deleteFirst()
# a.display()
# print()
# a.deleteBefore(44)
# a.display()
# print()
a.midElement()
a.whereIsMid()
