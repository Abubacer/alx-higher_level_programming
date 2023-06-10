#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # a function that adds 2 tuples
    # if a tuple is smaller than 2, use the value 0 for each missing integer
    # if a tuple is bigger than 2, use only the first 2 integers
    A = tuple_a + (0, 0)[:2 - len(tuple_a)]
    # create a new tuple (A) by concatenating tuple_a with a tuple (0, 0).
    # the slicing operation [:2 - len(tuple_a)] ensure that (A) has length of
    # at least 2. If tuple_a has a length of 2 or more the slicing is
    # essentially an empty slice[:] resulting in (A) being the same as tuple_a
    # otherwise, it appends (0, 0) to tuple_a to ensure (A) has two elements.
    B = tuple_b + (0, 0)[:2 - len(tuple_b)]
    sum_tuple = (A[0] + B[0], A[1] + B[1])
    return sum_tuple
