#!/usr/bin/python3

def no_c(my_string):
    # a function that removes all characters c and C from a string.
    char_filter = 'cC'
    new_str = [char for char in my_string if char not in char_filter]
    return ("".join(new_str))
