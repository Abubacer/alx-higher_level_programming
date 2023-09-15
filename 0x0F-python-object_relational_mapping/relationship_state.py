#!/usr/bin/python3
"""
Defines the State class and an instance of Base.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Represent a State class that inherits from Base.
    Establish one-to-many relationship between State and City.

    Attributes:
        __tablename__ (str): The class table name.
        id (int): The class state id.
        name (str): The class state name.
        cities (obj): The cities belonging to the state.
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

    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete"
    )
