
arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print('arr in:', arr)
### STEP 1: Split our list into sub-lists until they are all length 1 or less
def merge_sort(arr):
    # Check if it's length 1 or less. If so, return the list
    if len(arr) <= 1:
        return arr
    # Divide in half
    left = arr[ : len(arr) // 2]
    print('left:', left)
    right = arr[len(arr) // 2 : ]
    print('right:', right)
    # Sort the left
    left = merge_sort(left)
    print('left2ndtime:', left)
    # Sort the right
    right = merge_sort(right)
    print('right2ndtime:', right)
    # Merge together
    return merge(left, right)


# STEP 2: Merge two sorted sublists and return the sorted merged list
def merge(arr_a, arr_b):
    total_elements = len(arr_a) + len(arr_b)
    merged_arr = [None] * total_elements
    # Declare indices for each sublist
    a = 0
    b = 0
    for i in range(total_elements):
        # Check if either list is empty, if so append the other
        if a >= len(arr_a):
            merged_arr[i] = arr_b[b]
            print('if: merged_arr[i]:', merged_arr[i])
            b += 1
        elif b >= len(arr_b):
            merged_arr[i] = arr_a[a]
            print('elif:1st- merged_arr[i]:', merged_arr[i])
            a += 1
        # Otherwise, compare and append the smallest of the two
        elif arr_a[a] < arr_b[b]:
            merged_arr[i] = arr_a[a]
            print('elif: merged_arr[i]:', merged_arr[i])
            a += 1
        else:
            merged_arr[i] = arr_b[b]
            print('else: merged_arr[i]:', merged_arr[i])
            b += 1
    print('out:', merged_arr)
    return merged_arr

merge_sort(arr)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
