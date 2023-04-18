#!/usr/bin/python3
"""
Created on Sat April  8 09:05:11 2023
@author: joshua ik
"""import mysql.connector
import sys


def main(username, password, database_name, state_name):
    try:
        conn = mysql.connector.connect(
            user=username,
            password=password,
            database=database_name,
            host='localhost',
            port=3306
        )
        cursor = conn.cursor()

        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id;"
        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        conn.close()

    except mysql.connector.Error as error:
        print("Failed to connect to MySQL: {}".format(error))
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    main(username, password, database_name, state_name)

