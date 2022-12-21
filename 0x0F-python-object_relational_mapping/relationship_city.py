#!/usr/bin/python3
"""Write a python file that contains the class definition of a
State and an instance Base = declarative_base()"""
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State


class City(Base):
    """[summary]

    Args:
        Base ([type]): [description]
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
