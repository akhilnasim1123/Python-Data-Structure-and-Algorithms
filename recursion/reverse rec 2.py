def reverse(length,string):
    if length > 0:
        print(string[length-1],end=' ')
        reverse(length-1,string)
string = 'abdul Yazer'
reverse(len(string),string)