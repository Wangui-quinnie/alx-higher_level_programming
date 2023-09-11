#!/usr/bin/python3
"""Checks if an object is an instance of or inherited from the class"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or inherited from, the
    specified class.

    Returns:
        True if the object is an instance of or inherited from
    the class otherwise False.
    """
    return isinstance(obj, a_class)
