List = [1,2,3,4,6,7,8,9]

index = 5-1
l = len(List)-1
List.append(0)

while l!=index-1:
    List[l+1]= List[l]
    l -=1
List[l+1]=5
print(List)