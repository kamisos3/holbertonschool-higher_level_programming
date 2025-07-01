#!/usr/bin/python3
"""Makes SQL injection to delete"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    username, password, db_name, state_name = sys.argv[1:5]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
