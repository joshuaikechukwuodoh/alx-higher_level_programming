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

    username, password, data = sys.argv[1:]

    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{data}")

    with sessionmaker(bind=engine)() as session:
        states = session.query(State).filter(State.name.contains('a')).order_by(State.id)

        if states:
            for state in states:
                print(f"{state.id}: {state.name}")
        else:
            print("Nothing")

