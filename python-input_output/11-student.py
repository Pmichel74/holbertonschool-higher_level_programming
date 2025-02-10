#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

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
            attrs (list): Optional list of strings: attribute names.
                         If None, all attributes are included.
        Returns:
            dict: Dictionary containing the specified attributes.
        """
        if not isinstance(attrs, list):
            return self.__dict__

        # Verify all elements are strings
        for attr in attrs:
            if not isinstance(attr, str):
                return self.__dict__

        # Create filtered dictionary
        return {attr: self.__dict__[attr]
                for attr in attrs if attr in self.__dict__}

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            # Sets or updates attribute 'k' with value 'v' on Student instance
            setattr(self, key, value)
