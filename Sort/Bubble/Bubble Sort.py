array = [1, 5, 2, 6, 9, 8, 2, 8, 3, 2, 6, 2, 6, 3, 9, 1, 98, 43, 1, 72, 4, 2]

for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

print(array)
