#!/usr/bin/python3
"""Tests for the Base module."""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
import os
import sys


class TestBase(unittest.TestCase):

    def setUp(self):
        self.saved_output = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        sys.stdout = self.saved_output

    def test_id_argument(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_to_json_string_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_none(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        filename = "Rectangle.json"
        self.assertTrue(os.path.isfile(filename))

        with open(filename, "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        filename = "Rectangle.json"
        self.assertTrue(os.path.isfile(filename))

        with open(filename, "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_from_json_string_empty(self):
        json_str = ""
        result = Base.from_json_string(json_str)
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        json_str = None
        result = Base.from_json_string(json_str)
        self.assertEqual(result, [])

    def test_from_json_string_valid(self):
        json_str = (
            '[{"id": 1, "width": 10, "height": 7}, '
            '{"id": 2, "width": 2, "height": 4}]'
        )
        result = Base.from_json_string(json_str)
        expected_list = [
            {"id": 1, "width": 10, "height": 7},
            {"id": 2, "width": 2, "height": 4}
        ]
        self.assertEqual(result, expected_list)

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsInstance(r2, Rectangle)
        self.assertIsNot(r1, r2)

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertIsInstance(list_rectangles_output, list)
        self.assertTrue(
            all(isinstance(rect, Rectangle) for rect in list_rectangles_output)
        )
        self.assertEqual(len(list_rectangles_output), 2)

    def test_load_from_file_square(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertIsInstance(list_squares_output, list)
        self.assertTrue(
            all(isinstance(square, Square) for square in list_squares_output)
        )
        self.assertEqual(len(list_squares_output), 2)

    def test_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])


if __name__ == "__main__":
    unittest.main()
