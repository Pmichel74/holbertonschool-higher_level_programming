#!/usr/bin/python3
"""Module that handles object serialization using pickle."""
import pickle


class CustomObject:
    """Class that demonstrates pickle serialization/deserialization.

    This class provides methods to create, display and serialize/deserialize
    objects with basic attributes (name, age, student status).
    """

    def __init__(self, name, age, is_student):
        """Initialize object with provided attributes.

        Args:
            name (str): Person's name
            age (int): Person's age
            is_student (bool): Student status
        """
        # Initialize instance attributes
        self.name = name        # Name as string
        self.age = age         # Age as integer
        self.is_student = is_student  # Student status as boolean

    def display(self):
        """Display formatted object attributes."""
        # Print each attribute on new line with label
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Is_student : {self.is_student}")

    def serialize(self, filename):
        """Save object state to file using pickle.

        Args:
            filename (str): Path to save serialized data

        Returns:
            bool: True if successful, None if failed
        """
        try:
            # Open file in binary write mode
            with open(filename, "wb") as pickle_file:
                # Convert object to binary stream
                pickle.dump(self, pickle_file)
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Create new instance from serialized file.

        Args:
            filename (str): Path to serialized file

        Returns:
            CustomObject: New instance if successful
            None: If deserialization fails
        """
        try:
            # Open file in binary read mode
            with open(filename, "rb") as pickle_file:
                # Read binary and convert back to object
                return pickle.load(pickle_file)
        except Exception:
            return None
