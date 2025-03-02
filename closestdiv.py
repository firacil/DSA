def closest(n, m):
    close = 0
    min_diff = float('inf')
    
    # checking numbers arond n
    for i in range(n - abs(m), n + abs(m) + 1):
        if i % m == 0:
            difference = abs(n - i)
            
            if difference < min_diff or \
                (difference == min_diff and abs(i) > abs(close)):
                    close = i
                    min_diff = difference
    return close

if __name__ == "__main__":
    n = 15
    m = 6
    print(closest(n, m))