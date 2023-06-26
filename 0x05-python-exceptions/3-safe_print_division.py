#!/usr/bin/python3

def safe_print_division(a, b):
    # a function that divides 2 integers and prints the result.
    # Returns the value of the division, otherwise: None.
    try:
        quotient = a / b
        return quotient
    except (ZeroDivisionError, TypeError):
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
