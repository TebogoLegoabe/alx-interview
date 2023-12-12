#!/usr/bin/python3
"""
Text file with character H,can only execute two operations in the file:
copy all and paste
"""


def  minOperations(n):
    """
    method that calculates the fewest numbers of operations needed to result
    in exactly n H characters in the file.

    Return: 
    integer
    if n is impossible to achieve, return 0
    """
    if n == 1 or n < 0:
        return 0

    operations = 0
    divisor = 2

    while n > 2:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
