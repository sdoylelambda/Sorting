# TO-DO: Complete the selection_sort() function below

arr = [5, 4, 3, 1, 7, 2, 9]
print('arr in:', arr)
# Finds smallest then 2nd smallest and so on
# def selection_sort(arr):
#     for i in range(len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
#         # print(smallest_index)
#         for x in range(i, len(arr)):
#             # print('x:::', x)
#             if arr[smallest_index] > arr[x]:
#                 smallest_index = x
#                 # print(smallest_index)
#         arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
#     # print('ordered arr:', arr)
#     return arr

# selection_sort(arr)


# TO-DO:  implement the Bubble Sort function below
# Compares 1st to 2nd, 2nd to third and so on
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for x in range(n-i-1):
            if arr[x] > arr[x+1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]

    # print('bubble arr:', arr)
    return arr

bubble_sort(arr)


def bubble_sort2(arr):
    print('arr in::', arr)
    hasSwapped = True
    while hasSwapped:
        hasSwapped = False
        for i in range(len(arr)):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # temp = arr[i]
                # arr[i] = arr[i+1]
                # arr[i+1] = temp
                hasSwapped = True
    print('bubble sort2:', arr)
    return arr

bubble_sort2(arr)














import time
startTime = time.time()
endTime = time.time()
print(startTime, endTime)





















# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr



# print(smallest_index)
# # TO-DO: find next smallest element
# for x in range(0, len(arr) - 1):
#     # (hint, can do in 3 loc)
#     # TO-DO: swap
#     print('x', x)
#     if x > arr[0]:
#         print('If i:', i)
#     elif x < arr[0]:
#         print('If x:', x)
#
