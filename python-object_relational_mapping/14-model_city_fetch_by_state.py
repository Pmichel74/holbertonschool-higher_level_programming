#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Create database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],  # MySQL username
            sys.argv[2],  # MySQL password
            sys.argv[3]   # Database name
        ),
        pool_pre_ping=True
    )

    # Create session factory
    Session = sessionmaker(bind=engine)
 
    # Create session instance
    session = Session()

    # Query cities and their states, sorted by cities.id
    results = session.query(State, City).filter(
        State.id == City.state_id
    ).order_by(City.id)

    # Display results in required format
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
