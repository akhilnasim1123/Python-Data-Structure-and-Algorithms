array = [12, 4, 1, 6, 3, 7, 3, 7, 1, 8, 562425665, 2, 9, 1, 5, 8, 23, 6, 32, 7, 2]
for i in range(1, len(array)):
    current = array[i]
    j = i - 1
    while j >= 0 and array[j] > current:
        array[j + 1] = array[j]
        j -= 1

    array[j+1] = current

print(array)
