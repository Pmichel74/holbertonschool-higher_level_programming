#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Query all States containing letter 'a' and delete them
    states = session.query(State).filter(
        State.name.like('%a%')
    ).all()
    for state in states:
        session.delete(state)

    # Commit the transaction to persist the changes
    session.commit()

    # Close the session
    session.close()
