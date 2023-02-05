from array import *


def mergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    firsthalf = array[:mid]
    secondhalf = array[mid:]
    return join(array, mergeSort(firsthalf), mergeSort(secondhalf))


def join(array, first, last):
    sortArray = array
    i = j = k = 0
    while i < len(first) and j < len(last):
        if first[i] < last[j]:
            sortArray[k] = first[i]
            i += 1
        else:
            sortArray[k] = last[j]
            j += 1
        k += 1
    while i < len(first):
        sortArray[k] = first[i]
        i += 1
        k += 1
    while j < len(last):
        sortArray[k] = last[j]
        j += 1
        k += 1
    return sortArray


def Print(array):
    for i in range(len(array)):
        print(array[i], end=' ')


array = array('i', [123, 324, 51, 45432, 78, 3, 65, 2354444, 2, 5436, 4225, 1, 424, 0, 1, 2])
value = mergeSort(array)
Print(value)
