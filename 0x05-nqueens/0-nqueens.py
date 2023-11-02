#!/usr/bin/python3
""" N queens puzzle is the challenge of placing N
    non-attacking queens on an N×N chessboard
"""
def is_safe(board, row, col):
    """a function that """
    # Check if it's safe to place a queen at board[row][col]
    for i in range(row):
        if board[i][col] == 1:
            return False
        if col - i >= 0 and board[row - i][col - i] == 1:
            return False
        if col + i < N and board[row - i][col + i] == 1:
            return False
    return True

def solve_nqueens(N):
    """ a function that return """
    board = [[0] * N for _ in range(N)]
    solutions = []

    def backtrack(row):
        """Back track"""
        if row == N:
            solutions.append([list(row) for row in board])
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0  # Backtrack

    backtrack(0)
    return solutions