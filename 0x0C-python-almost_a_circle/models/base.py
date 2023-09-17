#!/usr/bin/python3
"""Defines a class for managing id attribute."""


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
        Initialize a bBase instance with an id.

        Args:
            id (int, optinal): Defaults to None - id of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
