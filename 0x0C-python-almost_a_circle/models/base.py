#!/usr/bin/python3
"""Defines a Base class
"""


class Base:
    """
    This class represents a Base.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base.

        Args:
            id (int): the id attribute.
        """
        self.id = id

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
