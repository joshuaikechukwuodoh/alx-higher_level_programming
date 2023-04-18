#!/usr/bin/python3
"""
Created on Sat April  8 09:05:11 2023
@author: joshua ik
"""
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print(f"Usage: {args[0]} username password database_name")
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{data}')
    # create custom session object class from database engine
    Session = sessionmaker(bind=engine)
    # create instance of new custom session class
    session = Session()
    results = session.query(State.name, City.id, City.name)\
                     .join(City, City.state_id == State.id)\
                     .order_by(City.id)
    for result in results:
        print(f"{result[0]}: ({result[1]}) {result[2]}")

