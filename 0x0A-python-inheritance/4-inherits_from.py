#!/usr/bin/python3
"""Checks the object instance"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj (any): the object to check.
        a_class (type): the class instance.

    Returns:
         True if the object is an instance of the class.
         False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
