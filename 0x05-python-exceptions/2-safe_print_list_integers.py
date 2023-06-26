#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    # a function that prints the first x elements of a list and only integers.
    # Returns the real number of integers printed.
    element_count = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            element_count += 1
        except (ValueError, TypeError):
            continue
    print()
    return element_count
