#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Method to calculate area.
        Raises:
            Exception: If area() is not implemented
        """
        raise Exception("area() is not implemented")
