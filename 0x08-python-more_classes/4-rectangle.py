#!/usr/bin/python3
"""This class defines a rectangle."""


class Rectangle:
    """Define private instance attributes width and height of the rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle object with width and height."""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with error checking."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with error checking."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle with #."""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self.height):
                rectangle_str += "#" * self.width + "\n"
            return rectangle_str.rstrip()

    def __repr__(self):
        """Return a string reperesentation that allows recreation."""
        return f"Rectangle({self.width}, {self.height})"
