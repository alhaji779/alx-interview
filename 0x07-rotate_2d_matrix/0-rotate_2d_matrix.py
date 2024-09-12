#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """
    matrix.reverse()
    # Next, we swap the elements in the diagonal only once
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
