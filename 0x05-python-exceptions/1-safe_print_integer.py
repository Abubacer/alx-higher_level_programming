#!/usr/bin/python3

def safe_print_integer(value):
    # a function that prints an integer.
    # Returns True if the value is an integer, Otherwise, returns False.
    try:
        integer = value
        print("{:d}".format(integer))
    except ValueError:
        return False
    else:
        return True
