#!/usr/bin/python3
"""Define a subclass MyList"""


class MyList(list):
    """MyList a subclass of list superclass."""

    def print_sorted(self):
        """Prints the list in ascending sorted order"""
        print(sorted(self))
