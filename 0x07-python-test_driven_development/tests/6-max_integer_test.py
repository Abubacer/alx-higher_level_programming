#!/usr/bin/python3
"""
Module: 6-max_integer_test

This module contains unittests for the max_integer function.

The max_integer function takes a list of integers as input
and returns the maximum value in the list.

The unit tests cover various testcases, including: ordered and unordered lists,
empty lists, lists with a single element, with max value at beginning, strings,
lists of floats and ints, and lists of strings.

To run the unit tests, execute this script directly.

Author: Aziz Belkharmoudi
"""
import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unit tests for the max_integer function."""

    def test_ordered(self):
        """An ordered list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered(self):
        """An unordered list of integers"""
        unordered = [2, 1, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_beginning(self):
        """A list with a beginning max value int"""
        max_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_beginning), 4)

    def test_empty_list(self):
        """An empty list"""
        empty_list = []
        self.assertIsNone(max_integer(empty_list))

    def test_single_element(self):
        """A list with only a single element"""
        single_element = [1]
        self.assertEqual(max_integer(single_element), 1)

    def test_floats(self):
        """a list of floats"""
        floats = [1.50, 8.30, -9.123, 25.2, 5.0]
        self.assertEqual(max_integer(floats), 25.2)

    def test_ints_floats(self):
        """A list of mixed ints and floats"""
        ints_floats = [1.5, 25.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_floats), 25.5)

    def test_str(self):
        """A string"""
        string = "Python"
        self.assertEqual(max_integer(string), 'y')

    def test_list_of_strs(self):
        """A list of strings"""
        strings = ["Python", "is", "awsome"]
        self.assertEqual(max_integer(strings), "is")

    def test_empty_str(self):
        """An empty string"""
        self.assertIsNone(max_integer(""))


if __name__ == '__main__':
    unittest.main()
