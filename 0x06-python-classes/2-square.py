#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    This class represents a Square
    """
    def __init__(self, size=0):
        """
        Initializes a Square with the given size.
        The size must be an integer, otherwise raise a TypeError.
        If size is less than Zero, raise a ValueError.

        Args:
            size: the size of the Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
