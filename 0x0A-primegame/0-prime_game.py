#!/usr/bin/python3
"""Prime game module.
"""

def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds."""
    
    if x < 1 or not nums:
        return None
    
    def generate_primes(limit):
        """Generates prime numbers up to the given limit."""
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if primes[i]:
                for j in range(i*i, limit + 1, i):
                    primes[j] = False
        return primes
    
    def count_primes(nums, primes):
        """Counts prime numbers in the given list."""
        return sum(1 for num in nums if primes[num])
    
    marias_wins, bens_wins = 0, 0
    max_num = max(nums)
    primes = generate_primes(max_num)
    for _ in range(x):
        primes_count = count_primes(nums, primes[:max_num + 1])
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
