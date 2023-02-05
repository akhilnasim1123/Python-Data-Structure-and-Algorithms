from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6, 7, 9])
arr2 = array('i', [8, 11, 22, 33, 44, 55, 66, 77, 88, 99])
arr3 = array('i',[])
k=0
last2 = arr2[len(arr2)-1]
for i in range(len(arr1)-1+len(arr2)-1):
    pass

# for i in range(len(arr2) - 1):
#     arr1.append(arr2[i])



arr1 = sorted(arr1)
len = (len(arr1)-1)//2
median = (arr1[len] + arr1[len+1])/2
print(median)

print(arr1)
