#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    # dictionnaire des attributs d'objet, ce qui représente sa structure simple
    return obj.__dict__
