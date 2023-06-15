#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # a function that returns a new dictionary with all values
    # multiplied by 2
    new_dict_x2 = {key: val * 2 for key, val in a_dictionary.items()}
    return new_dict_x2
