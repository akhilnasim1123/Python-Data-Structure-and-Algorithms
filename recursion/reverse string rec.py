def reverseRec(index, string):
    if string is None or index >= len(string):
        return
    reverseRec(index + 1, string)
    print(string[index], end=' ')
reverseRec(0, 'abdul Yazer')
