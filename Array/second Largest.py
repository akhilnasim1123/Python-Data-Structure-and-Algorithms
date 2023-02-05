from array import *

array = array('i', [2, 1, 2, 32, 1, 3, 5, 6, 32, 12, 7])
largest = 0
second = 0
for i in range(len(array) - 1):
    if array[i] > largest:
        second = largest
        largest = array[i]
    if array[i] > second and array[i] != largest:
        second = array[i]
print(largest)
print(second)
