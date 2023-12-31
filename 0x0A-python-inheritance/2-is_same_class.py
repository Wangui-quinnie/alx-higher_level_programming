#!/usr/bin/python3
"""Checks if an object is exactly an instance of the specified class."""


def is_same_class(obj, a_class):
    """Returns True if the object is an instance of the specified class."""
    return type(obj) == a_class
