def merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    first = arr[:mid]
    second = arr[mid:]
    return join(arr, merge(first), merge(second))


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
        i += 1
        k += 1
    while j < len(second):
        array[k] = second[j]
        j += 1
        k += 1
    return array

def Print(array):
    for i in range(len(array)):
        print(array[i],end=' ')
array = [12, 4, 1, 6, 3, 7, 3, 7, 1, 8, 562425665, 2, 9, 1, 5, 8, 23, 6, 32, 7, 2]
value=merge(array)

Print(value)