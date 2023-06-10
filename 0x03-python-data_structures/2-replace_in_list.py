#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # a function that replaces an element of a list at a specific position
    # If idx is negative or is out of range the function does not modify
    # anything and returns the original list.
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
