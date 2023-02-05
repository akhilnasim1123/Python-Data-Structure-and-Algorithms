prev = 0
next = 1
for i in range(20):
    print(prev)
    nth = prev+next
    prev = next
    next = nth
