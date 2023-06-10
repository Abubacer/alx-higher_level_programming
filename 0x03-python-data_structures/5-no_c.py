#!/usr/bin/env python3

def no_c(my_string):
    # a function that removes all characters c and C from a string.
    new_str = [ch for ch in my_string if ch != 'c' and ch != 'C']
    return ("".join(new_str))
