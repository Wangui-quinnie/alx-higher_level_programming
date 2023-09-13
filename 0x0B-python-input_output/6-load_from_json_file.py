#!/usr/bin/python3
"""A function that creates an object from a "JSON file"."""


import json


def load_from_json_file(filename):
    """Load and parse a JSON file to create an object.

    filename(str) name of the JSON file to be loaded.

    Returns the python object created.
    """
    with open(filename, mode='r', encoding='utf-8') as my_file:
        data = json.load(my_file)
    return data
