class linkedList:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class Solution:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertion(self,data):
        newNode = linkedList(data)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = newNode
            self.tail = newNode
        else:
            self.head= self.tail = newNode
    def zeroChecking(self):
        if self.head is None:
            print('there is no element in this linked list, empty')
        else:
            current = self.head
            # while current!= None:
            #     if current == self.head and current.data + current.next.data == 0:
            #         next = self.head.next
            #         self.head =  next.next
            #         current = self.head
            #
            #     else:
            #         prev = current
            #         next = current.next
            #         match = current.data + current.data
            #         if current != None and match != 0:
            #             prev = current
            #             current=current.next
            #         elif current != None and match == 0:
            #             next = current.next
            #             prev.next = next.next

                # prev.next = current.next
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current= current.next
obj = Solution()
obj.insertion(21)
obj.insertion(-21)
obj.insertion(5)
obj.insertion(43)
obj.insertion(2)
obj.insertion(-2)
obj.insertion(-421)
obj.insertion(-78)
obj.insertion(521)
obj.insertion(-18)
obj.insertion(18)


obj.zeroChecking()
obj.display()


