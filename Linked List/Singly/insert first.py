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

    def insertFirst(self, data):
        node = Node(data)
        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insertInBetween(self, index, data):
        node = Node(data)
        if self.head != None:
            count = 0
            current = self.head
            index = index-1
            if index == 0:
                node.next = self.head
                self.head = node
            else:

                while count != index - 1:
                    count = count + 1
                    current = current.next
                node.next = current.next
                current.next = node
        else:
            print('ur linked list is empty')
    # def insertIndex(self,index,data):
    #     current = self.head
    #     count = 0
    #     index -= 1
    #     prev = None
    #     node = Node(data)
    #     if index == 0:
    #         self.head = self.head.next
    #     else:
    #         while count != index:
    #             prev = current
    #             current = current.next
    #             count +=1
    #         node.next = current
    #         prev.next = node
    def delete_last(self):
        current = self.head
        prev = None
        if self.head and self.tail:
            while current.next:
                prev = current
                current = current.next
            self.tail = prev
            self.tail.next = None
        else:
            print('linked list is empty')
    def delete_first(self):
        if self.head:
            self.head = self.head.next
        else:
            print('linked list is empty')



    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
    def delete_by_index(self,index):
        count = 0
        index -= 1
        prev = None
        current = self.head
        if index == 0:
            self.head = self.head.next
        else:
            while count != index:
                prev =  current
                current = current.next
                count +=1
            prev.next = current.next
    def delete_by_value(self,value):
        current = self.head
        prev = None
        if self.head.data == value:
            self.head= self.head.next
        else:
            while current.data != value:
                prev = current
                current = current.next
            prev.next = current.next
    def reverse(self):
        prev = None
        while self.head:
            next = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = next
        self.head = prev
    def printEven(self):
        current = self.head
        while current:
            if current.data%2==0:
                print(current.data,end=' ')
            current = current.next
    def altrenative(self):
        current = self.head
        while current:
            next = current.next.next
            if next:
                print(next.data, end=' ')
                current = current.next.next



a = Linkedlist()
a.insertion(123)
a.insertion(345)
a.insertion(156324)
a.insertion(1234)
a.insertion(235123)
a.insertion(89769)
a.reverse()
a.display()
print()
b = Linkedlist()
b.insertion(0000)
b.insertion(111111)
b.insertion(77777)
a.printEven()
print()
a.altrenative()

