#!/usr/bin/python3
"""A function that reads a textfile and prints to stdout."""


def read_file(filename=""):
    """Reads a text file and prints to stdout"""
    with open(filename, mode='r', encoding='utf-8') as my_file:
       print(my_file.read(), end='')
