#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student.

    This class creates a student object with first name, last name and age.
    It also provides methods to convert the student object to JSON format,
    with optional attribute filtering.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        Args:
            attrs (list): Optional list of attribute names to include.
                         If None, all attributes are included.

        Returns:
            dict: A dictionary containing the requested Student attributes.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}
