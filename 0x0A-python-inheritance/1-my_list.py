#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A class that inherits from list."""
    def print_sorted(self):
        """Print the list elements in sorted order(ascending)."""
        sorted_list = sorted(self)
        print(sorted_list)
