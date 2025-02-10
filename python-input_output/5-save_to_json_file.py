#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.

    Args:
        my_obj (object): The object to write to the file.
        filename (str): The name of the file to write to.
    """
    # Convertir les ensembles en listes pour les rendre sérialisables en JSON
    # if isinstance(my_obj, set):
    # my_obj = list(my_obj)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
