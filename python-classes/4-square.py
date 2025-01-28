#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        # Validate that size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Validate that size is non-negative
        elif size < 0:
            raise ValueError("size must be >= 0")
        # Initialize the size attribute
        self.__size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        # Validate that the new size is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # Validate that the new size is non-negative
        elif value < 0:
            raise ValueError("size must be >= 0")
        # Set the size attribute to the new value
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        # Calculate and return the area of the square
        return self.__size * self.__size
