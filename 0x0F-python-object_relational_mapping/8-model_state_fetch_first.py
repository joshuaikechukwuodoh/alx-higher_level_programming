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
    args = sys.argv
    if len(args) != 4:
        print(f"Usage: {args[0]} username password database_name")
        exit(1)
    username, password, database = args[1:]
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database}")
    Session = sessionmaker(bind=engine)
    with Session() as session:
        state = session.query(State).order_by(State.id).first()
        if state:
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")

