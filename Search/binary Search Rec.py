from array import *


def binarySearchRec(array, value, leftIndex, righIndex):
    if leftIndex > righIndex:
        return -1
    midIndex = (leftIndex + righIndex) // 2
    midValue = array[midIndex] - 1

    if midValue == value:
        return midIndex
    if midValue < value:
        leftIndex = midIndex + 1
    else:
        righIndex = midIndex - 1
    return binarySearchRec(array, value, leftIndex, righIndex)


array = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
value = 6
print('the position of this element is :', binarySearchRec(array, value, 0, len(array) - 1))
