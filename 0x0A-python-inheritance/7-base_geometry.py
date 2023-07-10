#!/usr/bin/python3
"""Defines BaseGeometry class."""


class BaseGeometry:
    """A class representing the BaseGeometry."""
    def __init__(self):
        """Initializes the BaseGeometry"""

    def area(self):
        """The BaseGeometry area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value arg as an int.

        Args:
            name (str): the name of arg.
            value (int): the arg to validate

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
