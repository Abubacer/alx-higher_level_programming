#!/usr/bin/python3
"""Define a function that returns the JSON representation of an object.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: the object to return its JSON representation.

    Returns:
        the JSON representation of an object.
    """
    return json.dumps(my_obj)
