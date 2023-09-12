#!/usr/bin/python3
"""A function that writes an object to a textfile using a JSON string."""


import json


def save_to_json_file(my_obj, filename):
    """
    Serialize the input object to its JSON representation.

    my_obj is the object to be serialized and saved to the filename.
    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
