def quick(array):
    quicksort(array, 0, len(array) - 1)
    return array


def quicksort(array, start, endx):
    if start >= endx:
        return
    piviot = start
    left = start + 1
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
    quicksort(array, start, right - 1)
    quicksort(array, right + 1, endx)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


array = [2, 1, 3, 5, 2, 4, 3, 7, 8, 3, 7, 2, 5, 24, 67, 6, 2, 73, 458, 71]

print(quick(array))
