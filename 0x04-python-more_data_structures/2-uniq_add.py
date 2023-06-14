#!/usr/bin/python3
def uniq_add(my_list=[]):
    # a function that adds all unique integers in a list
    # (only once for each integer).
    my_set = set(my_list)
    sum_uniq = sum([n for n in my_set])
    return sum_uniq
