from array import *
array = array('i',[2,3,5,5,7,3,3,7,3,7,8,9,7,1,2])
target = 11
store = []
for i in range(len(array)-1):
    value = array[i]
    match = target-value
    if match in store:
        print(value,'x',match,'=',target)
    else:
        store.append(value)
