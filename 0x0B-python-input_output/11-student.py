#!/usr/bin/python3
"""Defines a class student."""


class Student:
    """
    Class that represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(self): Retrieves a dictionary representation
    of a Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args: attrs(list, optional) a list of attribute names to include
        in the dict.If None all attributes are included.

        Returns:
            dict: A dictionary containing the specified attributes of
        the Student instance.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a JSON dictionary.

        Args:
            json (dict): A dictionary with attribute names as keys and their
        values as values.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
