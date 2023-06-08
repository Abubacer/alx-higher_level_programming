#!/usr/bin/python3
import inspect

"""get_defined_names - a function that prints all the names defined
by the compiled module hidden_4.pyc
"""


def get_defined_names():
    def_names = [name for name in dir('hidden_4') if not name.startswith('__')]
    for name in sorted(def_names):
        print(name)


if __name__ == "__main__":
    get_defined_names()
