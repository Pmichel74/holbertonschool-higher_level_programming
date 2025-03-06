#!/usr/bin/python3
"""
Contains the class definition of a City
Represents the 'cities' table in MySQL database
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that inherits from Base
    Links to the MySQL table 'cities'

    Attributes:
        id (int): Auto-generated unique identifier and primary key
        name (str): Name of the city, max length 128 characters
        state_id (int): Foreign key referencing states.id
    """
    # Table name in the database
    __tablename__ = 'cities'

    # Primary key column
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # City name column, maximum 128 characters
    name = Column(String(128), nullable=False)

    # Reference to the state this city belongs to
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
