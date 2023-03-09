array = [2, 1, 3, 5, 2, 4, 3, 7, 8, 3, 7, 2, 5, 24, 67, 6, 2, 73, 458, 71]

for i in range(len(array)):
    current = array[i]
    j = i - 1
    while j >= 0 and array[j] > current:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = current

print(array)
