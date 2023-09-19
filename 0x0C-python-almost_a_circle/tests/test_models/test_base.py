#!/usr/bin/python3
"""Tests for the Base module."""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_set(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_to_json_string_empty(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_from_json_string_empty(self):
        json_list = Base.from_json_string("[]")
        self.assertEqual(json_list, [])

    def test_from_json_string_non_empty(self):
        json_str = '[{"id": 1}]'
        json_list = Base.from_json_string(json_str)
        self.assertEqual(json_list, [{"id": 1}])


if __name__ == "__main__":
    unittest.main()
