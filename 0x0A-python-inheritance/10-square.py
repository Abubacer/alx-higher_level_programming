#!/usr/bin/python3
"""Defines a subclass Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass representing a Square"""
    def __init__(self, size):
        """Initializes a Square.

        Args:
            size (int): the Square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
