#!/usr/bin/python3
"""A function that returns the JSON representation of an object."""


import json


def to_json_string(my_obj):
    """Converts my_obj to the JSON representation.

    my_obj: the object to be converted.

    Returns the JSON representation string.
    """
    return json.dumps(my_obj)
