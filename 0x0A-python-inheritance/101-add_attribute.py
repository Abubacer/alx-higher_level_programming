#!/usr/bin/python3
"""A function that adds a new attribute to an object"""


def add_attribute(obj, attrName, attrValue):
    """Add a new attribute to an object if it's possible.

    Args:
        obj: the object to which the attribute will be added.
        attrName (str): the name of the attribute.
        attrValue: the value of the attribute to be added.

    Raises:
        TypeError: if the object can’t have new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attrName, attrValue)
