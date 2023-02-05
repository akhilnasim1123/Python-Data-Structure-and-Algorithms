

def palindrome(value):
    new = str(value)
    new = new[::-1]
    print(new)
    if value >=0:
        if value == int(new):
            return 1
        else:
            return -1
    else:
        return -1

print(palindrome(121))