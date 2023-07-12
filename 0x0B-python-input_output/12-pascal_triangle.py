#!/usr/bin/python3
"""Defines a function representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of ints representing the Pascal’s triangle of n.

    Args:
        n (int): the number of rows to generate

    Returns:
         a list of lists of ints representing the Pascal’s triangle.
         if n <= 0 an empty list
    """
    if n <= 0:
        return []

    Pascal_triangle = []

    for row in range(n):
        current = []
        for colum in range(row + 1):
            if colum == 0 or colum == row:
                current.append(1)
            else:
                prev = Pascal_triangle[row - 1]
                current.append(prev[colum - 1] + prev[colum])
        Pascal_triangle.append(current)

    return Pascal_triangle
