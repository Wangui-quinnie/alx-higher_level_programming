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

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overrides the default string representation of the object.

        Returns:
            str: The string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square based on the given arguments.

        Args:
            *args: The non-keyword arguments to assign to the attributes.
            **kwargs: The keyword arguments to assign to the attributes.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dict representation of a Square.

        Returns:
            dict: The dictionary representation of a square.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
