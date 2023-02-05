from array import *
array = array('i',[1,34,6,2,45,6,2,6,34,8,4])
for i in range(len(array)-1):
    current = array[i]
    j=i-1
    while j >= 0 and array[j]>current:
        array[j+1]=array[j]
        j = j-1
    array[j+1]=current

for i in range(len(array)-1):
    print(array[i])
