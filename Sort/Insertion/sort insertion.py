array = [2,1,3,5,7,2,3,6,2,3,2,1,46,0]

for i in range(1,len(array)):
    current = array[i]
    j = i-1
    while j>=0 and array[j]>current:
        array[j+1] = array[j]
        j -= 1
    array[j+1] = current

print(array)