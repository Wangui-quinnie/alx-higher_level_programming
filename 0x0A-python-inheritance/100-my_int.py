#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """
    A custom integer class that inherits from int and inverts
    the == and != operators.

    This class overrides the equality (__eq__) and inequality (__ne__)
    operators to swap their behaviors.
    """

    def __eq__(self, other):
        """
        Override the equality operator (==) to invert its behavior.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator (!=) to invert its behavior.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
