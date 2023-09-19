#!/usr/bin/python3
"""Defines a class for managing id attribute."""


import json


class Base:
    """
    Base class for managing id attribute in all classes.

    Attributes:
        __nb_objects (int): A private class attribute.
        id (int): A public instance attribute representing the object's ID.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance with an id.

        Args:
            id (int, optinal): Defaults to None - id of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
           list_objs (list): A list of instances.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(filename, mode="w", encoding="utf-8") as my_file:
            json_str = cls.to_json_string([obj.to_dictionary()
                                          for obj in list_objs])
            my_file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary (dict): A dictionary of attributes.

        Returns:
            obj: An instance of the class with the attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a file.

        Returns:
            List: A list of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as my_file:
                json_data = my_file.read()
                json_list = cls.from_json_string(json_data)
                instances = [cls.create(**d) for d in json_list]
                return instances
        except FileNotFoundError:
            return []
