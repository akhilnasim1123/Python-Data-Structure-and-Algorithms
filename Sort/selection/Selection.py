array = [-1, 4, 2, 7, 2, 8, 2, 8, 1, 6, 9, 3, 8, 10, 4, 1, 4, 6, 9, 1, 5, 3, 9, 1, 2, 4, 6, 7, 2]

for i in range(len(array)):
    min = i
    for j in range(i + 1, len(array)):
        if array[j] < array[min]:
            min = j
    array[i], array[min] = array[min], array[i]

print(array)
