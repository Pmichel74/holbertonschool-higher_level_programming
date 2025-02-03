#!/usr/bin/python3
# File: 1-my_list.py
# Author: Student
# Description: Module containing the MyList class that inherits from list

"""
Defines an inherited list class MyList.
"""


class MyList(list):
    # MyList inherits from the built-in list class
    """A subclass of list that can print itself sorted."""

    def __init__(self, iterable=[]):
        # Initialize new MyList instance with optional iterable
        """Initializes the object with an optional iterable."""
        super().__init__(iterable)

    def print_sorted(self):
        # Print list in ascending order without modifying original list
        """Prints the list in sorted (ascending) order."""
        print(sorted(self))
