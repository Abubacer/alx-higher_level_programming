#!/usr/bin/python3

"""
fizzbuzz - a function that prints the numbers from 1 to 100
separated by a space. It prints instead of the number : for
multiples of three Fizz and for multiples of five Buzz, and for
multiples of three and five FizzBuzz
"""


def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz ", end="")
        elif n % 3 == 0:
            print("Fizz ", end="")
        elif n % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(n), end="")
