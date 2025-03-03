def max_subarray_sum(arr, k):
    # lets use sliding window technique to solve max subarray_sum
    
    max_sum = sum(arr[:k])
    window_sum = max_sum # now intializing our window starting from the first
    
    
    # we need for loop to implement sliding
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k] # sliding
        max_sum = max(window_sum, max_sum)
    
    return max_sum

print(max_subarray_sum([2, 1, 5, 1, 3, 2], 3))