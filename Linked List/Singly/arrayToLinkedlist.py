from array import *


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head= None
        self.tail = None

    def arrayToLinkedlist(self,array):
        i = 0
        while i<= len(array)-1:
            data = array[i]
            node = Node(data)
            if self.head:
                self.tail.next = node
                self.tail = node
            else:
                self.head = self.tail = node
            i += 1

    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next

array = array('i',[1,234,34,2,2,43,1,2,45])
a = Linkedlist()
a.arrayToLinkedlist(array)
a.display()