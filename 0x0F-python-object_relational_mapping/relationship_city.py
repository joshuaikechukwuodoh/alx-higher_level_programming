#!/usr/bin/python3
"""
Created on Sat April  8 09:05:11 2023
@author: joshua ik
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    A new table into de data base for city representation
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

