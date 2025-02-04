#!/usr/bin/env python3

# Import required modules
from abc import ABC, abstractmethod  # For creating abstract base class
import math  # For mathematical calculations


# Define abstract base class for shapes
class Shape(ABC):
    """Abstract base class that defines interface for all shapes."""

    @abstractmethod
    def area(self):
        """Abstract method that must be implemented by all shape classes."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for calculating shape perimeter."""
        pass


class Circle(Shape):
    """Circle implementation of Shape abstract class."""

    def __init__(self, radius):
        """Initialize Circle with radius."""
        # Store radius as private attribute
        self.__radius = radius

    def area(self):
        """Calculate circle area using pi*r^2 formula."""
        return math.pi * abs(self.__radius) ** 2

    def perimeter(self):
        """Calculate circle perimeter using 2*pi*r formula."""
        return 2 * math.pi * abs(self.__radius)


class Rectangle(Shape):
    """Rectangle implementation of Shape abstract class."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        # Store dimensions as private attributes
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate rectangle area using width*height formula."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate rectangle perimeter using 2*(width+height) formula."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Utility function to display shape information."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# Test the implementation if this file is run directly
# This block only executes if the script is run directly
if __name__ == "__main__":
    # Create test instances
    circle = Circle(radius=7)
    rectangle = Rectangle(width=5, height=2)

    # Display information for both shapes
    shape_info(circle)
    shape_info(rectangle)

    # Test with negative numbers
    print("\nTesting with negative numbers:")
    try:
        negative_circle = Circle(radius=-3)
    except ValueError as e:
        print(f"Error creating circle: {e}")

    try:
        negative_rectangle = Rectangle(width=-2, height=4)
    except ValueError as e:
        print(f"Error creating rectangle: {e}")

    try:
        negative_rectangle = Rectangle(width=2, height=-4)
    except ValueError as e:
        print(f"Error creating rectangle: {e}")

    try:
        negative_rectangle = Rectangle(width=-2, height=-4)
    except ValueError as e:
        print(f"Error creating rectangle: {e}")
