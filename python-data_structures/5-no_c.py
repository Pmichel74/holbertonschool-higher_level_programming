#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string."""

    result = []
    for char in my_string:
        if char != 'c' and char != 'C':
            result.append(char)
            # join(result) is used to convert the list to a string
            # "" no separator between characters
    return ("".join(result))
