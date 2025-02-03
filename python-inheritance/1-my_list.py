#!/usr/bin/python3
"""
Defines an inherited list class MyList.
"""


class MyList(list):
    """A subclass of list that can print itself sorted."""

    def __init__(self, iterable=[]):
        """Initializes the object with an optional iterable."""
        super().__init__(iterable)

    def print_sorted(self):
        """Prints the list in sorted (ascending) order."""
        print(sorted(self))
