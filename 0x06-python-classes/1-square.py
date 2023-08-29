#!/usr/python3
"""
This class represents a square
"""


class Square:
    """
    The size attribute is a private instance attribute
    """

    def __init__(self, size):
        """
        Initialize a square object with a given size

        Args:
            size (int): The length of the square
        """

        self.__size = size
