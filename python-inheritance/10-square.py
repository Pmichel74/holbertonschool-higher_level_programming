#!/usr/bin/python3
# Description: Class Square that inherits from Rectangle

"""Defines a Rectangle subclass Square."""
# Import Rectangle class from module 9-rectangle
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        # Validate size parameter using inherited method
        self.integer_validator("size", size)
        # Initialize the parent class with size for both width and height
        super().__init__(size, size)
        # Set private size attribute
        self.__size = size
