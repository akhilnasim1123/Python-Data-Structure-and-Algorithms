class Heap:
    def __init__(self, array):
        self.array = array
        self.MinHeap()

    def MinHeap(self):
        self.__build_heap()

    def __build_heap(self):
        for i in range(self.__parent(len(self.array) - 1), -1, -1):
            self.__shiftdown(i)

    def __shiftdown(self, currentidx):
        endidx = len(self.array) - 1
        leftidx = self.__leftindx(currentidx)
        while leftidx <= endidx:
            rightidx = self.__rightindx(currentidx)
            if rightidx <= endidx and self.array[rightidx] < self.array[leftidx]:
                idxToShift = rightidx
            else:
                idxToShift = leftidx
            if self.array[currentidx] > self.array[idxToShift]:
                self.__swap(currentidx, idxToShift)
                currentidx = idxToShift

                leftidx = self.__leftindx(currentidx)
            else:
                return

    def peek(self):
        print(self.array[0])

    def remove(self):
        self.__swap(0, len(self.array) - 1)
        self.array.pop(len(self.array) - 1)
        self.__shift_up(0)

    def __shift_up(self, currentindx):
        parentidx = self.__parent(currentindx)
        while currentindx > 0 and self.array[parentidx] > self.array[currentindx]:
            self.__swap(parentidx, currentindx)
            currentindx = parentidx
            parentidx = self.__parent(currentindx)

    def insert(self, data):
        self.array.append(data)
        self.__shift_up(len(self.array) - 1)

    def __swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def __rightindx(self, i):
        return (i * 2) + 2

    def __leftindx(self, i):
        return (i * 2) + 1

    def __parent(self, idx):
        value = int((idx - 1) / 2)
        return value

    def display(self):
        for i in range(len(self.array)):
            print('|', self.array[i], end=' ')
    def find(self):
        pass









array = [[1,5,9],[10,11,13],[12,13,15]]
heap = Heap(array)
heap.display()
print(heap.find(8))

