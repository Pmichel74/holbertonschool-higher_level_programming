#!/usr/bin/python3
"""
    Script that lists all states from the database.
"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port="3306",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                    ORDER BY id ASC")

    # Fetch all rows from the query results
    states = cursor.fetchall()

    for row in states:
        print(row)

    # Close cursor and database connection to free resources
    cursor.close()
    db.close()
