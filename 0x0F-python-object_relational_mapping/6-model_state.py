#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine

if __name__ == "__main__":
    user, password, db_name = sys.argv[1:]
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost/{db_name}",
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

