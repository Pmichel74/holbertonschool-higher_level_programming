#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    # Compare the object's class directly with the given class using 'is'
    # obj.__class__ gets the exact class of the object
    # 'is' checks for exact identity, not just equality
    return obj.__class__ is a_class
