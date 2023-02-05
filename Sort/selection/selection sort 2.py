array = [12, 4, 1, 6, 3, 7, 3, 7, 1, 8, 562425665, 2, 9, 1, 5, 8, 23, 6, 32, 7, 2]

for i in range(len(array)):
    min = i
    for j in range(i+1,len(array)):
        if array[j]<array[min]:
            min = j
    array[i],array[min] = array[min],array[i]
print(array)