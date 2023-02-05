def QuickSort(array):
    QuickSortHelper(array, 0, len(array) - 1)
    return array


def QuickSortHelper(array, startx, endx):
    if startx >= endx:
        return
    piviotx = startx
    leftx = startx + 1
    rightx = endx
    while leftx <= rightx:
        if array[leftx] > array[piviotx] > array[rightx]:
            swap(array, leftx, rightx)
            leftx += 1
            rightx -= 1
        if array[leftx] <= array[piviotx]:
            leftx += 1
        if array[rightx] >= array[piviotx]:
            rightx -= 1
    swap(array, rightx, piviotx)
    QuickSortHelper(array, startx, rightx - 1)
    QuickSortHelper(array, rightx + 1, endx)


def swap(array, leftx, rightx):
    array[leftx], array[rightx] = array[rightx], array[leftx]


array = [-1, 4, 2, 7, 2, 8, 2, 8, 1, 6, 9, 3, 8, 10, 4, 1, 4, 6, 9, 1, 5, 3, 9, 1, 2, 4, 6, 7, 2]

print(QuickSort(array))
