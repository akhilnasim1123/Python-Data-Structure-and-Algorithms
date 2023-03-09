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
        i += 1
        k += 1
    while j < len(second):
        array[k] = second[j]
        j += 1
        k += 1
    return array


array = [2, 1, 3, 5, 2, 4, 3, 7, 8, 3, 7, 2, 5, 24, 67, 6, 2, 73, 458, 71]

print(merge(array))
