#!/usr/bin/python3
"""
Created on Sat April  8 09:05:11 2023
@author: joshua ik
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

# Check command line arguments
if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} username password database_name")
    sys.exit(1)

# Get command line arguments
username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]

# Create engine and session
engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database_name}")
Session = sessionmaker(bind=engine)
session = Session()

# Query the database and print results
states = session.query(State).all()
for state in states:
    print(f"{state.id}: {state.name}")
    for city in state.cities:
        print(f"    {city.id}: {city.name}")

# Close the session
session.close()


