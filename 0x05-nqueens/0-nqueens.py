#!/usr/bin/python3
""" Function to solve nqueens cheess game
"""
import sys


def is_safe(board, row, col):
    """ Check if a queen can be placed on board at (row, col) """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, solutions):
    """ Use backtracking to solve the N Queens problem """
    if col >= len(board):
        solutions.append([[r, c] for r in range(len(board)) for c in
                         range(len(board)) if board[r][c] == 1])
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1, solutions)
            board[i][col] = 0

    return False


def nqueens(N):
    """ Solve the N Queens problem and print all solutions """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, solutions)

    for solution in solutions:
        print(solution)


def main():
    """ Main function to handle input and output """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)


if __name__ == "__main__":
    main()
