#!/usr/bin/python3
"""Prime game algorithm"""


def isWinner(x, nums):
    """Finds winner of prime game algorithm"""
    if not nums or x < 1:
        return None

    # Step 1: Precompute primes using the Sieve of Eratosthenes
    max_n = max(nums)  # Find the largest n in the input
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False

    # Step 2: Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    # Step 3: Determine the winner for each game
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of primes up to n
        primes_up_to_n = prime_count[n]
        # If the number of primes is odd, Maria wins; otherwise, Ben wins
        if primes_up_to_n % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Return the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return No
