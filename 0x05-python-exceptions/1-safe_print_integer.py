#!/usr/bin/python3

def safe_print_integer(value):
    # a function that prints an integer.
    # Returns True if the value is an integer, Otherwise, returns False.
    try:
        integer = int(value)
        print("{:d}".format(integer))
        return True
    except ValueError:
        pass
        return False
