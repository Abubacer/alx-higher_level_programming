#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # a function that prints a dictionary by ordered keys.
    ordered_keys = sorted(a_dictionary.keys())
    for key in ordered_keys:
        key_val = a_dictionary[key]
        print(key, ":", key_val)
