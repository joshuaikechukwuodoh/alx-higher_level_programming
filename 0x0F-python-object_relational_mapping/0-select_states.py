#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import the required module for interacting with MySQL databases
import MySQLdb

# Import the sys module for command-line arguments
import sys

# Check if the script is being run directly and not being imported as a module
if __name__ == '__main__':
    
    # Retrieve command-line arguments and check that there are exactly 4 arguments
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    
    # Extract the arguments for the MySQL database connection
    username = args[1]
    password = args[2]
    database_name = args[3]
    
    # Connect to the MySQL database using the provided arguments
    db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database_name, port=3306)
    
    # Create a cursor object that will be used to execute SQL statements
    cursor = db.cursor()
    
    # Execute a SELECT query to retrieve all rows from a table called `states` and order them by their `id` field
    num_rows = cursor.execute('SELECT * FROM states ORDER BY states.id;')
    
    # Fetch all the rows returned by the SELECT query
    rows = cursor.fetchall()
    
    # Loop through each row and print it to the console
    for row in rows:
        print(row)
    
    # Close the cursor and database connections
    cursor.close()
    db.close()
