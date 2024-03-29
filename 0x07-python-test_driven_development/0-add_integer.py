#!/usr/bin/python3

"""
this module contains a fuction that adds two numbers
"""


def add_integer(a, b=98):
    """
    this module returns the sum of two integers or floats that
    are integers.

    Args:
        a: first argument
        b: second argument
    Return:
        the sum of the two arguments
    Raises:
        TypeError: if either of the arguments not an integer
        or float

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
