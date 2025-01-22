#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    # Counter for successfully printed elements
    ret = 0
    
    # Try to print x elements from the list
    for i in range(x):
        try:
            # Attempt to print current element and increment counter
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            # Break loop if index is out of range
            break
    
    # Print newline after all elements
    print("")
    return (ret)
