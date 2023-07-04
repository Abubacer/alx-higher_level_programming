#!/usr/bin/python3
"""
Define a function for integer addition.
"""


def add_integer(a, b=98):
    """ Add two numbers.
    a and b must be first casted to integers if they are float.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int : The sum.

    Raises:
        TypeError: If either a or b is a non-integer and non-float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
