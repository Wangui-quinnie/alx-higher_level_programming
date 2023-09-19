#!/usr/bin/python3
"""Tests for the Square module."""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        s = Square(2)
        self.assertEqual(s.size, 2)

    def test_size_setter(self):
        s = Square(2)
        s.size = 4
        self.assertEqual(s.size, 4)

    def test_area(self):
        s = Square(2)
        self.assertEqual(s.area(), 4)

    def test_str(self):
        s = Square(2, 1, 4, 5)
        self.assertEqual(str(s), "[Square] (5) 1/4 - 2")

    def test_size_setter_negative(self):
        s = Square(2)
        with self.assertRaises(ValueError):
            s.size = -3

    def test_size_setter_string(self):
        s = Square(2)
        with self.assertRaises(TypeError):
            s.size = "invalid"

    def test_size_setter_zero(self):
        s = Square(2)
        with self.assertRaises(ValueError):
            s.size = 0

    def test_init_negative_size(self):
        with self.assertRaises(ValueError):
            s = Square(-2)

    def test_init_invalid_size_type(self):
        with self.assertRaises(TypeError):
            s = Square("invalid")

    def test_init_zero_size(self):
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_str_negative_id(self):
        s = Square(2, 1, 4, -5)
        self.assertEqual(str(s), "[Square] (-5) 1/4 - 2")


if __name__ == "__main__":
    unittest.main()
