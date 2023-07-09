#!/usr/bin/python


def lookup(obj):
    """ Returns the list of available attributes and methods of an object.
    """
    attr_list = [name for name in dir(obj)]
    return attr_list
