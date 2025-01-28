#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The real number of integers printed.
    """
    # Counter for successfully printed integers
    ret = 0

    # Iterate through x elements of the list
    for i in range(x):
        try:
            # Try to format and print value as integer
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            # Skip if value is not an integer or can't be converted
            continue
        except IndexError:
            # Raise exception if x is larger than list length
            raise

    # Print newline after all integers
    print("")
    return ret

if __name__ == "__main__":
    import doctest
    doctest.testmod()
