def longest_unique_substring(s):
    char_set = set() # declaring empty set to add unique s
    left = 0 # intializing left to use two pointer
    max_length = 0 # track the longest unique length
    
    # let's loop over a given string s to start counting unique
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
print(longest_unique_substring("abcabcbb"))  # Output: 3
print(longest_unique_substring("bbbbb"))  # Output: 1
print(longest_unique_substring("pwwkew"))  # Output: 3