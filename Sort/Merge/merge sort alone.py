def merge(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    first = array[:mid]
    second = array[mid:]
    return join(array, merge(first), merge(second))


def join(array, first, second):
    i = j = k = 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            array[k] = first[i]
            i += 1
        else:
            array[k] = second[j]
            j += 1
        k += 1
    while i < len(first):
            array[k] = first[i]
            k += 1
            i += 1
    while j < len(second):
            array[k] = second[j]
            k += 1
            j += 1
    return array

def Print(array):
    for i in range(len(array)):
        print(array[i], end=' ')


array = [4, 2, 5, 2, 5, 1, 4, 1, 9, 4, 3, 8, 7, 2, 6, 1, 9, 9, 1, 23, 4, 5, 6, 7]
returnValue = merge(array)
Print(returnValue)
