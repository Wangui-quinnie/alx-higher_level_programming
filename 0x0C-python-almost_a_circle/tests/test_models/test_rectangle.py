#!/usr/bin/python3
"""Tests for the Rectangle module."""


import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import sys
import os


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.saved_output = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        sys.stdout = self.saved_output

    def test_invalid_width_value(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertEqual(
            str(context.exception),
            "width must be > 0"
        )

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertEqual(
            str(context.exception),
            "x must be an integer"
        )

    def test_invalid_y_value(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(
            str(context.exception),
            "y must be >= 0"
        )

    def test_area_method(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display_method(self):
        r1 = Rectangle(4, 6)
        r1.display()
        output = sys.stdout.getvalue()
        expected_output = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(output, expected_output)

        r2 = Rectangle(2, 2)
        r2.display()
        output = sys.stdout.getvalue()
        expected_output += "##\n##\n"
        self.assertEqual(output, expected_output)

    def test_str_method(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_method_with_offsets(self):
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        output = sys.stdout.getvalue()
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(output, expected_output)

        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        output = sys.stdout.getvalue()
        expected_output += " ###\n ###\n"
        self.assertEqual(output, expected_output)

    def test_update_method(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")


if __name__ == "__main__":
    unittest.main()
