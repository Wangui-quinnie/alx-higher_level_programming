#!/usr/bin/python3
"""This class represents a Square."""


class Square:
    """Define an attribute representing the length of the square."""

    def __init__(self, size=0):
        """Initialize a Square object with size.

        Args:
            size (int): The length of the square.
        """

        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the character #."""

        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)
