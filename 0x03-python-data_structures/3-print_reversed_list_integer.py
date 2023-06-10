#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    # a function that prints all integers of a list, in reverse order.
    if type(my_list) == list:
        my_list.reverse()
        for integer in my_list:
            print("{:d}".format(integer))
