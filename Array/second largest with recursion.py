from array import *

array = array('i', [2, 1, 2, 32, 1, 3, 5, 6, 32, 12, 7])
largest = 0
second = 0
i = 0


def secondLargestRec(array, largest, second, i):
    if i <= len(array) - 1:
        if array[i] > largest:
            second = largest
            largest = array[i]
        if array[i] > second and array[i] != largest:
            second = array[i]
    if i == len(array) - 1:
        return second
    return secondLargestRec(array, largest, second, i + 1)


print(secondLargestRec(array, largest, second, i))
