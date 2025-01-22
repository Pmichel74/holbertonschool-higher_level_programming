#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of integers printed.
    """
    # Counter for successfully printed integers
    ret = 0
    
    # Try to print x elements, skipping non-integers
    for i in range(x):
        try:
            # Attempt to print current element as integer
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            # Skip non-integer values
            continue
    
    # Print newline after all elements
    print("")
    return ret
