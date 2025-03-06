#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def connectDb(user, password, db):
    """
        Get connection with the database.
        Args:
            user (str): Username of the user.
            password (str): Password of the user.
            db (str): Database to retrieve.
        Return:
            Connection database.
    """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db,
        charset="utf8"
    )
    return conn


if __name__ == "__main__":
    # Get command line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    # Connect to database
    conn = connectDb(user, password, db)
    cursor = conn.cursor()

    # Query to find all cities with their state name
    query = """ SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch all the results of the query
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
