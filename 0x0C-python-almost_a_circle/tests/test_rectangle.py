#!/usr/bin/python3
"""Unittest of the Rectangle class.
"""
import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """
    Test case of the Rectangle class.
    """
    def test_setup(self):
        """
        Create a rectangle object for testing.
        """
        self.rectangle = None

    def test_width(self):
        """
        Test getter/setter for width attribute.
        """
        rectangle = Rectangle(10, 5, 2, 3, id=1)
        self.assertEqual(rectangle.width, 10)  # Check initial w
        rectangle.width = 15
        self.assertEqual(rectangle.width, 15)  # Check updated w

    def test_height(self):
        """
        Test getter/setter for height attribute.
        """
        rectangle = Rectangle(10, 5, 2, 3, id=1)
        self.assertEqual(rectangle.height, 5)  # Check initial h
        rectangle.height = 8
        self.assertEqual(rectangle.height, 8)  # Check updated h

    def test_x(self):
        """
        Test getter/setter for x attribute.
        """
        rectangle = Rectangle(10, 5, 2, 3, id=1)
        self.assertEqual(rectangle.x, 2)  # Check initial x
        rectangle.x = 4
        self.assertEqual(rectangle.x, 4)  # Check updated x

    def test_y(self):
        """
        Test getter/setter for y attribute.
        """
        rectangle = Rectangle(10, 5, 2, 3, id=1)
        self.assertEqual(rectangle.y, 3)  # Check initial y
        rectangle.y = 6
        self.assertEqual(rectangle.y, 6)  # Check updated y

    def test_id(self):
        """
        Test getter for id attribute.
        """
        rectangle = Rectangle(10, 5, 2, 3, id=1)
        self.assertEqual(rectangle.id, 1)  # Check initial id

    def test_edgecases(self):
        """
        Test a rectangle with zero width and height.
        """
        rectangle = Rectangle(0, 0)
        self.assertEqual(rectangle.width, 0)  # Check zero width
        self.assertEqual(rectangle.height, 0)  # Check zero height

        rectangle.width = 5  # Update width to non-zero value
        rectangle.height = 10  # Update height to non-zero value
        self.assertEqual(rectangle.width, 5)  # Check updated width
        self.assertEqual(rectangle.height, 10)  # Check updated height

        """
        Test negative values for width, height, x, and y.
        """
        rectangle = Rectangle(-5, -10, -2, -3)
        self.assertEqual(rectangle.width, -5)  # Check negative width
        self.assertEqual(rectangle.height, -10)  # Check negative height
        self.assertEqual(rectangle.x, -2)  # Check negative x
        self.assertEqual(rectangle.y, -3)  # Check negative y


if __name__ == '__main__':
    unittest.main()
