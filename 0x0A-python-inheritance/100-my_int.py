#!/usr/bin/python3
"""Defines a MyInt subclass that inherits from int.
"""


class MyInt(int):
    """A subclass representing MyInt that invert == and !=."""

    def __eq__(self, value):
        """Override the (==) equality operator."""
        return not super().__eq__(value)

    def __ne__(self, value):
        """Override the (!=) inequality operator."""
        return not super().__ne__(value)
