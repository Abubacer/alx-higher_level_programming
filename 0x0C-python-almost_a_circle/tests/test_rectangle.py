#!/usr/bin/python3
"""Unittest with test cases and edge cases of Rectangle class.
"""
import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """
    Test case of the Rectangle class.
    """

    def test_init(self):
        """
        Test the initialization of the Rectangle class.
        """
        # Create a rectangle with width 10, height 5, x position 2, y position 3, and id 1
        rectangle = Rectangle(10, 5, 2, 3, id=1)
        # Check the attributes
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    def test_width(self):
        """
        Test the getter and setter for the width attribute.
        """
        # Create a rectangle with width 10
        rectangle = Rectangle(10, 5, 2, 3, id=1)
        # Check the initial width
        self.assertEqual(rectangle.width, 10)
        # Update the width to 15
        rectangle.width = 15
        # Check the updated width
        self.assertEqual(rectangle.width, 15)

        # Test invalid width values
        # Test non-integer width
        with self.assertRaises(TypeError):
            rectangle.width = "15"
        # Test width less than or equal to zero
        with self.assertRaises(ValueError):
            rectangle.width = 0
        with self.assertRaises(ValueError):
            rectangle.width = -10

    def test_height(self):
        """
        Test the getter and setter for the height attribute.
        """
        # Create a rectangle with height 5
        rectangle = Rectangle(10, 5, 2, 3, id=1)
        # Check the initial height
        self.assertEqual(rectangle.height, 5)
        # Update the height to 8
        rectangle.height = 8
        # Check the updated height
        self.assertEqual(rectangle.height, 8)

        # Test invalid height values
        # Test non-integer height
        with self.assertRaises(TypeError):
            rectangle.height = "8"
        # Test height less than or equal to zero
        with self.assertRaises(ValueError):
            rectangle.height = 0
        with self.assertRaises(ValueError):
            rectangle.height = -5

    def test_x(self):
        """
        Test the getter and setter for the x attribute.
        """
        # Create a rectangle with x position 2
        rectangle = Rectangle(10, 5, 2, 3, id=1)
        # Check the initial x position
        self.assertEqual(rectangle.x, 2)
        # Update the x position to 4
        rectangle.x = 4
        # Check the updated x position
        self.assertEqual(rectangle.x, 4)

        # Test invalid x values
        # Test non-integer x
        with self.assertRaises(TypeError):
            rectangle.x = "4"
        # Test negative x
        with self.assertRaises(ValueError):
            rectangle.x = -2

    def test_y(self):
        """
        Test the getter and setter for the y attribute.
        """
        # Create a rectangle with y position 3
        rectangle = Rectangle(10, 5, 2, 3, id=1)
        # Check the initial y position
        self.assertEqual(rectangle.y, 3)
        # Update the y position to 6
        rectangle.y = 6
        # Check the updated y position
        self.assertEqual(rectangle.y, 6)

        # Test invalid y values
        # Test non-integer y
        with self.assertRaises(TypeError):
            rectangle.y = "6"
        # Test negative y
        with self.assertRaises(ValueError):
            rectangle.y = -3

    def test_update(self):
        """
        Test the update method with positional and keyword arguments.
        """
        # Create a rectangle with initial values
        rectangle = Rectangle(10, 5, 2, 3, id=1)
        # Update using positional arguments
        rectangle.update(2, 8, 6, 4, 5)
        # Check the updated attributes
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)
        # Update using keyword arguments
        rectangle.update(id=3, width=12, height=7, x=6, y=7)
        # Check the updated attributes
        self.assertEqual(rectangle.id, 3)
        self.assertEqual(rectangle.width, 12)
        self.assertEqual(rectangle.height, 7)
        self.assertEqual(rectangle.x, 6)
        self.assertEqual(rectangle.y, 7)

    def test_str(self):
        """
        Test the string representation of the rectangle.
        """
        # Create a rectangle with id 1, width 10, height 5, x position 2, and y position 3
        rectangle = Rectangle(10, 5, 2, 3, id=1)
        # Check the string representation
        expected_str = "[Rectangle] (1) 2/3 - 10/5"
        self.assertEqual(str(rectangle), expected_str)

    def test_display(self):
        """
        Test the display method.
        """
        # Create a rectangle with width 5, height 3, and x position 2
        rectangle = Rectangle(5, 3, 2, 3, id=1)
        # Redirect stdout to a StringIO object for testing
        import sys
        from io import StringIO
        stdout = sys.stdout
        sys.stdout = output = StringIO()
        # Call the display method
        rectangle.display()
        # Get the printed output
        output_value = output.getvalue()
        # Restore stdout
        sys.stdout = stdout
        # Check the printed output
        expected_output = '\n\n\n  #####\n  #####\n  #####\n'
        self.assertEqual(output_value, expected_output)

    def test_area(self):
        """
        Test the area method.
        """
        # Create a rectangle with width 10 and height 5
        rectangle = Rectangle(10, 5, 2, 3, id=1)
        # Check the area
        self.assertEqual(rectangle.area(), 50)


if __name__ == '__main__':
    unittest.main()
