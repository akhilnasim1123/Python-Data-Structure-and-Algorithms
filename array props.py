from array import *

arr1 = array('i', [1, 2, 3, 44, 5])
arr2 = array('i', [111, 2, 323, 4433, 52, 32,3])
arr3 = array('i', [11, 2, 32, 443, 51, 34, 6, 3, 765, 2])
arr1 = sorted(arr1)
arr2 = sorted(arr2)
arr3 = sorted(arr3)
j = 0



def array(arr1, arr2, arr3, left1, left2, right1, right2, j,val):
    if j <= len(arr1) - 1:
        element = arr1[j]
        mid1 = (left1 + right1 // 2)
        mid2 = (left2 + right2 // 2)
        midValue1 = arr2[mid1]
        midValue2 = arr3[mid2]
        if midValue1 == element:
            val = midValue1
        if midValue2 == val:
            print(val)

        else:
            if midValue1 < element:
                left1 = mid1 + 1
            elif midValue1 > element:
                right1 = mid1 - 1
            elif midValue2 < element:
                left2 = mid2 + 1
            elif midValue2 > element:
                left2 = mid2 - 1
        array(arr1, arr2, arr3, left1, left2, right1, right2, j + 1,val)
        j = j + 1

        array(arr1, arr2, arr3, left1, left2, right1, right2, j + 1,val)


array(arr1, arr2, arr3, 0, 0, len(arr2)-1, len(arr3)-1, j,0)
