#!/usr/bin/python3
"""A function that returns the list of available attributes and methods."""


def lookup(obj):
    """Returns the list of available attributes and methods."""
    return dir(obj)
