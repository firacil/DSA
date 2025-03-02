# partition function

def partition(arr, low, high):
    
    # choose the pivot
    pivot = arr[high]
    
    # index of smaller element and indicates
    # the right position of pivot found so far
    i = low - 1
    
    # traverse arr[low..high] and move all smaller
    # elements to the left side. elements from low to
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    # move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)
    return i + 1

# swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# Quicksort function implementation
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        
        # recursion calls for smaller elements
        # and greater or equals element
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# main driver code
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    
    quicksort(arr, 0, n - 1)
    for val in arr:
        print(val, end=" ")