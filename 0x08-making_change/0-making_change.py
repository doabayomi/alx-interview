#!/usr/bin/python3
"""Coin change problem"""


def makeChange(coins, total):
    """Function to find least amount of coins"""
    coins.sort()
    change = [float('inf')] * (total + 1)
    change[0] = 0
    for n in range(1, total + 1):
        for coin in coins:
            if n - coin >= 0:
                change[n] = min(change[n],  change[n - coin] + 1)
    return change[total] if change[total] != float('inf') else -1
