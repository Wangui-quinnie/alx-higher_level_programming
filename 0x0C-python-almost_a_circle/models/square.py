#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square that inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optiional): The x-coordinate of the square's position
defaults to 0.
            y (int, optinal): The y-coordinate of the square's position
defaults to 0.
            id (int, optional): the id of the square defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overrides the default string representation of the object.

        Returns:
            str: The string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
