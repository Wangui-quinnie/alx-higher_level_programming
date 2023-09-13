#!/usr/bin/python3
"""A func that returns a dict description for JSON serialization."""


def class_to_json(obj):
    """
    Convert an instance of a class to a dictionary description
    for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing the serializable attributes
    of the object.
    """
    obj_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            obj_dict[attr] = value
    return obj_dict
