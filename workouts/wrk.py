class Sort:
    def quick(self, array):
        self.quicksort(array, 0, len(array) - 1)
        return array

    def quicksort(self, array, start, end):
        if start >= end:
            return
        piviot = start
        left = start + 1
        right = end
        while left <= right:
            if array[left] > array[piviot] > array[right]:
                self.swap(array, left, right)
                left += 1
                right -= 1

            if array[left] <= array[piviot]:
                left += 1
            if array[right] >= array[piviot]:
                right -= 1
        self.swap(array, right, piviot)
        self.quicksort(array, start, right - 1)
        self.quicksort(array, right + 1, end)

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]

    def merge(self, array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        first = array[:mid]
        second = array[mid:]
        return self.join(array, self.merge(first), self.merge(second))

    def join(self, array, first, second):
        i = j = k = 0
        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                array[k] = first[i]
                i += 1
            else:
                array[k] = second[j]
                j += 1
            k += 1
        while i < len(first):
            array[k] = first[i]
            i += 1
            k += 1
        while j < len(second):
            array[k] = second[j]
            j += 1
            k += 1
        return array


list1 = [1, 2, 5, 2, 6, 3, 5, 12]
a = Sort()
print(a.quick(list1))
print(a.merge(list1))
