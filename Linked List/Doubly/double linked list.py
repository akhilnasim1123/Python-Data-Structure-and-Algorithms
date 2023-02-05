class Node:
    def __init__(self,data):
        self.next = None
        self.prev = None
        self.data=data

class Solution:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertDouble(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head= self.tail = newNode
        else:
            current = self.head
            self.tail.next = newNode
            newNode.prev = self.tail
        self.tail = newNode
    def reverse(self):
        tail = self.tail
        current = self.head
        while current :
            temp = current
            current = tail
            tail = temp
            current = current.next
            tail = tail.prev


    def display(self):
        current = self.head
        while current.next:
            print(current.data,end=" ")

            current= current.next
        print()


a = Solution()
a.insertDouble(34)
a.insertDouble(44)
a.insertDouble(342534)
a.insertDouble(3424)
a.insertDouble(5234)
a.insertDouble(342)
a.insertDouble(342345)
a.insertDouble(4534)
a.insertDouble(34234)
a.insertDouble(3654)
a.insertDouble(3490)
a.display()
a.reverse()
a.display()




