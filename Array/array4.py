from array import *
array = array('i',[-1,1,45,32,-2,2,12,23,-10,10])
target = 0
store =[]
for i in range(len(array)-1):
    match = target - array[i]
    if match in store:
        store.remove(match)
        # store.remove(array[i])
    else:
        store.append(array[i])
for i in range(len(store)-1):
    print(store[i])