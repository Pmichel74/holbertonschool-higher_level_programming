#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary."""
    # Check if key exists in dictionary
    if key in a_dictionary == " ":
        # Delete the key if it exists
        del a_dictionary[key]
    return (a_dictionary)
