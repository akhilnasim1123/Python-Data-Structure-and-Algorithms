class Heap:
    def __init__(self, array):
        self.array = array
        self.__build_heap()

    def __build_heap(self):
        for i in range(len(self.array) - 1, -1, -1):
            self.__shift_down(i)

    def __shift_down(self, current):
        end = len(self.array) - 1
        left = self.__left(current)
        while left <= end:
            right = self.__right(current)
            if right <= end and self.array[right] < self.array[left]:
                inx = right
            else:
                inx = left
            if self.array[current] > self.array[inx]:
                self.__swap(current, inx)
                current = inx
                left = self.__left(current)
            else:
                return

    def remove(self):
        self.__swap(0, len(self.array) - 1)
        self.array.pop(len(self.array) - 1)
        self.__shift_up(0)

    def __shift_up(self, current):
        parent = self.__parent(current)
        while current > 0 and self.array[parent] > self.array[current]:
            self.__swap(parent, current)
            current = parent
            parent = self.__parent(current)

    def __parent(self, current):
        value = int(current - 1) / 2
        return value

    def display(self):
        print(self.array)

    def __swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def __right(self, i):
        return (i * 2) + 2

    def __left(self, i):
        return (i * 2) + 1


array = [6, 21, 8, 4, 2, 9, 7, 5]

heap = Heap(array)
heap.remove()
heap.display()
