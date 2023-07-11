#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass representing a Rectangle"""
    def __init__(self, width, height):
        """Initializes a Rectangle.

        Args:
            width (int): the Rectangle width.
            height (int): the Rectangle height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns and prints the rectangle description:
        [Rectangle] <width>/<height>.
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
