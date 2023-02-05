from array import *

array = array('i', [1, 2, 3, 4, 5, 6, 8, 9])
l = len(array) - 1
index = 6-1
array.append(0)
while l != index:
    array[l + 1] = array[l]
    # array[l] = 0
    l -= 1
array[index+1] = 7
print(array)
