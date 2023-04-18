#!/usr/bin/python3
"""
Created on Sat April  8 09:05:11 2023
@author: joshua ik
"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == '__main__':
    args = sys.argv
    # Check if the script was called with the correct number of arguments
    if len(args) != 4:
        print(f"Usage: {args[0]} username password database_name")
        exit(1)
    # Assign username, password, and database name to variables based on arguments
    username, password, data = args[1], args[2], args[3]
    # Create engine object that connects to the database
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{data}")
    # Create custom session object class from database engine
    Session = sessionmaker(bind=engine)
    # Create instance of new custom session class
    session = Session()
    # Query the database for all rows in the cities table
    rows = session.query(City).all()
    # Iterate over result set and print info about each City object
    for city in rows:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    # Close the session
    session.close()

