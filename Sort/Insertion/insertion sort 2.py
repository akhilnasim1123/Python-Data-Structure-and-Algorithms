from array import *

arr = array('i', [12, 1, 4556, 2, 65, 3, 26, 345, 2, 45, 76, 124, 64, 71, 45, 44, 54, 342, 5, 456])
for i in range(1,len(arr)-1):
    a = arr[i]
    j = i-1
    while j>= 0 and arr[j]>a:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1] = a

for i in range(len(arr)-1):
    print(arr[i],end=' ')

