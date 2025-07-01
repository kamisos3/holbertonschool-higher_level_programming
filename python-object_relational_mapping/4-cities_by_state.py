#!/usr/bin/python3
"""Lists all cities from usa database"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, db_name = sys.argv[1:4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
    """)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
