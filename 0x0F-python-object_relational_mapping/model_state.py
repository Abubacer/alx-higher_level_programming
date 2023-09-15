#!/usr/bin/python3
"""
Defines the State class and an instance of Base.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represent a State class that inherits from Base.

    Attributes:
        __tablename__ (str): The class table name.
        id (int): The class state id.
        name (str): The class state name.
    """
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )

    name = Column(
        String(128),
        nullable=False
    )
