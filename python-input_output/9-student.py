#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student.
    
    This class creates a student object with first name, last name and age.
    It also provides a method to convert the student object to JSON format.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        # Initialise les attributs d'instance
        self.first_name = first_name  # Stocke le prénom
        self.last_name = last_name    # Stocke le nom
        self.age = age                # Stocke l'âge

    def to_json(self):
        """Get a dictionary representation of the Student.
        
        Returns:
            dict: A dictionary containing all properties of the Student instance.
                 The dictionary will contain:
                 - first_name
                 - last_name
                 - age
        """
        # Retourne un dictionnaire contenant tous les attributs de l'instance
        return self.__dict__
