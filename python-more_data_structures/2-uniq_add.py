#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list (only once for each integer)"""
    # Initialize result variable to store sum
    result = 0
    # set() : convertit liste en ensemble
    # pour supprimer les doublons et parcourir uniquement les valeurs uniques
    for x in set(my_list):
        # Add each unique number to result
        result += x
    # Return the sum of all unique integers
    return (result)
