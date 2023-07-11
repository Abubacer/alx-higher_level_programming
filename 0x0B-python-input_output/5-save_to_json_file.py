#!/usr/bin/python3
"""Define a function that writes an Object to a text file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: the objet to be writeen.
        filename: the text file.
    """
    with open(filename, mode='w', encoding='utf-8') as filename:
        json.dump(my_obj, filename)
