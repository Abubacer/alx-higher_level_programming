#!/usr/bin/python3
"""Checks the object instance"""


def is_kind_of_class(obj, a_class):
    """Checks if  if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class.

    Args:
        obj (any): the object to check.
        a_class (type): the class instance.

    Returns:
         True if the object is an instance of the class.
         False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
