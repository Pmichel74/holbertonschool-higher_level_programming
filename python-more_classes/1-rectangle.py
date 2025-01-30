#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width  # Use the setter to validate and set the width
        self.height = height  # Use the setter to validate and set the height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width  # Return the current width of the rectangle

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")  # Raise error if width is not an integer
        if value < 0:
            raise ValueError("width must be >= 0")  # Raise error if width is negative
        self.__width = value  # Set the width of the rectangle

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height  # Return the current height of the rectangle

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")  # Raise error if height is not an integer
        if value < 0:
            raise ValueError("height must be >= 0")  # Raise error if height is negative
        self.__height = value  # Set the height of the rectangle
