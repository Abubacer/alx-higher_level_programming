#!/usr/bin/python3
""" print_matrix_integer - a function that prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        element_join = " ".join("{:d}".format(element) for element in row)
        print(element_join)
