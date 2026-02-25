from array import *


def linearSearch(array, value):
    for data in range(len(array) - 1):
        if array[data] == value:
            print('your element is a ', data+1, ' item in this array')
            print(value)


def binarySearch(array, value):
    array = sorted(array)
    left_index = 0
    end_index = len(array)-1
    while left_index <= end_index:
        mid_index = (left_index + end_index)//2
        mid_number = array[mid_index]
        if mid_number == value:
            print('your element is a ', mid_index + 1, ' item in this array')
            print(value)
        if mid_number < value:
            left_index = mid_index+1
        else:
            end_index = mid_index -1



array = array('i', [1, 2, 4, 7, 3, 2, 543, 213, 213, 56, 23, 46, 45])
value = 213
# linearSearch(array,value)
binarySearch(array,value)


