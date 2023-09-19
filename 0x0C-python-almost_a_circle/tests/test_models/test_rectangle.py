#!/usr/bin/python3
"""Tests for the Rectangle module."""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)

    def test_width_setter(self):
        r = Rectangle(2, 3)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_height_setter(self):
        r = Rectangle(2, 3)
        r.height = 6
        self.assertEqual(r.height, 6)

    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(2, 3, 1, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 1/4 - 2/3")

    def test_width_setter_negative(self):
        r = Rectangle(2, 3)
        with self.assertRaises(ValueError):
            r.width = -3

    def test_width_setter_string(self):
        r = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r.width = "invalid"

    def test_width_setter_zero(self):
        r = Rectangle(2, 3)
        with self.assertRaises(ValueError):
            r.width = 0

    def test_height_setter_negative(self):
        r = Rectangle(2, 3)
        with self.assertRaises(ValueError):
            r.height = -3

    def test_height_setter_string(self):
        r = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r.height = "invalid"

    def test_height_setter_zero(self):
        r = Rectangle(2, 3)
        with self.assertRaises(ValueError):
            r.height = 0

    def test_init_negative_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-2, 3)

    def test_init_negative_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(2, -3)

    def test_init_invalid_width_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 3)

    def test_init_invalid_height_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, "invalid")

    def test_init_zero_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 3)

    def test_init_zero_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(2, 0)

    def test_str_negative_id(self):
        r = Rectangle(2, 3, 1, 4, -5)
        self.assertEqual(str(r), "[Rectangle] (-5) 1/4 - 2/3")


if __name__ == "__main__":
    unittest.main()
