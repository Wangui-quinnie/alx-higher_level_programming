#!/usr/bin/python3
"""Defines a function that appends a string at the end of a textfile."""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file.

    text (str) to be added to the text file.

    Returns the number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as my_file:
        my_file.write(text)
    return len(text)
