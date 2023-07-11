#!/usr/bin/python3
"""Define a function that reads a text file.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: the text file input.
    """
    with open(filename, encoding='utf-8') as filename:
        content = filename.read()
        print(content, end="")
