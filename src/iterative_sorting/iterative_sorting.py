# TO-DO: Complete the selection_sort() function below

arr = [5, 4, 3, 1, 7, 2, 9]
print('arr in:', arr)
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # print(smallest_index)
        for x in range(i, len(arr)):
            # print('x:::', x)
            if arr[smallest_index] > arr[x]:
                smallest_index = x
                # print(smallest_index)
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    print('ordered arr:', arr)

        # UPER
        # UNDERSTAND
        # GOAL - PUT ARR IN ORDER
        # TAKE





    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

selection_sort(arr)

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
