#!/usr/bin/python3
"""
Created on Sat April  8 09:05:11 2023
@author: joshua ik
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} username password database_name")
        sys.exit(1)

    username, password, database_name = sys.argv[1:]

    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database_name}")
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    california.cities = [City(name="San Francisco")]
    session.add(california)
    session.commit()
    session.close()

