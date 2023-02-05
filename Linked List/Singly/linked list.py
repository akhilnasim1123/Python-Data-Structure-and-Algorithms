class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,data):
        newNode=Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            self.tail = newNode
        else:
            self.head = self.tail = newNode
    def delete(self,data):
        current = self.head
        if current != None and current == data:
            head = current.next
        if current != None and current != data:
            prev = current
            current = current.next
        if current == None:
            pass
        if current == None:
            tail = prev
            tail.next = None
        prev.next = current.next
    def insertAfter(self,nextTo,data):
        newNode = Node(data)
        current = self.head
        if current!=null and current.data != nextTo:
            current = current.next
        if current != null:
            pass
        if current == tail:
            tail.next = newNode
            tail = newNode
        newNode.next = current.next
        current.next = newNode
    def print(self):
        current=self.head
        while current:
            print(current.data)
            current = current.next


LL = LinkedList()
LL.insert(3242)
LL.insert(324)
LL.insert(765)


print("Head is :",LL.head.data)
print("Tail is :",LL.tail.data)
aa =  LinkedList()
aa.delete(324)
LL.print()
