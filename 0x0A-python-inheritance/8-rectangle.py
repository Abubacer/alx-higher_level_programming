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
