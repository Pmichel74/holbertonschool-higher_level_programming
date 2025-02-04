#!/usr/bin/env python3
# File: task_02_verboselist.py
# Author: Student
# Description: A list subclass that provides verbose output for modifications

class VerboseList(list):
    """A list subclass that prints notifications when modified.
    
    Inherits from built-in list class and overrides common methods
    to provide feedback when operations are performed.
    """

    def append(self, item):
        """Add an item to the end of the list and print notification.
        
        Args:
            item: The item to append to the list
            
        Example:
            >>> vlist = VerboseList()
            >>> vlist.append(5)  # Outputs: Added [5] to the list
        """
        # Call parent class append method
        super().append(item)
        # Print notification of operation
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list by appending elements from iterable.
        
        Args:
            iterable: Collection of items to add
            
        Example:
            >>> vlist = VerboseList([1])
            >>> vlist.extend([2,3])  # Outputs: Extended list with [2] items
        """
        # Call parent class extend method
        super().extend(iterable)
        # Print notification with number of items added
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove first occurrence of item and notify.
        
        Args:
            item: The item to remove
            
        Example:
            >>> vlist = VerboseList([1,2,3])
            >>> vlist.remove(2)  # Outputs: Removed [2] from list
        """
        # Call parent class remove method
        super().remove(item)
        # Print notification of removal
        print(f"Removed [{item}] from the list")

    def pop(self, index=-1):
        """Remove and return item at index with notification.
        
        Args:
            index: Position to remove from (default: last item)
            
        Returns:
            The removed item
            
        Example:
            >>> vlist = VerboseList([1,2,3])
            >>> vlist.pop()  # Outputs: Popped [3] from list
        """
        # Get and remove item using parent class pop
        item = super().pop(index)
        # Print notification of pop operation
        print(f"Popped [{item}] from the list.")
        return item