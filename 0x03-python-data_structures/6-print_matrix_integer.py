#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # a function that prints a matrix of integers.
    for row in matrix:
        element_join = " ".join("{:d}".format(element) for element in row)
        print(element_join)
