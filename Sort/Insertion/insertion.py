array = [1, 5, 2, 6, 9, 8, 2, 8, 3, 2, 6, 2, 6, 3, 9, 1, 98, 43, 1, 72, 4, 2]

for i in range(1, len(array)):
    current = array[i]
    j = i - 1
    while j >= 0 and array[j] > current:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = current

print(array)
