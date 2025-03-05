#!/usr/bin/python3
"""
    Script that lists all states from the database.
"""
import MySQLdb
import sys  # Module to access command line arguments


def connectDb(user, password, db):
    """
    Connects to the MySQL database and returns the connection.

    Arguments:
        user (str): MySQL username
        password (str): MySQL password
        db (str): Database name

    Returns:
        Connection: MySQL database connection
    """
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db,
        charset="utf8"
    )
    return connection


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Establish the database connection
    db = connectDb(username, password, database)

    # Create a cursor
    cursor = db.cursor()

    # Execute a query to select all states
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)
    cursor.close()
    db.close()
