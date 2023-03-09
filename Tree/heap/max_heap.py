class MaxHeap:
    def __init__(self):
        self.array = []

    def insert(self, data):
        self.array.append(data)
        self.shift_up(len(self.array) - 1)

    def shift_up(self, current):
        parent = self.parent(current)
        while current > 0 and self.array[parent] < self.array[current]:
            self.swap(parent, current)
            current = parent
            parent = self.parent(current)

    def array_to(self, array):
        for i in array:
            self.array.append(i)
        self.heapfy()

    def heapfy(self):
        for i in range(len(self.array) - 1, -1, -1):
            self.shift_down(i)

    def shift_down(self, current):
        end = len(self.array) - 1
        left = self.left(current)
        while left <= end:
            right = self.right(current)
            if right <= end and self.array[right] > self.array[left]:
                idx = right
            else:
                idx = left
            if self.array[current] < self.array[idx]:
                self.swap(current, idx)
                current = idx
                left = self.left(current)
            else:
                return

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def parent(self, i):
        value = int((i - 1) / 2)
        return value

    def left(self, current):
        return (current * 2) + 1

    def right(self, current):
        return (current * 2) + 2

    def show(self):
        print(self.array)

    def remove(self):
        self.swap(0, len(self.array) - 1)
        self.array.append([len(self.array) - 1])
        self.shift_down(0)

    def second_largest(self):
        left = self.left(0)
        right = self.right(0)
        if self.array[left] > self.array[right]:
            print(self.array[left])
        else:
            print(self.array[right])


array = [1, 2, 13, 41, 3, 13, 512]

heap = MaxHeap()
heap.insert(21)
heap.insert(3451)
heap.insert(123)
heap.insert(724)
heap.insert(31111)
heap.array_to(array)
heap.show()
heap.second_largest()
