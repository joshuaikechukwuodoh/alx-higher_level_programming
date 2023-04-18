#!/usr/bin/python3
# -*- coding: utf-e-8 -*-
"""
Created on Sat april  8 09:05:11 2023
@author: joshua ikechukwu
"""
import MySQLdb
import argparse


def main(args):
    # Connect to the database
    db = MySQLdb.connect(
        host='localhost',
        user=args.username,
        passwd=args.password,
        db=args.database,
        port=3306
    )

    # Execute the query and fetch the results
    with db.cursor() as cursor:
        cursor.execute('SELECT * FROM states ORDER BY states.id')
        rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('username', help='MySQL username')
    parser.add_argument('password', help='MySQL password')
    parser.add_argument('database', help='MySQL database name')
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args)
