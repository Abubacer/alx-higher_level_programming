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
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the Square.

        Returns:
            int: the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the the size of the Square.

        Args:
            value (int): the new size value.

        Raises:
            TypeError: If size is not an int.
            ValueError: If size is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the current area of the Square.

        Returns:
            int: the current square area.
        """
        return (self.__size * self.__size)
