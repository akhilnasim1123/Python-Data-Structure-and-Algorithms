array = [12, 4, 1, 6, 3, 7, 3, 7, 1, 8, 562425665, 2, 9, 1, 5, 8, 23, 6, 32, 7, 2]


def quick(array):
    quickhelper(array, 0, len(array)-1)
    return array


def quickhelper(array, startx, endx):
    if startx >= endx:
        return
    piviot = startx
    left = startx + 1
    rightx = endx
    while left <= rightx:
        if array[left] > array[piviot] > array[rightx]:
            swap(array, left, rightx)
            left += 1
            rightx -= 1
        if array[left] <= array[piviot]:
            left += 1
        if array[rightx] >= array[piviot]:
            rightx -= 1
    swap(array,rightx,piviot)
    quickhelper(array,startx,rightx-1)
    quickhelper(array,rightx+1,endx)



def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


print(quick(array))