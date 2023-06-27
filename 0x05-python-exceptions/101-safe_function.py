#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    # a function that executes a function safely.
    # Returns the result of the function.
    # Or returns None if something happens during the function,
    # and prints in stderr the error precede by Exception:
    try:
        quotient = fct(*args)
        return quotient
    except Exception as ex_info:
        print("Exception: {}".format(ex_info), file=sys.stderr)
        return None
