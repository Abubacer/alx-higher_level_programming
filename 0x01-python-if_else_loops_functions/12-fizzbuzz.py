#!/usr/bin/python3

"""
fizzbuzz - a function that prints the numbers from 1 to 100
separated by a space it prints For multiples of three Fizz
instead of the number and for multiples of five Buzz and for
multiples of three and five, print FizzBuzz
"""


def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0:
            print("Fizz ", end="")
        elif n % 5 == 0:
            print("Buzz ", end="")
        elif n % 3 and n % 5 == 0:
            print("FizzBuzz ", end="")
        else:
            print("{} ".format(n), end="")
