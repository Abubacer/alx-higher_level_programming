#!/usr/bin/python3
"""Defines a student class."""


class Student:
    """
    This class represents a Student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student.

        Args:
            first_name (str): the first name.
            last_name (str): the last name.
            age (int): the age of the Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved.

        Args:
            attrs: optional list of attribute names to be retrieved.
        """
        jsonDict = {}

        obj_attr = vars(self)

        for attr, value in obj_attr.items():
            if attrs is None or attr in attrs:
                if isinstance(value, (list, dict, str, int, bool)):
                    jsonDict[attr] = value

        return jsonDict
