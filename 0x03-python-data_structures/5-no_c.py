#!/usr/bin/env python3

def no_c(my_string):
    # a function that removes all characters c and C from a string.
    no_char = "cC"
    new_string = [char for char in my_string if char not in no_char]
    return ("".join(new_string))
