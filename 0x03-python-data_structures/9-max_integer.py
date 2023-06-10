#!/usr/bin/python3

def max_integer(my_list=[]):
    # a function that finds the biggest integer of a list.
    # If the list is empty, return None.
    if len(my_list) == 0:
        return None

    max_int = my_list[0]

    for n in my_list:
        if n > max_int:
            max_int = n
    return max_int
