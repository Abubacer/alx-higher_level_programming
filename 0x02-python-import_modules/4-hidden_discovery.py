#!/usr/bin/python3
import hidden_4

"""get_defined_names - a function that prints all the names defined
by the compiled module hidden_4.pyc
"""


def get_defined_names():
    compiled_module = dir(hidden_4)
    def_names = [name for name in compiled_module if not name.startswith('__')]
    for name in sorted(def_names):
        print(name)


if __name__ == "__main__":
    get_defined_names()
