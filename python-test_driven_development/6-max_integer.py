#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    
    # Initialize the result with the first element of the list
    result = list[0]
    
    # Iterate over the list starting from the second element
    for num in list[1:]:
        if num > result:
            result = num
    
    return result
