#!/usr/bin/python3
"""
    Script that lists all states from the database.
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
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    arg = sys.argv[4]

    conn = connectDb(user, password, db)
    cur = conn.cursor()

    # %s is a placeholder for the state name, preventing SQL injection
    query = """ SELECT * FROM states WHERE states.name = %s
        ORDER BY states.id ASC
    """
    cur.execute(query, (arg,))

    # Fetch all the results of the query
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
