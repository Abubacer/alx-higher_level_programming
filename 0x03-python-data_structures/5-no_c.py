#!/usr/bin/env python3

def no_c(my_string):
    # a function that removes all characters c and C from a string.
    no_char = "cC"
    chars = [char for char in my_string if char not in no_char]
    new_string = "".join(chars)
    return new_string
