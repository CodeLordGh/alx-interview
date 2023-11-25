#!/usr/bin/python3

"""
Module for determining the minimum number of coins required to make a given change.

This module provides a function `makeChange` that takes a list of coin denominations and a target change amount
and returns the minimum number of coins needed to make the change. If the change cannot be made, it returns -1.

Example Usage:

```python
import making_change

coins = [1, 2, 25]
total = 37
min_coins = making_change.makeChange(coins, total)
print(f"Minimum coins required: {min_coins}")

"""

# Function to make change with minimum number of coins
def makeChange(coins, total):
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins required for each total
    minCoins = [float('inf')] * (total + 1)

    # Set the minimum number of coins for 0 total to 0
    minCoins[0] = 0

    # Iterate through all coins
    for coin in coins:
        # Iterate through all possible totals up to the current total
        for i in range(1, total + 1):
            # If the current coin value is less than or equal to the current total
            if coin <= i:
                # Update the minimum number of coins for the current total
                # by considering the current coin and the minimum number of coins for the remaining total
                minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)

    # If the minimum number of coins for the total is not updated, it means the total cannot be met by any number of coins
    if minCoins[total] == float('inf'):
        return -1

    return minCoins[total]
