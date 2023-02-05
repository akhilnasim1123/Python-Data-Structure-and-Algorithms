def MissingNumber(array, n):
    # code here
    array = sorted(array)
    for i in range(n):
        if array[i + 1] != array[i] + 1:
            print(array[i] + 1)

from array import *
array = array('i',[1,2,3,4,5,6,7,8,10])
MissingNumber(array,len(array)-1)
number = 2214
number = str(number)
print(number[::-1])

