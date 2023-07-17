#!/usr/bin/python3
"""Defines a Base class
"""
import json
import csv


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
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
                dictslist = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(dictslist))

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

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            dictionary (dict): the key/value pairs of attributes.

        Returns:
            base: an instance with all attributes already set.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_inst = cls(1, 2)
            else:
                new_inst = cls(3)
            new_inst.update(**dictionary)
            return new_inst

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances.

        Returns:
            return an empty list, if the file doesn’t exist.
            otherwise, a list of instances.
        """
        filename = f"{cls.__name__ }.json"
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                dictslist = Base.from_json_string(file.read())
                return [cls.create(**d) for d in dictslist]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a CSV file.

        Args:
            list_objs (list): The data to be serialized.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline="", encoding='utf-8') as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes objects from a CSV file.

        Returns:
            list: The list of deserialized objects.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(file, fieldnames=fieldnames)
                listdicts = [
                    dict([k, int(v)] for k, v in d.items())
                    for d in reader
                ]
                return [cls.create(**d) for d in listdicts]
        except FileNotFoundError:
            return []
