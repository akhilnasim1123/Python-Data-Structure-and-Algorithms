def quick(array):
    quickhelper(array, 0, len(array) - 1)
    return array


def quickhelper(array, startx, endx):
    if startx >= endx:
        return
    piviot = startx
    left = startx + 1
    right = endx
    while left <= right:
        if array[left] > array[piviot] > array[right]:
            swap(array, left, right)
            left += 1
            right -= 1
        if array[left] <= array[piviot]:
            left += 1
        if array[right] >= array[piviot]:
            right -= 1
    swap(array, right, piviot)
    quickhelper(array, startx, right - 1)
    quickhelper(array, right + 1, endx)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


array = [10,10,10, 4, 11,2, 7, 2, 8, 2, 8, 1, 6, 9, 3, 8, 10, 4, 1, 4, 6, 9, 1, 5, 3, 9, 1, 2, 4, 6, 7, 2]
print(quick(array))
