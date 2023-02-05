def factorialRec(n):
    if n == 1:
        return n
    else:
        return n * factorialRec(n-1)


print(factorialRec(7))
