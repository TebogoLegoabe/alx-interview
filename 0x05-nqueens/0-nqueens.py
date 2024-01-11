#!/usr/bin/python3
"""
N queens
"""
import sys

def is_safe(board, row, col, n):
    """Check if there is a queen in the same row on the left side"""
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_nqueens_util(board, col, n):
    if col == n:
        print([[i, board[i]] for i in range(n)])
        return
    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[col] = i
            solve_nqueens_util(board, col + 1, n)

def solve_nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens_util([0] * n, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
