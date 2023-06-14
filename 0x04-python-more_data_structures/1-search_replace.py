#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # a function that replaces all occurrences of an element by another
    # in a new list.
    return [replace if n == search else n for n in my_list]
