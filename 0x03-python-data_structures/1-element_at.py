#!/usr/bin/python3
""" element_at - a function that retrieves an element from a list like in C.
return None if idx is negative or idx is out of range (greater than the number
of element in my_list).
"""


def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
