def quicksort(array):
    quicksortHelper(array, 0, len(array)-1)
    return array


def quicksortHelper(array, startx, endx):
    if startx >= endx:
        return
    pivotx = startx
    leftx = startx + 1
    rightx = endx
    while leftx <= rightx:
        if array[leftx] > array[pivotx] and array[pivotx]> array[rightx]:
            swap(array,leftx,rightx)
            leftx +=1
            rightx -=1
        if array[leftx] <= array[pivotx]:
            leftx +=1

        if array[rightx] >= array[pivotx]:
            rightx -=1

    swap(array,rightx,pivotx)
    quicksortHelper(array,startx,rightx-1)
    quicksortHelper(array,rightx+1,endx)





def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


array = [12,766,23,765,12,3,678,23,43]
print(quicksort(array))
