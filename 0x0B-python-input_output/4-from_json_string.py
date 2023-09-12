#!/usr/bin/python3
"""A function that returns an object represented by a json string."""


import json


def from_json_string(my_str):
    """
    Converts a JSON string to an object.

    my_str: is the string to be converted.

    Returns a python data structure(an object).
    """
    return json.loads(my_str)
