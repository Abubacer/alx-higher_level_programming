#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    # a function that prints an integer with error message.
    # Returns True if value  is an integer, Otherwise, returns False.
    # and prints in stderr the error precede by Exception:
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as ex_info:
        print("Exception: {}".format(ex_info), file=sys.stderr)
        return False
