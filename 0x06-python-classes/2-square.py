#!/usr/bin/python3
"""This class represents a Square."""


class Square:
    """Define an attribute representing the length of the square."""

    def __init__(self, size=0):
        """Initialize a Square object with size.

        Args:
            size (int): The length of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
