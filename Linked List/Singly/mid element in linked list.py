class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class midElement:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertion(self,data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            self.tail = newNode
        else:
            self.head = self.tail = newNode
    def sort(self):
        current = self.head
        while current != None:
            nextElement = current.next
            while nextElement != None:
                if current.data > nextElement.data:
                    temp = current.data
                    current.data= nextElement.data
                    nextElement.data = temp
                nextElement = nextElement.next
            current = current.next
    def lessComplexitySort(self):
        current= self.head

        while current != None:
            minValue = current
            nextElement = current.next
            while nextElement:
                if nextElement.data < minValue.data:
                    minValue= nextElement
                temp = current.data
                current.data = minValue.data
                minValue.data = temp
                nextElement= nextElement.next
            current = current.next
    def whereIsMid(self):
        current=mid= self.head
        while current!=None and current.next != None:
            current = current.next.next
            mid = mid.next
        print(mid.data)
    def betweenSort(self):
        nextElement = self.head.next
        tail = self.tail
        prev = None
        while nextElement != self.head and nextElement != tail:
            next  = nextElement.next
            nextElement.next = prev
            prev = nextElement
            nextElement = next
        nextElement = prev




    def display(self):
        current = self.head
        while current!= None:
            print(current.data)
            current = current.next

a = midElement()
a.insertion(1)
a.insertion(134)
a.insertion(53)
a.insertion(34232)
a.insertion(23423)
a.insertion(13423)
a.insertion(1324)
# a.sort()
# a.lessComplexitySort()
a.betweenSort()

a.display()
# a.whereIsMid()
