list = [1, 3, 4, 2, 5, 4, 6, 7, 8]

largest = 0
second = 99999
for i in range(len(list)):
    if list[i]>largest:
        largest = list[i]

    if list[i]<second:
            second = list[i]




print('largest element is : ', largest)
print('smallest element is : ', second)