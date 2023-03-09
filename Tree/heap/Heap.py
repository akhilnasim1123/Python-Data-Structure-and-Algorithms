from array import *

array = array('i', [6, 2, 8])


class MinHeap:
    def __init__(self, array):
        self.array = array
    # def MinHeap(self):
    #     self.buildHeap()

    def buildHeap(self):
        for i in range(self.parent(len(self.array) - 1), 0, -1):
            self.shiftdown(i)

    def shiftdown(self, index):
        endidx = len(self.array) - 1
        leftidx = self.left_child(index)
        while leftidx <= endidx:
            rightidx = self.right_child(index)
            if rightidx <= endidx and self.array[rightidx] < self.array[leftidx]:
                idxToShift = rightidx
            else:
                idxToShift = leftidx

            if self.array[index] > self.array[idxToShift]:
                self.array[index], self.array[idxToShift] = self.array[idxToShift], self.array[index]
                index = idxToShift
                leftidx = self.left_child(index)
            else:
                return

    def shift_up(self, index):
        parentidx = self.parent(index)
        while index > 0 and self.array[parentidx] > self.array[index]:
            self.array[index], self.array[parentidx] = self.array[parentidx], self.array[index]
            index = parentidx
            parentidx = self.parent(index)

    def remove(self):
        self.array[0], self.array[len(self.array) - 1] = self.array[len(self.array) - 1], self.array[0]
        self.array.pop(len(array) - 1)
        self.shiftdown(0)

    def insert(self, value):
        self.array.append(value)
        self.shift_up(len(self.array) - 1)

    def peek(self):
        return self.array[0]

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return (i * 2) + 1

    def right_child(self, i):
        return (i * 2) + 2

    def display(self):
        for i in range(len(self.array)):
            print(self.array[i], end=' ')


heap = MinHeap(array)
heap.display()
print()
heap.insert(1)
heap.insert(5)
heap.insert(15)
heap.buildHeap()
heap.display()
# print(heap.peek())
print()
heap.remove()
heap.display()

