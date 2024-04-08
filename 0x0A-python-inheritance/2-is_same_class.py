#!/usr/bin/python3
"""
is_same_class: function to be called"""


def is_same_class(obj, a_class):
    """
     a function that returns True otherwise False"""
    if type(obj) == a_class:
        return True
    else:
        return False
