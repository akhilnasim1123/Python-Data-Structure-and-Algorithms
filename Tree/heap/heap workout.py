class Heap:
    def __init__(self):
        self.array = []
        self.root = None

    def array_to_heap(self, array):
        for i in array:
            self.array.append(i)
        self.heapfy()

    def heapfy(self):
        for i in range(len(self.array) - 1, -1, -1):
            self.__shift_down(i)

    def __shift_down(self, current):
        end = len(self.array) - 1
        left = self.__left(current)
        while left <= end:
            right = self.__right(current)
            if right <= end and self.array[right] < self.array[left]:
                idx = right
            else:
                idx = left
            if self.array[current] > self.array[idx]:
                self.__swap(current, idx)
                current = idx
                left = self.__left(current)
            else:
                return

    def max_heapfy(self):
        for i in range(len(self.array) - 1, -1, -1):
            self.__min_down(i)

    def __min_down(self, current):
        end = len(self.array) - 1
        left = self.__left(current)
        while left <= end:
            right = self.__right(current)
            if right <= end and self.array[right] > self.array[left]:
                idx = right
            else:
                idx = left
            if self.array[current] < self.array[idx]:
                self.__swap(current, idx)
                current = idx
                left = self.__left(current)
            else:
                return

    def min_up(self, current):
        parent = self.__parent(current)
        while current:
            if current > 0 and self.array[parent] < self.array[current]:
                self.__swap(parent, current)
                parent = current
                current = self.__parent(current)

    def peek(self):
        print(self.array[0])

    def remove(self):
        self.__swap(0, len(self.array) - 1)
        self.array.pop(len(self.array) - 1)
        self.__shift_down(0)

    def __left(self, i):
        return (i * 2) + 1

    def __right(self, i):
        return (i * 2) + 2

    def insert_min(self, data):
        self.array.append(data)
        self.__shift_up(len(self.array) - 1)

    def __shift_up(self, current):
        parent = self.__parent(current)
        while current > 0 and self.array[parent] > self.array[current]:
            self.__swap(parent, current)
            current = parent
            parent = self.__parent(current)

    def __swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def __parent(self, current):
        value = int((current - 1) / 2)
        return value

    def display(self):
        print(self.array)
    def second_larest(self):
        self.max_heapfy()
        left = self.__left(0)
        right = self.__right(0)
        if self.array[left]>self.array[right]:
            return self.array[left]
        else:
            return self.array[right]
heap = Heap()
heap.insert_min(3)
heap.insert_min(5)
heap.insert_min(234)
heap.insert_min(6)
heap.insert_min(621)
heap.insert_min(71)
heap.insert_min(1)
heap.insert_min(4)
lst = [9, 7, 23, 8]
heap.array_to_heap(lst)
heap.max_heapfy()

heap.display()
print(heap.second_larest())