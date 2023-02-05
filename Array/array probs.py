from array import *
array = array('i',[3,4,2,3,5,6,7])
target = 10

for first in range(len(array)-1):
    for second in range(first+1,len(array)):
        if array[first]*array[second] == target:
            print(array[first],'x',array[second],'=',target)
