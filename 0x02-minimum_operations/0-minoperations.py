#!/usr/bin/env python3
""" Code to calculate number of possible operations
"""


def minOperations(n):
    """ Function takes @args n, returns no of operations
    """
    operations = 0
    divisor = 2
    if n <= 1:
        return 0
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
