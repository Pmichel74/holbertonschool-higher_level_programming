#!/usr/bin/python3
"""
Script that displays the ID of a State object from its name given as argument.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Verify the number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create the SQLAlchemy engine to connect to MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True  # Check if connection is alive before using it
    )

    # Create a Session class bound to our engine
    Session = sessionmaker(bind=engine)

    # Create a session instance to interact with the database
    session = Session()

    # Look for the State by its exact name
    # Note: filter_by uses exact equality (==)safer against SQL injection
    state = session.query(State).filter_by(name=state_name).first()

    # Display result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
