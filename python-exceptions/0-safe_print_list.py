#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Safely prints x elements of a list
    Args:
        my_list: list to print elements from
        x: number of elements to print
    Returns:
        The real number of elements printed
    """
    try:
        # Attempt to print x elements from the list
        for i in range(x):
            print(my_list[i], end="")
        print()  # Print newline after elements
        return x  # Return requested number if successful
    except IndexError:
        # Handle case where x is larger than list length
        print()
        return i
    except TypeError:
        # Handle case where list elements can't be printed
        print()
        return i
