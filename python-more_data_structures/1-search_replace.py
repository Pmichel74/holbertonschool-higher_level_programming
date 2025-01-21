#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""

    # Create a copy of the original list to NOT MODiFYING it
    # [:] Les modifications de new_list n'affectent pas my_list
    new_list = my_list[:]
    # Iterate through the list using index
    for i in range(len(new_list)):
        # If element matches search value, replace it
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
