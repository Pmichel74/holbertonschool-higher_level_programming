#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.

    Args:
        filename (str): The name of the file to read from.
    Returns:
        The Python object created from the JSON file.
    """
    # Ouvre le fichier en mode lecture
    with open(filename) as f:
        # Charge le contenu JSON du fichier et le convertit en objet Python
        return json.load(f)
