#!/usr/bin/python3
""" Defines an empty class Rectangle."""


class Rectangle:
    """ A class representing a rectangle.
    """
    def __init__(self, width=0, height=0):
        """ Initializes a rectangle with the given width and height.

        Args:
            width: The rectangle width.
            height: The rectangle height.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Retrieves the rectangle width.

        Returns:
            int: The width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the rectangle width value.

        Args:
            value (int): the width value.

        Raises:
            TypeError: If the width value is not an integer.
            ValueError: If the width value is less than Zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves the rectangle height.

        Returns:
            int: The height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the rectangle height value.

        Args:
            value (int): the height value.

        Raises:
            TypeError: If the height value is not an integer.
            ValueErrror: If the height value is less than Zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns the rectangle perimeter."""
        if self.__width == 0 or self__.height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
