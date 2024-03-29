#!/usr/bin/python3

"""
this module prints a square in '#'
"""

def print_square(size):
    """
    """

    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is not float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
