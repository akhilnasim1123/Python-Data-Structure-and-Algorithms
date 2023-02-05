from array import *
array = array('i',[1,2,1,3,1,5,3,1,3,5,2,1])
for i in range(len(array)-1):
    for j in range(len(array)-1,0,-1):
        if array[i] == array[j]:
            print(array[j-1])
            temp=array[j-1]
            array[j-1] = array[j]
            array[i]=temp
