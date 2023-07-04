#!/usr/bin/python3
""" Defines an empty class Rectangle."""


class Rectangle:
    """ A class representing a rectangle.

    Attributes:
        number_of_instances (int): The rectangle instances count.
        print_symbol (any): The print symbol used in sting represntation.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initializes a rectangle with the given width and height.

        Args:
            width: The rectangle width.
            height: The rectangle height.
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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
        """ Returns the rectangle area.

        Returns:
            int: The area.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns the rectangle perimeter.

        Returns:
            int: The perimeter
        """
        if self.__width == 0 or self.height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ Returns the rectangle representation with the character #.
        If width or height is equal to 0, return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = [str(self.print_symbol) * self.__width] * self.__height
        return ("\n".join(rect))

    def __repr__(self):
        """ Returns a string string representation of the rectangle.
        """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """ Detect the rectangle instance deletion.
        Prints (Bye rectangle...) when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area value.

        Args:
            rect_1 (int): The first rectangle.
            rect_2 (int): The seconde rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 are not an instance of Rectangle.

        Returns:
            rect_1 if both have the same area value.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance with equal width and height.
        """
        return cls(size, size)
