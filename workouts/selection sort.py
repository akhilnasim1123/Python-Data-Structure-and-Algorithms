array = [2, 1, 3, 5, 2, 4, 3, 7, 8, 3, 7, 2, 5, 24, 67, 6, 2, 73, 458, 71]

for i in range(len(array)):
    min = i
    for j in range(i+1,len(array)):
        if array[j]<array[min]:
            min = j
    array[i],array[min] = array[min],array[i]

print(array)