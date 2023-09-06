#!/usr/bin/python3
"""This function adds integers."""


def add_integer(a, b=98):
    """The function returns the sum of a and b.

    Float arguments are typecasted to int before addition.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
