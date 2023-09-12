#!/usr/bin/python3
"""A function that writes a string to a text file."""


def write_file(filename="", text=""):
    """
    Write the given text to a text file (UTF-8) specified by the filename.

    Args:
        filename (str): The name of the file to be written.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        my_file.write(text)

    return len(text)
