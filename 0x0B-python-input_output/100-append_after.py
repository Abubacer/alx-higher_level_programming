#!/usr/bin/python3
"""Defines a function that inserts a line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a
    specific string.

    Args:
        filename: the name of the file.
        search_string: the str to search for.
        new_string: the new line to insert.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []

    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as file:
        file.writelines(new_lines)
