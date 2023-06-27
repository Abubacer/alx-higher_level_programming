#!/usr/bin/python3

def magic_calculation(a, b):
    #  a function that calculates a and b and returns the result.
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
        except Exception as exps:
            raise exps
    return result
