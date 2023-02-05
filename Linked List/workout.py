
def binarySearch(array ,target):
    start = 0
    end = len(array ) -1

    while start <= end:
        midIndex = (start + end) // 2
        midValue = array[midIndex]
        if midValue == target:
            return midIndex
        if midValue < target:
            start = midIndex + 1
        else:
            end = midIndex -1

def TwoSum(array,value):
    store = []
    for i in range(len(array)-1):
        element = array[i]
        target = value - array[i]
        if target in store:
            print(target,' + ',array[i],' = ',value)
        else:
            store.append(element)

def binaryRec(array,start,end,target):
    if start > end:
        return
    midIndex = (start + end)//2
    midValue = array[midIndex]
    if midValue == target:
        return midIndex
    if midValue < target:
        start = midIndex + 1
    else:
        end = midIndex - 1
    return binaryRec(array,start,end,target)

def factorialRec(n):
    if n == 1:
         return n
    else:
        return n*factorialRec(n-1)

def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum = i*sum
    return sum




print(factorialRec(5))
print(factorial(5))
array = [1,2, 3, 4, 5, 6, 7, 8, 9]
TwoSum(array,10)
print(binaryRec(array,0,len(array)-1,6)+1)
print('Your Value is the ',binarySearch(array, 6)+1, ' nth Value in this array')
