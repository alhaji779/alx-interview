#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    # Edge case: if total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize a DP array with a large value (inf) to represent unattainable amounts
    dp = [float('inf')] * (total + 1)

    # Base case: It takes 0 coins to make total 0
    dp[0] = 0

    # Iterate over all coin values
    for coin in coins:
        for amount in range(coin, total + 1):
            # Update the dp array for each amount by checking if we can use the current coin
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, return -1 (total can't be met)
    return dp[total] if dp[total] != float('inf') else -1
