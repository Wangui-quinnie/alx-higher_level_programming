#!/usr/bin/python3
"""Checks if an obj is an instance of a class inherited from a_class."""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a class inherited from
        a_class, else False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
