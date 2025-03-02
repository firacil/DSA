# function to check whether any pair exists
# whose sum is equal to the given target value
def two_sum(arr, target):
    # first ensure the arr is sorted
    arr.sort()
    
    left, right = 0, len(arr) - 1
    
    # i terating while left pointer is less than right
    while left < right:
        sum = arr[left] + arr[right]
        
        # check if the sum matches the target
        if sum == target:
            return True
        elif sum < target:
            left += 1 # move left pointer to the right
        else:
            right -= 1 # move right pointer to the left
    
    # if no pair is found
    return False

arr = [0, -1, 2, -3, 1]
target = -2

if two_sum(arr, target):
    print("true")
else:
    print("false")