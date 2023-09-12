#!/usr/bin/python3
"""defines a class BaseGeometry."""


class BaseGeometry:
    """Represents a class basegeometry."""
    def area(self):
        """Raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value, raising errors if conditions are not met.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
