#!/usr/bin/python3
"""
Created on Sat April  8 09:05:11 2023
@author: joshua ik
"""
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} username password database_name state_name")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306,
    )

    cur = db.cursor()

    query = f"""
        SELECT cities.name 
        FROM cities 
        WHERE state_id = (
            SELECT id 
            FROM states 
            WHERE name LIKE BINARY %s
        ) 
        ORDER BY cities.id
    """

    num_rows = cur.execute(query, (state_name,))
    rows = cur.fetchall()

    output = ", ".join(row[0] for row in rows)
    print(output)

    cur.close()
    db.close()

