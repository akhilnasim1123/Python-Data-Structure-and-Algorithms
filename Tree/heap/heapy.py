class Heap:
    def __init__(self, array):
        self.array = array
        self.__heapfy()

    def __heapfy(self):
        for i in range(len(self.array) - 1, -1, -1):
            self.__shift_down(i)

    def __shift_down(self, current_idx):
        end = len(self.array) - 1
        left = self.__left(current_idx)
        while left <= end:
            right = self.__right(current_idx)
            if right <= end and self.array[right] < self.array[left]:
                idx = right
            else:
                idx = left
            if self.array[idx] > self.array[current_idx]:
                self.__swap(idx, current_idx)
                current_idx = idx
                left = current_idx(current_idx)
            else:
                return

    def __shift_up(self, current_idx):
        parent = self.__parent(current_idx)
        while parent > 0 and self.array[parent] > self.array[current_idx]:
            self.__swap(parent, current_idx)
            current_idx = parent
            parent = self.__parent(current_idx)

    def __parent(self, i):
        value = int(i - 1) / 2
        return value

    def insert(self, data):
        self.array.append(data)
        self.__shift_down(len(self.array) - 1)

    def __swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def __left(self, i):
        return (i * 2) + 1

    def __right(self, i):
        return (i * 2) + 2






def shifdown(current_idx):
    end = len(array)-1
    left = left(current_idx)
    while left<= end:
        right = right(current_idx)
        if right <= end and array[right]<array[left]:
            idx  = right
        else:
            idx = left
        if array[idx]<array[current_idx]:
            swap(idx,current_idx)
            current_idx = idx
            left = left(current_idx)
        else:
            return
def shifup(current_idx):
    parent = parent(current_idx)
    while current_idx>0 and array[parent]>array[current_idx]:
        swap(parent,current_idx)
        current_idx = parent
        parent = parent(current_idx)