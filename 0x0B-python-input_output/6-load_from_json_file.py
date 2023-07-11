#!/usr/bin/python3
"""Define a function that creates an Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”

    Args:
        filename: the json file.

    Returns:
        the created object.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
