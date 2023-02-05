def QuickSort(array):
    quicksorthelper(array, 0, len(array) - 1)
    return array


def quicksorthelper(array, startx, endx):
    if startx >= endx:
        return
    piviot = startx
    leftx = startx + 1
    rightx = endx
    while leftx <= rightx:
        if array[leftx] > array[piviot] > array[rightx]:
            swap(leftx, rightx, array)
            leftx += 1
            rightx -= 1
        if array[leftx] <= array[piviot]:
            leftx += 1
        if array[rightx] >= array[piviot]:
            rightx -= 1
    swap(rightx, piviot, array)
    quicksorthelper(array, startx, rightx - 1)
    quicksorthelper(array, rightx + 1, endx)


def swap(startx, rightx, array):
    array[startx], array[rightx] = array[rightx], array[startx]


array = [-1, 4, 2, 7, 2, 8, 2, 8, 1, 6, 9, 3, 8, 10, 4, 1, 4, 6, 9, 1, 5, 3, 9, 1, 2, 4, 6, 7, 2]
print(QuickSort(array))
