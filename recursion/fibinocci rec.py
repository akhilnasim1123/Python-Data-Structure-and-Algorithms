first = 0
second = 1
count = 0
nth = 0


def fibRec(first, second, count, nth):
    if count < 20:
        print(first)
        nth = first + second
        first = second
        second = nth

    return fibRec(first, second, count+1, nth)

print(fibRec(first, second, count, nth))
