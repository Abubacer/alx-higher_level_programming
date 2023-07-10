#!/usr/bin/python3
"""Define an object attributes and methods lookup function.
"""


def lookup(obj):
    """ Returns the list of available attributes and methods of an object.
    """
    attr_list = dir(obj)
    return attr_list
