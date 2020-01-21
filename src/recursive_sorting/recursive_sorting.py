# TO-DO: complete the helper function below to merge 2 sorted arrays

arrA = [1, 2, 3]
arrB = [4, 5, 6]

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # print('elements:', elements)
    merged_arr = [0] * elements
    # UPER
    # U - UNDERSTAND
    # TAKE 2 ORDERED LISTS AND MERGE THEM TOGETHER
    # P - PLAN
    # FOR EACH ITEM

    for i in arrA:
        print('i:', i)
        merged_arr[i-1] = i
    for x in arrB:
        print('x', x)
        merged_arr[x - 1] = x

    print('merged_arr:', merged_arr)
    merged_arr.remove(1)
    return merged_arr

merge(arrA, arrB)

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


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
