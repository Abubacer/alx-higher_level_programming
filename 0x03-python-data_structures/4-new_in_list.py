#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # a function that replaces an element in a list.
    # at a specific position without modifying the original list.
    # returns a copy of the original list if idx is negative.
    # or if idx is out of range.
    copy_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return copy_list
    else:
        copy_list[idx] = element
        return copy_list
