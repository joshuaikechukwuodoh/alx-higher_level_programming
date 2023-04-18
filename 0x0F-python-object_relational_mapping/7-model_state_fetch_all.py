#!/usr/bin/python3
"""
Created on Sat April 8 09:05:11 2023
@author: joshua ik
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} username password database_name")
        sys.exit(1)
    username, password, data = sys.argv[1:4]
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{data}")
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")

