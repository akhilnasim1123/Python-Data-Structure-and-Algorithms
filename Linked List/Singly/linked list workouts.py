# Definition for singly-linked list.
class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution:
    def __init__(self):
        self.head = None
        self.tail = None
# using seletion sort for this sort....
    def sortList(self,val1,val2):

        for firstListElement in range(len(val2)-1):
            val1.append(firstListElement)
        print('length is : ',len(val1))
        return val1


    def toLinkedList(self, val1):
        for element in val1:
            newNode = LinkedList(val1[element])

            if self.head is None:
                self.head= self.tail=newNode
            elif self.head:
                current = self.head
                while current.next:
                    current = current.next
                current.next = newNode
                self.tail = newNode

    def display(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next
solution = Solution()
list1 = [1,2,5,2,6,3,5,12]
list2 = [2,3,43,12,65,123,54]

returnValue = solution.sortList(list1,list2)

solution.toLinkedList(returnValue)
solution.display()
print('head is :',solution.head.val)
print('head next is :',solution.head.next.val)
print('tail is :',solution.tail.val)






