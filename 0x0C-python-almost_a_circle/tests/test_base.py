#!/usr/bin/python3
"""Unittest for the Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Unittest and testcase for the base class.
    """
    def test_constructor_id(self):
        """
        Test the constructor when id is given.
        """
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_constructor_without_id(self):
        """
        Test the constructor when id is not given.
        """
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_constructor_negative_id(self):
        """
        Test the constructor when a negative id is given.
        """
        obj = Base(-5)
        self.assertEqual(obj.id, -5)

    def test_constructor_zero_id(self):
        """
        Test the constructor when a zero id is given.
        """
        obj = Base(0)
        self.assertEqual(obj.id, 0)


if __name__ == '__main__':
    unittest.main()
