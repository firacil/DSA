def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)  # Initialize with infinity
    dp[0] = 0  # 0 coins needed to make amount 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)  # Use the coin

    return dp[amount] if dp[amount] != float('inf') else -1  # Return -1 if no solution

# Example
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))  # Output: 3