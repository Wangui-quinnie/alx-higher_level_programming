#!/usr/bin/python3
"""A fuction that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int or None: A peak in the list if found, or None if the list is empty.
    """

    n = len(list_of_integers)

    if n == 0:
        return None

    start = 0
    end = n - 1

    while start < end:
        mid = (start + end) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return list_of_integers[start]
