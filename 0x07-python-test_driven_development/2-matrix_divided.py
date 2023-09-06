#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists) of integers or floats.
        div (int or float) must not be zero.

    Returns:
        A new matrix with elements divided by the divisor (rounded to 2 dp).

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   or if each row of the matrix does not have the same size,
                   or if the divisor is not a number (integer or float).
        ZeroDivisionError: If the divisor is zero.
    """
    if not isinstance(matrix, list) or
    not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        "integers/floats")
    if not all(isinstance(num, (int, float))
               for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        "integers/floats")
    if not matrix:
        return []

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for row in matrix:
        new_row = [round(element / div, 2)for element in row]
        result.append(new_row)

    return result
