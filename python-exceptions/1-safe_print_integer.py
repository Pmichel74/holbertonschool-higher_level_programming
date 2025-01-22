#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value: The value to print, can be any type.

    Returns:
        True if value was correctly printed as integer,
        False otherwise.
    """
    try:
        # Attempt to print value as integer using format specifier
        print("{:d}".format(value))
        return (True)
    except (TypeError. ValueError):
        # Return False if value can't be formatted as integer
        return (False)
