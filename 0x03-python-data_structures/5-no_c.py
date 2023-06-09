#!/usr/bin/env python3
""" no_c - a function that removes all characters c and C from a string.
Return the new string.
"""


def no_c(my_string):
    no_char = "cC"
    chars = [char for char in my_string if char not in no_char]
    new_string = "".join(chars)
    return new_string
