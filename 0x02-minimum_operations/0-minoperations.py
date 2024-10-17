#!/usr/bin/python3
"""Minimum operations problem."""


def minOperations(n: int) -> int:
    """Find minimum number of copyAll and paste operations to reach n.

    Args:
        n (int): Target character count.

    Returns:
        int: the number of minimum operations to reach n.
    """
    if n < 0:
        return 0

    min_ops = [0] * (n + 1)

    for i in range(2, n + 1):
        min_ops[i] = i

        for j in range(1, (i // 2) + 1):
            if i % j == 0:
                min_ops[i] = min(min_ops[i], min_ops[j] + (i // j))

    return min_ops[n]
