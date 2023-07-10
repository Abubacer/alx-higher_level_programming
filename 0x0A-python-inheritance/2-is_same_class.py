#!/usr/bin/python3
"""Checks if the object is an instance of the specified class"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class.

    Args:
        obj (any): the object to check.
        a_class (type): the class instance.

    Returns:
         True if the object is an instance of the class.
         False otherwise.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
