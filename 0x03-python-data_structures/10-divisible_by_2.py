#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # a function that finds all multiples of 2 in a list.
    # Return a new list with True or False, depending on whether the integer
    # at the same position in the original list is a multiple of 2
    # The new list have the same size as the original list
    multiples = ([True if my_list[n] % 2 == 0 else False
                 for n in range(len(my_list))])

    return multiples
