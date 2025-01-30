#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle.

        Calculates area by multiplying width and height.
        """
        # Calculate area (width * height)
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle.

        Returns 0 if width or height is 0.
        """
        # Check if rectangle has zero dimensions
        if self.__width == 0 or self.__height == 0:
            return (0)
        # Calculate perimeter (2 * width + 2 * height)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        Returns empty string if width or height is 0.
        """
        # Return empty string for zero dimensions
        if self.__width == 0 or self.__height == 0:
            return ("")
        # Initialize list for building rectangle string
        rect = []
        # Build rectangle row by row
        for i in range(self.__height):
            # Add '#' characters for the width of current row
            [rect.append('#') for j in range(self.__width)]
            # Add newline except for last row
            if i != self.__height - 1:
                rect.append("\n")
        # Convert list to string and return
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle.
        
        Returns:
            str: String that can recreate Rectangle using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for every deletion of a Rectangle.

        Called automatically when instance is deleted.
        """
        type(self).number_of_instances -= 1
        # Print deletion message
        print("Bye rectangle...")
