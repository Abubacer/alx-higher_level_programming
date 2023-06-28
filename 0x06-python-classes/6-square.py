#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    This class represents a Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square with the given size.

        Args:
            size (int): the size of the Square.
            position (int, int): the position of the Square.
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the Square.

        Returns:
            tuple: the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the Square.

        Args:
            value (tuple): the new position value.

        Raises:
            TypeError: If position is not a tuple of 2 positive int.
        """
        if not (
            isinstance(value, tuple)
            and len(value) == 2
            and all(isinstance(n, int) for n in value)
            and all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the current area of the Square.

        Returns:
            int: the current square area.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Prints in stdout the square with the character #.
        If size is equal to Zero, print an empty line.
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print("")
