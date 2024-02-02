#!/usr/bin/python3
"""
Determine the fewest number of coins needed to meet
a given amount total
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount.

    Args:
        coins: A list of the values of the coins in your possession.
        total: The target amount to meet.

    Returns:
        The fewest number of coins needed to meet the target amount,
        or -1 if it's impossible.
    """

    if total == 0:
        return 0
    elif total < 0:
        return -1

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
