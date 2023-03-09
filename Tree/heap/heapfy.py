class MaxHeap:
    def __init__(self):
        self.array = []
        self.root = None

    def array_to_heap(self, array):
        for i in array:
            self.array.append(i)
        self.__heapfy()

    def __heapfy(self):
        for i in range(len(self.array) - 1, -1, -1):
            self.__min_shift_down(i)

    def __min_shift_down(self, current):
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

    def remove(self):
        self.__swap(0, len(self.array) - 1)
        self.array.pop(len(self.array) - 1)
        self.__min_shift_down(0)

    def __left(self, current):
        return (current * 2) + 1

    def __right(self, i):
        return (i * 2) + 2

    def min_heapfy_insert(self, data):
        self.array.append(data)
        self.__min_shift_up(len(self.array) - 1)

    def __min_shift_up(self, current):
        parent = self.__parent(current)
        while current > 0 and self.array[parent] > self.array[current]:
            self.__swap(current, parent)
            current = parent
            parent = self.__parent(current)

    def __swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def __parent(self, i):
        value = int((i - 1) / 2)
        return value

    def show(self):
        print(self.array)


lst = [61, 7, 3, 4, 23]
heap = MaxHeap()
heap.min_heapfy_insert(3)
heap.min_heapfy_insert(5)
heap.min_heapfy_insert(234)
heap.min_heapfy_insert(6)
heap.min_heapfy_insert(621)
heap.min_heapfy_insert(71)
heap.min_heapfy_insert(1)
heap.min_heapfy_insert(4)

heap.array_to_heap(lst)
heap.remove()
heap.show()
