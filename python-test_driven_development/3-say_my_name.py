#!/usr/bin/python3
"""Defines a name-printing function."""

def say_my_name(first_name, last_name=""):
    """Print a full name in the format: My name is <first_name> <last_name>.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    # Verify that first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Verify that last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the resulting full name
    print("My name is {} {}".format(first_name, last_name))
    