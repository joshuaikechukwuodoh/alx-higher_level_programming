#!/usr/bin/python3
"""
Created on Sat April  8 09:05:11 2023
@author: joshua ik
"""
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main(username, password, database_name):
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database_name}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(f"New state '{new_state.name}' created with id {new_state.id}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('username', help='MySQL username')
    parser.add_argument('password', help='MySQL password')
    parser.add_argument('database_name', help='MySQL database name')
    args = parser.parse_args()
    
    try:
        main(args.username, args.password, args.database_name)
    except Exception as e:
        print(f"Error: {e}")

