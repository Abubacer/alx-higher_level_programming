#!/usr/bin/python3
""" replace_in_list - a function that replaces an element of a list
at a specific position (like in C) If idx is negative or is out of range
the function does not modify anything and returns the original list
"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
