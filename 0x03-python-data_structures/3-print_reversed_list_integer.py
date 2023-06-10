#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    # a function that prints all integers of a list, in reverse order.
    my_list.reverse()
    for number in my_list:
        print("{:d}".format(number))
