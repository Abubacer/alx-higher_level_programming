#!/usr/bin/python3
"""Define a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide each element in a matrix by a given number.

    Args:
        matrix (list[list[int or float]]): The matrix to be divided.
        div (int or float): The number to divide each matrix element by.

    Returns:
        list[list[float]]: A new matrix with each element divided
                           by the given number.

    Raises:
        TypeError: If the matrix is not a valid matrix of integers/floats,
                   if the div is not a number,
                   or if the rows of the matrix have different sizes.
        ZeroDivisionError: If the div is Zero
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(error)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error)
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError(error)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
