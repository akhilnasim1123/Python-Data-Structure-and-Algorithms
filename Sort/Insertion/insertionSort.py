from array import *

array = array('i', [123, 324, 51, 45432, 78, 3, 65, 235476, 2, 5436, 4225])

for i in range(1,len(array)):
    current = array[i]
    j = i - 1
    while array[j]>current and j >= 0:
        array[j+1] = array[j]
        j -= 1
    array[j+1] = current

print(array)
print(len(array))
