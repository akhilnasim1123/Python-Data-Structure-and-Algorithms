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
        if self.head is None:
            self.head = self.tail = node
        else:
            current = self.head
            self.tail.next = node
            self.tail = node
            # while current.next:
            #     current = current.next
            # current.next = node
            # self.tail = current
    def quick(self):
        self.quicksort(self.head,self.tail)
    def quicksort(self,start,end):
        if start is None:
            return
        piviot = start
        left = start.next
        right = end
        while start:
            if start.data > piviot.data >right.data:
                self.swap(start,right)
                start = start.next
    def swap(self,ar,i,j):
        pass
    def insertAtBegening(self,data):
        node = Node(data)
        if self.head is None:
            print('there is no linked list exist')
        else:
            current = self.head
            self.head = node
            self.head.next = current

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
a.insertAtBegening(10)
print(a.head.next.data)
a.display()
