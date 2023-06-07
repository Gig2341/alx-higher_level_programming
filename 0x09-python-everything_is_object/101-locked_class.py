#!/usr/bin/python3

"""
this module defines a locked class
"""


class LockedClass:
    """
    this class only allows instantiation of an attribute called first_name
    """
    
    __slots__ = ["first_name"]
