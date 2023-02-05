array = [12, 4, 1, 6, 3, 7, 3, 7, 1, 8, 562425665, 2, 9, 1, 5, 8, 23, 6, 32, 7, 2]


def quick(array):
    quickhelper(array, 0, len(array)-1)
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
    quickhelper(array,startx,right-1)
    quickhelper(array,right+1,endx)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


print(quick(array))
