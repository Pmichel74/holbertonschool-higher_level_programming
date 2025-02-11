#!/usr/bin/python3
"""Module that handles JSON serialization and deserialization operations"""
import json


def serialize_and_save_to_file(data, filename):
    """Converts a Python dictionary to JSON format and saves it to a file
    
    Args:
        data: Python dictionary to be converted to JSON
        filename: Name of the file where JSON will be saved
        
    Example:
        my_dict = {"name": "John", "age": 30}
        serialize_and_save_to_file(my_dict, "person.json")
    """
    # Open file in write mode with UTF-8 encoding for special characters
    with open(filename, "w", encoding="utf-8") as f:
        # Convert Python dict to JSON and write to file
        json.dump(data, f)


def load_and_deserialize(filename):
    """Reads JSON data from a file and converts it back to Python dictionary
    
    Args:
        filename: Path to the JSON file to read
        
    Returns:
        dict: Python dictionary containing the deserialized JSON data
        
    Example:
        loaded_data = load_and_deserialize("person.json")
        print(loaded_data)  # {"name": "John", "age": 30}
    """
    # Open JSON file in read mode
    with open(filename, "r", encoding="utf-8") as f:
        # Parse JSON and convert to Python dictionary
        dictionary = json.load(f)
        return dictionary
