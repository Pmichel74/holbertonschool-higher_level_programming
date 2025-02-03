#!/usr/bin/python3
# File: 9-rectangle.py
# Author: Student
# Description: Class Rectangle that inherits from BaseGeometry

"""Defines a class Rectangle that inherits from BaseGeometry."""
# Import BaseGeometry class from module 8-base_geometry
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        # Validate width parameter using inherited method
        self.integer_validator("width", width)
        # Set private width attribute
        self.__width = width
        # Validate height parameter using inherited method
        self.integer_validator("height", height)
        # Set private height attribute
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        # Create string representation with class name and dimensions
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
