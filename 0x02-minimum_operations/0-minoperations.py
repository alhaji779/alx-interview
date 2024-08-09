#!/usr/bin/env python3
""" Code to calculate number of possible operations
"""


def minOperations(n):
    """ Function takes @args n, returns no of operations
    """
    if not isinstance(n, int):
        return 0
    operator = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            operator += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            operator += 2
        elif clipboard > 0:
            done += clipboard
            operator += 1
    return operator
