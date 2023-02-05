
list=[]
def push(data):
    list.append(data)
def pop():
    if not list:

        print('stack Is Empty')
    else:
        list.pop()
def display():
    print(list)
push(21)
push(34)
push(6776)
display()
pop()
display()
