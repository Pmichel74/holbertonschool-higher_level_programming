#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Check if the list is not empty
    if my_list:
        # Iterate over the list in reverse order
        for i in reversed(my_list):
            # Print each integer using str.format()
            print("{:d}".format(i))
