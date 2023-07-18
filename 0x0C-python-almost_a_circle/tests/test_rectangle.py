#!/usr/bin/python3
"""Unittest with test cases and edge cases of Rectangle class.
"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittest for testing Rectangle"""
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_three_args(self):
        r = Rectangle(5, 10, 2)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 0)

    def test_four_args(self):
        r = Rectangle(5, 10, 2, 3)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_five_args(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, 2, 3, 1, 6)

    def test_width_private(self):
        r = Rectangle(5, 10)
        with self.assertRaises(AttributeError):
            print(r.__width)

    def test_width_getter_setter(self):
        r = Rectangle(5, 10)
        r.width = 7
        self.assertEqual(r.width, 7)

    def test_height_private(self):
        r = Rectangle(5, 10)
        with self.assertRaises(AttributeError):
            print(r.__height)

    def test_height_getter_setter(self):
        r = Rectangle(5, 10)
        r.height = 12
        self.assertEqual(r.height, 12)

    def test_x_private(self):
        r = Rectangle(5, 10)
        with self.assertRaises(AttributeError):
            print(r.__x)

    def test_x_getter_setter(self):
        r = Rectangle(5, 10)
        r.x = 2
        self.assertEqual(r.x, 2)

    def test_y_private(self):
        r = Rectangle(5, 10)
        with self.assertRaises(AttributeError):
            print(r.__y)

    def test_y_getter_setter(self):
        r = Rectangle(5, 10)
        r.y = 3
        self.assertEqual(r.y, 3)


class TestRectangle_width(unittest.TestCase):
    """Unittest for testing Rectangle width"""
    def test_width_none(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(None, 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_string(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle("5", 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_float(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5.5, 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_complex(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5 + 3j, 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_dict(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle({"width": 5}, 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_list(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle([5], 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_set(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle({5}, 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_type(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(int, 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_frozenset(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(frozenset({5}), 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_bool(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(True, 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_range(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(range(5), 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_byte(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(b'5', 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_bytearray(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(bytearray(5), 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_infinity(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(float('inf'), 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_nan(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(float('nan'), 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_negative(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(-5, 10)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_width_zero(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(0, 10)
        self.assertEqual(str(context.exception), "width must be > 0")


class TestRectangle_Height(unittest.TestCase):
    """Unittest for testing Rectangle Height"""
    def test_height_none(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, None)
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_string(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, "10")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_float(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10.5)
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_complex(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 5 + 3j)
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_dict(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, {"height": 10})
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_list(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, [10])
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_set(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, {10})
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_type(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, int)
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_frozenset(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, frozenset({10}))
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_bool(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, True)
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_range(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, range(10))
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_byte(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, b'10')
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_bytearray(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, bytearray(10))
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_infinity(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, float('inf'))
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_nan(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, float('nan'))
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_negative(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(5, -10)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_height_zero(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(5, 0)
        self.assertEqual(str(context.exception), "height must be > 0")


class TestRectangle_X(unittest.TestCase):
    """Unittest for testing Rectangle x"""
    def test_x_none(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, None)
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_string(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, "2")
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_float(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2.5)
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_complex(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2 + 3j)
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_dict(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, {"x": 2})
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_list(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, [2])
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_set(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, {2})
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_type(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, int)
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_frozenset(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, frozenset({2}))
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_bool(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, True)
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_range(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, range(2))
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_byte(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, b'2')
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_bytearray(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, bytearray(2))
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_infinity(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, float('inf'))
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_nan(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, float('nan'))
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_negative(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(5, 10, -2)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_x_zero(self):
        r = Rectangle(5, 10, 0)
        self.assertEqual(r.x, 0)


class TestRectangle_Y(unittest.TestCase):
    """Unittest for testing Rectangle y"""
    def test_y_none(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, None)
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_string(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, "3")
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_float(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, 3.5)
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_complex(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, 3 + 4j)
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_dict(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, {"y": 3})
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_list(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, [3])
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_set(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, {3})
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_type(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, int)
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_frozenset(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, frozenset({3}))
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_bool(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, True)
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_range(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, range(3))
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_byte(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, b'3')
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_bytearray(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, bytearray(3))
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_infinity(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, float('inf'))
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_nan(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, float('nan'))
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_negative(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(5, 10, 2, -3)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_y_zero(self):
        r = Rectangle(5, 10, 2, 0)
        self.assertEqual(r.y, 0)


class TestRectangleMethods(unittest.TestCase):
    """Unittest for testing Rectangle methods"""
    def setUp(self):
        self.r = Rectangle(5, 10, 2, 3)

    @staticmethod
    def capture_stdout(Rectangle, cls_method):
        """Returns the text printed to stdout.

        Args:
            Rectangle: The Rectangle to print to stdout.
            cls_method (str): The method to run on rect.

        Returns:
            The text printed to stdout.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if cls_method == "print":
            print(Rectangle)
        else:
            Rectangle.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_methods(self):
        r1 = Rectangle(2, 3, 0, 0, 0)
        r2 = Rectangle(3, 2, 1, 0, 1)
        r3 = Rectangle(4, 5, 0, 1, 0)
        r4 = Rectangle(2, 4, 3, 2, 0)
        r5 = Rectangle(5, 1, 2, 4, 7)

        # Test display method for width and height only
        capture1 = TestRectangleMethods.capture_stdout(r1, "display")
        self.assertEqual("##\n##\n##\n", capture1.getvalue())

        # Test display method for width, height, and x
        capture2 = TestRectangleMethods.capture_stdout(r2, "display")
        self.assertEqual(" ###\n ###\n", capture2.getvalue())

        # Test display method for width, height, and y
        capture3 = TestRectangleMethods.capture_stdout(r3, "display")
        display3 = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display3, capture3.getvalue())

        # Test display method for width, height, x, and y
        capture4 = TestRectangleMethods.capture_stdout(r4, "display")
        display4 = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display4, capture4.getvalue())

        # Test display method with an extra argument
        with self.assertRaises(TypeError):
            r5.display(1)

    def test_area(self):
        self.assertEqual(self.r.area(), 50)

    def test_str_methods(self):
        r1 = Rectangle(4, 6)
        r2 = Rectangle(5, 5, 1)
        r3 = Rectangle(1, 8, 2, 4)
        r4 = Rectangle(13, 21, 2, 4, 7)
        r5 = Rectangle(7, 7, 0, 0, [4])

        # Test __str__() method for width and height only
        capture1 = TestRectangleMethods.capture_stdout(r1, "print")
        correct1 = "[Rectangle] ({}) 0/0 - 4/6\n".format(r1.id)
        self.assertEqual(correct1, capture1.getvalue())

        # Test __str__() method for width, height, and x
        correct2 = "[Rectangle] ({}) 1/0 - 5/5".format(r2.id)
        self.assertEqual(correct2, r2.__str__())

        # Test __str__() method for width, height, x, and y
        correct3 = "[Rectangle] ({}) 2/4 - 1/8".format(r3.id)
        self.assertEqual(correct3, str(r3))

        # Test __str__() method for width, height, x, y, and id
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r4))

        # Test __str__() method after changing attributes
        r5.width = 15
        r5.height = 1
        r5.x = 8
        r5.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r5))

        # Test __str__() method with an extra argument
        with self.assertRaises(TypeError):
            r5.__str__(1)

    def test_update_args(self):
        self.r.update(10, 20, 30, 40, 50)
        self.assertEqual(str(self.r), "[Rectangle] (10) 40/50 - 20/30")

    def test_update_kwargs(self):
        self.r.update(id=10, width=20, height=30, x=40, y=50)
        self.assertEqual(str(self.r), "[Rectangle] (10) 40/50 - 20/30")

    def test_to_dictionary_method(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r3 = Rectangle(10, 2, 4, 1, 2)

        # Test to_dictionary method output
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r1.to_dictionary())

        # Test no object changes after updating with to_dictionary
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

        # Test to_dictionary with an extra argument
        with self.assertRaises(TypeError):
            r3.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
