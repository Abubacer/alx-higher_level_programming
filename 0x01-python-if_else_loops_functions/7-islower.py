#!/usr/bin/python3

""" islower: a function that checks for lowercase character.
Returns True if c is lowercase or False otherwise."""


def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
