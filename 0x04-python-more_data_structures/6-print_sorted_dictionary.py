#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # a function that prints a dictionary by ordered keys.
    ordered_dict = dict(sorted(a_dictionary.items()))
    for key in ordered_dict:
        key_val = ordered_dict[key]
        print(key, ":", key_val)
