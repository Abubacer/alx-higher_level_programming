#!/usr/bin/python3
""" print_reversed_list_integer - a function that prints all integers
of a list, in reverse order.
"""


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for number in my_list:
        print("{}".format(number))
