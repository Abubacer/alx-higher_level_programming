#!/usr/bin/python3

def safe_print_integer(value):
    # a function that prints an integer.
    # Returns True if the value is an integer, Otherwise, returns False.
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except ValueError:
        return False
