#!/usr/bin/python3
"""Define a a function that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8).

    Args:
        filename: the text file.
        text: the string to write.

    Returns:
        the number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as filename:
        num_chars = filename.write(text)
        return num_chars
