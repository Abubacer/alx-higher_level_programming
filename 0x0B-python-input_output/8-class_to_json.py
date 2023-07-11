#!/usr/bin/python3
"""Defines a function that returns the dictionary description for
JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object.

    Args:
        obj: an instance of a Class.

    Returns:
        A dictionary description representing the object's attributes.
    """
    jsonDict = {}

    obj_attr = vars(obj)

    for attr, value in obj_attr.items():
        if isinstance(value, (list, dict, str, int, bool)):
            jsonDict[attr] = value

    return jsonDict
