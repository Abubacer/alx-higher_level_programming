#!/usr/bin/python3
"""Define a function that returns an object represented by a JSON.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str: the JSON string.

    Returns:
        an object (Python data structure) represented by a JSON str    ing.
    """
    return json.loads(my_str)
