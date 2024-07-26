#!/usr/bin/python3
""" Module to build pascal triangle"""


def pascal_triangle(n):
    """ Function to create a list of list of a
    pascal triangle given an integer n
    """
    pascal = []
    if n <= 0:
        return []
    for i in range(n):
        tr = []
        for j in range(i + 1):
            if j == 0 or j == i:
                tr.append(1)
            elif i > 0 and j > 0:
                tr.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        pascal.append(tr)
    return pascal
