#!/usr/bin/python3
"""
Lists all states in database hbtn_0e_0_usa,
it should take 3 arguments
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connects to SQL on localhost
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Creates a cursor to get SQL queries
    cur = db.cursor()

    # Excutes SQL querie that gets states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Prints list of states
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
