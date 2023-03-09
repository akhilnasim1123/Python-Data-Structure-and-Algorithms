def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array


def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array


def quick(array):
    quicksort(array, 0, len(array) - 1)
    return array


def quicksort(array, start, end):
    if start >= end:
        return
    piviot = start
    left = start + 1
    right = end
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
    quicksort(array, right + 1, end)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


array = [2, 1, 3, 5, 2, 4, 3, 7, 8, 3, 7, 2, 5, 24, 67, 6, 2, 73, 458, 71]


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


print('|-------------------------Quick Sort-----------------------------|')
print(quick(array))
print('|-------------------------Merge Sort-----------------------------|')
print(merge(array))
print('|-------------------------Bubble Sort----------------------------|')
print(bubble_sort(array))
print('|-------------------------Insertion Sort-------------------------|')
print(insertion_sort(array))
print('|-------------------------Selection Sort-------------------------|')
print(selection_sort(array))


