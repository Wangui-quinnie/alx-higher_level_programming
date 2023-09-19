#!/usr/bin/python3
"""Tests for the Square module."""


import unittest
from models.square import Square
import io
import sys


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.saved_output = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        sys.stdout = self.saved_output

    def test_square_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)

        s3 = Square(3, 1, 3, 12)
        self.assertEqual(s3.area(), 9)

    def test_square_display(self):
        s1 = Square(5)
        s1.display()
        output = sys.stdout.getvalue()
        expected_output = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(output, expected_output)

        s2 = Square(2, 2)
        s2.display()
        output = sys.stdout.getvalue()
        expected_output += "  ##\n  ##\n"
        self.assertEqual(output, expected_output)

        s3 = Square(3, 1, 3, 12)
        s3.display()
        output = sys.stdout.getvalue()
        expected_output += "\n\n\n ###\n ###\n ###\n"
        self.assertEqual(output, expected_output)

    def test_square_size_getter(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s2 = Square(2, 2)
        self.assertEqual(s2.size, 2)

        s3 = Square(3, 1, 3, 12)
        self.assertEqual(s3.size, 3)

    def test_square_size_setter(self):
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)

        s2 = Square(2, 2)
        s2.size = 3
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.width, 3)
        self.assertEqual(s2.height, 3)

        s3 = Square(3, 1, 3, 12)
        s3.size = 4
        self.assertEqual(s3.size, 4)
        self.assertEqual(s3.width, 4)
        self.assertEqual(s3.height, 4)

    def test_square_size_setter_invalid_type(self):
        s1 = Square(5)
        with self.assertRaises(TypeError):
            s1.size = "9"

    def test_square_update_with_args(self):
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s1.update(1, 2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s1.update(1, 2, 3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 0)

        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

    def test_square_update_with_kwargs(self):
        s1 = Square(5)
        s1.update(x=12)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 0)


if __name__ == "__main__":
    unittest.main()
