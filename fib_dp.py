def fib_dp(n, memory={}):
    # first check if it is less than or equal to 1
    if n <= 1:
        return n
    
    # now check if the solution is not in our memory
    if n not in memory:
        memory[n] = fib_dp(n - 1, memory) + fib_dp(n - 2, memory)
    
    return memory[n]

print(fib_dp(10)) # output must 55