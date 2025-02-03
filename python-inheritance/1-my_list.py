#!/usr/bin/python3
"""
This module contains the MyList class.
"""

class MyList(list):
    """A subclass of list that can print itself sorted."""
    
    def __init__(self):
        """Initializes the object."""
        super().__init__()

    def print_sorted(self):
        """Prints the list in sorted (ascending) order."""
        print(sorted(self))
