#!/usr/bin/python3
"""Defines functions that serialize and deserialize data"""
import json


def serialize_and_save_to_file(data, filename):
    """Function serializes data to JSON
    Args:
        data: Python dictionary
        filename: File name of JSON file
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Function desirializes JSON data into python dictionery
    Args:
        filename: file to read data from
    Return:
        returns the python string
    """

    with open(Filename, "r", encoding="utf-8") as f:
        dictionary = json.load(f)
        return dictionary
