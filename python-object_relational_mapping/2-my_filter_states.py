#!/usr/bin/python3
"""
    script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb

def connectDb(user, password, db):
    """
    Connect to MySQL database
    
    Args:
        user (str): MySQL username
        password (str): MySQL password
        db (str): Database name
        
    Returns:
        Connection: MySQL database connection
    """
    return MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db
    )

if __name__ == "__main__":

    db = connectDb(sys.argv[1], sys.argv[2], sys.argv[3])

    cursor = db.cursor()
    # Query to find states with name matching user input (sys.argv[4]), case sensitive
    cursor.execute("SELECT * FROM states WHERE name = BINARY '{}'\
                     ORDER BY id ASC".format(sys.argv[4]))

    states = cursor.fetchall()

    for row in states:
        print(row)

    cursor.close()
    db.close()
