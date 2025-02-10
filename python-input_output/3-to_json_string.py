#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object.

    Args:
        my_obj (str): The string object to convert to JSON.
    Returns:
        str: The JSON representation of the string object.
    """
    # Utilise fonct dumps de biblio json pour convertir objet en chaîne JSON
    return json.dumps(my_obj)
