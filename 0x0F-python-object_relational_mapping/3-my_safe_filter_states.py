#!/usr/bin/python3
"""
Created on Sat April 8 09:05:11 2023
@author: joshua ik
"""
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print(f"Usage: {sys.argv[0]} username password database_name")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database_name,
        port=3306
    )

    cursor = db.cursor()

    num_rows = cursor.execute(
        f"SELECT * FROM states WHERE states.name LIKE BINARY %s ORDER BY states.id;",
        (state_name,)
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

