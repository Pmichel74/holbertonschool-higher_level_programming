#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multipled by 2."""
    # Create new dictionary and multiply each value by 2
    new_dict = {}
    for k in a_dictionary:
        new_dict[k] = a_dictionary[k] * 2
    return new_dict
