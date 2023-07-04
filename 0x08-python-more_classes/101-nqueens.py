#!/usr/bin/python3
import sys


def solve_nqueens(n):
    """
    Solves the N queens puzzle problem and returns all possible solutions.

    Args:
        n (int): The size of NxN chessboard.

    Returns:
        list: A list of lists of all possible solutions to placing N
              N non-attacking queens on an NxN chessboard

    Raises:
        ValueError: If n is less than 4.
    """

    def check_is_safe(board, row_position, col_position):
        """ Check if a queen can be placed at the given position.

        Args:
            board (list): The current state of the board.
            row_position (int): The row of the position to be checked.
            col_position (int): The column of the position to be checked.

        Returns:
            True if it is safe to place the queen, otherwise False.
        """
        for i in range(row_position):
            if board[i] == col_position or \
               board[i] - i == col_position - row_position or \
               board[i] + i == col_position + row_position:
                return False
        return True

    def recursive_solve(board, current_row):
        """ Solve the N-queens puzzle using recursion.

        Args:
            board (list): The current state of the board.
            current_row (int): The current row to be processed.

        Returns:
            list: A list of lists that represent the solutions.
        """
        if current_row == n:
            return [board.copy()]

        solutions = []
        for colum in range(n):
            if check_is_safe(board, current_row, colum):
                board[current_row] = colum
                solutions.extend(recursive_solve(board, current_row + 1))
        return solutions

    board = [-1] * n
    return recursive_solve(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for sol in solutions:
        print([[i, sol[i]] for i in range(n)])
