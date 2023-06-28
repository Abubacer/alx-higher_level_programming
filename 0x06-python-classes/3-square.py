#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    This class represents a Square
    """
    def __init__(self, size=0):
        """
        Initializes a Square with the given size.

        Args:
            size (int): the size of the Square.

        Raises:
            TypeError: If size is not an int.
            ValueError: If size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the current area of the Square.

        Returns:
            int: the current square area.
        """
        return (self.__size * self.__size)
