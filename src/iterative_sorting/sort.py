# TO-DO: Complete the selection_sort() function below

arr = [5, 4, 8, 3, 1, 7, 9, 1]
print('arr in:', arr)

# Finds smallest then 2nd smallest and so on
def selection_sort(arr):
    for i in range(len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
                arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    print('arr out:', arr)
    return arr

selection_sort(arr)


def selection_sort2(arr):
    # 1 - loop one
    for i in range(len(arr) - 1):
        lowNum = i
        # 2 - 2nd loop
        for x in range(i, len(arr)):
            # find lowest
            if arr[lowNum] > arr[x]:
                arr[i], arr[lowNum] = arr[lowNum], arr[i]

    print('arr2 out:', arr)
    return arr

selection_sort2(arr)


# Compares 1st to 2nd, 2nd to third and so on
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for x in range(n-i-1):
            if arr[x] > arr[x+1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]

    # print('bubble arr:', arr)
    return arr

# bubble_sort(arr)

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for x in range(n-i-1):
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]
    print('arrbubble', arr)
    return arr

bubbleSort(arr)

def oneAtATime(arr):
    x = len(arr)
    for i in range(x):
        for z in range(x-i-1):
            if arr[z] > arr[z+1]:
                arr[z], arr[z+1] = arr[z+1], arr[z]
    print('1atatime', arr)
    return arr

oneAtATime(arr)