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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        jsonDict = {}

        obj_attr = vars(self)

        for attr, value in obj_attr.items():
            if isinstance(value, (list, dict, str, int, bool)):
                jsonDict[attr] = value

        return jsonDict
