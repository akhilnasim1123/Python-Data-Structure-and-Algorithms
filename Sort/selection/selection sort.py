from array import *
array= array("i",[1,2,3,4,56,1,23,5,8,6,54,3,45,2])
for i in range(len(array)-1):
    min=i
    for j in range(i+1,len(array)-1):
        if array[j]<array[min]:
            min=j
    array[i],array[min]=array[min],array[i]

for i in range(len(array)-1  ):
    print(array[i])



