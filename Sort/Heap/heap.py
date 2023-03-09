def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


# def shift_down(lst, i, upper):
#     while True:
#         l, r = i * 2 + 1, i * 2 + 2
#         if max(l, r) < upper:
#             if lst[i] >= max(lst[l], lst[r]):
#                 break
#             elif lst[l] > lst[r]:
#                 swap(lst, l, i)
#                 i = l
#             else:
#                 swap(lst, i, r)
#                 i = r
#         elif l < upper:
#             if lst[l] > lst[i]:
#                 swap(lst, l, i)
#                 i = l
#             else:
#                 break
#         elif r < upper:
#             if lst[r] > lst[i]:
#                 swap(lst, r, i)
#                 i = r
#             else:
#                 break
#         else:
#             break
#
#
# def heapsort(array):
#     for j in range((len(array) - 2) // 2, -1, -1):
#         shift_down(array, j, len(array))
#     for end in range(len(array) - 1, 0, -1):
#         swap(array, 0, end)
#         shift_down(array, 0, end)


def shift_down(lst, i, upper):
    while True:
        l, r = i * 2 + 1, i * 2 + 2
        if max(l, r) < upper:
            if lst[i] >= max(lst[l], lst[r]):
                break
            elif lst[l] > lst[r]:
                swap(lst, l, i)
                i = l
            else:
                swap(lst, i, r)
                i = r
        elif l < upper:
            if lst[l] > lst[i]:
                swap(lst, l, i)
                i = l
            else:
                break
        elif r < upper:
            if lst[r] > lst[i]:
                swap(lst, r, i)
                i = r
            else:
                break
        else:
            break

def shift(array, i, upper):
    while True:
        l, r = i * 2 + 1, i * 2 + 2
        if max(l, r) < upper:
            if array[i] >= max(array[l], array[r]):
                break
            elif array[l] > array[r]:
                swap(array, l, i)
                i = l
            else:
                swap(array, r, i)
                i = r
        elif l<upper:
            if array[l]>array[i]:
                swap(array,l,i)
                i = l
            else:
                break
        elif r<upper:
            if array[r]>array[i]:
                swap(array,r,i)
                i = r
            else:
                break
        else:
            break


def heapsort(array):
    for j in range((len(array) - 2) // 2, -1, -1):
        shift(array, j, len(array))
    for end in range(len(array) - 1, 0, -1):
        swap(array, 0, end)
        shift(array, 0, end)


array = [2, 1, 521, 3, 7, 3, 8, 48, 4, 44, 2]
heapsort(array)
print(array)
