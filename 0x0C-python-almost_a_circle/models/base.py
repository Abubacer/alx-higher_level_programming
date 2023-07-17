#!/usr/bin/python3
"""Defines a Base class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): the list of dictionaries.

        Returns:
            str: the JSON string representation of the list of dicts.
            if list_dictionaries is None or empty, return the string: "[]".
        """
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        If list_objs is None, save an empty list.
        The filename must be: <Class name>.json.

        Args:
            list_objs (list): The list of instances who inherits of Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                o_list = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(o_list))

    @classmethod
    def from_json_string(cls, json_string):
        """Returns a list of instances from the JSON str representation.

        Args:
            json_string (str): The JSON string representation.

        Returns:
            list: A list of instances.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            dictionary (dict): the key/value pairs of attributes.

        Returns:
            the instance with all attributes already set.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                insts = cls(6, 6)
            else:
                insts = cls(2)
            insts.update(**dictionary)
            return insts
