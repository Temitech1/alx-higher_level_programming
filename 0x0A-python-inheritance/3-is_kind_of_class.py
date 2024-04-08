#!/usr/bin/python3
"""
 is_kind_of_class: function will run"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance, else False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
