#!/usr/bin/python3
"""add_tuple - a function that adds 2 tuples.
Returns a tuple with 2 integers
"""


def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    b = tuple_b + (0, 0)[:2 - len(tuple_b)]
    first_sum = a[0] + b[0]
    second_sum = a[1] + b[1]
    sum_tuple = (first_sum, second_sum)
    return sum_tuple
