#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replace or add key/value in a dictionary.

    Args:
        a_dictionary: the dictionary to modify
        key: string key to update or add
        value: value to associate with key
    Returns:
        The modified dictionary
    """

    # - Update the value if key exists
    # - Create a new key/value pair if key doesn't exist
    a_dictionary[key] = value
    return (a_dictionary)
