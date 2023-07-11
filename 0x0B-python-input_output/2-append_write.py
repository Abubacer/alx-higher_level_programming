#!/usr/bin/python3
"""Define a function that appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8).

    Args:
        filename: The path to the text file.
        text: The string to be written.

    Returns:
        the number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as filename:
        append_content = filename.write(text)
        return append_content
