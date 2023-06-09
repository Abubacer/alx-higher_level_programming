#!/usr/bin/python3
""" new_in_list - a function that replaces an element in a list
at a specific position without modifying the original list. return
a copy of the original list if idx is negative or is out of range
"""


def new_in_list(my_list, idx, element):
    cp_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return cp_list
    else:
        cp_list[idx] = element
        return cp_list
