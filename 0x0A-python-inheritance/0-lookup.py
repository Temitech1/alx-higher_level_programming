#!/usr/bin/python3
"""
lookup: function to be called"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    """
    return dir(obj)
