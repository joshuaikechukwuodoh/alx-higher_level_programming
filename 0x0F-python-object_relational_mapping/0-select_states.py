#!/usr/bin/python3

# Import the necessary modules
import MySQLdb
from sys import argv

# Check if this script is being run as the main program
if __name__ == '__main__':

    # Get the command-line arguments that contain the database credentials
    # Note: argv[0] is the script name, so we start with argv[1]
    db_username = argv[1]  # The MySQL username
    db_password = argv[2]  # The MySQL password
    db_name = argv[3]      # The name of the database we want to connect to

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",   # The hostname of the database server
        port=3306,          # The port number to use for the connection
        user=db_username,   # The MySQL username (from command-line arguments)
        passwd=db_password, # The MySQL password (from command-line arguments)
        db=db_name          # The name of the database to connect to (from command-line arguments)
    )

    # Create a cursor object, which we will use to execute SQL commands
    cursor = db.cursor()

    # Execute a simple SELECT statement to retrieve all rows from the "states" table
    cursor.execute("SELECT * FROM states")

    # Fetch all the rows returned by the SELECT statement
    rows = cursor.fetchall()

    # Iterate over the rows and print them to the console
    for row in rows:
        print(row)

    # Close the cursor and database connection to clean up resources
    cursor.close()
    db.close()

