#!/usr/bin/python3
"""
Define a function that prints a square.
"""


def print_square(size):
    """
    Print a square of '#' characters.

    Args:
        size (int): The size of the square to print.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than Zero.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    square = "#" * size
    for idx in range(size):
        print(square)
